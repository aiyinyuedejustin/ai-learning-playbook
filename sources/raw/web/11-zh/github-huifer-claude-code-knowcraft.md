# huifer/Claude-Code-KnowCraft（中文）

- 链接：https://github.com/huifer/Claude-Code-KnowCraft
- 作者：huifer
- 仓库说明：AI-powered personal knowledge management system with natural language interface and spaced repetition learning
- 星数：76
- 获取方式：GitHub README + SKILL/说明文件

---

## README

# 🧠 个人知识系统 - Claude Code 智能集成

> 基于本地文件的智能知识管理系统,集成 Claude Code 实现自然语言交互和智能学习

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Integrated-brightgreen)](https://claude.ai/claude-code)
[![Stage](https://img.shields.io/badge/Stage-7_Complete-blue)]()
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)]()

[![Knowledge Items](https://img.shields.io/badge/Knowledge_Items-0+-green)]()
[![Commands](https://img.shields.io/badge/Commands-19-orange)]()
[![AI Agents](https://img.shields.io/badge/AI_Agents-8-purple)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)]()

这是一个革命性的个人知识管理系统,完全基于本地文件存储(JSON + Markdown),无需数据库依赖。通过深度集成 Claude Code,支持自然语言交互、智能网络搜索、间隔重复学习、费曼技巧验证等先进功能,让知识管理变得前所未有的智能和高效。

**核心优势**: 本地优先、AI驱动、科学学习、完全掌控你的知识。

---

## 👥 开发团队与社区

| 项目 | 链接/信息 |
|------|-----------|
| 开发团队官网 | https://www.wellally.tech/ |
| 交流群 | ![社群](./public/社群.jpg) |
| 社群介绍 | 使用 Claude Code 替代现有的一切软件,让任何一个人都可以享受到 Claude Code 对一切的改变 |

---

## ✨ 核心特性

### 🎯 智能知识管理
- **📝 多源知识输入**: 支持手动输入、PDF导入、URL抓取、图片OCR、网络搜索
- **🏷️ 智能标签系统**: 自动推荐标签、标签层级管理、相似标签合并建议
- **🔗 知识关联**: 自动识别相关条目、双向链接、关联类型(references/builds-on/related)
- **📊 版本控制**: 自动版本备份、差异对比、一键恢复历史版本

### 🧠 AI驱动的学习系统
- **🔄 间隔重复 (SuperMemo SM-2算法)**: 科学计算复习间隔,提高记忆效率
- **👨‍🏫 费曼技巧**: 通过教学验证理解,发现知识盲区
- **📝 智能测验**: 自动生成测试题(选择题/填空题/应用题),评估掌握程度
- **📅 复习提醒**: 基于遗忘曲线的智能复习提醒

### 🗣️ 自然语言交互
- **💬 对话式操作**: 用自然语言管理知识(如"记一条React笔记"、"修改第一条")
- **🎯 意图识别**: 自动理解用户意图,6大意图类型(添加/搜索/编辑/学习/导入/网络搜索)
- **🧠 上下文理解**: 记住对话历史,解析代词("它"、"这个"、"第一条")
- **⚡ 智能建议**: 主动推荐关联、学习路径、优化建议

### 🔍 智能网络搜索
- **🌐 Google集成**: 使用Google Custom Search API搜索最新资料
- **🤖 AI整理**: 自动抓取、提取、摘要、评分搜索结果
- **⭐ 多维度评分**: 内容质量(40%) + 权威性(30%) + 时效性(15%) + 相关性(15%)
- **🎯 对话式筛选**: 支持多轮搜索优化("太泛了,专注于useMemo")

### 🏗️ 8个专业AI Agent
1. **Knowledge Architect** - 知识架构师,分析知识结构
2. **Knowledge Enricher** - 知识增强师,完善内容质量
3. **Quiz Master** - 测验大师,生成智能测试
4. **Research Assistant** - 研究助手,深度研究主题
5. **Search Assistant** - 搜索助手,整理网络资源
6. **Student** - 学生Agent,模拟学习过程
7. **Tutor** - 导师Agent,提供个性化指导
8. **Version Keeper** - 版本管理员,追踪知识演化

### 💾 本地优先设计
- **📁 纯文本存储**: JSON + Markdown,无数据库依赖,数据永久可控
- **🔒 隐私保护**: 所有数据存储在本地,不上传云端
- **📂 时间组织**: 按日期自动分层存储(年/月/日)
- **🔍 可搜索**: 纯文本格式,支持任何文本搜索工具

---

## 🚀 快速开始

### 前置要求
- [Claude Code CLI](https://claude.ai/claude-code) - Anthropic官方AI命令行工具
- [Node.js](https://nodejs.org/) (v16+) - 可选

### 安装
```bash
# 克隆仓库
git clone https://github.com/huifer/Claude-Code-KnowCraft.git
cd Claude-Code-KnowCraft

# 启动 Claude Code
claude

# 测试功能
claude> /kb-add --type=learning-note
claude> /kb-list
```

### 更多文档
📖 [完整快速开始指南](docs/GETTING_STARTED.md)

---

## 📚 文档导航

### 使用指南
- 📖 [快速开始](docs/GETTING_STARTED.md) - 安装、配置、首次使用
- 📖 [使用指南](docs/USER_GUIDE.md) - 自然语言交互、命令参考、学习系统
- 📖 [配置说明](docs/CONFIGURATION.md) - 用户偏好、API配置、自定义模板

### 技术文档
- 📖 [系统架构](docs/ARCHITECTURE.md) - 架构图、目录结构、核心组件
- 📖 [命令参考](docs/COMMAND_REFERENCE.md) - 完整命令列表、Agent文档、Skill文档
- 📖 [开发指南](docs/DEVELOPMENT.md) - 贡献指南、添加命令、测试调试

### 项目信息
- 📖 [更新日志](docs/CHANGELOG.md) - 版本历史、新功能
- 📖 [发展路线](docs/ROADMAP.md) - 已完成功能、未来计划

---

## 🆚 功能对比

| 功能特性 | 本系统 | Obsidian | Notion | Logseq | Roam Research |
|---------|--------|----------|--------|--------|---------------|
| **存储方式** | 本地JSON+MD | 本地MD | 云端 | 本地MD | 云端 |
| **自然语言交互** | ✅ 支持 | ❌ | ❌ | ❌ | ❌ |
| **AI智能学习** | ✅ 间隔重复+费曼技巧 | ❌ | ❌ | 部分插件 | ❌ |
| **智能搜索** | ✅ AI整理结果 | 基础搜索 | 全文搜索 | 全文搜索 | 全文搜索 |
| **网络搜索集成** | ✅ Google+AI整理 | ❌ | ❌ | ❌ | ❌ |
| **版本控制** | ✅ 自动备份 | Git集成 | 历史版本 | Git集成 | 历史版本 |
| **知识关联** | ✅ 智能推荐+双向链接 | 双向链接 | 关联数据库 | 双向链接 | 双向链接 |
| **学习系统** | ✅ SM-2算法+测验 | 插件支持 | ❌ | 插件支持 | ❌ |
| **AI Agent** | ✅ 8个专业Agent | ❌ | ❌ | ❌ | ❌ |
| **PDF导入** | ✅ 自动提取 | 插件支持 | ✅ | 插件支持 | ❌ |
| **图片OCR** | ✅ 支持 | 插件支持 | ❌ | ❌ | ❌ |
| **数据库依赖** | ❌ 无依赖 | ❌ | ✅ 需要 | ❌ | ✅ 需要 |
| **离线使用** | ✅ 完全离线 | ✅ | ❌ | ✅ | ❌ |
| **隐私保护** | ✅ 完全本地 | ✅ | ⚠️ 云端 | ✅ | ⚠️ 云端 |
| **学习曲线** | 🟢 低(自然语言) | 🟡 中 | 🟢 低 | 🟡 中 | 🟡 中 |
| **定制化** | ✅ 高度可定制 | 插件生态 | 模板系统 | 插件生态 | 模板系统 |
| **价格** | ✅ 免费(MIT) | ✅ 免费 | 💰 付费 | ✅ 免费 | 💰 付费 |

---

## 🤝 常见问题

**Q: 如何配置Google搜索API？**
A: 查看 [配置说明](docs/CONFIGURATION.md#网络搜索api配置) 的详细指南。

**Q: 知识库可以迁移到其他设备吗？**
A: 可以！整个项目都是纯文本文件，可以直接复制或使用Git同步。

**Q: 支持中文搜索吗？**
A: 完全支持！所有功能都针对中文优化。

更多问题请查看 [使用指南](docs/USER_GUIDE.md)。

---

## 📄 许可证

本项目采用 **MIT License** 开源。

详见 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

感谢您选择本系统！如果您觉得这个项目对您有帮助,请给个⭐️Star支持一下！

**让我们一起,用AI改变知识管理！** 🚀


## 文件 .claude/skills/knowledge-manager/skill.md

---
name: knowledge-manager
description: 智能知识管理助手,自动分析、组织和优化知识库
trigger:
  - on_add: true
  - on_edit: true
  - explicit: "帮我整理知识" "优化知识库" "分析标签"
priority: high
---

# Knowledge Manager Skill

智能知识管理助手,自动分析和优化知识库结构。

## 功能概述

Knowledge Manager 是一个自动触发的智能助手,帮助用户:

1. **自动标签建议**: 基于内容智能推荐标签
2. **自动关联建议**: 识别相关条目并建议链接
3. **分类检测**: 自动判断条目应该属于哪个分类
4. **智能组织**: 识别重复、孤立和需要整合的条目
5. **质量评估**: 评估条目的完整性和质量

## 触发条件

### 自动触发

1. **添加知识后** (`on_add: true`)
   - 用户执行 `/kb-add` 后自动触发
   - 分析新添加的条目
   - 建议标签、分类和关联

2. **编辑知识后** (`on_edit: true`)
   - 用户执行 `/kb-edit` 后自动触发
   - 检查编辑后的内容
   - 更新建议和关联

### 手动触发

用户可以通过以下方式手动触发:
- "帮我整理知识"
- "优化知识库"
- "分析标签使用情况"
- "查找重复条目"
- "建议知识关联"

## 执行流程

### 1. 内容分析

```markdown
## 分析新添加的条目

当用户添加知识时:

1. **提取关键词**
   - 从标题中提取核心概念
   - 从正文中识别技术术语
   - 提取专有名词和缩写

2. **主题识别**
   - 判断讨论的主要主题
   - 识别技术栈和工具
   - 检测应用场景

3. **质量评估**
   - 检查内容完整性
   - 评估是否有代码示例
   - 判断是否需要补充信息
```

### 2. 标签建议

```markdown
## 智能标签推荐

基于内容分析推荐标签:

1. **现有标签匹配**
   - 查找 tags.json 中相似的标签
   - 推荐使用现有标签体系

2. **新标签建议**
   - 识别内容中的关键概念
   - 建议新的标签名称
   - 避免标签冗余

3. **标签层级**
   - 建议主标签和副标签
   - 保持标签体系的一致性

输出格式:
```
建议标签:
  主标签: react, hooks
  相关标签: frontend, javascript, useState

说明:
  - react: React 框架相关内容
  - hooks: React Hooks 特性
  - frontend: 前端开发通用
  - javascript: JavaScript 语言

是否应用这些标签? (yes/no/edit)
```
```

### 3. 分类建议

```markdown
## 分类推荐

分析内容并建议分类:

**code 分类特征**:
- 代码片段
- API 文档
- 技术实现细节

**projects 分类特征**:
- 项目文档
- 开发日志
- 技术决策记录

**learning 分类特征**:
- 学习笔记
- 概念解释
- 教程和指南

**personal 分类特征**:
- 个人思考
- 经验总结
- 反思和感悟

输出格式:
```
建议分类: learning

置信度: 高 (85%)

理由:
  - 包含概念解释
  - 有学习笔记特征
  - 包含理解过程

是否应用此分类? (yes/no)
```
```

### 4. 关联建议

```markdown
## 智能关联推荐

识别可能相关的知识条目:

1. **标题相似度**
   - 计算与现有条目标题的相似度
   - 识别同义词和相关词

2. **标签重叠度**
   - Jaccard 相似系数
   - 标签重叠越多,关联性越强

3. **内容引用**
   - 检测是否提及了其他条目的 ID
   - 识别标题或内容中提到的其他概念

4. **时间邻近性**
   - 近期创建的相关条目
   - 同一时期学习的内容

输出格式:
```
发现 3 个可能相关的条目:

1. [2025-01-03-102015] React 基础概念
   相关度: 95% (高)
   关联类型: references
   理由: 标题和内容都有 "React" 关键词

2. [2025-01-02-084530] 函数组件
   相关度: 82% (中高)
   关联类型: builds-on
   理由: Hooks 是在函数组件基础上构建的

3. [2025-01-01-120000] JavaScript 闭包
   相关度: 45% (低)
   关联类型: related
   理由: 都涉及前端开发

是否创建这些关联? (all/select/none)
```
```

### 5. 知识组织分析

```markdown
## 组织结构分析

定期分析知识库的组织状况:

1. **重复检测**
   - 查找标题或内容相似的条目
   - 建议合并或建立关联

2. **孤立条目检测**
   - 没有链接的条目
   - 没有反向链接的条目
   - 建议创建关联

3. **标签分析**
   - 统计标签使用频率
   - 识别过度使用或很少使用的标签
   - 建议标签优化

4. **分类分布**
   - 分析各分类的条目数量
   - 识别不平衡的分类

输出格式:
```
知识库组织分析报告:

📊 总体统计
  总条目: 45 个
  总标签: 32 个
  总链接: 23 个

🔍 重复检测
  发现 2 对相似条目:
  - [2025-01-01-100000] React Hooks
    [2025-01-03-150000] React Hooks 详解
    相似度: 78%
    建议: 建立关联或合并

🏝️  孤立条目
  5 个条目没有链接:
  - [2025-01-02-120000] CSS Grid
  - [2025-01-04-090000] TypeScript 基础
  ...

🏷️  标签分析
  最常用标签:
  1. react (12 次)
  2. javascript (8 次)
  3. hooks (6 次)

  很少使用的标签:
  - debugging (1 次)
  - optimization (1 次)

📁 分类分布
  code: 15 个 (33%)
  learning: 18 个 (40%)
  projects: 8 个 (18%)
  personal: 4 个 (9%)

💡 优化建议
  1. 为孤立条目创建关联
  2. 合并相似的 React Hooks 条目
  3. 考虑合并 debugging 和 optimization 标签
```
```

## 智能建议示例

### 场景 1: 用户添加 React Hooks 笔记

```markdown
用户执行: /kb-add --type=learning-note
标题: React Hooks 学习笔记

[用户输入内容后]

Knowledge Manager 自动触发:

✨ 内容分析完成!

建议标签:
  主标签: react, hooks
  相关标签: frontend, functional-components
  理由: 内容主要讨论 React Hooks 和函数组件

建议分类: learning
置信度: 高 (92%)
理由: 学习笔记格式,包含概念解释

发现相关条目:
  1. [2025-01-03-102015] React 基础概念 (相关度: 88%)
     建议: references - 引用了 React 基础概念

  2. [2025-01-02-084530] 函数组件 (相关度: 75%)
     建议: builds-on - 在函数组件基础上讨论

是否应用这些建议?
输入选项:
  - apply all: 应用所有建议
  - select: 选择性应用
  - skip: 跳过,稍后手动处理

用户选择: apply all

✅ 已应用所有建议!
标签已更新: react, hooks, frontend, functional-components
分类已更新: learning
关联已创建:
  → references: 2025-01-03-102015
  → builds-on: 2025-01-02-084530
```

### 场景 2: 用户请求知识库分析

```markdown
用户输入: 帮我分析知识库的组织情况

Knowledge Manager 执行:

📊 知识库组织分析报告

=== 总体概况 ===
  总条目数: 45 个
  总标签数: 32 个
  总链接数: 23 个
  平均每个条目链接数: 0.51 个

=== 重复检测 ===
  发现 3 对可能重复的条目:

  1. React Hooks 相关 (相似度: 82%)
     [2025-01-01-100000] React Hooks 入门
     [2025-01-03-150000] React Hooks 详解
     建议: 建立关联 (builds-on)

  2. JavaScript 异步 (相似度: 75%)
     [2025-01-02-110000] Promise 和 async/await
     [2025-01-04-120000] JavaScript 异步编程
     建议: 合并为一个条目

  3. CSS Flexbox (相似度: 68%)
     [2025-01-05-090000] Flexbox 布局
     [2025-01-06-100000] Flexbox 完整指南
     建议: 保留较新的版本

=== 孤立条目 ===
  8 个条目没有任何链接:

  1. [2025-01-02-120000] CSS Grid 布局
     建议关联: [2025-01-05-090000] Flexbox 布局 (related)

  2. [2025-01-04-090000] TypeScript 基础
     建议关联: [2025-01-01-100000] React Hooks (related)

  ... (其余 6 个)

=== 标签分析 ===
  使用频率分布:
    高频 (>10次): react (12), javascript (8)
    中频 (5-10次): hooks (6), async (5)
    低频 (<5次): 其余 28 个标签

  标签优化建议:
    1. 合并相似标签:
       - js → javascript
       - ts → typescript

    2. 拆分宽泛标签:
       - frontend → react, vue, angular

=== 分类分布 ===
  code: 15 个 (33%) ⚖️  平衡
  learning: 18 个 (40%) ⚖️  平衡
  projects: 8 个 (18%) ⚖️  偏低
  personal: 4 个 (9%) ⚠️  过低

  建议: 增加项目和反思类内容的记录

=== 质量评估 ===
  高质量条目 (>500字): 12 个 (27%)
  中等质量 (200-500字): 23 个 (51%)
  低质量条目 (<200字): 10 个 (22%)

  建议: 丰富低质量条目的内容

💡 行动建议:
  1. 立即处理: 合并重复的 JavaScript 异步条目
  2. 本周完成: 为孤立条目创建关联
  3. 持续优化: 增加项目和反思类内容
  4. 标签整理: 统一 js 和 javascript 标签

是否需要我帮你执行这些建议?
```

## 技术实现

### 1. 相似度计算

```javascript
// Jaccard 相似系数 (标签重叠度)
function jaccardSimilarity(tags1, tags2) {
  const intersection = tags1.filter(tag => tags2.includes(tag));
  const union = [...new Set([...tags1, ...tags2])];
  return intersection.length / union.length;
}

// 文本相似度 (简单的词频统计)
function textSimilarity(text1, text2) {
  const words1 = tokenize(text1);
  const words2 = tokenize(text2);
  const common = words1.filter(word => words2.includes(word));
  return common.length / Math.max(words1.length, words2.length);
}
```

### 2. 标签推荐算法

```
1. 提取内容中的关键词
2. 与 tags.json 中的现有标签匹配
3. 计算每个相关标签的权重
4. 推荐权重最高的 3-5 个标签
```

### 3. 分类判断

```
1. 统计内容中的特征词
2. 每个分类有对应的特征词列表
3. 计算内容与每个分类的匹配度
4. 选择匹配度最高的分类
```

## 配置选项

### 自动应用阈值

```json
{
  "autoApply": {
    "tags": {
      "confidence": 0.9,
      "minMatches": 2
    },
    "category": {
      "confidence": 0.85
    },
    "links": {
      "minSimilarity": 0.8
    }
  }
}
```

### 分析频率

```json
{
  "analysis": {
    "onAdd": true,
    "onEdit": true,
    "scheduled": "weekly"
  }
}
```

## 注意事项

1. **用户控制**: 所有建议都需要用户确认,不自动修改
2. **性能优化**: 大量条目时使用缓存和增量分析
3. **隐私保护**: 分析过程仅在本地进行,不上传数据
4. **可配置性**: 允许用户自定义分析规则和阈值

## 未来扩展

1. **语义分析**: 使用 NLP 技术进行更深入的语义理解
2. **自动摘要**: 为长内容生成简洁的摘要
3. **知识图谱**: 可视化知识网络
4. **智能问答**: 基于知识库内容回答问题
5. **学习路径**: 自动推荐学习顺序和关联内容


## 文件 .claude/skills/nlp-interface/skill.md

---
name: nlp-interface
description: 自然语言接口，理解用户意图并映射到对应的命令
trigger:
  - auto: true  # 自动拦截所有非斜杠开头的输入
priority: highest
version: 1.0
---

# NLP Interface Skill - 自然语言接口

智能自然语言接口，理解用户的日常语言并自动映射到对应的斜杠命令，让知识管理更自然、更高效。

## 功能概述

NLP Interface 是一个自动触发的智能接口层，位于用户和命令系统之间：

```
用户输入 → NLP Interface → 意图识别 → 命令映射 → 执行命令
   ↓              ↓              ↓          ↓
 "记笔记"      识别为添加      /kb-add    执行添加
```

**核心能力**：
1. **意图识别**：理解用户想要做什么（6大类意图）
2. **上下文管理**：记住对话历史，理解代词指代
3. **智能路由**：将自然语言映射到具体的斜杠命令
4. **参数提取**：从自然语言中提取命令参数
5. **澄清策略**：当意图不明确时，主动询问

## 工作流程

### Step 1: 输入检测

```python
检测用户输入:
IF 输入以 "/" 开头:
    → 不处理，交给原有命令系统
ELSE:
    → 进入意图识别流程
```

### Step 2: 意图识别

```python
意图分类（6大类）:

1. 添加知识意图
   关键词: "记", "添加", "学习", "了解", "保存", "记录"
   映射命令: /kb-add

2. 搜索查找意图
   关键词: "找", "搜索", "查", "看看", "有没有", "关于"
   映射命令: /kb-search

3. 编辑修改意图
   关键词: "修改", "更新", "编辑", "改", "补充", "添加内容"
   映射命令: /kb-edit

4. 学习复习意图
   关键词: "测试", "测验", "练习", "复习", "回顾", "教我", "讲解"
   映射命令: /kb-quiz, /kb-review, /kb-teach

5. 导入内容意图
   关键词: "保存这个网页", "抓取", "导入", "从URL", "从PDF"
   映射命令: /kb-from-url, /kb-from-pdf, /kb-from-image

6. 网络搜索意图
   关键词: "搜索资料", "网上找", "Google一下", "查资料", "找资料"
   映射命令: /kb-search-web
```

### Step 3: 置信度计算

```python
置信度评估:

高置信度 (>90%):
    → 直接执行命令

中置信度 (70-90%):
    → 显示确认信息
    → "我要执行: [命令]，确认吗？(回车确认 / n取消)"

低置信度 (<70%):
    → 询问澄清
    → 显示选项列表
    → "你想做什么？1. 搜索 2. 添加 3. 测试"
```

### Step 4: 参数提取

```python
从自然语言提取命令参数:

标题提取:
    - 从引号内提取: "标题: React Hooks"
    - 从冒号后提取: "学习: useState"
    - 核心名词短语: "React Hooks学习笔记"

标签提取:
    - "标签: xxx" → ["xxx"]
    - "带tag xxx" → ["xxx"]
    - "#xxx" → ["xxx"]
    - 从内容中识别关键词

分类提取:
    - "学习笔记" → learning-note
    - "代码" → code-snippet
    - "项目" → project-doc
    - "研究" → research-note

其他参数:
    - 时间: "最近", "这个月" → --after=DATE
    - 难度: "简单", "困难" → --difficulty=LEVEL
    - 数量: "5个", "前10" → --count=N
```

### Step 5: 上下文解析

```python
上下文管理（最近10轮对话）:

代词解析:
    "它" → 最近提到的主体
    "这个" → 最近操作的对象
    "那个" → 前一轮提到的对象
    "第一条" → 上次搜索结果的第1个

话题追踪:
    - 持续时间: 30分钟内视为同一话题
    - 主题延续: "再搜索XXX"（在当前话题内细化）
    - 话题切换: "现在搜索Python"（清空上下文）

参考解析:
    "修改它" → /kb-edit [last_id]
    "关联这个" → /kb-link [last_id] [current_id]
```

### Step 6: 执行命令

```python
构建完整命令并执行:

1. 构建命令字符串:
    intent = "kb-add"
    params = {"title": "React Hooks", "tags": ["react"]}
    command = f"/{intent} \"{params['title']}\" --tags={','.join(params['tags'])}"

2. 传递给命令系统:
    执行构建的命令

3. 返回结果给用户:
    显示命令输出
    保存到对话历史
```

## 意图识别规则

### 1. 添加知识

**触发模式**：
```
"记一条笔记"
"添加知识"
"学习XXX"
"了解XXX"
"记录XXX"
"保存笔记"
```

**示例对话**：
```
用户: "记一条React Hooks学习笔记"
系统:
  意图: kb-add
  提取:
    - 标题: "React Hooks学习笔记"
    - 类型: learning-note
    - 标签: [react, hooks] (智能推荐)

  执行: /kb-add "React Hooks学习笔记" --type=learning-note --tags=react,hooks
```

### 2. 搜索查找

**触发模式**：
```
"找XXX"
"搜索XXX"
"查XXX"
"看看XXX"
"有没有XXX"
"关于XXX的笔记"
```

**示例对话**：
```
用户: "找useState相关内容"
系统:
  意图: kb-search
  提取:
    - 查询词: "useState"
    - 过滤: 无

  执行: /kb-search useState
```

### 3. 编辑修改

**触发模式**：
```
"修改XXX"
"更新XXX"
"编辑XXX"
"改XXX"
"给XXX补充"
"修改第一条"
"更新刚才那个"
```

**示例对话**：
```
用户: "修改刚才那条笔记"
系统:
  意图: kb-edit
  上下文:
    - 上次操作: 搜索结果
    - 最近ID: 2026-01-04-105815

  执行: /kb-edit 2026-01-04-105815
```

### 4. 学习复习

**触发模式**：
```
"测试XXX"
"测验XXX"
"练习XXX"
"复习今天"
"回顾最近"
"教我XXX"
"讲解XXX"
```

**示例对话**：
```
用户: "测试React部分"
系统:
  意图: kb-quiz
  提取:
    - 主题: "React"
    - 难度: medium (默认)

  执行: /kb-quiz "React" --difficulty=medium
```

### 5. 导入内容

**触发模式**：
```
"保存这个网页: URL"
"导入PDF"
"抓取URL"
"从URL导入"
"从PDF提取"
```

**示例对话**：
```
用户: "保存https://react.dev这篇文章"
系统:
  意图: kb-from-url
  提取:
    - URL: "https://react.dev"

  执行: /kb-from-url https://react.dev
```

### 6. 网络搜索

**触发模式**：
```
"搜索XXX资料"
"网上找XXX"
"Google一下XXX"
"查XXX的资料"
"找XXX的学习资源"
```

**示例对话**：
```
用户: "搜索React性能优化最新资料"
系统:
  意图: kb-search-web
  提取:
    - 查询: "React性能优化"
    - 约束: ["最新"]

  执行: /kb-search-web "React性能优化" --time=recent
```

## 上下文管理

### 对话历史结构

```json
{
  "sessionId": "2026-01-04-session-001",
  "startTime": "2026-01-04T14:30:00Z",
  "lastActivity": "2026-01-04T14:35:22Z",
  "turnCount": 5,
  "currentTopic": "React Hooks",

  "recentContext": {
    "lastCommand": "kb-search",
    "lastQuery": "useState",
    "lastIds": ["2026-01-04-105815", "2026-01-04-105644"],
    "lastResult": "3个结果"
  },

  "turns": [
    {
      "turnId": 1,
      "timestamp": "2026-01-04T14:30:05Z",
      "userInput": "找React笔记",
      "intent": "kb-search",
      "confidence": 0.92,
      "executedCommand": "/kb-search React"
    },
    ...
  ]
}
```

### 上下文解析策略

```python
代词解析规则:

"它" → 指向最近操作的主体
  例: "修改它" → 修改上次搜索/编辑的条目

"这个" → 指向当前讨论的对象
  例: "这个不错" → 当前查看的条目

"那个" → 指向前一轮的对象
  例: "那个呢？" → 前一轮提到的另一个对象

"第一条" → 指向列表中的第1个
  例: "修改第一条" → 上次搜索结果的第1条

"刚才那个" → 指向上一次操作的对象
  例: "再搜索刚才那个" → 继续细化搜索
```

## 澄清策略

### 模糊输入处理

```python
当意图不明确时:

示例1: 单词输入
用户: "React"
系统:
  "你想要对React做什么？
   1. 搜索相关笔记
   2. 添加新笔记
   3. 测试相关知识
   4. 学习React

   请回复数字或详细描述。"

示例2: 多种可能
用户: "Hooks"
系统:
  "我找到了几种可能:
   1. 搜索: React Hooks相关笔记
   2. 添加: 添加Hooks学习笔记
   3. 测试: Hooks知识测验

   请告诉我具体需求。"
```

## 偏好学习

### 自动学习用户习惯

```python
学习维度:

1. 标签偏好
   观察: 最近10次添加笔记，8次使用"frontend"
   学习: 默认建议标签包含"frontend"

2. 分类偏好
   观察: 70%的笔记在"learning"分类
   学习: 默认分类设为"learning"

3. 格式偏好
   观察: 用户经常使用详细格式查看搜索结果
   学习: 默认使用 --format=detailed

4. 时间偏好
   观察: 用户多在下午2-5点学习新知识
   学习: 下午主动建议学习资源
```

### 偏好应用

```python
应用偏好到命令:

用户: "记一条笔记"
系统应用:
  - 默认分类: learning (从偏好中获取)
  - 推荐标签: [react, hooks] (基于上下文)
  - 默认模板: learning-note

  输出: "我要添加一条学习笔记
          建议标签: react, hooks (基于最近话题)
          要修改吗？(回车确认 / 输入新标签)"
```

## 智能建议

### 操作后建议

```python
在命令执行完成后触发建议:

添加知识后:
  - 发现相关条目 (相似度>80%)
  - 建议创建关联
  - 建议开始学习计划

搜索后:
  - 建议细化搜索
  - 建议学习路径
  - 推荐相关主题

测验后:
  - 显示薄弱环节
  - 建议针对性复习
  - 推荐练习资源
```

## 配置选项

```json
{
  "nlp": {
    "enabled": true,
    "confirmThreshold": 0.7,
    "contextWindow": 10,
    "sessionTimeout": 1800,
    "maxHistory": 100
  },
  "preferences": {
    "autoLearn": true,
    "suggestAfterCommand": true,
    "showConfidence": false
  }
}
```

## 使用示例

### 完整对话流程

```
# 对话开始

用户: "找React笔记"
系统: [执行 /kb-search React]
      找到 3 个相关条目...

用户: "修改第一条"
系统: [从上下文解析 ID: 2026-01-04-105815]
      [执行 /kb-edit 2026-01-04-105815]

用户: "补充useEffect的内容"
系统: [识别为编辑操作，保持当前ID]
      请输入要补充的内容...

用户: "测试一下React"
系统: [执行 /kb-quiz "React" --difficulty=medium]

# 30分钟后，新会话开始

用户: "搜索useState"
系统: [新会话，清空上下文]
      [执行 /kb-search useState]
```

## 性能优化

```python
优化策略:

1. 意图识别缓存
   - 常见输入模式缓存
   - 避免重复计算

2. 对话历史压缩
   - 只保留关键信息
   - 定期清理过期会话

3. 异步处理
   - 偏好学习异步执行
   - 不阻塞主流程
```

## 错误处理

```python
错误处理策略:

1. 意图识别失败
   → 询问用户具体需求
   → 提供命令列表

2. 参数提取失败
   → 使用默认值
   → 询问用户确认

3. 命令执行失败
   → 显示原始错误
   → 建议正确的命令格式

4. 上下文丢失
   → 提示用户重新指定
   → 提供历史记录
```

## 调试模式

```python
调试模式输出:

当 showConfidence=true 时:

用户: "记笔记"
系统: [DEBUG]
      意图: kb-add
      置信度: 0.85
      提取参数: {title: null, tags: []}
      构建命令: /kb-add
      状态: 需要澄清

      请提供标题和内容...
```

## 与其他组件配合

```python
协作组件:

1. Knowledge Manager
   - 添加知识后触发
   - 接收标签和关联建议

2. Suggestion Engine
   - 接收操作上下文
   - 返回智能建议

3. Search Assistant
   - 网络搜索触发
   - 返回整理结果

4. User Preferences
   - 读取用户偏好
   - 更新使用统计
```

## 版本历史

- v1.0 (2026-01-04): 初始版本
  - 实现6大意图识别
  - 上下文管理
  - 参数提取
  - 澄清策略


## 文件 .claude/skills/suggestion-engine/skill.md

---
name: suggestion-engine
description: 智能建议引擎，根据上下文和用户行为主动推荐相关操作
trigger:
  - after-command: true  # 在命令执行后触发
priority: high
version: 1.0
---

# Suggestion Engine Skill - 智能建议引擎

智能建议引擎，在用户执行操作后主动提供个性化推荐，提升知识管理效率。

## 核心功能

### 1. 上下文感知建议
基于当前操作的内容和上下文，智能推荐下一步操作

### 2. 关联发现
自动发现相关知识条目，建议创建关联

### 3. 学习路径推荐
根据知识图谱和学习进度，推荐学习路径

### 4. 最佳实践建议
根据用户偏好和行为模式，提供优化建议

## 触发时机

### 在以下操作后触发建议：

```python
触发条件：

1. 添加知识后 (kb-add, kb-from-url, kb-from-pdf, kb-from-image)
   → 发现相关条目
   → 建议创建关联
   → 推荐学习计划

2. 搜索后 (kb-search, kb-search-web)
   → 建议细化搜索
   → 推荐相关主题
   → 建议学习路径

3. 编辑知识后 (kb-edit)
   → 检测内容变化
   → 建议更新关联
   → 推荐复习

4. 测验后 (kb-quiz)
   → 显示薄弱环节
   → 推荐针对性复习
   → 建议练习资源

5. 复习后 (kb-review)
   → 显示复习统计
   → 预测下次复习
   → 推荐扩展学习

6. 学习计划更新后 (kb-learn, kb-progress)
   → 显示学习进度
   → 调整学习建议
   → 推荐配套资源
```

## 建议类型

### 类型1: 关联建议

**触发时机**: 添加知识、编辑知识后

**检测逻辑**:
```python
def find_associations(new_item):
    candidates = []

    # 1. 标签重叠度检测
    for item in knowledge_base:
        overlap = calculate_tag_overlap(new_item.tags, item.tags)
        if overlap > 0.5:  # 50%以上重叠
            candidates.append({
                'item': item,
                'reason': f"标签重叠度: {overlap*100}%",
                'confidence': overlap
            })

    # 2. 主题提及检测
    for item in knowledge_base:
        if new_item.title.lower() in item.content.lower():
            candidates.append({
                'item': item,
                'reason': f"内容中提到了 '{new_item.title}'",
                'confidence': 0.8
            })

    # 3. 时间邻近性检测
    recent_items = get_items_from_last_week()
    for item in recent_items:
        if has_similar_context(new_item, item):
            candidates.append({
                'item': item,
                'reason': "最近添加的相似内容",
                'confidence': 0.6
            })

    # 按置信度排序
    return sorted(candidates, key=lambda x: x['confidence'], reverse=True)[:5]
```

**建议输出**:
```
💡 发现相关条目

  [2026-01-04-105644] React基础概念 (92%相关)
    标签重叠: react, hooks
    原因: 标签重叠度 85%

  [2026-01-04-105900] 函数组件实践 (85%相关)
    标签重叠: react
    原因: 内容提及了相似概念

建议操作:
  1. 创建关联 - /kb-link new-id 2026-01-04-105644
  2. 批量关联 - /kb-link new-id all
  3. 暂不关联 - skip

执行哪些？(输入序号或all)
```

### 类型2: 学习路径建议

**触发时机**: 搜索后、添加系列知识后

**推荐逻辑**:
```python
def suggest_learning_path(topic):
    # 获取主题相关的所有条目
    related_items = search_by_topic(topic)

    # 按难度和依赖关系排序
    sorted_items = topological_sort(related_items)

    # 分组为学习阶段
    path = {
        'beginner': sorted_items[:3],
        'intermediate': sorted_items[3:7],
        'advanced': sorted_items[7:]
    }

    return path
```

**建议输出**:
```
🎓 推荐学习路径: React Hooks

基于您的内容和搜索记录，为您规划了学习路径：

第1阶段: 基础入门 (2-3天)
  1. React Hooks概述 [2026-01-04-105644]
  2. useState基础 [2026-01-03-102415]
  3. useEffect入门 [2026-01-03-105822]

第2阶段: 进阶实践 (1周)
  4. Hook规则和限制 [2026-01-02-091533]
  5. 自定义Hooks [2026-01-02-104511]
  6. 性能优化 [2026-01-01-101234]

第3阶段: 深入理解 (2周)
  7. Hooks源码分析 [2026-01-01-095822]
  8. 高级模式 [2026-01-01-093211]

建议操作:
  1. 创建学习计划 - /kb-learn "React Hooks" --items=1-8
  2. 开始学习第一阶段 - /kb-learn "React Hooks" --stage=1
  3. 测试当前水平 - /kb-quiz "React Hooks"

选择: _
```

### 类型3: 薄弱环节建议

**触发时机**: 测验后、复习评分低后

**分析逻辑**:
```python
def analyze_weaknesses(quiz_results):
    weaknesses = {}

    for question in quiz_results:
        if not question.correct:
            topic = question.topic

            if topic not in weaknesses:
                weaknesses[topic] = {
                    'count': 0,
                    'items': []
                }

            weaknesses[topic]['count'] += 1
            weaknesses[topic]['items'].append(question.related_item)

    # 按错误频率排序
    return sorted(weaknesses.items(),
                  key=lambda x: x[1]['count'],
                  reverse=True)
```

**建议输出**:
```
📊 测验分析: React Hooks

总分: 75/100

薄弱环节识别:
  ❌ useEffect依赖项 (3个错误)
     相关条目: [2026-01-03-105822], [2026-01-02-091533]

  ⚠️ 自定义Hooks (1个错误)
     相关条目: [2026-01-02-104511]

建议改进计划:
  1. 重点复习useEffect - /kb-review 2026-01-03-105822
  2. 重做useEffect练习 - /kb-quiz "useEffect" --difficulty=hard
  3. 费曼技巧讲解 - /kb-teach "useEffect依赖项" --role=teacher
  4. 创建专项复习计划 - /kb-learn "useEffect深入理解" --focus=true

执行哪些？(输入序号或all)
```

### 类型4: 搜索细化建议

**触发时机**: 搜索结果过多/过少后

**判断逻辑**:
```python
def suggest_search_refinement(search_results, query):
    result_count = len(search_results)

    if result_count == 0:
        return {
            'type': 'no_results',
            'suggestions': [
                f"尝试相关词: '{query}'的同义词",
                f"检查拼写: '{query}'是否正确",
                f"扩大范围: 移除一些过滤条件"
            ]
        }

    elif result_count < 5:
        return {
            'type': 'few_results',
            'suggestions': [
                f"相关主题: 搜索 '{query}'相关概念",
                f"扩展标签: 使用更宽泛的标签",
                f"网络搜索: /kb-search-web '{query}'"
            ]
        }

    elif result_count > 20:
        return {
            'type': 'many_results',
            'suggestions': [
                f"添加过滤: --tag=xxx, --category=xxx",
                f"时间范围: --after=2026-01-01",
                f"精确匹配: 使用双引号 '{query}'"
            ]
        }

    else:
        return None  # 结果数量合适，不需要建议
```

**建议输出**:
```
💡 搜索优化建议

找到 35 个结果，结果较多。建议：

1. 添加标签过滤
   /kb-search React --tag=hooks
   预计减少到 15 个结果

2. 按时间筛选
   /kb-search React --after=2026-01-01
   只显示最近内容

3. 搜索更具体
   /kb-search "React Hooks useState"
   使用精确短语

4. 网络搜索补充
   /kb-search-web "React Hooks 最新实践"
   查找在线资源

执行哪个？(输入序号或done)
```

### 类型5: 复习提醒建议

**触发时机**: 每日、学习计划更新时

**算法**: SuperMemo 2 (SM-2)

```python
def calculate_next_review(item):
    if not item.reviews:
        return today + 1 day

    last_review = item.reviews[-1]
    ease_factor = item.easeFactor  # 默认 2.5
    interval = item.interval  # 默认 1 天

    # SM-2 算法
    if last_review.quality < 3:
        # 记忆不好，重置间隔
        next_interval = 1
    else:
        # 记忆好，增加间隔
        next_interval = interval * ease_factor

    # 调整难度系数
    ease_factor = max(1.3,
                      ease_factor + (0.1 - (5 - last_review.quality) * (0.08 + (5 - last_review.quality) * 0.02)))

    return today + next_interval days, ease_factor, next_interval
```

**建议输出**:
```
📅 今日复习提醒 (5条待复习)

  1. [2026-01-03-105822] useEffect依赖项
     上次评分: 4/5 | 复习间隔: 3天 | 遗忘概率: 35%

  2. [2026-01-02-104511] 自定义Hooks
     上次评分: 5/5 | 复习间隔: 7天 | 遗忘概率: 20%

  3. [2026-01-01-101234] React性能优化
     上次评分: 3/5 | 复习间隔: 2天 | 遗忘概率: 50% ⚠️

建议操作:
  1. 开始今日复习 - /kb-review --today
  2. 优先复习遗忘概率高的 - /kb-review --priority=high
  3. 查看复习统计 - /kb-review --stats

预计耗时: 15分钟
```

### 类型6: 内容质量建议

**触发时机**: 添加知识后、批量导入后

**检测逻辑**:
```python
def analyze_content_quality(item):
    issues = []
    score = 100

    # 1. 完整性检测
    if len(item.content) < 200:
        issues.append({
            'type': 'too_short',
            'severity': 'warning',
            'message': '内容较短，建议补充更多细节'
        })
        score -= 10

    # 2. 代码示例检测
    if 'code' in item.tags and not has_code_examples(item.content):
        issues.append({
            'type': 'missing_examples',
            'severity': 'info',
            'message': '代码片段建议添加实际示例'
        })
        score -= 5

    # 3. 标签完整性
    if len(item.tags) < 2:
        issues.append({
            'type': 'few_tags',
            'severity': 'info',
            'message': f'建议添加更多标签，当前: {item.tags}'
        })
        score -= 5

    # 4. 关联检测
    related = find_related_items(item)
    if len(related) > 0 and not item.links:
        issues.append({
            'type': 'missing_links',
            'severity': 'suggestion',
            'message': f'发现{len(related)}个相关条目，建议创建关联',
            'related': related[:3]
        })
        score -= 10

    return {
        'score': max(0, score),
        'issues': issues
    }
```

**建议输出**:
```
📝 内容质量分析

质量得分: 75/100

改进建议:
  ⚠️ 内容较短
     当前: 180字 | 建议: >500字
     操作: /kb-edit [id] 补充细节

  ℹ️ 缺少代码示例
     检测到标签: code-snippet
     建议: 添加实际使用示例

  💡 发现2个相关条目
     • [2026-01-03-105822] useEffect依赖项
     • [2026-01-02-104511] 自定义Hooks
     操作: /kb-link [id] 2026-01-03-105822

立即改进？(y/n)
```

## 建议呈现策略

### 1. 时机控制

```python
建议频率控制:

用户偏好级别:
  - conservative: 每操作3-5次后建议1次
  - moderate (默认): 每操作1-2次后建议1次
  - aggressive: 每次操作后都建议

时间控制:
  - 不要在短时间内重复建议 (>5分钟)
  - 不要建议用户明确拒绝过的内容
```

### 2. 个性化排序

```python
def rank_suggestions(suggestions, user_preferences):
    scores = []

    for suggestion in suggestions:
        score = 0

        # 1. 相关性加分
        score += suggestion.relevance * 0.4

        # 2. 用户兴趣加分
        if suggestion.topic in user_preferences.interests:
            score += 0.3

        # 3. 学习阶段匹配
        if suggestion.difficulty == user_preferences.expertiseLevel:
            score += 0.2

        # 4. 时间合适性
        if is_preferred_time(user_preferences.activeHours):
            score += 0.1

        scores.append((suggestion, score))

    # 按分数排序
    return sorted(scores, key=lambda x: x[1], reverse=True)[:3]
```

### 3. 呈现格式

```markdown
💡 智能建议 (最多3条)

  [优先级高] 建议标题
  说明: 简短解释原因
  操作: /command-args

  [优先级中] 建议标题
  说明: 简短解释原因
  操作: /command-args

  [优先级低] 建议标题
  说明: 简短解释原因
  操作: /command-args

---
快捷操作:
  1 - 执行第1条
  2 - 执行第2条
  3 - 执行第3条
  all - 全部执行
  done - 跳过
  never - 不再显示此类建议

选择: _
```

## 用户反馈机制

### 记录用户选择

```python
用户响应类型:

1. accept - 接受建议
   → 记录为成功建议
   → 增加该类型建议的权重

2. reject - 拒绝建议
   → 记录为失败建议
   → 降低该类型建议的权重

3. skip - 跳过
   → 不影响权重
   → 可能在下次重新建议

4. never - 永不显示
   → 加入黑名单
   → 永久不再建议该类型

5. modify - 修改后执行
   → 记录用户偏好
   → 调整未来建议
```

### 学习用户偏好

```python
def update_suggestion_preferences(user_action, suggestion):
    preferences = load_user_preferences()

    # 更新建议接受率
    if user_action == 'accept':
        preferences.suggestionAcceptRate += 0.1
    elif user_action == 'reject':
        preferences.suggestionAcceptRate -= 0.05

    # 更新类型偏好
    suggestion_type = suggestion.type
    if user_action == 'accept':
        preferences.suggestionTypeWeights[suggestion_type] += 0.2
    elif user_action == 'reject':
        preferences.suggestionTypeWeights[suggestion_type] -= 0.1

    # 更新黑名单
    if user_action == 'never':
        preferences.suggestionBlacklist.append({
            'type': suggestion_type,
            'content': suggestion.content_hash
        })

    # 归一化权重
    normalize_weights(preferences.suggestionTypeWeights)

    save_preferences(preferences)
```

## 配置选项

### 用户可配置项

```json
{
  "suggestions": {
    "enabled": true,
    "aggressiveness": "moderate",  // conservative | moderate | aggressive
    "maxSuggestions": 3,
    "showConfidence": false,

    "typeWeights": {
      "association": 0.8,
      "learning_path": 0.9,
      "weakness": 0.7,
      "search_refinement": 0.6,
      "review_reminder": 0.8,
      "quality_improvement": 0.5
    },

    "blacklist": [],
    "acceptRate": 0.65,
    "lastShown": "2026-01-04T14:30:00Z"
  }
}
```

## 与其他组件集成

### 1. Knowledge Manager Skill

```python
协作模式：

Knowledge Manager 负责内容分析
→ Suggestion Engine 基于分析结果生成建议

例如：
  - Knowledge Manager 检测到标签冲突
  → Suggestion Engine 建议标准化标签
```

### 2. NLP Interface Skill

```python
协作模式：

NLP Interface 解析用户意图
→ Suggestion Engine 提供操作建议

例如：
  - 用户: "我想学习React"
  - NLP: 识别为学习意图
  - Suggestion: "建议创建学习计划: /kb-learn 'React'"
```

### 3. User Preferences

```python
协作模式：

User Preferences 提供行为数据
→ Suggestion Engine 个性化推荐

例如：
  - 偏好显示用户下午2-5点活跃
  → Suggestion 在下午推荐学习资源
  → 早上推荐复习任务
```

## 性能优化

### 1. 异步处理

```python
# 建议生成不阻塞主流程
async def generate_suggestions_after_command(command_result):
    # 在后台生成建议
    suggestions = await async_analyze_and_suggest(command_result)

    # 只在合适时机显示
    if should_show_suggestions():
        display_suggestions(suggestions)
```

### 2. 缓存机制

```python
# 缓存常见建议
cache = {
    'react_learning_path': {
        'suggestions': [...],
        'generated_at': '2026-01-04',
        'ttl': 86400  # 24小时
    }
}

def get_suggestions(topic):
    if topic in cache and not cache_expired(topic):
        return cache[topic]['suggestions']

    return generate_fresh_suggestions(topic)
```

### 3. 智能去重

```python
# 避免重复建议
def deduplicate_suggestions(suggestions, history):
    seen = set()
    unique = []

    for suggestion in suggestions:
        signature = (suggestion.type, suggestion.content_hash)

        if signature not in seen and signature not in history.recently_shown:
            seen.add(signature)
            unique.append(suggestion)

    return unique
```

## 最佳实践

### 1. 不要过度打扰

```
❌ 不好:
  - 每次操作都弹出建议
  - 一次显示10条建议
  - 无法关闭建议

✅ 好:
  - 控制频率 (moderate模式)
  - 最多显示3条
  - 提供"never"选项
```

### 2. 建议要有价值

```
❌ 无价值建议:
  "您可以查看帮助文档"

✅ 有价值建议:
  "发现3个useState相关条目，建议创建关联以提高学习效率"
```

### 3. 个性化是关键

```
根据用户调整:
  - 新用户: 更多引导性建议
  - 高级用户: 更少但更精准的建议
  - 特定兴趣: 优先推荐相关领域
  - 活跃时间: 学习vs复习建议
```

## 使用示例

### 示例1: 添加知识后的建议

```
用户: /kb-add "React Hooks学习笔记" --tags=react,hooks
系统: ✅ 已添加: [2026-01-04-143052]

💡 智能建议

  1. [85%] 创建关联
     发现2个相关条目:
     • [2026-01-03-105822] useEffect依赖项
     • [2026-01-02-104511] 自定义Hooks
     操作: /kb-link 2026-01-04-143052 2026-01-03-105822

  2. [75%] 开始学习
     建议创建学习计划掌握React Hooks
     操作: /kb-learn "React Hooks深入理解"

  3. [60%] 测试理解
     检验对Hooks的掌握程度
     操作: /kb-quiz "React Hooks"

选择: _ (或done跳过)
```

### 示例2: 测验后的建议

```
用户: /kb-quiz "React Hooks"
系统: 📊 测验完成: 75/100

💡 改进建议

  薄弱环节: useEffect依赖项 (3个错误)

  1. 重点复习
     /kb-review 2026-01-03-105822 --focus

  2. 费曼技巧讲解
     /kb-teach "useEffect依赖项" --role=teacher

  3. 额外练习
     /kb-quiz "useEffect" --difficulty=hard

选择: _
```

### 示例3: 每日复习提醒

```
用户: (早晨打开系统)
系统: 📅 早上好！今日学习提醒

  📚 复习任务: 5条待复习 (预计15分钟)
  🆕 新知识: 昨日添加3条React相关内容
  🎯 学习进度: "React Hooks"计划进行中(35%)

建议操作:
  1. 开始复习 - /kb-review --today
  2. 继续学习 - /kb-learn "React Hooks" --continue
  3. 查看详情 - /kb-progress

开始今日学习？(y/n)
```

## 版本历史

- v1.0 (2026-01-04): 初始版本
  - 实现6大建议类型
  - 用户反馈学习
  - 个性化排序

