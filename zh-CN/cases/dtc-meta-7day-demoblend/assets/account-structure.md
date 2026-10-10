# 账户结构示意（仿真）

```
Campaign  [TEST][202610][Purchase] DemoBlend-US
│  目标：销售
│  预算：广告组层级 · 测试期约 $70/天上限
│
├─ 广告组  Broad-US-25-54-ADV+
│  ├─ 广告  VID-Outcome30s-v1
│  └─ 广告  VID-SpecPower-v1
├─ 广告组  Interest-Cooking-US
│  ├─ 广告  VID-Outcome30s-v1
│  └─ 广告  STATIC-PriceAnchor-v1
└─ 广告组  Interest-Cooking-STATIC-only
   └─ 广告  STATIC-PriceAnchor-v1
```

追踪（仿真）：Pixel + CAPI · 购物事件 · GA4 差异 <12%
