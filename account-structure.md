# Account structure (DemoBlend simulation)

```
Campaign  [TEST][202610][Purchase] DemoBlend-US
  Objective: Sales
  Budget: ad set level, ~$70/day cap (test)

  Ad set  Broad-US-25-54-ADV+
    Ad  VID-Outcome30s-v1
    Ad  VID-SpecPower-v1

  Ad set  Interest-Cooking-US
    Ad  VID-Outcome30s-v1
    Ad  STATIC-PriceAnchor-v1

  Ad set  Interest-Cooking-STATIC-only
    Ad  STATIC-PriceAnchor-v1
```

Week 1: **3 ad sets** (1 Broad + 2 Interest variants). Hook A/B only on Broad. Interest ads exist to run the audience stack and to compare the same Outcome video vs Broad ([creative-summary.csv](./creative-summary.csv)). Week 2 adds **UGC-POV-v2 on Broad only**.

Tracking (simulation): Pixel + CAPI, Purchase event, GA4 within 12% of Meta.

Full report: [week1-report.md](./week1-report.md)
