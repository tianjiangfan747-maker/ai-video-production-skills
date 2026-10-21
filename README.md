# AI 视频制作

小范同学的个人 AI 视频制作辅助 Skill 合集。

一套覆盖 **AI 广告 / 短视频创作全流程** 的个人辅助技能包：创意 → 剧本分镜 → 角色/场景/道具资产 → 生成 Prompt → 风格与质感增强 → 成片 QC → 剪辑交付。共 **18 个技能**，配套一套开源 prompt 知识库（自动拉取）。这些是我日常做广告项目时自用的一套辅助工具，分享给有需要的人。适配 Kimi Work / Kimi Code。

## 技能清单

### A. 全流程主线（11 个，按使用顺序）

| 技能 | 干什么用 |
|---|---|
| `creative-campaign-director` | 一句话启动广告/宣传片创意：受众洞察 → 创意概念 → 分镜 → 文案 → 制作计划 |
| `film-director-orchestrator` | 项目总导演：判断当前阶段、锁定项目事实、分配职责、控制返修与交付 |
| `storyboard-director` | 剧本/场景 → 节拍、blocking、coverage、镜头卡与连续性方案 |
| `character-asset` | 角色身份合同 + 四面参考板，防多镜头人物漂移 |
| `scene-asset` | 场景空间合同、Clean Plate、机位区域、主光锚点 |
| `prop-asset` | 关键道具的资产合同与跨镜头状态管理 |
| `style-quality-boost` | 质感提升（光线/材质/镜头/色彩/运动五层诊断）+ 六方向风格库（多巴胺/网红/复古胶片/怪诞超现实/极简高级/手绘混合） |
| `shot-execution` | 把定好的镜头编译成平台中性的 AI 视频生成 Prompt（I2V/T2V/R2V） |
| `image-control-pass` | 生图失控时诊断并选择最短的多阶段控制链 |
| `video-production-qc` | 成片分层验收、失败诊断、最低成本返修 |
| `edit-assembly` | 生成片段 → 可剪辑时间线：镜头接续、J/L-cut、声音桥、交付检查 |

### B. 模型与 Prompt 工具（7 个）

| 技能 | 干什么用 |
|---|---|
| `model-selector` | 按需求选视频生成模型（16 个主流模型对比决策树） |
| `prompt-translator` | 同一条 prompt 跨模型转换（基于 110 条对照基准查表） |
| `seedance-prompter` | 即梦 Seedance 2.0 专用 prompt 公式与模板 |
| `seedance-storyboard` | 即梦多镜头分镜拆分 |
| `seedance-debugger` | 即梦生成失败 12 类问题诊断修复 |
| `kling-prompter` | 可灵 Kling 3.0 三套写法（基础/进阶/图生视频） |
| `happyhorse-prompter` | HappyHorse 紧凑短片 + 原生音频 prompt |

## 安装（2 分钟）

```bash
git clone https://github.com/tianjiangfan747-maker/ai-video-production-skills.git
cd ai-video-production-skills
python scripts/fetch-third-party.py   # 拉取第三方 prompt 知识库（MIT，来自 lanshu-awesome-ai-video-kit）
```

然后把 `skills/` 目录下的**全部内容**（18 个技能文件夹 + `_shared` 文件夹）复制到技能目录：

- **Kimi Work (Windows)**：`C:\Users\<用户名>\AppData\Roaming\kimi-desktop\daimon-share\daimon\skills\`
- **Kimi Work (macOS)**：`~/Library/Application Support/kimi-desktop/daimon-share/daimon/skills/`
- **Kimi Code**：`~/.kimi-code/skills/`

新开一个对话即可自动生效（技能按描述自动触发，无需手动调用）。

> ⚠️ `_shared/` 目录是 7 个模型工具技能引用的共享知识库（21 篇方法论 SOP + 600+ 条实测 prompt + 跨模型对照数据），请勿删除。
> 如果网络无法访问 GitHub，也可以手动 clone [cclank/lanshu-awesome-ai-video-kit](https://github.com/cclank/lanshu-awesome-ai-video-kit)，把其中的 `methodology/`、`prompts/`、`tools/` 和根目录的 `RESOURCES.md`、`CONTRIBUTING.md`、`LICENSE`、`README.md` 复制到 `skills/_shared/lanshu-kit/`。

## 典型用法（自然语言直接说）

- "我有一句广告创意，帮我推进到可执行方案" → creative-campaign-director
- "这场戏怎么拍？做分镜和镜头表" → storyboard-director
- "给这个角色建参考板，后面镜头不能变脸" → character-asset
- "这个镜头帮我写成即梦能用的 prompt" → shot-execution + seedance-prompter
- "这条视频画面太平了，提升质感、做得更风格化" → style-quality-boost
- "生成的视频脸变了/接不上，帮我诊断" → video-production-qc / seedance-debugger
- "把这些片段剪成连贯短片" → edit-assembly

## 版权说明

- A 组 11 个技能（`creative-campaign-director`、`film-director-orchestrator`、`storyboard-director`、`character-asset`、`scene-asset`、`prop-asset`、`style-quality-boost`、`shot-execution`、`image-control-pass`、`video-production-qc`、`edit-assembly`）为个人自建，可自由使用、修改、再分发。
- B 组 7 个技能及 `_shared/lanshu-kit/` 知识库改写自开源项目 [cclank/lanshu-awesome-ai-video-kit](https://github.com/cclank/lanshu-awesome-ai-video-kit)，**MIT License**（`fetch-third-party.py` 拉取后见 `skills/_shared/lanshu-kit/LICENSE`），按许可证保留版权声明即可自由使用。
