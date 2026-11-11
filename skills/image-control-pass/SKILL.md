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

## MJ 风格探索分支（按需）

当目标是先找到鲜明、统一的视觉风格，或现有画面“准确但缺少记忆点”时，可把 Midjourney 用于 **Style Master / 风格资产母版探索**，再进入现有最短控制链。不是所有项目都要加这一阶段。

1. 固定一个主体或场景，少量探索不同风格方向；先选方向，再细化材质与光线。
2. 选定 Style Master，记录可复用的风格合同：媒介/笔触、配色、造型比例、材质、主光与背景处理。
3. 将风格参考、主体/身份参考、构图/空间参考分开管理；每种参考只承担它的职责。
4. 风格成立后，仍用 Identity Master 管角色，用 Spatial Master/Blockout 管空间，不能假设 MJ 风格参考天然保证跨镜头身份或结构一致。
5. 向 `character-asset`、`scene-asset` 或视频关键帧交接时，传风格合同与已选图，不把探索期的整段形容词重复塞进每镜。

MJ 的具体参数、版本支持和参考图组合方式保持可配置，以实际可用的官方功能为准；不把未经验证的版本参数写死进项目。操作与交接模板见 `references/midjourney-style-assets.md`。

## 参考资料

失败点与控制层对照表：`${KIMI_SKILL_DIR}/references/control-decision.md`。

MJ 风格母版与资产交接：`${KIMI_SKILL_DIR}/references/midjourney-style-assets.md`。
