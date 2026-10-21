---
name: image-control-pass
description: 诊断生图中风格、身份、结构或细节的失稳点，并选择最短的多阶段控制链，而不是机械跑完整流程
type: prompt
whenToUse: 当角色/场景一次生成同时控制风格、身份、比例、服装结构和细节失败，或需要更强图像控制时
---

# Image Control Pass

## 核心原则

先诊断“哪个维度失稳”，只增加那一层控制。

## 控制层

- Style Master
- Identity Master
- Silhouette / Color Block
- White / Gray Blockout
- Line / Mask
- Final Fusion

## 角色

简单真人：Style → Identity → Final

风格化角色：Style → Identity → Silhouette → Final

复杂玄幻/机甲：Style → Identity → Silhouette → Blockout → Line/Mask → Final

## 场景

不要照搬角色链。场景重点：Style → Spatial Master → White Spatial Blockout → Lighting Logic → Material → Clean Plate。

## 规则

失败原因是什么就增加什么控制层；不要因为“看起来专业”强制生成六张中间图，也不要把 Prompt 越写越长当成默认修复策略。

## 参考资料

失败点与控制层对照表：`${KIMI_SKILL_DIR}/references/control-decision.md`。
