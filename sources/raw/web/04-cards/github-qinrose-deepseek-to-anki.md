# qinrose/deepseek-to-anki

- 链接：https://github.com/qinrose/deepseek-to-anki
- 作者：qinrose
- 仓库说明：DeepSeek Anki 制卡助手 - 浏览器扩展：自动识别 DeepSeek 对话中的 Anki 卡片 JSON，一键添加/创建牌组到 Anki
- 星数：0
- 获取方式：GitHub README

---

## README

# DeepSeek to Anki 制卡助手

> 浏览器扩展：在 DeepSeek 网页对话中，把 AI 生成的 Anki 卡片 JSON **一键变成 Anki 卡片 / 层级牌组**。

在 `chat.deepseek.com` 的对话中，只要 AI 按约定格式输出卡片 JSON，扩展会自动在回复下方渲染「添加卡片 / 创建牌组」操作栏，点击即可通过 [AnkiConnect](https://foosoft.net/projects/anki-connect/) 写入本地 Anki，无需复制粘贴。

## ✨ 功能特性

| 功能 | 说明 |
|------|------|
| 🃏 卡片自动识别 | 自动检测 DeepSeek 回复中的 `cards` JSON 并渲染卡片栏 |
| ➕ 一键添加卡片 | 点击「添加到 Anki」，支持带 `deckName` 直接定位牌组 |
| 📚 批量创建层级牌组 | 识别 `createDeck` JSON，一键创建 `课程::章节::小节` 层级牌组 |
| ➕ 添加卡片 | 悬浮球菜单：一键注入扁平 JSON 制卡提示词（可选牌组），AI 直接返回卡片 |
| 🎴 弹窗管理 | 牌组选择 / 新建 / 删除、同步到 Anki、导出 TXT / JSON、自定义提示词与卡片模板 |
| ✨ Markdown 保留 | 卡片内容按 Markdown 提取（加粗、代码块、斜体等），导入 Anki 后保留格式 |
| 🔌 AnkiConnect 对接 | 通过本地 `localhost:8765` 与 Anki 通信，无需上传任何数据到云端 |

## 🔧 工作原理

```
DeepSeek 网页对话
      ↓ (content script 监听)
检测到卡片 JSON (cards / createDeck)
      ↓
渲染卡片栏 / 牌组创建栏（回复下方）
      ↓ (用户点击确认)
background.js → AnkiConnect API (localhost:8765)
      ↓
写入本地 Anki（addNote / createDeck）
```

## 📦 安装

### 1. 准备 Anki

1. 安装 [Anki](https://apps.ankiweb.net/) 并启动
2. 安装 [AnkiConnect](https://ankiweb.net/shared/info/2055492159) 插件（插件代码 `2055492159`）
3. 确认 AnkiConnect 已运行（默认监听 `http://localhost:8765`）

### 2. 安装扩展

**Chrome / Edge（开发者模式）：**

1. 下载本仓库并解压（或 `git clone`）
2. 打开 `chrome://extensions`（Edge 为 `edge://extensions`）
3. 打开右上角「开发者模式」
4. 点击「加载已解压的扩展程序」，选择本仓库目录
5. 安装完成，可固定到工具栏

### 3. 开始使用

1. 打开 [chat.deepseek.com](https://chat.deepseek.com)，保持 Anki 运行
2. 让 AI 按下方 JSON 格式生成卡片（可用页面上的悬浮球一键注入提示词）
3. AI 回复出现 JSON 后，操作栏自动出现，点击即可添加

## 📐 卡片 JSON 格式

扩展识别两种 JSON：`cards`（添加卡片）和 `createDeck`（创建牌组结构）。

### 添加卡片

```json
{
  "cards": [
    {
      "front": "问题（正面）",
      "back": "答案（背面，支持 Markdown）",
      "note": "助记/补充说明（可选）",
      "deckName": "牌组名::子牌组（可选，缺省时手动选择）"
    }
  ]
}
```

### 创建层级牌组

```json
{
  "createDeck": {
    "name": "Python基础教程",
    "chapters": [
      {
        "name": "第一章",
        "sections": [
          { "name": "1.1 变量" },
          { "name": "1.2 运算符" }
        ]
      }
    ]
  }
}
```

将创建：`Python基础教程::第一章::1.1`、`Python基础教程::第一章::1.2` 等层级牌组。

## 📁 项目结构

```
deepseek-to-anki/
├── manifest.json        # 扩展清单（MV3）
├── background.js        # Service Worker：AnkiConnect 通信、卡片/牌组写入
├── content.js           # 页面注入：JSON 识别、卡片栏渲染
├── content.css          # 卡片栏样式
├── deck-creator.js      # 层级牌组解析与创建
├── deck-ui.js           # 牌组创建栏 UI
├── floating-ball.js     # 悬浮球菜单（提示词注入）
├── floating-ball.css    # 悬浮球样式
├── popup/               # 弹窗：牌组管理、同步、导出、模板配置
├── icons/               # 扩展图标
└── docs/                # 功能说明 / 测试指南 / 开发文档
```

## 📚 文档

- [悬浮球功能说明](docs/悬浮球功能说明.md)
- [AI 自动创建层级牌组-使用示例](docs/AI自动创建层级牌组-使用示例.md)
- [功能改进总结](docs/功能改进总结.md)
- [牌组创建功能测试指南](docs/牌组创建功能测试指南.md)
- [牌组识别调试指南](docs/牌组识别调试指南.md)
- [AIAnki 移植文档-卡片牌组模板逻辑](docs/AIAnki_移植文档_卡片牌组模板逻辑.md)
- [安卓移植文档-DeepSeek 制卡四大能力](docs/安卓移植文档_DeepSeek制卡四大能力.md)

## 📄 许可证

[MIT](LICENSE)

