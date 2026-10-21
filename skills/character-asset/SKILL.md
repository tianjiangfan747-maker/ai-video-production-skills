---
name: character-asset
description: 建立可持续复用的角色身份合同、16:9 四面参考板、服装/身体结构与状态变化，降低多镜头人物漂移
type: prompt
whenToUse: 当用户要创建角色、角色参考板、多角度角色资产、一致性资产，或需要修复人物身份/服装漂移时
---

# Character Asset

## 1. 四面自定义参考板（16:9 横版）

这是本项目唯一标准，不使用旧的“五视图”说法。

从左到右：
1. **正面头部身份参考**：脸、发际线、耳部、下颌与自然可见的颈肩连接。
2. **正面全身无头身体参考**：从颈部基底以上干净裁切，只显示身体、服装和鞋，不产生伤口/断头感。
3. **完整侧面全身**：验证头部轮廓、体积、衣物前后层次。
4. **完整背面全身**：验证后脑、后领、肩背、服装背面和后部配件。

第一格承担身份；第二格承担身体/服装控制；侧面与背面负责三维验证。

## 2. Identity Contract

建立：
`character_id / identity_anchors / body_proportions / wardrobe / hair / props / locked_features / variable_states / forbidden_changes`

不要承诺“100% 像素一致”，而要让锚点可验证。

## 3. Locked vs Variable

**Locked**：脸型、眼鼻口关系、发际线、体型、服装核心结构、关键配件、非人类关键生理结构。

**Variable**：表情、姿态、动作、湿、脏、血迹、轻微破损、服装状态、道具状态。

Canonical identity 不因为剧情状态变化而被重写。

## 4. Reference-first

角色图负责身份；场景图负责空间；风格图负责视觉语言；动作参考负责运动。冲突时显式指定主参考。

## 5. 生图策略

简单真人不强制多阶段；复杂玄幻/机甲/风格化角色才调用 `image-control-pass`。

## 6. QC

检查：四面是否同一身份、Panel 2 是否真正干净无头、体型/服装结构是否一致、侧背面有没有破坏关键识别点、图板是否 16:9 且职责清楚。

## 7. 交付纪律

没有真实视觉审核，不声称“已经通过一致性验收”。

## 参考资料

合同字段与 QC 清单细则：`${KIMI_SKILL_DIR}/references/character-contract.md`。
