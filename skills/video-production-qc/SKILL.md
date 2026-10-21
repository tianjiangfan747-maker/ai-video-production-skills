---
name: video-production-qc
description: 对 AI 视频 take 做分层验收、失败诊断、最低成本返修与连续失败升级，避免无休止重抽
type: prompt
whenToUse: 当视频已经生成、用户反馈脸变了/动作错/空间错/镜头乱/像 PPT/接不上，或需要建立生成验收流程时
---

# Video Production & QC

## 1. 交付对象是时间线

漂亮单帧 ≠ 合格 take。优先审完整运动和相邻镜头。

## 2. 三道门

### Gate A：单镜头
身份、空间、动作、摄影机、结束态。

### Gate B：相邻镜头
handoff、screen direction、eyeline、道具状态、光线/天气。

### Gate C：时间线
节奏、镜头功能、音画桥、剪辑边界、重复镜头。

## 3. Failure Codes

- F1 Identity drift
- F2 Spatial/axis error
- F3 Action failure
- F4 Camera failure
- F5 Reference conflict
- F6 Handoff failure
- F7 Style/lighting drift
- F8 Platform capability mismatch
- F9 Edit/sound bridge failure

## 4. 修复梯子

资产 → blocking/continuity → keyframe → Prompt → 参数/平台适配 → 换平台/重做。

一次只改导致问题的主要变量。

## 5. 连续失败规则

同一问题第二次失败先改变变量；第三次失败前必须改变控制层、参考策略、镜头拆分或平台，而不是复制原 Prompt。

## 6. 验收输出

`diagnosis / root_cause / cheapest_fix / revised_shot / acceptance_criteria`

## 参考资料

各失败码的症状与首选修复：`${KIMI_SKILL_DIR}/references/failure-modes.md`。
