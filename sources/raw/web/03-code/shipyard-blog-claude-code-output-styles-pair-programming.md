# Shipyard：Claude Code 输出风格与结对编程

- 链接：https://shipyard.build/blog/claude-code-output-styles-pair-programming/
- 作者：Shipyard Team
- 获取方式：网页正文（trafilatura 提取）

---

As a developer, you’ve gone into software likely because you *enjoy* writing code. This isn’t a chore for you, and you get some degree of fulfillment from it. If you’re reading this, you’re probably using agentic devtools to improve your productivity, and take away some of the toil that comes with dev work.

Why should agents get to do all the fun parts of software dev, like writing code? [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (the world’s favorite AI coding agent) has a feature that allows you to make agentic dev more *active.*

Here’s how you can write code *alongside* Claude Code, instead of through pure natural language prompts.

## Why pair program with AI agents?

Agents can generate code incredibly fast, and at volumes that are tough for humans to truly digest. Many devs end up turning off their brains at a certain point, because understanding the agent’s code is *much slower* than prompting fast and getting a working result.

This leads to devs accepting agentic code suggestions blindly. It’s a slippery slope for sure: if 90% of an LLM’s suggestions are good, why should you have to sift through all of them with a fine-toothed comb, especially if you hardly find anything off? Then next thing you know, your agent accidentally corrupts your database or changes your file permissions.

Pair programming with an agent keeps you, as the developer, engaged and in the driver’s seat. You’re actively thinking through every choice, being intentional. It’s more akin to the mindset you get into when you’re 100% writing code.

Plus, AI agents are good for many things beyond picking up coding tickets. Thanks to their LLMs’ wide knowledge bases, they can explain things pretty well, and pick up on niche software patterns. They can step into that “pair” role and guide you. This brings them closer to human-human pair programming

## Claude Code output styles

In August 2025, Anthropic introduced a new feature for changing how Claude Code interacts with a user. [Output styles](https://docs.anthropic.com/en/docs/claude-code/output-styles) can help extend CC beyond its popular use cases, and Anthropic suggests this can make CC act as any kind of agent (with the same core read/write/execute/list capabilities).

An output style for Claude Code is functionally the same as a system prompt. Claude’s default output style is concise, and targeted mainly at solving software engineering tasks.

CC includes two other built-in output styles, which are (in our opinion) more conducive to pair programming.

### Explanatory output style

To set: `/output-style explanatory`

Claude Code’s explanatory mode is similar to the default system prompt, but offers educational insights along the way. This is a good mode for newer devs who don’t want CC to do all the thinking for them, and are hoping to stay engaged during agentic dev tasks.

CC will add little “insight” blocks within its responses. These are kind of like pro tips, or just extra background info. Since default CC is concise, this is helpful for getting more complete, detailed answers.

**Sample prompt:**

`look at the CLI docs, and tell me what can be improved in the scope of DevEx`

**CC explanatory mode response (excerpt):**

`...`

`Strategic Long-term Enhancements`

`7. **Progressive disclosure with expandable sections**`

`8. **Integration examples with popular IDEs and tools**`

`9. **Video walkthroughs for complex workflows**`

`10. **Interactive CLI tutorial or guided setup**`

`★ Insight ─────────────────────────────────────`

`The current documentation is comprehensive but lacks the user-centric`

`design principles that make modern developer tools delightful to use. The`

`biggest opportunities are in restructuring content around workflows and`

`reducing friction in the getting-started experience.`

`──────────────────────────────────────────`

### Learning output style

To set: `/output-style learning`

Learning mode is more interactive than default or explanatory mode. It gives the user small programming tasks to complete during development, so they can contribute code. It’s really beneficial for junior engineers looking for a pair programming setup, as it will break down tasks, assign them, and then give feedback on the completed snippet.

This was our favorite CC output style, since it let us pick up fun coding tasks and walked us through the why/how of every action.

**Sample prompt:**

`look at the CLI docs, and tell me what can be improved in the scope of DevEx`

**CC learning mode response (excerpt):**

**`Your Task:`** In docs/CLI.mdx, create a new “Quick Start” section\`

`that should appear right after line 13 (after the opening description).`

`Look for TODO(human). This section should provide developers with the`

`fastest possible path from installation to their first successful CLI`

`interaction.`

**`Guidance:`** Consider what a developer most wants to accomplish when they\`

`first install the CLI - probably seeing their environments and confirming`

`everything works. Think about the psychological impact of early success`

`vs. getting stuck on setup details. The section should be concise (3-5`

`commands max) and include a verification step that shows success.`

## Creating your own custom output style

Claude Code is super customizable, and most of this can be done via natural language in Markdown files. You can create your own output style (which is a system prompt for CC) by running:

`/output-style:new [name] [verbose description]`

Remember, everything that CC knows about software engineering lives in the default output style. You’ll need to re-enlighten it here if you want it to be a strong software engineering pair.

Once you provide a description of what output style you’d like, Claude will generate a markdown file, inferring what other characteristics it should have. You can find it in your `~/.claude/output-styles/` directory. You’ll want to tweak this to fit what you had in mind.

## Changing Claude Code’s system prompt

There are a few ways to change/augment CC’s system prompt.

### Option 1: with output styles (recommended)

Claude’s output styles *are* system prompts. If you want to completely override Claude’s default personality, skillset, and behavior, this is how you can do it.

This means you’ll need a super high-quality, detail-oriented prompt. Claude Code can help you write one, but don’t expect it to be as optimized as CC’s default prompt. This is still a great exercise for prompt engineers, and also valuable for those who want to use a terminal-based agent for miscellaneous non-dev tasks.

To recap: you’ll do this by launching a Claude Code session and running:

```
/output-style:new [name] [verbose description]
```
### Option 2: with append-system-prompt

If you want to keep the general behavior of Claude Code’s system prompt, but add a few more high-priority instructions, you can use the `--append-system-prompt` flag. As part of the system prompt, CC will prioritize this over any other config settings (e.g. CLAUDE.md) or prompts.

You can append your own instructions by running:

```
claude --append-system-prompt "Never commit to main. Alert me when a new feature does not have unit tests written for it"
```
### Option 3: with CLAUDE.md

Your CLAUDE.md file is not a system prompt. Rather, it’s a prioritized instruction that Claude Code will refer to *one tier below* the instructions in the system prompt.

Usually, A CLAUDE.md file is stored at the project level, and is automatically pulled into context when you launch a session. It’ll typically store instructions and context relevant to a project, which will save you tokens and guarantee better outputs.

You can run the `/init` slash command to create it, or add one manually to your project’s root directory.

## Keep your dev skills sharp

A hybrid of agentic and human dev can be a really refreshing balance for many programmers. You can keep learning good patterns, stay engaged during a dev session, and use your brain in a different way (vs. pure agentic dev). Thankfully, you’ve got plenty of ways to customize this to your liking with Claude Code’s output styles. You can get a more fulfilling dev experience just by toggling system prompts.

Happy coding!
