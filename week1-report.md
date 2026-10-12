# Week-1 Purchase Test - DemoBlend One - United States

Report: closed test, Meta Ads (Facebook / Instagram)  
Period: 2026-10-04 to 2026-10-10 (7 days)  
Advertiser: DemoBlend One (fictional DTC blender, ~$89 AOV, no real store)  
Objective: Purchase  
Data: methodology simulation (not Ads Manager export)

Files: [daily-account.csv](./daily-account.csv) | [adset-daily.csv](./adset-daily.csv) | [adset-summary.csv](./adset-summary.csv) | [creative-summary.csv](./creative-summary.csv) | [account-structure.md](./account-structure.md)

---

## Executive summary

Week-one spend **$418.32** on Purchase: **two ad sets** — **Broad** vs **Interest (cooking)**. Two video hooks compared **inside Broad only**. **Broad won; Interest killed end of D5.** From **D6**, only Broad spends. Account **7 purchases, CPA $59.76** mixes cells — **decide by ad set CPA, not account average.**

| Ad set | 7d spend | Purchases | CPA | Call |
|--------|----------|-----------|-----|------|
| Broad-US-25-54-ADV+ | $198.40 | 5 | $39.68 | Scale +20% from D6 |
| Interest-Cooking-US | $219.92 | 2 | $109.96 | Kill end D5; $0 spend D6–D7 |

Next: Broad only, add **UGC-POV-v2** (one variable).

---

## Test design (before spend)

| Parameter | Choice |
|-----------|--------|
| Primary KPI | Purchase CPA |
| Guardrail (scale reference) | CPA <= $55 on ad set |
| Kill rule | **Ad set spend > $40 and CPA > $82.5** → pause that ad set |
| Variables | Audience first (Broad vs Interest), then hook test inside Broad only |

Interest met kill rule on **D5** (cum spend $219.92, CPA $109.96). **Paused before D6.**

---

## Daily account

See [daily-account.csv](./daily-account.csv). [adset-daily.csv](./adset-daily.csv) shows **Interest spend = 0 on D6–D7**.

| Day | Spend | Purch. | Note |
|-----|-------|--------|------|
| D1 | $58.20 | 0 | Launch |
| D2 | $62.40 | 1 | First purchase |
| D3 | $61.80 | 1 | Hold |
| D4 | $60.50 | 2 | Interest CPA drift; trim Interest |
| D5 | $59.10 | 3 | Kill rule → **pause Interest** |
| D6 | $58.72 | 5 | **Broad only**, +20% budget |
| D7 | $57.60 | 7 | Close week |

---

## Ad set post-mortem

See [adset-summary.csv](./adset-summary.csv).

**Broad:** CPA $39.68. Scale.

**Interest:** Same Outcome video **$98.50 CPA** on Interest vs **$37.43** on Broad → audience mismatch. **CPA $109.96** at ad set level → kill. No spend after D5.

---

## Creative layer

See [creative-summary.csv](./creative-summary.csv) — **4 ads** (2 on Broad, 2 on Interest). Week-2 **UGC-POV** is Broad-only.

**Broad hooks:** Outcome $37.43 vs Spec $43.05.

---

## Week 2

1. Broad only, keep +20% direction.  
2. Ship UGC-POV-v2.  
3. Do not reopen Interest unless Broad breaks guardrail.

---

## Disclaimer

Fictional brand and simulated numbers. Shows test structure and kill/scale rules used on live accounts.
