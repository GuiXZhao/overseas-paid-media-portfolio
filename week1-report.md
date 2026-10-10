# Week-1 Purchase Test - DemoBlend One - United States

Report: closed test, Meta Ads (Facebook / Instagram)  
Period: 2026-10-04 to 2026-10-10 (7 days)  
Advertiser: DemoBlend One (fictional DTC blender, ~$89 AOV, no real store)  
Objective: Purchase  
Data: methodology simulation (not Ads Manager export)

Files: [daily-account.csv](./daily-account.csv) | [adset-summary.csv](./adset-summary.csv) | [creative-summary.csv](./creative-summary.csv) | [account-structure.md](./account-structure.md)

---

## Executive summary

Week-one spend about **$418** on Purchase: Broad vs Interest audiences, two hooks on Broad. **Broad won; Interest killed.** Account **8 purchases, CPA $52.29** mixes a good Broad cell with a dead Interest cell. **Decide by ad set CPA, not account average.**

| Ad set | 7d spend | Purchases | CPA | Call |
|--------|----------|-----------|-----|------|
| Broad-US-25-54-ADV+ | $198.40 | 5 | $39.68 | Scale +20% |
| Interest-Cooking-US | $156.20 | 2 | $78.10 | Kill |
| Interest-Cooking-STATIC-only | $63.72 | 1 | $63.72 | Off |

Next: Broad only, add **UGC-POV-v2** (one variable).

---

## Test design (before spend)

| Parameter | Choice |
|-----------|--------|
| Primary KPI | Purchase CPA |
| Guardrail CPA | <= $55 |
| Kill rule | CPA > $82.5 and spend > $40 on ad set |
| Variables | Audience first (Broad vs Interest), then hook on Broad |

Hypotheses: (1) Broad matches or beats Interest with same Outcome creative. (2) Outcome hook beats spec hook on Broad.

---

## Daily account

See [daily-account.csv](./daily-account.csv) for full series.

| Day | Spend | Purch. | Note |
|-----|-------|--------|------|
| D1 | $58.20 | 0 | Launch |
| D2 | $62.40 | 1 | First purchase |
| D3 | $61.80 | 1 | Hold |
| D4 | $60.50 | 2 | Trim Interest budget 15% |
| D5 | $59.10 | 1 | Pause Interest main |
| D6 | $58.72 | 2 | Broad budget +20% |
| D7 | $57.60 | 1 | Close week |

---

## Ad set post-mortem

See [adset-summary.csv](./adset-summary.csv).

**Broad:** CPA $39.68, enough spend to trust for week one. Scale.

**Interest:** Same Outcome video at $98.50 CPA vs $37.43 on Broad = audience problem. Kill before creative tests inside a bad cell.

---

## Creative (Broad)

See [creative-summary.csv](./creative-summary.csv).

Outcome30s CPA $37.43 vs SpecPower $43.05. Keep both; scale toward Outcome.

---

## Week 2

1. Broad only, +20% budget.  
2. Ship UGC-POV-v2, same audience and LP promise.  
3. Do not reopen Interest until Broad fatigues or CPA breaks guardrail.

---

## Disclaimer

Fictional brand and simulated numbers. Shows test structure and kill/scale rules used on live accounts.
