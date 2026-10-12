"""Rebuild week1 CSVs: 2 ad sets, kill CPA>82.5 & spend>40, Interest off after D5."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BROAD_SPEND = 198.40
BROAD_PURCH = 5
INTEREST_SPEND = 219.92
INTEREST_PURCH = 2
KILL_CPA = 82.5
MIN_SPEND = 40

assert INTEREST_SPEND / INTEREST_PURCH > KILL_CPA

DAILY_ACCOUNT = [58.20, 62.40, 61.80, 60.50, 59.10, 58.72, 57.60]
assert abs(sum(DAILY_ACCOUNT) - (BROAD_SPEND + INTEREST_SPEND)) < 0.02

# D6-D7 account spend = Broad only
b_d67 = DAILY_ACCOUNT[5] + DAILY_ACCOUNT[6]
b_d15 = BROAD_SPEND - b_d67
# Interest all in D1-D5
i_total = INTEREST_SPEND

# D1-D5 split interest heavier toward D4-D5 until kill pause end of D5
i_daily = [38.0, 42.0, 44.0, 48.0, i_total - (38 + 42 + 44 + 48)]
b_daily = [DAILY_ACCOUNT[i] - (i_daily[i] if i < 5 else 0) for i in range(7)]
b_daily[5] = DAILY_ACCOUNT[5]
b_daily[6] = DAILY_ACCOUNT[6]

for i in range(5):
    b_daily[i] = round(DAILY_ACCOUNT[i] - i_daily[i], 2)
b_daily[5] = round(DAILY_ACCOUNT[5], 2)
b_daily[6] = round(DAILY_ACCOUNT[6], 2)
i_daily = [round(x, 2) for x in i_daily]

assert abs(sum(b_daily) - BROAD_SPEND) < 0.05
assert abs(sum(i_daily) - INTEREST_SPEND) < 0.05

dates = [f"2026-10-{4 + i:02d}" for i in range(7)]
b_cum = i_cum = 0.0
b_p = [0, 0, 0, 1, 2, 4, 5]
i_p = [0, 0, 0, 1, 2, 2, 2]  # Interest: 2 purchases by end D5; D6–D7 spend 0

adset_daily_lines = [
    "date,ad_set_name,spend_usd_day,spend_usd_cum,purchases_cum,cpa_usd_cum,note"
]
for i in range(7):
    b_cum += b_daily[i]
    if i < 5:
        i_cum += i_daily[i]
    day_i = i_daily[i] if i < 5 else 0.0
    notes_b = [
        "D1 learning",
        "D2",
        "D3 hold",
        "D4 Interest CPA drift",
        "D5 hit kill rule pause Interest",
        "D6 Broad +20%",
        "D7 close scale Broad",
    ]
    notes_i = [
        "D1 learning",
        "D2",
        "D3",
        "D4 spend cum review",
        "D5 kill: spend>40 CPA>82.5 then pause",
        "D6 paused spend 0",
        "D7 paused spend 0",
    ]
    for name, day_s, cum, p, note in [
        ("Broad-US-25-54-ADV+", b_daily[i], b_cum, b_p[i], notes_b[i]),
        ("Interest-Cooking-US", day_i, i_cum, i_p[i], notes_i[i]),
    ]:
        cpa = f"{cum / p:.2f}" if p else ""
        adset_daily_lines.append(
            f"{dates[i]},{name},{day_s:.2f},{cum:.2f},{p},{cpa},{note}"
        )

daily_account_lines = [
    "date,spend_usd,impressions,clicks,ctr_pct,cpc_usd,purchases,cpa_usd,phase_note"
]
acc_p = [0, 1, 2, 2, 3, 5, 7]  # 7 total purchases
notes = [
    "D1 launch learning",
    "D2 first purchase",
    "D3 hold structure",
    "D4 interest CPA drift trim budget",
    "D5 pause Interest after kill rule",
    "D6 Broad +20% only",
    "D7 close week",
]
for i, sp in enumerate(DAILY_ACCOUNT):
    p = acc_p[i]
    cpa = f"{sp / (p - acc_p[i - 1]):.2f}" if i > 0 and p > acc_p[i - 1] else ""
    if i == 0:
        cpa = ""
    elif p == acc_p[i - 1]:
        cpa = ""
    else:
        day_p = p - acc_p[i - 1]
        cpa = f"{sp / day_p:.2f}" if day_p else ""
    daily_account_lines.append(
        f"{dates[i]},{sp:.2f},,,,,{p},{cpa},{notes[i]}"
    )

adset_summary = """ad_set_name,spend_usd,impressions,clicks,ctr_pct,cpc_usd,purchases,cpa_usd,frequency,decision,decision_rule_ref
Broad-US-25-54-ADV+,198.40,45200,610,1.35,0.33,5,39.68,2.1,scale,CPA <= 55 guardrail and freq < 2.5
Interest-Cooking-US,219.92,41200,445,1.08,0.49,2,109.96,2.3,kill,spend > 40 and CPA > 82.5 (paused end D5)
"""

creative = """ad_name,ad_set,spend_usd,impressions,clicks,ctr_pct,purchases,cpa_usd,note
VID-Outcome30s-v1,Broad-US-25-54-ADV+,112.30,25800,352,1.37,3,37.43,winner hook Broad
VID-SpecPower-v1,Broad-US-25-54-ADV+,86.10,19400,258,1.33,2,43.05,secondary Broad
VID-Outcome30s-v1,Interest-Cooking-US,98.50,18600,210,1.13,1,98.50,same video audience mismatch
STATIC-PriceAnchor-v1,Interest-Cooking-US,121.42,22600,235,1.04,1,121.42,supporting ad on Interest only
"""

paths = [
    ROOT / "adset-daily.csv",
    ROOT / "daily-account.csv",
    ROOT / "adset-summary.csv",
    ROOT / "creative-summary.csv",
    ROOT / "data" / "adset-daily.csv",
    ROOT / "data" / "daily-account.csv",
    ROOT / "data" / "adset-summary.csv",
    ROOT / "data" / "creative-summary.csv",
    ROOT / "cases/dtc-meta-7day-demoblend/data/adset-daily.csv",
    ROOT / "cases/dtc-meta-7day-demoblend/data/daily-account.csv",
    ROOT / "cases/dtc-meta-7day-demoblend/data/adset-summary.csv",
    ROOT / "cases/dtc-meta-7day-demoblend/data/creative-summary.csv",
]

(ROOT / "adset-daily.csv").write_text("\n".join(adset_daily_lines) + "\n", encoding="utf-8")
(ROOT / "daily-account.csv").write_text("\n".join(daily_account_lines) + "\n", encoding="utf-8")
(ROOT / "adset-summary.csv").write_text(adset_summary, encoding="utf-8")
(ROOT / "creative-summary.csv").write_text(creative, encoding="utf-8")

for p in paths:
    if p.name == "adset-daily.csv":
        p.write_text((ROOT / "adset-daily.csv").read_text(encoding="utf-8"), encoding="utf-8")
    elif p.name == "daily-account.csv":
        p.write_text((ROOT / "daily-account.csv").read_text(encoding="utf-8"), encoding="utf-8")
    elif p.name == "adset-summary.csv":
        p.write_text(adset_summary, encoding="utf-8")
    elif p.name == "creative-summary.csv":
        p.write_text(creative, encoding="utf-8")

print("OK broad", sum(b_daily), "interest", sum(i_daily), "purch", acc_p[-1])
