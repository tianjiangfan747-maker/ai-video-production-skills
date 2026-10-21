---
name: prop-asset
description: 建立关键道具的可复用资产合同、状态变化、持握/挂载关系与镜头连续性，避免武器/手机/饰品/车辆等在镜头间漂移
type: prompt
whenToUse: 当镜头中存在重要道具、武器、手机、车辆、容器、饰品、机械部件，或道具状态会跨镜头变化时
---

# Prop Asset

## 1. 什么时候值得独立建道具

只要道具满足以下任一项：反复出现、推动剧情、与人物动作强交互、形状/纹理是识别点、状态会跨镜头变化，就应建立道具合同。

## 2. Prop Contract

`prop_id / design_anchors / scale / material / owner / attachment_point / interaction_state / damage_state / quantity`

## 3. State

记录：新/旧、开/关、装/空、湿/干、破损程度、是否被拿在手中、挂在哪一侧、是否留在场景锚点。

## 4. 参考职责

道具参考只锁道具；不要为了展示道具把不必要的人物重新生成进去。

## 5. QC

特别检查：左右手、腰侧/背部挂点、物体大小、数量、损伤连续性、与场景固定位置的关系。
