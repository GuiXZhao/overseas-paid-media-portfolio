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
```

Week 1: **two ad sets only** — Broad vs Interest (cooking interest). Hook compare **inside Broad** (two videos). Interest runs Outcome + one static so the cell can deliver volume; **same Outcome video** is compared to Broad for audience diagnosis. Week 2 adds **UGC-POV-v2 on Broad only**.

Kill (ad set): **spend > $40 and CPA > $82.5** → pause Interest from **D6** (rule met end of **D5**).

Tracking (simulation): Pixel + CAPI, Purchase event, GA4 within 12% of Meta.

Full report: [week1-report.md](./week1-report.md)
