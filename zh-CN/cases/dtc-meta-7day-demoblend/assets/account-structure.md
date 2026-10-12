# 账户结构示意（仿真）

```
Campaign  [TEST][202610][Purchase] DemoBlend-US
│  目标：销售
│  预算：广告组层级 · 测试期约 $70/天上限
│
├─ 广告组  Broad-US-25-54-ADV+（大范围）
│  ├─ 广告  VID-Outcome30s-v1
│  └─ 广告  VID-SpecPower-v1
└─ 广告组  Interest-Cooking-US（兴趣：烹饪）
   ├─ 广告  VID-Outcome30s-v1
   └─ 广告  STATIC-PriceAnchor-v1
```

**Week1 只有两个广告组对照**：Broad vs Interest。视频 A/B **只在 Broad 内**比；Interest 上挂 Outcome + 静态是为了能投出去，并用 **同一 Outcome 在 Broad $37.43 vs Interest $98.50** 说明是受众问题。

**关停（组级）：** 累计花费 **> $40** 且 CPA **> $82.5** → **D5 末暂停 Interest，D6–D7 不再花 Interest 预算**。

追踪（仿真）：Pixel + CAPI · 购物事件 · GA4 差异 <12%
