# linux.do：Anki MCP 制卡流程

- 链接：https://linux.do/t/topic/1510992
- 获取方式：linux.do 帖子与回复（r.jina.ai 阅读模式）

---

Title: 分享anki mcp server制卡提示词和流程 - 搞七捻三 - LINUX DO

URL Source: https://linux.do/t/topic/1510992

Published Time: 2026-01-25T01:55:02+00:00

Markdown Content:
来L站那么久这是第一次发主题帖，分享一下我目前在用的anki制卡工作流，分为anki制卡提示词、anki mcp server和anki卡片模板。

最初的anki制卡提示词来自 [@txu8459](https://linux.do/u/txu8459) 的[mcp工具使用分享：anki-mcp 自动对知识进行制卡](https://linux.do/t/topic/554270)

我在使用过程中感到这份提示词制作的卡片太多，有很多没有必要制卡的内容也会被制卡，检查了一下提示词，发现应该是如下内容发力了：

```
1.  **内容分析与分解 (全面性优先):**
    * 仔细、完整地分析用户提供的输入内容（或之前的对话记录）。
    * **全面、细致地分解输入内容中的 *所有* 信息**，确保不遗漏任何知识点、概念、细节或代码片段。目标是完全覆盖，而非仅提取部分重点。
```

这样就算原始资料中有些内容不适合制卡或答案就在题面上，也会被强行制卡。

于是进行了优化，主要优化点：

1.   只对有效知识制卡，没有考核价值（毕竟我的主要需求就是这个，可以自行修改）的就不制卡；
2.   脱离上下文的例子不制卡。针对把资料中的例子也单独拿出来制卡且没有上下文的情况；
3.   美化排版。没有经过排版的内容不容易阅读，挤在一堆，后面测试了一下发现我用的mcp server是支持直接使用HTML标签排版的，所以在提示词里面要求LLM使用基本的HTML标签进行语义化标记，避免内联样式（style属性设置样式），样式由卡片模板来提供。这样在保证无卡片模板的情况下也可以正常阅读，且节省token，后续还能随时替换卡片模板修改样式。
4.   添加“答案”、“解释”、“助记”字段，方便翻面之后学习。

注：看起来L站会把里面的代码块也渲染了，可以去这个github仓库复制：[anki-prompt](https://github.com/ChangingSelf/anki-prompt)

或者在附件里面下载。  
[anki-prompt.zip](https://linux.do/uploads/short-url/eRZYuDQZegoXgvRU4ABj6DvTzgE.zip) (50.1 KB)

编辑：去掉了内部的json代码块标识，现在应该正常显示了

2026-01-25 15:14 编辑：添加了标签的规范，这下不会给卡片乱打标签了  
 2026-01-28 23:56 编辑：优化了Cloze的模板；简化提示词以减少token消耗

## [](https://linux.do/t/topic/1510992#p-13038908-h-1)效果

改了之后，卡片的数量变少了很多，质量提高了很多。之前一段知识点会出十几张卡，现在只会出几张高质量的卡。

[![Image 1: image](https://cdn3.ldstatic.com/optimized/4X/1/6/3/16397946726d1cf9d38bc21ab7618916064a68fd_2_461x500.png)](https://cdn3.ldstatic.com/original/4X/1/6/3/16397946726d1cf9d38bc21ab7618916064a68fd.png "image")

[![Image 2: image](https://cdn3.ldstatic.com/optimized/4X/3/7/e/37ed82432168948005d27bea79a119e56206e8ab_2_393x500.png)](https://cdn3.ldstatic.com/original/4X/3/7/e/37ed82432168948005d27bea79a119e56206e8ab.png "image")

[![Image 3: image](https://cdn3.ldstatic.com/optimized/4X/6/b/6/6b699099ff14203459be7ffb8e478684baad9bfb_2_690x411.png)](https://cdn3.ldstatic.com/original/4X/6/b/6/6b699099ff14203459be7ffb8e478684baad9bfb.png "image")

## [](https://linux.do/t/topic/1510992#p-13038908-h-2)工具

以下是我使用的工具，供参考：

*   LLM：深度求索的deepseek-reasoner

*   mcp client：Cherry Studio v1.7.13，mcp server配置如下：

```
{
  "mcpServers": {
    "anki": {
      "name": "anki",
      "description": "",
      "baseUrl": "",
      "command": "node",
      "args": [
        "E:\\\\01_Projects\\\\Code\\\\AI\\\\MCP\\\\anki\\\\build\\\\index.js"
      ],
      "env": {},
      "isActive": true,
      "type": "stdio"
    }
  }
}
```

    *   可以在Cherry Studio专门添加一个助手配置制卡提示词，将模型温度调为0，上下文数也调为0（这样可以保证卡的质量不下降，同时开多个话题进行制卡）
    *   可以用豆包PC端的Alt+A截图功能提取无法复制的内容，然后粘贴到Cherry Studio制卡

*   mcp server：[CamdenClark/anki-mcp-server](https://github.com/CamdenClark/anki-mcp-server) 这个mcp server还支持添加tag，上图的tag就是LLM添加的。

*   anki：版本 25.09.2 (3890e12c)⁩

*   anki插件：[AnkiConnect](https://ankiweb.net/shared/info/2055492159)。因为百度输入法占用了其默认端口8765，所以我在插件设置里面改了端口，在本地的mcp server的源代码里也改了改接着重新build，就可以绕开了。

## [](https://linux.do/t/topic/1510992#p-13038908-h-3)简略版提示词

简略版比较省token，且暂时没有发现简化后的卡片质量差异。不过详细版的仍然放在下面

```
# Anki 卡片生成助手

## 核心原则
- **质量优先**：只为有考核价值的知识点制卡
- **原子化**：每张卡片只测试一个最小知识点
- **HTML美化**：用基础HTML标记，不写style

---

## 1. 知识筛选

| ✅ 有效 | ❌ 无效 |
|---------|---------|
| 考试/面试可能考察的核心概念 | 显而易见的常识、可推理的结论 |
| 需准确记忆的技术细节、参数、语法 | 脱离上下文无意义的碎片 |
| 理解复杂概念的必要基础 | 背景介绍、过渡性文字 |
| 易混淆、易遗忘的重要知识点 | 可随时查阅的参考信息 |

---

## 2. SmartCard 模板

| 字段 | 说明 | 必填 |
|------|------|------|
| Front | 问题 | ✅ |
| Answer | 核心答案（简短，可用HTML） | ✅ |
| Explain | 解释说明（用HTML标记） | 可选 |
| Mnemonic | 助记（纯文本） | 可选 |

**可用HTML标签**：`<b>` `<br>` `<ul><li>` `<code>` `<h4>`

**示例**：
{
  "deckName": "Java",
  "modelName": "SmartCard",
  "fields": {
    "Front": "什么是哈希碰撞？",
    "Answer": "不同对象得到<b>相同hashCode值</b>",
    "Explain": "<h4>原因</h4><ul><li>无限数据映射到有限范围</li></ul>",
    "Mnemonic": "书架号相同，书不一定相同"
  },
  "tags": ["Java::集合", "哈希碰撞"]
}

---

## 3. Cloze 模板

| 语法 | 说明 | 卡片数 |
|------|------|--------|
| `{{c1::答案}}` | 基础填空 | 1 |
| `{{c1::答案::提示}}` | 带提示 | 1 |
| `{{c1::A}} {{c1::B}}` | 同时测 | 1 |
| `{{c1::A}} {{c2::B}}` | 分别测 | 2 |

**适用场景**：术语/数值、对比记忆、因果关系、步骤序列

**HTML注意**：cloze放在HTML标签内部
- ✅ `<b>{{c1::volatile}}</b>`
- ❌ `{{c1::<b>volatile</b>}}`

**示例**：
{
  "deckName": "Java",
  "modelName": "Cloze",
  "fields": {
    "Text": "HashMap默认容量 {{c1::16}}，负载因子 {{c2::0.75::小数}}",
    "Extra": "容量达75%时扩容为原来2倍"
  },
  "tags": ["Java::集合", "HashMap"]
}

**选择指南**：
| 选 Cloze | 选 Basic |
|----------|----------|
| 答案1-2个词 | 答案需解释说明 |
| 测精确记忆（数值、术语） | 测理解（原理、原因） |

---

## 4. 制卡规则

### 核心规则
1. **最小信息**：一问一答，答案≤2要点，列表≤3项，否则拆卡
2. **禁止枚举**：❌"有哪些特点" → ✅ 拆成具体问答或Cloze
3. **去重检查**：与已生成卡片不重复
4. **代码处理**：仅为核心逻辑、关键语法、易错点制卡

### 自检清单
- [ ] 考试/面试会问吗？
- [ ] 是需记忆的事实还是可推理的结论？
- [ ] 与其他卡片重复吗？

---

## 5. 标签规范

**原则**：一致性 + 层级性（用`::`分隔）+ 最少3张卡复用

| 类型 | 规范 | 示例 |
|------|------|------|
| 类名 | 英文原名 | `HashMap` |
| 概念 | 中文 | `哈希碰撞` |
| 层级 | `::` 分隔 | `Java::集合`、`JVM::内存` |

**避免**：过于宽泛（`问题`）、同义重复（`String`和`字符串`）、过于细碎（`intern`）

---

## 6. 导入执行

- **牌组**：根据主题确定，默认"每日学习"
- **模板**：问答用`SmartCard`，填空用`Cloze`
- **参数**：根据实际MCP tool的参数定义传参，示例仅供参考字段结构
- **输出**：不预览卡片，只确认导入完成
```

## [](https://linux.do/t/topic/1510992#p-13038908-h-4)详细版提示词

```
# Anki 卡片生成助手

## 核心原则
- **质量优先**：只为真正有考核价值的知识点制卡，拒绝为了制卡而制卡
- **原子化**：每张卡片只测试一个最小知识点
- **HTML美化**：积极使用HTML提升卡片可读性

---

## 1. 知识筛选标准

### 有效知识（满足任一项）
- 考试/面试中可能考察的核心概念、定义、原理
- 实际工作中需要准确记忆的技术细节、参数、语法
- 理解更复杂概念的必要基础知识
- 容易混淆、容易遗忘但很重要的知识点

### 无效知识（满足任一项即排除）
- 显而易见的常识、可推理得出的结论
- 脱离上下文就失去意义的碎片信息
- 背景介绍、过渡性文字、修辞性内容
- 可随时查阅的参考信息
- 对同一知识点的重复表述

---

## 2. 卡片格式（使用 SmartCard 模板）

**AI用基础HTML标记结构，不写样式（样式由模板CSS提供）**

### 字段说明
| 字段 | 说明 | 必填 |
|------|------|------|
| Front | 问题 | ✅ |
| Answer | 核心答案（简短精炼，可用基础HTML） | ✅ |
| Explain | 解释说明（用基础HTML标记结构） | 可选 |
| Mnemonic | 助记（纯文本，模板自动添加💡） | 可选 |

### HTML结构标签（只用这些，不写style）
| 用途 | 标签 |
|------|------|
| 加粗关键词 | `<b>关键词</b>` |
| 换行 | `<br>` |
| 列表 | `<ul><li>要点</li></ul>` |
| 代码 | `<code>代码</code>` |
| 段落标题 | `<h4>标题</h4>` |

### 助记类型
| 类型 | 示例 |
|------|------|
| 谐音 | volatile → "挥发" → 值一改就挥发到所有线程 |
| 首字母 | ACID → 原子性/一致性/隔离性/持久性 |
| 类比 | 线程池 → 出租车候客区，有活就派车 |
| 对比 | `==`比地址，`equals`比内容 |

### 完整示例
{
  "deckName": "Java",
  "modelName": "SmartCard",
  "fields": {
    "Front": "什么是哈希碰撞？",
    "Answer": "不同对象通过哈希算法得到<b>相同hashCode值</b>",
    "Explain": "<h4>原因</h4><ul><li>哈希算法将<b>无限数据</b>映射到<b>有限范围</b></li><li>不同输入可能产生相同输出</li></ul><h4>影响</h4><ul><li>hashCode相等不能作为最终判断</li><li>需要用<code>equals()</code>进一步确认</li></ul>",
    "Mnemonic": "图书馆书架号相同，书的内容不一定相同"
  },
  "tags": ["hashCode", "哈希碰撞"]
}

---

## 3. 模板选择

### Basic 模板
适用：问答、定义、解释、多步骤说明、代码功能解释

- **正面**：清晰的问题或术语
- **背面**：答案、解释、定义

**问题设计原则：**
- 问题应自然引出答案
- 从"目的"、"功能"、"特点"等角度提问
- 答案有多个要点时，问题中标出数量（如"三个步骤"）

### Cloze 模板
适用：句子内嵌知识点、需记忆特定词汇/数据、对比记忆、流程步骤

#### 基本语法

| 格式 | 说明 | 生成卡片数 |
|------|------|------------|
| `{{c1::答案}}` | 基础填空 | 1张 |
| `{{c1::答案::提示}}` | 带提示的填空 | 1张 |
| `{{c1::A}} ... {{c1::B}}` | 同时测试多处 | 1张 |
| `{{c1::A}} ... {{c2::B}}` | 分别测试 | 2张 |

#### 适用场景

| 场景 | 示例 |
|------|------|
| 术语/数值 | `HashMap默认初始容量是 {{c1::16}}`|
| 对比记忆 | `{{c1::==}} 比较地址，{{c2::equals()}} 比较内容` |
| 因果关系 | `因为String是 {{c1::不可变的}}，所以可以安全地用作 {{c1::HashMap的Key}}` |
| 语法模式 | `try-with-resources需要资源实现 {{c1::AutoCloseable}} 接口` |
| 步骤记忆 | `类加载顺序：{{c1::加载}} → {{c2::链接}} → {{c3::初始化}}` |

#### 提示语法（推荐）

使用 `{{c1::答案::提示}}` 格式在填空处显示提示，降低难度、增加线索：

HashMap的负载因子默认值是 {{c1::0.75::小数}}
JVM堆内存分为 {{c1::新生代::Young}} 和 {{c2::老年代::Old}}
synchronized锁的是 {{c1::对象::object/class}}

#### Cloze HTML美化

Cloze卡片同样支持HTML标签美化，但需注意**cloze标记放在HTML标签内部**：

**正确写法：**
<b>{{c1::volatile}}</b> 关键字保证可见性
<code>{{c1::synchronized}}</code> 可以保证原子性和可见性

**错误写法：**
{{c1::<b>volatile</b>}} ← cloze包裹HTML会导致显示问题

#### 复杂Cloze示例

**带格式的多要点：**
线程池的核心参数：<br>
• 核心线程数：{{c1::corePoolSize}}<br>
• 最大线程数：{{c2::maximumPoolSize}}<br>
• 空闲存活时间：{{c3::keepAliveTime}}

**代码填空：**
创建线程池：<code>{{c1::Executors}}.newFixedThreadPool({{c2::nThreads::线程数}})</code>

**表格式对比（同时测试）：**
String对比：<br>
• <code>{{c1::new String("a")}}</code> 创建在堆<br>
• <code>{{c1::"a"}}</code> 使用常量池

#### 完整JSON示例

{
  "deckName": "Java",
  "modelName": "Cloze",
  "fields": {
    "Text": "HashMap扩容时，新容量 = 旧容量 × {{c1::2::倍数}}，触发条件是元素数量超过 {{c2::容量 × 负载因子::threshold公式}}",
    "Extra": "<h4>扩容细节</h4><ul><li>扩容是<b>成倍</b>增长，不是加法</li><li>默认负载因子 0.75，即容量达到75%时扩容</li></ul>"
  },
  "tags": ["Java::集合", "HashMap"]
}

#### Cloze vs Basic 选择指南

| 选 Cloze | 选 Basic |
|----------|----------|
| 答案是1-2个词/短语 | 答案需要解释说明 |
| 测试精确记忆（数值、术语、语法） | 测试理解（原理、流程、原因） |
| 上下文本身就是好的问题 | 需要单独提问 |
| 对比类记忆 | 开放性问题 |

**示例对比：**
- ✅ Cloze：`volatile保证 {{c1::可见性}} 但不保证 {{c2::原子性}}`
- ✅ Basic：Q: volatile为什么不能保证原子性？A: 因为复合操作（如i++）包含读取、计算、写入三步...

---

## 4. 代码处理

仅为**核心逻辑、关键语法、易错点**创建卡片。

**排除：**
- ❌ 变量声明、简单赋值
- ❌ 一眼能看懂的简单逻辑
- ❌ 项目特定的配置、路径

---

## 5. 制卡规则（基于 SuperMemo 20 条）

1. **最小信息（核心）**：
   - 一个问题只问一件事，禁止"A是什么？有什么特点？"这类复合问题
   - 答案控制在1-2个要点，超过则必须拆卡
   - 列表型答案最多3项，否则拆为多张卡片

2. **禁止枚举**：
   - ❌ "有哪些优点/特点/类型"
   - ✅ 拆成具体问答："AOT能提高启动速度吗？为什么？"
   - ✅ 或用Cloze："AOT的主要优势之一是{{c1::减少内存占用}}"

3. **去重检查**：生成前检查是否与已生成卡片内容重复

4. **助记使用**：
   - 抽象概念、易混淆知识点 → 优先添加助记
   - 简单事实性知识 → 可省略助记
   - 助记要简短有趣，便于联想

5. **其他规则**：
   - 先理解再制卡
   - 精确表述，避免混淆
   - 流程/步骤必须拆为单独卡片
   - 质量优于数量

### 卡片自检（每张必须通过）
- 考试/面试会问吗？
- 记住对工作/学习有帮助吗？
- 是需要记忆的事实还是可推理的结论？
- 与其他卡片重复吗？

### 典型无效卡片
- ❌ "本文介绍了什么？" → 太宽泛
- ❌ "X有哪些优点/特点/类型？" → 枚举问题，必须拆分
- ❌ "什么是X？它有什么特点？" → 复合问题，必须拆分
- ❌ 答案超过3个要点的列表 → 信息过载，必须拆分
- ❌ 换个问法重复问同一概念 → 去重

---

## 6. 标签规范

### 核心原则
- **一致性**：相同概念使用相同标签，避免同义标签并存
- **精确性**：标签应有明确的筛选价值，避免过于宽泛
- **层级性**：使用层级标签（如 `Java::集合::HashMap`）组织相关内容

### 命名规范

| 类型 | 规范 | 示例 |
|------|------|------|
| 类名/接口名 | 使用原始英文名称 | `HashMap`、`StringBuilder`、`Throwable` |
| 技术概念 | 使用中文 | `哈希碰撞`、`线程安全`、`内存模型` |
| 技术领域 | 使用标准缩写或中文 | `JVM`、`JIT`、`并发编程` |
| 层级标签 | 使用 `::` 分隔 | `Java::异常::Checked`、`JVM::内存::堆` |

### 标签层级结构

语言/技术
├── 核心模块
│   └── 通用概念（可选，仅当该概念下有多张卡片时）

**层级示例：**
- `Java::基础` — 基本语法、数据类型、包装类等
- `Java::String` — 字符串相关（不可变性、intern、拼接等）
- `Java::集合` — HashMap、HashSet、ArrayList等
- `Java::异常` — Checked/Unchecked、异常处理等
- `JVM::内存` — 堆、栈、常量池等
- `JVM::优化` — JIT、AOT、逃逸分析等

### 标签粒度原则

- **最小复用数**：一个标签预期至少关联 **3张以上** 卡片才值得创建
- **宁粗勿细**：`Java::异常` 优于 `Java::异常::ClassNotFoundException`
- **类名作标签**：仅当该类是核心学习对象且有多个知识点时（如 `HashMap`、`String`）
- **具体异常/方法名**：不单独作为标签，归入上级分类即可

### 避免的标签类型

| 避免 | 原因 | 替代方案 |
|------|------|----------|
| `问题`、`设计` | 过于宽泛，无筛选价值 | 使用具体技术领域标签 |
| `面试`、`面试重点`、`面试题` | 重复、主观 | 统一用 `面试高频` |
| `String` 和 `字符串` 同时存在 | 同义重复 | 统一用 `Java::String` |
| `ClassNotFoundException`、`intern` | 过于细碎，复用率低 | 归入 `Java::异常`、`Java::String` |
| `异常`、`异常体系`、`异常处理` | 层级混乱 | 统一用 `Java::异常` |

### 同一会话一致性

- **首次使用**：为某个概念打标签时，确定其标准名称
- **后续复用**：相同概念必须使用完全相同的标签
- **跨卡片检查**：生成新卡片前，检查已有卡片的标签，保持一致

### 建议的标准标签（示例）

| 领域 | 推荐标签 | 说明 |
|------|----------|------|
| Java基础 | `Java::基础` | 语法、数据类型、运算符等 |
| Java字符串 | `Java::String` | 所有String相关知识点 |
| Java集合 | `Java::集合` | HashMap、HashSet等统一归入 |
| Java异常 | `Java::异常` | Checked、Unchecked、Error统一归入 |
| JVM内存 | `JVM::内存` | 堆、栈、常量池等 |
| JVM优化 | `JVM::优化` | JIT、AOT、逃逸分析等 |
| 通用标记 | `面试高频`、`易混淆` | 跨领域的辅助标签 |

---

## 7. 导入执行

使用anki的mcp server提供的工具直接导入：
- **牌组**：根据内容主题自动确定，默认"每日学习"
- **模板**：优先使用 `SmartCard`，Cloze题型使用 `Cloze`

**不输出卡片预览**，只确认导入完成或报告问题。
```

## [](https://linux.do/t/topic/1510992#p-13038908-smartcard-5)笔记模板：SmartCard

### [](https://linux.do/t/topic/1510992#p-13038908-fields-6)字段（Fields）

1.   **Front** - 问题
2.   **Answer** - 核心答案
3.   **Explain** - 解释说明（可选，支持多行）
4.   **Mnemonic** - 助记（可选）

* * *

## [](https://linux.do/t/topic/1510992#p-13038908-front-template-7)正面模板（Front Template）

```
<div class="front">{{Front}}</div>
```

* * *

## [](https://linux.do/t/topic/1510992#p-13038908-back-template-8)背面模板（Back Template）

```
<div class="front">{{Front}}</div>

<hr id="answer">

<div class="back">
  <div class="answer">{{Answer}}</div>
  
  {{#Explain}}
  <div class="explain">{{Explain}}</div>
  {{/Explain}}
  
  {{#Mnemonic}}
  <div class="mnemonic">💡 {{Mnemonic}}</div>
  {{/Mnemonic}}
</div>
```

* * *

## [](https://linux.do/t/topic/1510992#p-13038908-styling-css-9)样式（Styling / CSS）

```
/* ===== 整体卡片 ===== */
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  font-size: 18px;
  line-height: 1.7;
  color: #333;
  background: #fafafa;
  padding: 24px;
  max-width: 600px;
  margin: 0 auto;
}

/* ===== 问题区 ===== */
.front {
  font-size: 20px;
  font-weight: 500;
  color: #222;
}

/* ===== 分隔线 ===== */
hr#answer {
  border: none;
  border-top: 2px solid #e0e0e0;
  margin: 20px 0;
}

/* ===== 背面容器 ===== */
.back {
  text-align: left;
}

/* ===== 核心答案区 ===== */
.answer {
  font-size: 20px;
  font-weight: 600;
  color: #1a73e8;
  background: #e8f0fe;
  padding: 14px 18px;
  border-radius: 8px;
  margin-bottom: 20px;
  border-left: 4px solid #1a73e8;
  line-height: 1.5;
}

/* ===== 解释说明区 ===== */
.explain {
  font-size: 16px;
  color: #444;
  background: #fff;
  padding: 16px 20px;
  border-radius: 8px;
  margin-bottom: 20px;
  border: 1px solid #e0e0e0;
}

/* ===== 助记区 ===== */
.mnemonic {
  font-size: 15px;
  color: #5d4037;
  background: #fff8e1;
  padding: 12px 16px;
  border-radius: 8px;
  border-left: 4px solid #ffc107;
  line-height: 1.6;
}

/* ===== 基础HTML标签美化 ===== */

/* 加粗/关键词 */
b, strong {
  color: #c62828;
  font-weight: 600;
}

/* 段落小标题 */
h4 {
  font-size: 15px;
  font-weight: 600;
  color: #1565c0;
  margin: 16px 0 8px 0;
  padding-bottom: 4px;
  border-bottom: 1px solid #e3f2fd;
}
h4:first-child {
  margin-top: 0;
}

/* 列表 */
ul, ol {
  margin: 10px 0;
  padding-left: 24px;
}
li {
  margin: 8px 0;
  line-height: 1.6;
}

/* 代码 */
code {
  background: #f5f5f5;
  padding: 2px 8px;
  border-radius: 4px;
  font-family: "SF Mono", Monaco, Consolas, monospace;
  font-size: 0.9em;
  color: #d63384;
  border: 1px solid #e0e0e0;
}

/* 代码块 */
pre {
  background: #263238;
  color: #aed581;
  padding: 12px 16px;
  border-radius: 6px;
  overflow-x: auto;
  font-size: 14px;
  line-height: 1.5;
}
pre code {
  background: none;
  border: none;
  padding: 0;
  color: inherit;
}
```

* * *

## [](https://linux.do/t/topic/1510992#p-13038908-h-10)导入方法

1.   打开 Anki → 工具 → 管理笔记类型
2.   点击「添加」→ 选择「添加: 基础」→ 命名为 `SmartCard`
3.   点击「字段」→ 添加字段：`Answer`, `Explain`, `Mnemonic`
4.   点击「卡片」→ 分别粘贴正面模板、背面模板、CSS样式
5.   保存

## [](https://linux.do/t/topic/1510992#p-13038908-cloze-11)笔记类型名称：Cloze（用的是官方自带模板直接改）

### [](https://linux.do/t/topic/1510992#p-13038908-fields-12)字段（Fields）

1.   **Text** - 包含填空标记的主内容
2.   **Back Extra** - 补充说明（可选）

* * *

## [](https://linux.do/t/topic/1510992#p-13038908-front-template-13)正面模板（Front Template）

```
<div class="cloze-card">
  <div class="cloze-text">{{cloze:Text}}</div>
</div>
```

* * *

## [](https://linux.do/t/topic/1510992#p-13038908-back-template-14)背面模板（Back Template）

```
<div class="cloze-card">
  <div class="cloze-text">{{cloze:Text}}</div>
  
  {{#Back Extra}}
  <hr id="extra">
  <div class="extra">{{Back Extra}}</div>
  {{/Back Extra}}
</div>
```

* * *

## [](https://linux.do/t/topic/1510992#p-13038908-styling-css-15)样式（Styling / CSS）

```
/* ===== 整体卡片 ===== */
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  font-size: 18px;
  line-height: 1.8;
  color: #333;
  background: #fafafa;
  padding: 24px;
  max-width: 600px;
  margin: 0 auto;
}

/* ===== Cloze卡片容器 ===== */
.cloze-card {
  text-align: left;
}

/* ===== 主文本区 ===== */
.cloze-text {
  font-size: 19px;
  color: #222;
  line-height: 1.9;
}

/* ===== 填空答案（正面显示[...]，背面显示答案） ===== */
.cloze {
  font-weight: 700;
  color: #1a73e8;
  background: #e8f0fe;
  padding: 2px 10px;
  border-radius: 4px;
  border-bottom: 2px solid #1a73e8;
}

/* ===== 未激活的填空（其他编号的cloze） ===== */
.cloze-inactive {
  color: #666;
  background: #f0f0f0;
  padding: 2px 8px;
  border-radius: 4px;
  text-decoration: underline;
  text-decoration-style: dotted;
  text-underline-offset: 3px;
}

/* ===== 分隔线 ===== */
hr#extra {
  border: none;
  border-top: 2px solid #e0e0e0;
  margin: 24px 0 20px 0;
}

/* ===== 补充说明区 ===== */
.extra {
  font-size: 16px;
  color: #444;
  background: #fff;
  padding: 16px 20px;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
  border-left: 4px solid #4caf50;
}

/* ===== 基础HTML标签美化 ===== */

/* 加粗/关键词 */
b, strong {
  color: #c62828;
  font-weight: 600;
}

/* 段落小标题 */
h4 {
  font-size: 15px;
  font-weight: 600;
  color: #1565c0;
  margin: 16px 0 8px 0;
  padding-bottom: 4px;
  border-bottom: 1px solid #e3f2fd;
}
h4:first-child {
  margin-top: 0;
}

/* 列表 */
ul, ol {
  margin: 10px 0;
  padding-left: 24px;
}
li {
  margin: 8px 0;
  line-height: 1.6;
}

/* 代码 - 行内 */
code {
  background: #f5f5f5;
  padding: 2px 8px;
  border-radius: 4px;
  font-family: "SF Mono", Monaco, Consolas, monospace;
  font-size: 0.9em;
  color: #d63384;
  border: 1px solid #e0e0e0;
}

/* 代码块 */
pre {
  background: #263238;
  color: #aed581;
  padding: 12px 16px;
  border-radius: 6px;
  overflow-x: auto;
  font-size: 14px;
  line-height: 1.5;
}
pre code {
  background: none;
  border: none;
  padding: 0;
  color: inherit;
}

/* ===== 夜间模式适配 ===== */
.nightMode .card,
.night_mode .card {
  background: #1e1e1e;
  color: #e0e0e0;
}
.nightMode .cloze-text,
.night_mode .cloze-text {
  color: #e0e0e0;
}
.nightMode .cloze,
.night_mode .cloze {
  background: #1e3a5f;
  color: #64b5f6;
  border-bottom-color: #64b5f6;
}
.nightMode .cloze-inactive,
.night_mode .cloze-inactive {
  background: #2d2d2d;
  color: #999;
}
.nightMode .extra,
.night_mode .extra {
  background: #2d2d2d;
  border-color: #444;
}
.nightMode code,
.night_mode code {
  background: #2d2d2d;
  border-color: #444;
  color: #f48fb1;
}
```

