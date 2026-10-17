# Sheriaties/adaptive-learning-skill（中文）

- 链接：https://github.com/Sheriaties/adaptive-learning-skill
- 作者：Sheriaties
- 仓库说明：自适应学习 skill for Claude Code — 防止「读了就以为懂了」，把学习过程变成 资料搜集→理解验证→Obsidian 知识网络 的完整闭环
- 星数：3
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# adaptive-learning

> 一个自适应学习 skill —— 把"想学 X"变成一条从资料搜集、理解验证到 Obsidian 知识网络的完整闭环。

支持 [Claude Code](https://github.com/anthropics/claude-code) / [OpenClaw](https://github.com/openclaw/openclaw) / [Hermes Agent](https://github.com/NousResearch/hermes-agent)（遵循 [agentskills.io](https://agentskills.io) 标准）。每个 session 结尾会加「喵」。

---

## 是什么

`adaptive-learning` 是一个 agent skill。当你说"我想搞懂 X"，它会：

1. **分层前置**：找出理解 X 之前必须先懂的概念，按依赖关系分 2-4 层呈现
2. **让你选**：每个前置概念你可以选 详细学 / 简略了解 / 跳过 / 已掌握
3. **递归学习**："详细学"会把那个前置当成新目标重新走一遍流程，递到底再回来
4. **理解验证**：先在对话里讲一遍，再开放答疑，最后小测——通过才算学会
5. **写入 Obsidian**：所有概念笔记都写在 `03_Knowledge_Network/`，状态由 `understanding:` 字段 + tag 表达（黄=待验证、浅绿=简略、深绿=已掌握）。资料原文留在 `00_Sources/`。每个用户主动请求的学习根目标会自动生成一份 `04_MOC/` 学习地图，记录这次学习涉及哪些前置、各自状态。
6. **图谱可视化**：通过 Obsidian Graph View 颜色（黄=待验证、浅绿=简略、深绿=已掌握）一眼看到学习状态

核心价值不是"让 AI 帮你写笔记"，而是**防止"读了就以为懂了"的伪学习污染你的知识网络**。

---

## 安装

### 前置要求

支持的 agent 框架（任选一个）：
- [Claude Code](https://github.com/anthropics/claude-code) CLI
- [OpenClaw](https://github.com/openclaw/openclaw)
- [Hermes Agent](https://github.com/NousResearch/hermes-agent)（OpenClaw 的官方继任）

笔记浏览：
- [Obsidian](https://obsidian.md/)（用来浏览 Vault 和看 Graph View）

> **格式说明**：本 skill 遵循 [agentskills.io](https://agentskills.io) 的 `SKILL.md` 开放标准。同一份代码三个生态都能跑，只是安装路径和触发方式略有差异。

### 两种安装方式

**方式 A：命令行一键装**（推荐）。一条命令完成 clone + 触发器注册（如适用），全程无需手贴任何文件：

```bash
curl -fsSL https://raw.githubusercontent.com/Sheriaties/adaptive-learning-skill/main/install.sh | bash
```

脚本会自动检测你装的是 Claude Code / OpenClaw / Hermes 中的哪一个，clone 到对应的 skills 目录。如果同时装了多个，按 `Hermes > OpenClaw > Claude Code` 优先级；想强制选一个：

```bash
curl -fsSL https://raw.githubusercontent.com/Sheriaties/adaptive-learning-skill/main/install.sh | bash -s -- --target=claude
# --target 可选值: claude / openclaw / hermes
```

**方式 B：对话内安装**（适合不想敲命令的用户，让 agent 帮你做）——把下面这段话发给你的 agent，它会自动 clone 仓库并启动 onboarding：

> 帮我安装 adaptive-learning skill：
> 1. 检测我用的是 Claude Code / OpenClaw / Hermes 中的哪一个
> 2. 把 https://github.com/Sheriaties/adaptive-learning-skill.git clone 到对应的 skills 目录
> 3. 如果是 Claude Code，把 SKILL.md 顶部的 `# adaptive-learning skill` 触发器段追加到 ~/.claude/CLAUDE.md（先 grep 查重避免重复）
> 4. 完成后立刻读 SKILL.md 里的 "Step -1: Onboarding 对话" 段落，按那个脚本问我配置问题，最后生成 config.json + 创建 Vault 目录结构

> 三个生态对应的 skill 安装路径：
> - Claude Code → ~/.claude/skills/adaptive-learning/
> - OpenClaw → ~/.openclaw/workspace/skills/adaptive-learning/
> - Hermes Agent → ~/.hermes/skills/adaptive-learning/

**两种方式装完后都一样**：第一次说「我想学 X」时，agent 会先跑 onboarding 对话问你 3 个问题（Vault 路径、状态目录、session 尾巴字符），然后自动创建配置文件和 Vault 目录。**全程不需要手写任何 JSON 或粘贴任何配置。**

---

### 高级：手动安装（不想用脚本）

如果你不想跑 install.sh，下面是各生态的手动 clone 命令。

#### Claude Code

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/Sheriaties/adaptive-learning-skill.git ~/.claude/skills/adaptive-learning
```

并在 `~/.claude/CLAUDE.md` 追加触发器（install.sh 自动做的就是这一步）：

```markdown
# adaptive-learning skill
- **adaptive-learning** (`~/.claude/skills/adaptive-learning/SKILL.md`) - 自适应学习工作流，资料搜集→理解验证→Obsidian 知识整合。Trigger: `/adaptive-learning`
When the user types `/adaptive-learning`, invoke the Skill tool with `skill: "adaptive-learning"` before doing anything else.
Also invoke when user expresses learning intent with phrases like: 想深入学习、想搞懂、系统学习、学习...架构、想深度学、从零开始学。
```

然后在 Claude Code 里直接说「我想学 X」即可触发 onboarding。

#### OpenClaw

```bash
mkdir -p ~/.openclaw/workspace/skills
git clone https://github.com/Sheriaties/adaptive-learning-skill.git ~/.openclaw/workspace/skills/adaptive-learning
```

OpenClaw 会自动发现 `workspace/skills/` 下的 SKILL.md，无需手动注册。在对话里用 `/adaptive-learning` 触发，或直接说"我想学 X"。

也可以从 [ClawHub](https://clawhub.ai)（OpenClaw 官方 skills registry）发布后供他人一键安装。

#### Hermes Agent

```bash
mkdir -p ~/.hermes/skills
git clone https://github.com/Sheriaties/adaptive-learning-skill.git ~/.hermes/skills/adaptive-learning
```

或放进 `~/.hermes/skills/openclaw-imports/`（如你已有 OpenClaw 习惯，统一管理）。

在 Hermes 里用 `/skills` 命令查看已注册 skills；用 `/adaptive-learning` 触发或表达学习意图自动触发。Hermes 还支持从 [agentskills.io](https://agentskills.io) 发现并安装。

---

## 配置

**通常你不需要手写 config.json**——首次运行 skill 时 agent 会通过对话引导你填，自动生成。下面只是字段说明，给想手动改的高级用户参考。

| 字段 | 含义 | 默认 |
|---|---|---|
| `vault_path` | Obsidian Vault 根目录 | `~/Documents/LearningVault/` |
| `state_dir` | 学习状态目录（含 user_profile.json + current_session.json） | `./.adaptive-learning/`（相对当前项目 cwd） |
| `session_suffix` | 每个 session 结尾追加的字符 | `喵`（设 `""` 关闭） |

**为什么 state_dir 默认相对 cwd？** 让每个项目维护自己的学习状态，跨项目不会互相污染。建议把 `.adaptive-learning/` 加入项目 `.gitignore`。如果你想多个项目共享一份学习画像，把 state_dir 改成绝对路径即可（例如 `~/.adaptive-learning/`）。

### Vault 目录结构

onboarding 完成时 agent 会**自动**在 `vault_path` 下 `mkdir -p` 出下面四个目录，并把笔记模板拷到 `99_Templates/`。**你不需要手动建任何目录**：

```
LearningVault/                  ← 你在 onboarding 时填的 vault_path
├── 00_Sources/                 ← 原始资料（仅联网模式）
│   └── <资料标题>.md            （frontmatter 含 source URL，2-3 句要点 + 与主题的关系）
│
├── 03_Knowledge_Network/       ← 全部概念笔记，state 由 frontmatter 表达，不靠目录区分
│   ├── <概念A>.md  (黄 pending-verify)   ← 占位 / 待验证
│   ├── <概念B>.md  (浅绿 understanding/brief)  ← 简略了解
│   └── <概念C>.md  (深绿 understanding/full)   ← 充分理解
│
├── 04_MOC/                     ← 学习地图，每个用户主动请求的根目标自动生成一份
│   └── <根目标> MOC.md          （记录前置层级、状态汇总，跟随学习进度自动更新）
│
└── 99_Templates/               ← agent 写笔记时参考的模板
    └── knowledge-note-template.md
```

另外在 `state_dir`（默认是当前项目 cwd 下的 `./.adaptive-learning/`）会有：

```
.adaptive-learning/             ← 学习状态（建议加进项目 .gitignore）
├── user_profile.json           ← 长期学习画像（已掌握的概念集合、学习历史）
└── current_session.json        ← 当前 session 的递归调用栈，用于断线恢复
```

**关键设计**：
- 概念的"已掌握 / 简略 / 待验证"状态完全由 `understanding:` 字段 + tag 表达，**不靠文件夹位置**——所以 03_Knowledge_Network 是单一目录，三种状态混在一起，靠 Graph View 颜色区分。
- 04_MOC 是导航层，不是知识本体——MOC 笔记不算"已学概念"，只是路径目录。
- 00_Sources 只在联网模式下使用；非联网模式不会有这个目录的内容。

### Obsidian Graph View 推荐配色

打开 Obsidian → Settings → Graph View → Groups，添加：

| Tag 查询 | 颜色 | 含义 |
|---|---|---|
| `tag:#understanding/full` | `#006400` 深绿 | 充分理解 |
| `tag:#understanding/brief` | `#5FF25F` 浅绿 | 简略了解 |
| `tag:#pending-verify` | `#FFFF00` 黄色 | 待确认 |
| `tag:#learning/root-request` | `#800080` 紫色 | 用户主动请求的根目标 |
| `tag:#moc` | `#FFA500` 橙色 | 学习地图（MOC，导航笔记） |

---

## 用法

在 Claude Code 里直接说想学什么：

```
/adaptive-learning 我想搞懂 Transformer 架构
```

或者直接用自然语言：

```
我想深入学习一下 Self-Attention
```

skill 会引导你完成：搜索决策 → 前置分层 → 你选学习粒度 → 资料搜集 → 讲课 → 答疑 → 小测 → 写入知识网络。

---

## 已知限制

- **目前仅支持中文 UI**：所有提示和笔记模板是中文。
- **不做自动去重**：v0.1 只用文件名查重 + `aliases` 字段。Vault 超过 200 篇笔记时建议接入第三方 dedup 工具。
- **不做图谱算法分析**：路径、孤立节点、社区检测请用 Obsidian 自带的 Graph View 或 [obsidian-graph-query](https://github.com/HEmile/juggl) 等成熟工具。
- **依赖模型自觉**：反幻觉守则、前置严格判定都是 prompt 层约束，不是硬保证。
- **session 断线恢复未完全实现**：v0.1 把递归栈写到 `<state_dir>/current_session.json`，但恢复路径还在打磨中。
- **不支持自动多设备同步**：如果 Vault 在 iCloud / Dropbox 上，注意路径含空格时所有 Bash 命令要加双引号。

---

## 设计原则

- **Occam's Razor**：能用一条 skill 规则解决的，不写工具
- **不重复造轮子**：Obsidian 读写、Markdown 规范、网页搜索都用现成能力
- **保持 skill 轻量**：`SKILL.md` 只管工作流，模板/范文/角色拆到子目录
- **小步迭代**：v0.1 不追求完美，先能跑

完整设计哲学见 `SKILL.md` 顶部和 [evaluator role](.claude/roles/evaluator.md)（如果你 fork 时带过来）。

---

## 反馈

- Bug / 改进建议：开 GitHub Issue
- 你自己的 Vault 用法、你的 Obsidian 配色截图：欢迎在 Discussions 分享

---

## License

MIT。详见 [LICENSE](LICENSE)。


## 文件 SKILL.md

---
name: adaptive-learning
description: "自适应学习工作流 — 从资料搜集、理解验证到 Obsidian 知识整合的完整学习闭环。当用户表达学习意图时触发（「想深入学习」「想搞懂」「系统学习」「学习...架构」等）。"
trigger: /adaptive-learning
---

# /adaptive-learning

自适应学习工作流。帮助用户完成从资料搜集、理解验证到知识整合的完整学习闭环。

**使用语言**：全程中文。每个 session 结尾加「喵」。

**教学人格**：执行本 skill 时必须先读 `<skill_root>/roles/teacher.md`，按 v3.2 对话教学指南行事。核心原则：
- 目标是学会，不是解决问题
- 教学有两种模式：阐述（exposition）和探索（exploration），不要混淆
- 不要直接给答案、不要堆方案、不要急于推进
- 笔记是讲义，对话窗口是课堂——必须当面讲一遍

## 环境配置

skill 启动时**第一件事**：检查 `<skill_root>/config.json` 是否存在。

- **不存在** → 进入 **Step -1: Onboarding 对话**（见下文），由 agent 引导用户生成 config.json + 创建 Vault 目录结构。
- **存在** → 读取后直接进入 Step 0。

`<skill_root>` 取决于你用的 agent 框架，常见位置：
- Claude Code: `~/.claude/skills/adaptive-learning/`
- OpenClaw: `~/.openclaw/workspace/skills/adaptive-learning/`
- Hermes Agent: `~/.hermes/skills/adaptive-learning/`（或 `~/.hermes/skills/openclaw-imports/adaptive-learning/`）

config.json 字段：
- `vault_path`：Obsidian Vault 根目录。
- `state_dir`：学习状态目录，存放 `user_profile.json` 和 `current_session.json`。**默认相对当前项目 cwd**（`./.adaptive-learning/`），让每个项目维护自己的学习状态。绝对路径也可。
- `session_suffix`：每个 session 结尾追加的字符（默认 `喵`，设为 `""` 可关闭）。

**Bash 注意**：vault_path 若含空格（如 iCloud 同步路径），所有 Bash 命令必须用双引号包裹路径。

- **模板文件**：`<skill_root>/templates/knowledge-note-template.md`
- **参考范文**：`<skill_root>/references/` 目录

---

## Step -1: Onboarding 对话（首次启动 / config.json 不存在时）

agent 在对话窗口里**主动**问用户三个问题，每问一个等用户回复，最后一次性 Write `<skill_root>/config.json` + 创建 Vault 目录结构。

**对话脚本**（agent 严格按这个开场白和顺序，**不要**改写问题或合并问题）：

**默认值的真值源**：所有问题里的"默认值"**必须**先 Read `<skill_root>/config.example.json` 取对应字段的值，不要在 SKILL.md 里硬编码默认值。这样将来改默认值只需改 example.json 一处。下面提示语里写的具体值仅作示例，agent 实际呈现给用户的提示**用 example.json 当前值替换**。

```
你好！这是 adaptive-learning skill 的首次启动配置，我会问你 3 个问题，
完成后你就可以直接说"我想学 X"开始学习。

问题 1/3：你的 Obsidian Vault 在哪？
（默认 <vault_path 来自 config.example.json>，回车采用默认；也可以填绝对路径）
```

收到回答 → 解析路径，处理 `~` 和相对路径。继续：

```
问题 2/3：学习状态文件（user_profile.json + current_session.json）放哪？
（默认 <state_dir 来自 config.example.json>，相对当前 cwd；也可以填绝对路径）

提示：默认值会让每个项目维护自己的学习状态，跨项目不会互相污染。
建议把 .adaptive-learning/ 加到项目 .gitignore，避免学习记录进 git。
```

收到回答 → 继续：

```
问题 3/3：每个 session 结尾的小尾巴字符？
（默认 <session_suffix 来自 config.example.json>，可以改成别的，留空表示不要）
```

收到回答 → 立刻执行：

1. **Write** `<skill_root>/config.json`（用三个回答）
2. **Bash** 创建 Vault 目录结构：
   ```bash
   mkdir -p "<vault_path>/00_Sources" \
            "<vault_path>/03_Knowledge_Network" \
            "<vault_path>/04_MOC" \
            "<vault_path>/99_Templates"
   ```
3. **Bash** 创建 state_dir：
   ```bash
   mkdir -p "<state_dir>"
   ```
4. **Bash** 把笔记模板拷到 Vault（让用户在 Obsidian 里能看到模板）：
   ```bash
   cp "<skill_root>/templates/knowledge-note-template.md" "<vault_path>/99_Templates/"
   ```
5. 向用户口头确认：

```
配置完成！
- Vault: <vault_path>（已创建 00_Sources / 03_Knowledge_Network / 04_MOC / 99_Templates）
- 状态目录: <state_dir>
- session 尾巴: <session_suffix 或"已关闭">

接下来：在 Obsidian 里打开这个 Vault，按 README 配置 Graph View 颜色（或随时让我帮你解释怎么配）。
现在告诉我你想学什么，我们开始吧。
```

**onboarding 完成后**，**不要**继续走 Step 0 学习流程——等用户**重新**说"我想学 X"再开始。理由：onboarding 是配置流程，和学习意图是两件事，混在一起容易让用户困惑。

## Vault 目录结构

```
LearningVault/
  00_Sources/           ← 原始资料（联网模式）
  03_Knowledge_Network/ ← 全部概念笔记（按 understanding tag 区分黄/浅绿/深绿三态）
  04_MOC/               ← 根目标 = MOC，由用户主动请求学习的根概念组成
  99_Templates/         ← 笔记模板
```

**为什么没有 02_Unknown？** 概念的"已掌握 / 简略 / 待验证"状态由 `understanding:` 字段 + tag 表达，不再用文件夹位置重复表达一遍。所有概念笔记从生命周期一开始就写到 `03_Knowledge_Network/`，验证通过时**原地覆写** frontmatter 即可（Edit 工具改 `understanding:` + tag），不需要在目录间搬来搬去。

## Obsidian Graph 颜色说明

| 颜色 | Tag | 含义 |
|------|-----|------|
| 深绿 `#006400` | `#understanding/full` | 充分理解，经过完整学习验证 |
| 浅绿 `#5FF25F` | `#understanding/brief` | 简略了解，知道是什么但没深入 |
| 黄色 `#FFFF00` | `#pending-verify` | 待确认，正文已写但未通过理解验证 |
| 紫色 `#800080` | `#learning/root-request` | 用户主动请求学习的根目标 |
| 橙色 `#FFA500` | `#moc` | 学习地图（MOC），由根目标自动生成 |

---

## Step 0: 搜索决策

**路径解析约定（贯穿全文）**：本文档中所有形如 `00_Sources/`、`03_Knowledge_Network/`、`04_MOC/`、`99_Templates/` 的相对路径，**一律相对 `<vault_path>` 解析**（`<vault_path>` 来自 config.json，由 onboarding 时用户填写）。agent 在执行 Read / Write / Edit / Bash 时**必须**把这些子路径前缀替换为 `<vault_path>/`，不要假设当前 cwd 是 vault 根目录——cwd 通常是用户的项目目录而非 vault。例如「在 `03_Knowledge_Network/` 创建笔记」实际操作是 `Write("<vault_path>/03_Knowledge_Network/<concept>.md", ...)`。

在学习前判断是否需要联网：

**不联网**（直接用模型知识）：通用基础知识、2025 年及之前已有共识的概念

**必须联网**：公司专有名词、模型无法给出完整答案、2025 年后新概念

```
用户想学 X
  ├─ X 是公开通用知识且 ≤2025？ → 不联网，直接写总结进 03_Knowledge_Network（带 pending-verify）
  ├─ X 是专有名词？ → 联网：WebSearch + WebFetch
  └─ 模型对 X 无法明确回答？ → 联网
```

---

## Step 1: 初始化

### 1.1 读用户状态
用 Read 工具读取 `<state_dir>/user_profile.json`（state_dir 来自 config），提取 `understanding: full/brief` 的概念集合。文件不存在则视为"无已知知识"。

### 1.2 澄清学习目标 + 创建 MOC（如果是根目标）
确认用户想学什么、为什么。判断是否为"用户主动请求的根目标"。

**根目标 = MOC**：如果是根目标，**立刻**在 `04_MOC/` 创建一个 MOC 笔记（同时给概念加 `#learning/root-request` tag）。MOC 是这次学习的"主题地图"，记录这个根目标下都学了哪些前置、各自处于什么状态。

写入前查重：先 `ls 04_MOC/ | grep -i "<concept>"`。已存在则覆写或追加（用户选）。

MOC 模板：

```markdown
---
title: [根目标名称] MOC
aliases: []
tags: [moc, learning/root-request, 概念标签]
date_started: [YYYY-MM-DD]
related:
  - "[[根目标名称]]"   # 指向根目标本身的概念笔记
---

# [根目标名称] 学习地图

> 本 MOC 由 adaptive-learning skill 自动维护。每完成一个前置的学习状态变化（新增 / 转绿 / 转 brief），下方对应分组会被更新。

## 学习目标
[1-2 句话：为什么要学这个 / 学到什么程度算够]

## 学习路径（按依赖层级，从底层到目标）

### 层级 N（底层）
（待 Step 1.4 用户做完选择后由 Step 1.5 自动填充）

### 层级 1（紧邻目标）
（待填充）

## 状态汇总
- ⏳ 待学习（pending-verify）：0
- 🟢 简略了解（brief）：0
- 🌳 充分理解（full）：0
- ⏭️ 跳过：0
```

**注意**：递归学习时（Step 4.5 把前置 X 当作新根目标），X **不**加 `#learning/root-request` tag，也**不**为 X 单独创建 MOC——只有最外层的用户主动请求才是 MOC 入口。这避免了递归 5 层后产生 5 个 MOC。

### 1.3 前置知识分层
分析目标概念的前置依赖，按"离目标的远近"分 2-4 层：
- 层级 1（最上层）= 紧邻目标的前置知识
- 层级 N（最底层）= 最基础的底层知识

**严格判定标准**（避免擦边关联污染列表）：
- 一个概念能列入前置 ⇔ **不知道它就完全无法理解当前目标**。读懂只是"更全面"不算前置。
- "相关概念"、"常见搭配"、"同领域名词"、"应用场景" → **都不是前置**，不要列入。它们应该在 Step 6 笔记的"与相关概念的关系"段落出现，而不是占用前置名额。
- **同一层软上限 4，硬上限 8**：默认控制在 4 个以内。超过 4 时 agent 必须显式解释"为什么这一项不能砍"；任何情况下都不能超过 8。超过 4 通常说明分层不够细，把弱依赖下沉到下一层。
- 列出来之前每一项都问一次："砍掉它，用户还能理解当前目标吗？"能 → 砍掉。

过滤掉用户状态文件中已掌握的概念。

### 1.4 呈现前置概念列表
从层级 1 开始（从前沿往回走），每层默认 4 个以内，硬上限 8（与 1.3 严格判定保持一致）。让用户选择：
- 哪些需要**详细学习**（→ 该概念作为新根目标，递归走 Step 0，见 Step 4.5）
- 哪些需要**简略了解**
- 哪些可以**跳过**
- 或者**此层全部掌握**（直接跳过该层，进入目标学习）

### 1.5 立刻写占位笔记 + 建立双向链接（用户做完选择的下一动作）

**时机**：用户在 1.4 完成选择的**那一刻**就执行，不要拖到后面任何一步。

**两件事必须一起做**：

**a) 创建占位笔记**：对 1.4 中被用户标记为"详细学"和"简略学"的每一个概念（**跳过**的不写），用 Write 工具在 `03_Knowledge_Network/` 创建：

**写入前查重**：先用 Bash `ls 03_Knowledge_Network/ | grep -i "<concept>"` 检查是否已有同名或近似名笔记。若存在，问用户：覆写 / 重命名当前节点 / 把当前内容并入已有节点（并把别名写入已有笔记的 `aliases:` 字段）。

```markdown
---
title: [概念名称]
aliases: []  # 中英文别名、缩写、常见误写，防止重复节点
understanding: none
date_added: [YYYY-MM-DD]
tags: [pending-verify, 概念标签]
related:
  - "[[上层目标]]"
---

## 简略说明（占位，后续覆盖）
[1-3 句话，回答两件事：这个概念大致是什么 + 它为什么是 [上层目标] 的前置。
只用模型已有的高置信度知识写，不要编造数字/年份/API 名称。如果不确定就只写"是什么"，跳过"为什么"。
后续 Step 6 写完整笔记时整文件覆盖。]

## ⏳ 待学习
[概念名称] 等待学习。下次 session 从这里继续。
```

**b) 立刻双向回链**：用 Edit 工具更新上层目标的笔记（如果存在占位），在它的 `related:` 字段加上指向这个新占位的双链。新占位的 `related:` 也要指回上层目标。

**为什么必须现在就建链接**：
- 占位本身就是"这个概念存在于知识图谱"的声明
- Graph View 在节点出现的同时就能显示边，立刻看到学习地图
- 等到 Step 6 写正文才补链接，中途退出 session 时图谱看起来是"孤岛节点"，无法理解学习路径

写完后立刻向用户口头确认："已在 03_Knowledge_Network/ 为以下概念创建占位笔记 + 与 [上层目标] 双向链接（Graph View 黄色节点带边）：[列表]"。

**c) 同步更新 MOC**：找到当前学习栈最外层根目标对应的 `04_MOC/<根目标> MOC.md`，用 Edit 工具：
- 在对应"层级 N"段落 append 这一批新前置（格式 `- ⏳ [[X]]`）
- "状态汇总"段的 `pending-verify` 计数 +N
- "跳过"项也单列在"层级"内（格式 `- ⏭️ [[Y]] — 跳过`），便于回看完整决策记录

后续状态变化（Step 4.5 brief 转浅绿、Step 6 转深绿、Step 5.3 阻塞）都要同步 Edit MOC：
- 把 `⏳ [[X]]` 改成 `🟢 [[X]]` 或 `🌳 [[X]]`
- 状态汇总三个计数对应增减

### 1.6 层级递进
- 用户"全部掌握"且状态确认已掌握 → 跳过该层，直接进入目标概念
- 用户在该层选了学习项 → 学完后继续往下一层
- 答疑阶段出现阻塞 → 回到 1.4 补充更底层

---

## Step 2: 搜集资料（仅联网模式）

使用以下工具搜集 3-5 篇资料：
- `WebSearch` — 搜索最新博客、教程、讨论
- `WebFetch` — 提取网页完整内容
- Read 工具 — 读取本地已有笔记

---

## Step 3: 记录原始资料（仅联网模式）

在 `00_Sources/` 创建笔记（Write 工具）：

```markdown
---
title: [资料标题]
source: [URL]
date: [YYYY-MM-DD]
tags: [source, 概念标签]
---

**来源**：[URL]

## 核心要点
[2-3 句话总结]

## 与主题的关系
[这篇资料对理解目标概念的帮助]
```

---

## Step 4: 知识总结

**反幻觉守则（贯穿 Step 4 和 Step 5）**：
- **只写有来源的内容**：联网模式只写 Sources 里出现过的事实；非联网模式只写模型高置信度知识。
- **不编造具体值**：年份、版本号、参数量、论文作者、API 名字、命令选项——拿不准就不写，或写"（待查证）"。
- **区分"事实"和"我的解释"**：解释/类比可以发挥，但要让用户看得出哪段是发挥。
- **不要把跳过/未学的前置当作已讲过**：用户没选学的概念，正文里出现时只能用 `[[wikilink]]` 指过去，不能展开讲。
- 拿不准就标 `（不确定）` 或 `（待查证）`，比编造好十倍。

**非联网模式**：直接在 `03_Knowledge_Network/` 创建待确认笔记（如果 Step 1.5 已建占位，则 Edit 在原文件上扩写正文部分，frontmatter 不动）：

```markdown
---
title: [概念名称]
aliases: []  # 中英文别名、缩写、常见误写
understanding: none
date_added: [YYYY-MM-DD]
tags: [pending-verify, 概念标签]
related:
  - "[[上层目标]]"
---

## 什么是 [概念名称]
[清晰定义，2-3 句话]

## 核心要点
- 要点 1
- 要点 2

## 与已知知识的联系
- [[相关概念]] — 关系描述

## 待确认
用户对以上理解是否充分？→ Step 5
```

**联网模式**：综合多篇资料，同样写入 `03_Knowledge_Network/`（同上模板，加 `sources:` 字段）。

**关键**：所有未验证笔记都先以 `understanding: none` + `pending-verify` 黄色 tag 出现在 `03_Knowledge_Network/`，验证通过后由 Step 6 **原地** Edit frontmatter（不创建新文件、不移动文件）。

---

## Step 4.5: 前置知识处理（详细 = 递归 loop，不是直接生成笔记）

遇到用户缺少前置知识时，**必须**根据 Step 1.4 的标记区分两种处理方式：

### 选项 1：简略了解（brief）
- 给 2-3 句话概要 + 直觉性解释
- 在 `03_Knowledge_Network/` 直接覆写占位笔记，标记 `understanding: brief` + `#understanding/brief`
- **不**递归追溯该概念的前置
- 学完立刻继续主目标

### 选项 2：详细学习（full）→ 必须递归 loop

**重要规则**：用户选"详细学" X 时，**禁止直接给出 X 的总结或知识内容**。X 立刻成为一个新的根目标，回到 Step 0 重新走完整流程：

```
用户对当前目标 T 的前置 X 选"详细学"
  ↓
把 X 当作新的"用户主动请求的学习目标"（但不加 root-request tag，root 只属于最外层 T）
  ↓
回到 Step 0：判断 X 是否需要联网
  ↓
Step 1：读用户状态 → 分析 X 的前置依赖 → 分层 → 过滤已知 → 向用户呈现 X 的前置列表
  ↓
让用户继续选择：X 的前置里哪些详细学 / 简略学 / 跳过 / 全部掌握
  ↓
（递归继续。直到某一层用户全选"全部掌握" 或 "简略" 或 "跳过"，才真正学到 X 的具体内容）
  ↓
X 学完并验证理解 → 用户回到 T 这一层继续
```

**判断"已经到底了"**：当用户对当前层的所有前置都选了"全部掌握 / 简略 / 跳过"中之一（即没有任何一个选"详细"），才允许开始生成当前层目标本身的内容（Step 2-4）。否则继续递归。

**实例**：

> 用户要学 Transformer，选择"详细学 Self-Attention"  
> → ❌ 不要立刻写 Self-Attention 笔记  
> → ✅ Self-Attention 成为新根，回到 Step 0：分析 Self-Attention 的前置（点积、softmax、词向量...），让用户继续选  
> → 用户对所有前置都选"全部掌握" → 此时才生成 Self-Attention 笔记  
> → 笔记完成、用户验证理解 → 弹回 Transformer 层继续

**保存调用栈**：递归时在内存中维护一个栈 `[Transformer → Self-Attention → ...]`，每完成一层就弹出，让用户知道当前在第几层、最终目标是什么。可以在每轮开始时显式提示："当前在学 X，是为了回到上层目标 T。"

---

## Step 5: 讲课 + 答疑 + 小测（教学三步）

**核心心智模型**：笔记是讲义（学生课后翻），**对话窗口是课堂讲解**（老师当面讲）。两者不能互相代替。

### Step 5.1：在对话窗口里完整讲一遍

**禁止**：把笔记写完就丢一句"读一下笔记然后告诉我懂没懂"——这是发讲义不是上课。

**必做**：在对话窗口里**口语化、有节奏地把概念再讲一遍**：
- 用提问引入（"你想过为什么 X 不能直接 Y 吗？"）
- 关键点配类比、配具体数字
- 重要的转折用粗体或代码块强调
- 可以比笔记更口语、更"老师味"，因为这是讲课不是写书
- 一次讲一个完整的"理解块"（不是从头读到尾），结束后停下问问题

笔记可以写得很详细很全面，但讲课时要**抓主干**：来龙去脉 → 它是什么 → 怎么运作 → 一个例子。细节（踩坑、命令清单）留给笔记，不在对话里念。

**讲课时的反幻觉规则**：
- 只讲笔记里写过的内容。**笔记里没有的具体数字、版本、API、人名、年份，不要在对话里"补充"出来**——这是幻觉最高发的位置。
- 类比和直觉解释可以发挥，但事实性陈述必须能在笔记里找到对应。
- 用户追问到笔记没覆盖的细节时，正确反应是："笔记没写到这一层，要不要展开学？"（→ 触发 Step 4.5 递归），而不是即兴编造。
- 不确定的地方**明确说不确定**："这个我不太确定，可能是 X 也可能是 Y，要不要查一下？"

### Step 5.2：先答疑（必须）

讲完后**第一句**永远是开放性提问：

> 「这里有什么问题？哪里没听明白？想深入追问哪个子概念？」

不要直接出题。让用户先消化，先指出他的卡点。

**用户的回答分三种情况**：

1. **"懂了 / 没问题"** → 进入 Step 5.3 小测
2. **指出具体卡点** → 针对那个卡点再讲一段，讲完回到 5.2 再问"还有别的吗"
3. **要求深入追问子概念 X** → 启动 Step 4.5 递归：把 X 作为新前置，让用户选详细/简略

### Step 5.3：用户表示无问题后，出小测题

小测题目设计：
- **2-3 题，混合类型**：自述题（用自己的话说）+ 场景判断题（选项区分） + 应用题（具体小问题）
- 难度适中，能区分"真懂"和"以为自己懂"
- 不要全是选择题（无法验证真理解）

用户回答后：
- **完全对** → Step 6 迁绿
- **部分对** → 指出错的地方，简短纠正 → 回到 5.2 问"还有疑问吗"
- **不会答** → 笔记的对应章节再讲一遍，回到 5.2

通过 → 迁入 `03_Knowledge_Network/`（Step 6）
未通过且多次纠正后仍不会 → 在该笔记尾部追加"## 阻塞点"段落，保持 `pending-verify` tag，提供 Step 4.5 的两个选项

---

## Step 6: 转绿（原地 Edit frontmatter）

用户在 Step 5.3 小测通过 → **不创建新文件，不移动文件**，用 Edit 工具改这一篇 `03_Knowledge_Network/` 笔记的 frontmatter：

- `understanding: none` → `understanding: full`（或 `brief`）
- `tags: [pending-verify, ...]` → `tags: [understanding/full, ...]`（或 `understanding/brief`）
- 加 `date_learned: [YYYY-MM-DD]` 字段

如果是 full 路径，正文也要按"详细笔记结构"扩写（见下文模板）。如果是 brief，正文用"简略笔记结构"。Step 1.5 已有的占位 body（"⏳ 待学习"段、"简略说明（占位，后续覆盖）"段）整段替换。

**写入前查重**：若该概念在 Step 1.5 没创建过占位（极少见，例如直接走简略路径且跳过了占位步骤），先用 Bash `ls 03_Knowledge_Network/ | grep -i "<concept>"` 检查是否已有同名或近似名笔记。若存在，问用户：覆写 / 重命名 / 并入已有笔记（把别名写入 `aliases:` 字段）。

**同步 MOC**：转绿后同步更新当前学习栈最外层根目标对应的 `04_MOC/` 笔记——把 `⏳ [[X]]` 改成 `🟢 [[X]]`（brief）或 `🌳 [[X]]`（full），状态汇总计数对应调整。

笔记写作要求（**概念 + 实操，两手都要**）：
- 教科书式展开，不是速查卡
- 每步说清"做什么"和"为什么做"
- 用具体例子贯穿始终
- 关联段落用 2-3 句讲清关系内容
- **必须包含可立即上手的实操内容**：命令、配置示例、调试方法、踩坑点
- 详细参考 `<skill_root>/templates/knowledge-note-template.md`

### 详细笔记（full）结构

```markdown
---
title: [概念名称]
aliases: []  # 中英文别名、缩写、常见误写
understanding: full
date_learned: [YYYY-MM-DD]
tags: [understanding/full, 概念标签]
related:
  - "[[相关概念1]]"
  - "[[相关概念2]]"
---

## 背景与动机
[为什么会出现这个概念，之前怎么做、卡在哪]

## 它是什么
[精确定义 + 类比/直觉 + 一个具体例子]

## 具体运作方式
[步骤分解，每步说清做什么 + 为什么 + 举例]

## 关键组件详解
[每个组件：功能定位 + 上下文位置 + 内部机制]

## 一个完整的例子
[从头到尾走一遍整个流程]

## 上手操作（必填，实操维度）
**最小可用示例**：能直接复制运行的命令/代码/配置，从零到看到结果。

```bash
# 示例：从安装到第一次成功调用
[具体可执行命令]
```

**关键命令清单**：日常使用中最常用的 5-10 条命令/操作。每条注明"什么时候用 + 干什么 + 输入输出"。

**调试与排查**：
- 如何确认它在正常工作？（查看日志、状态命令、健康检查）
- 报错 X 时，怎么定位根因？
- 在哪里看运行时数据？

**常见踩坑**（至少 3 条）：
- 坑 1：现象 → 原因 → 解决方案
- 坑 2：...
- 坑 3：...

**最小复现实验**：用户跟着做一遍就能验证"我真的会用了"的小实验，5-15 分钟可完成。

## 与相关概念的关系
- [[概念A]] — 2-3 句讲清关系

## 实际应用案例
[具体场景 + 为什么这样用 + 业界实现]

## 局限性与已知改进
[技术根源 + 实际严重程度 + 改进方向]

## 参考资料
- [来源] — 核心贡献 1 句话
```

### 简略笔记（brief）结构

```markdown
---
title: [概念名称]
aliases: []  # 中英文别名、缩写、常见误写
understanding: brief
date_learned: [YYYY-MM-DD]
tags: [understanding/brief, 概念标签]
related:
  - "[[相关概念]]"
---

## 它是什么
[1-3 句话直觉性理解]

## 上手要点（实操维度，简化版）
- 最常用的 1-3 条命令或操作
- 1 条最容易踩的坑

## 与 [[当前学习目标]] 的关系
[在整体图景中扮演什么角色]
```

**双链层级规则**：`related:` 字段只链接相邻层级（父↔子类型、机制↔应用关系可豁免）。

---

## Step 6.5: 知识图谱链接检查

写入 `03_Knowledge_Network/` 后：
1. 用 Bash 列出所有现有笔记：`ls "<vault_path>/03_Knowledge_Network/"*.md`
2. 用 Read 工具读取相关笔记的 `related:` 字段
3. 判断是否有父↔子、机制↔应用、同层并列关系
4. 如果有，用 Edit 工具在新笔记和已有笔记的 `related:` 字段**双向**添加链接

---

## Step 7: 更新用户状态

用 Write/Edit 工具更新 `<state_dir>/user_profile.json`：
- 在 `learning_history` 追加本次学习记录
- 更新 `knowledge_network_size`（+1 per full/brief note）
- 更新 `current_focus` 和 `next_learning_goals`

---

## Step 8: 清理空文件

```bash
# 只删除真正的空文件，有 frontmatter 的占位笔记保留
find "<vault_path>" -name "*.md" -empty -delete
```

---

## 常见陷阱

1. 看到用户在学某个工具/框架的架构，就跳过本 skill → **不对**，工具架构同样走本流程
2. 联网搜到资料就直接标 `understanding: full` → **不对**，必须先以 `understanding: none + pending-verify` 写入 03_Knowledge_Network，通过理解验证后才转绿（Step 6 原地 Edit）
3. 占位笔记（有 frontmatter + `#pending-verify`）当空文件删除 → **不对**，有内容的占位笔记要保留
4. `related:` 字段跨层链接 → 相邻层级才能双链，跨层用 `**概念名** — 解释` 格式
5. 用户选"详细学"前置 X，就直接生成 X 的笔记 → **绝对不对**。详细 = 把 X 当成新根目标重新走 Step 0，继续追溯 X 的前置。只有递归到底（没有任何前置选"详细"）才生成内容。见 Step 4.5。
6. 占位笔记延后到 Step 6 才写 → **不对**，必须在 Step 1.5（用户做完选择那一刻）就写，否则中途退出 session 时 Graph View 看不到。
7. 占位笔记不带 `related:` 字段 → **不对**，占位时就要写双向链接到上层目标，Graph View 才能立刻显示边和学习地图。
8. 写完笔记直接让用户"读笔记后告诉我懂没懂" → **不对**，笔记是讲义，对话是课堂。Step 5.1 必须在对话窗口完整口语化讲一遍。
9. 讲完直接出小测题 → **不对**，Step 5.2 必须先开放性问"有什么问题？"让用户先说卡点，Step 5.3 才出题。
10. 把"详细 / 简略 / 跳过 / 已掌握"四个选项意译 → **不对**，必须按字面理解。"详细"= 想详细学（触发递归），不是"已经详细掌握"。歧义时停下来澄清，不要猜。


