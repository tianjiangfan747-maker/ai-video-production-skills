---
name: edit-assembly
description: 把生成片段组织成可剪辑的 AI 影视时间线，负责镜头选择、连续性边界、动作/视线匹配、声音桥与最终交付检查
type: prompt
whenToUse: 当用户要把多个 AI 视频片段剪成连贯短片、处理镜头接法、节奏、J/L-cut、反应镜头或成片验收时
---

# Edit Assembly

## 1. 先看时间线

选择 take 以：叙事功能 → 可剪辑性 → 连续性 → 技术稳定性排序，不只看最好看的截图。

## 2. Boundary strategies

优先考虑：
- action match
- eyeline match
- screen-direction match
- composition match
- reaction
- insert / cutaway
- occlusion cut
- hard cut
- J-cut / L-cut

## 3. 节奏

镜头长度服务信息密度、动作完整度和情绪压力，不使用固定秒数模板。

## 4. 声音桥

脚步、动作声、环境声、台词尾音或音乐连续性可替代严格画面无缝。

## 5. 最终 QC

找到“观众第一次失去人物/空间/动作信任”的位置，从那个点修，而不是平均地修所有镜头。

## 参考资料

剪辑桥类型与边界细则：`${KIMI_SKILL_DIR}/references/edit-logic.md`。
