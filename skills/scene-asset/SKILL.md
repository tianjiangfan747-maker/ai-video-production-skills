---
name: scene-asset
description: 建立可复用 AI 影视场景的空间合同、Clean Plate、镜头区域、出入口、主光与关键锚点，保证换机位时空间不被重新发明
type: prompt
whenToUse: 当用户需要创建电影场景、环境参考图、Clean Plate、空间连续性资产或人物走位空间时
---

# Scene Asset

## 1. 先建立空间合同

至少记录：
`location_id / geography / anchor_objects / entry_exit / camera_zones / axis / light_direction / world_time / weather / palette`

## 2. Clean Plate 优先

默认纯场景，不自动嵌入人物。需要 previs 时另建，不污染主 Clean Plate。

## 3. Reference set 按用途生成

可能需要：Master Wide / Reverse / Side or High / Detail Plate / Clean Plate。不是每个场景都机械生成全部视图。

## 4. 摄影机区域

运镜场景需要明确哪些位置可站机、哪些物体可作为 foreground occlusion carrier、人物如何进出。

## 5. 光线与材质

锁定会跨镜头变化的主光源与材质信息；动态光影必须有物理原因。

## 6. 输出

先输出空间合同 + 参考图计划，再输出实际图像 Prompt。不要用“8K/极致/工业级”替代空间结构。

## 参考资料

空间合同字段细则：`${KIMI_SKILL_DIR}/references/scene-contract.md`。
