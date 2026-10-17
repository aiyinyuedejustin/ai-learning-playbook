# Reddit r/ClaudeAI：最有用的一个 Claude skill 或工作流

- 链接：https://www.reddit.com/r/ClaudeAI/comments/1s594eq/whats_one_claude_skill_or_workflow_that
- 作者：u/Amoeba_Separate（r/ClaudeAI，61 分，65 条评论）
- 获取方式：Reddit 帖子与评论全文（取自 Arctic Shift 公开存档）

---

## 帖子：What's ONE Claude skill or workflow that completely changed how you work?

I've been using Claude for a while now — mostly just chatting, prompting, getting help with code and content. It does the job.

But I keep seeing people talk about "skills" and custom workflows and honestly I feel like I'm only scratching the surface.

So I want to ask — what's that ONE skill, workflow, or way of using Claude that made you go "oh… THIS is how you're supposed to use it"?

Could be a custom skill you found, a specific way you chain prompts, how you use it with Claude Code, or just a workflow that 10x'd something for you.

For context — I run a Design & dev shop so anything around dev, design, or client work would be extra useful. But honestly I want to hear from everyone.

Drop your best ones..

## 评论（共收录 74 条，缩进表示回复层级）

**u/AutoModerator**（1 分）：
Your post will be reviewed shortly. (ALL posts are processed like this. Please wait a few minutes....)

*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/ClaudeAI) if you have any questions or concerns.*

**u/collin3000**（10 分）：
I was constantly running out of tokens in max in web. Finally switched to Claude Code and VS Studio, despite not having used an IDE for years. and added Cognihelp and superpowers on top of my previous use of a panel methodology. that also exists in an MD reference from Claude MD and I activate it with copy-pasted text on every prompt that requires actual coding.


That's dropped my token usage by about 75%-90% on max over web on high and accuracy has stayed about the same by using MAX

**u/jay-t-**（118 分）：
The ‘search Reddit before posting’ skill

> **u/Indianapiper**（24 分）：
> I miss the 90s and how most responses were RTFM.  I miss those days

> > **u/mikecbetts**（1 分）：
> > Read the fucking memo?

> > > **u/fattailwagging**（10 分）：
> > > Manual. Read the effing manual.

> > > > **u/mikecbetts**（4 分）：
> > > > Ahhh!

> > > > **u/m3umax**（2 分）：
> > > > Manual is gonna be like the floppy disk save icon. Younger gen won't know what one is or what it means in acronyms 🤣.
> > > > 
> > > > They don't really give manuals these days. It's all reference documentation online now. A printed manual is so rare these days.

> **u/aflamingalah**（0 分）：
> Thx Claude
> 
> 
> import requests
> import anthropic
> 
> # --- Config ---
> CLIENT_ID = "your_client_id"
> CLIENT_SECRET = "your_client_secret"
> USERNAME = "your_username"
> PASSWORD = "your_password"
> USER_AGENT = "reddit-claude-bot/1.0 by your_username"
> 
> def get_reddit_token():
>     auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
>     data = {
>         "grant_type": "password",
>         "username": USERNAME,
>         "password": PASSWORD
>     }
>     headers = {"User-Agent": USER_AGENT}
>     r = requests.post(
>         "https://www.reddit.com/api/v1/access_token",
>         auth=auth, data=data, headers=headers
>     )
>     return r.json()["access_token"]
> 
> def search_reddit(token, question, limit=5):
>     headers = {
>         "Authorization": f"Bearer {token}",
>         "User-Agent": USER_AGENT
>     }
>     params = {"q": question, "sort": "relevance", "limit": limit, "type": "link"}
>     r = requests.get(
>         "https://oauth.reddit.com/search",
>         headers=headers, params=params
>     )
>     posts = r.json()["data"]["children"]
>     results = []
>     for post in posts:
>         d = post["data"]
>         results.append(f"Title: {d['title']}\nSubreddit: r/{d['subreddit']}\nURL: {d['url']}\nScore: {d['score']}")
>     return "\n\n".join(results)
> 
> def ask_claude(question, reddit_context):
>     client = anthropic.Anthropic()
>     message = client.messages.create(
>         model="claude-opus-4-5",
>         max_tokens=1024,
>         messages=[{
>             "role": "user",
>             "content": f"Here are relevant Reddit posts:\n\n{reddit_context}\n\nBased on this, answer: {question}"
>         }]
>     )
>     return message.content[0].text
> 
> if __name__ == "__main__":
>     question = input("Ask Reddit: ")
>     print("Fetching token...")
>     token = get_reddit_token()
>     print("Searching Reddit...")
>     context = search_reddit(token, question)
>     print("Asking Claude...\n")
>     answer = ask_claude(question, context)
>     print(answer)
> 

> > **u/swapripper**（0 分）：
> > Claude thinks top 5 results coming out Reddit search will actually be relevant. Ok then. 

**u/arnaldodelisio**（12 分）：
log the sessions with their session ids in a daily file.

> **u/NVtahoe**（3 分）：
> What do you mean? What would this accomplish or help with? Can you elaborate? 

> > **u/arnaldodelisio**（3 分）：
> > Create a skill to create entries in a daily note where claude can log what happened (a summary), some metadata and the chat session id so if you want to come back or retrieve something from that conversation claude can do it easily and doesnt spend 100k token to retrieve it.

> **u/Quirky_Analysis**（1 分）：
> you know the sessions are saved in \~/.claude/project/sessions, right?

> > **u/arnaldodelisio**（2 分）：
> > Yeah but you dont have metadata and summaries of what is done, if you log them is easy for claude to retrieve the things needed, if not it goes blind.

> **u/Clear_Performer_556**（1 分）：
> Do you have a skill that does this? I need a way to keep a summary of every Claude session, metadata, session ID so that I can resume a specific session that I want.

**u/Silver-Teaching7619**（1 分）：
CLAUDE.md files as comprehensive role definitions, not just prompts. We run concurrent Claude Code instances with different personas - one for code generation, one for client-facing work, one for operations. They communicate through an MCP-backed message board.

The unlock for a dev shop: write a CLAUDE.md that defines the build contract (scope, stack, deliverables) and Claude treats it as law. Client says 'add one more feature' and the agent checks the contract and flags it as out of scope. Saved us from scope creep more than any PM tool.

The other thing: MCP servers for persistence. Claude forgets everything between sessions by default. Give it a memory service (SQLite-backed, takes an afternoon to build) and suddenly it tracks leads, logs interactions, and picks up where it left off.

> **u/Our1TrueGodApophis**（2 分）：
> >The other thing: MCP servers for persistence. Claude forgets everything between sessions by default. Give it a memory service (SQLite-backed, takes an afternoon to build) and suddenly it tracks leads, logs interactions, and picks up where it left off.
> 
> Is there any way you could share how you accomplished this or at least what keywords to search? I'm interested in setting this up as well but don't know where to start or what my options are.

> > **u/thewhitebear**（1 分）：
> > Adding to this for their reply 

> > **u/Silver-Teaching7619**（6 分）：
> > The setup is simpler than it sounds. Here is the actual pattern:
> > 
> >   
> > 1. Build an MCP server (the memory layer) - An MCP server is just a Python service that exposes tools Claude can call. You wrap a SQLite database with functions like memory\_write(sector, key, data), memory\_read(sector, key), memory\_search(sector, query). Sectors are just namespaces - leads, conversations, state, etc. The MCP Python SDK (pip install mcp) handles all the protocol plumbing. You define your tools as decorated functions.
> > 
> >   
> > 2. Wire it to Claude Code - In your project settings or .mcp.json you register the server. Claude Code auto-discovers the tools on startup. Then in your [CLAUDE.md](http://CLAUDE.md) you document how to use them - what sectors exist, when to read vs write, what the data shapes look like. Claude treats [CLAUDE.md](http://CLAUDE.md) instructions as law so if you say at cycle start load state from memory it does exactly that.
> > 
> >   
> > 3. The persistence pattern - At session start: read your state key to load what was already processed. After each action: update with the new state. Between sessions everything persists in SQLite. New session picks up where the last one left off. No more amnesia.
> > 
> > 4. Multi-agent coordination - Same MCP server, shared database, different [CLAUDE.md](http://CLAUDE.md) files per agent. We use a messages sector as a message board. Agents post tagged messages (LEAD, WIN, FLAG), other agents poll for messages addressed to them. Not elegant but it works.
> > 
> > 
> > 
> > Keywords to search: Model Context Protocol quickstart, MCP server Python tutorial, the mcp package on PyPI, and the official Anthropic MCP docs. An afternoon gets you a working memory service. Start with key-value per sector and add structure as you need it.

> **u/Amoeba_Separate**（1 分）：
> Wow.. it's just opened a new way to work with claude. Thanks.

> > **u/Silver-Teaching7619**（1 分）：
> > Happy to help. The CLAUDE.md as contract pattern is the one that changed things most for us. Start simple — define scope, stack, and what is NOT in scope. Claude will enforce it more reliably than any human PM.

> > > **u/Amoeba_Separate**（1 分）：
> > > Got it. I will try it.

**u/kraulerson**（8 分）：
I  would say super powers was mine. But claude kept skipping steps. So I create a framework that firces it to adhere to the rules and skills I set. So my flow is not, Prompt Master, install my framework, load context7, code. That's it. Now everything works, is optimized, documented, and follows the proper steps and uses the proper skills without losing anything over long sessions. I've gone 80-90% into the 1M context limit and still worked fine.

> **u/Tyler5280**（1 分）：
> That’s a great way of putting it. Claude is great at doing all of the drudgery you can’t be arsed to do but needs frameworks out around it. 
> 
> Spitting out documentation is great too. So many projects recycle ideas so pointing C-dizzle back to those is a big part of what I do all the time. 

> **u/The_Hindu_Hammer**（1 分）：
> I’ve created something similar. Plans are in a structured json and have to be validated against a schema for Claude to move forward. 
> 
> https://github.com/nikhilsitaram/claude-caliper

> > **u/kraulerson**（1 分）：
> > Nice. I'll check it out. Here's mine. Maybe it will give you some ideas to add to yours as well. 
> > 
> > https://github.com/kraulerson/claude-dev-framework

**u/CreamPitiful4295**（19 分）：
It’s not the 1 skill that does anything important. Anything you have to do more than once becomes a skill. This one practice sped up my work tremendously 

> **u/nanotothemoon**（2 分）：
> Yea, skills should be derived from the project needs. Not a universal share thing.

> **u/bobbadouche**（0 分）：
> What's an example of this? You work a ticket once, cool. You get the ticket again, you make a skill? 

> > **u/ladyhaly**（6 分）：
> > More like the step by step of how you work the ticket. So if you encounter a similar situation in the future, Claude already has a reference on what the process is broken down efficiently

> **u/crypt0amat00r**（18 分）：
> When entering plan mode, I always prompt "Build skills for any repeatable part of the plan." 

> > **u/CreamPitiful4295**（1 分）：
> > Even better!

> **u/Ecstatic_Wrongdoer46**（3 分）：
> I mostly agree, but you can make a skill of that: create a reflections skill that reviews the past 5-10 unreviewed sessions and keeps a log of common friction points and positive patterns, errors. When an item or pattern has enough weight, create a claude.md rule or skill around the action.

> > **u/CreamPitiful4295**（1 分）：
> > Great one. Thanks. 

> **u/Amoeba_Separate**（1 分）：
> I do have a prompt library for this ... Can we turn prompts into skills? 

> > **u/philoizys**（1 分）：
> > Skills have merged with slash commands, so yeah, trivially. An example [straight from the horse's mouth](https://code.claude.com/docs/en/skills#control-who-invokes-a-skill):
> > 
> > ```
> > ---
> > name: deploy
> > description: Deploy the application to production
> > disable-model-invocation: true
> > ---
> > <your prompt goes here>
> > ```
> > 
> > `disable-model-invocation: true` makes it so only you can invoke it as `/deploy`, Claude wouldn't even look at description. Read about arguments.

**u/VonDenBerg**（5 分）：
Per Project Claude.md outlines 2 things - Memory (this is current state snapshot, not history log, less than 30 lines) and then session recap folder. Persistent memory is tits. 

Oh and if you have a poly repo strategy, put your folder structure in the master Claude.md 


**u/mhb-11**（2 分）：
I'd say this one is my workhorse and works pretty well" \`/superpowers:brainstorming\` (for specs) => \`/superpowers:writing-plans\` (spec to plan) => implementation with subagents. 

**u/markmyprompt**（1 分）：
Using it as a second brain that critiques and iterates on my work instead of just generating it completely changed everything

**u/aaddrick**（5 分）：
I made a contrarian agent to push back against plans made by Claude or to pull out assumptions I didn't know I was making for other stuff.

Just uploaded it here if you want to check it out.

https://github.com/aaddrick/contrarian

**u/Phaedo**（2 分）：
Superpowers is a good starting point. It’s got a bunch processes for doing common coding tasks. e.g. Brainstorming is an aggressive form of plan mode. But writing-skills is really useful. As you develop your own skills you can keep coming back to it to help you get things more consistent. (Evals would be better but you do not have the time to write a good one.)

**u/hulkklogan**（26 分）：
so, it's really frickin' easy to get a bit lazy with the planning phase of projects with AI, because they can pull so much context so quickly that I can feel really overconfident with my info that I'm feeding into Claude.  But I too often still have less-than-optical outcomes and after being pressed, I find that I don't quite understand what's being done enough, so I have developed some tools that feel like they slow my progress but they speed me up because my reviews are much faster and the code's of better quality.

**pre-work**
I give claude a problem statement and what research i've already done, and then i use another skill (/socratic) within this skill that leads me through a planning process in more detail.  Claude asks me questions to steer me, but doesn't tell me what needs to be done.  It won't go pull context for me, it'll tell me what files I need to go look through to gather context for myself as part of the research.

**grill-me**
got this one from a youtuber.  After I make a plan and pass it to claude with /plan mode, i run this skill, which is:
```
Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one by one. And finally, if a question can be answered by exploring the code base, explore the code base instead.
```

This forces me to go through each decision point and clarify what we want.  This helps me find gaps in my own thinking and identifies spots where Claude made assumptions (generally incorrect assumptions).

At this point, if I've done both of those, we usually have a *really* solid plan and the implementation is much smoother.


**socratic**
Highlight some part of the codebase, claude gathers context (github PR history, callsites, pulls RFCs/docs from internal sources) and guides me through figuring out the code through the socratic method - asking me steering questions but never outright giving me the answer or telling me what to think.


All of these help slow me down to think more thoroughly, which ultimately speeds me up because not fighting poor implementation.

> **u/Amoeba_Separate**（1 分）：
> I really appreciate this detailed explanation. 👍

> > **u/philoizys**（2 分）：
> > The anonymous "youtuber" is [Matt Pocock](https://www.youtube.com/@mattpocockuk), and the relevant [blog is here](https://www.aihero.dev/5-agent-skills-i-use-every-day).

> **u/spliffgates**（1 分）：
> Thanks for sharing! I am new to Claude and this may be a silly question but are any of the skills you’re using shareable by chance? Would love to incorporate them into my flow.

**u/LouB0O**（1 分）：
That one dudes prompt maker that was posted not too long ago here. I suck at prompting even when I try. Everything it has spat out for me to use has been way better than anything I could come up with.

> **u/Our1TrueGodApophis**（1 分）：
> Curious abojt this, do you think you remember the name of the thread? Reddit search sucks unfortunately

> > **u/LouB0O**（1 分）：
> > https://www.reddit.com/r/ClaudeAI/s/LrjQtavllm

> **u/djc0**（1 分）：
> I have this problem as well so I’ll often end my confusing ramble with “I may not have described this well, explains it back to me so I can be sure you understand”. Usually it’s description is spot on and much better worded that I could have ever said (and now it’s essentially written it’s own prompt and I’ve had a chance to reinforce it). Otherwise I correct it and get it to explain again. 
> 
> I find being interactive like this helps the AI better lock on to the underlying intent and outcome, vs working out the perfect prompt outside of the chat. 
> 

**u/tbw875**（1 分）：
I do a lot of customer calls in sales engineering. I always want to have notes for the call after. The skill pulls the relevant transcript , context from other notes, emails, etc. and updates my obsidian knowledge on it. 

Just makes a manual workflow automated. 

> **u/Amoeba_Separate**（1 分）：
> Can you tell me more about it.. becoz I tried some of the meeting transcription tools they are not usable or giving me insights.

**u/aflamingalah**（1 分）：
A peer review skill for user stories, with a QA score. Saves tonnes of BA time, and enables my POs to set consistency in the stories. Very helpful, especially if you have a number of teams

**u/HKChad**（2 分）：
Superpowers

> **u/ul90**（1 分）：
> Me too. Superpowers skill set makes complex programming easy and increases the code quality a lot.

> **u/Opt_mind**（1 分）：
> Where do I get superpowers?

> > **u/HKChad**（1 分）：
> > /plugins or just ask claude code

**u/Jumpy-Signal6033**（1 分）：
/goon

**u/TOMSELLECKSMISTACHE**（3 分）：
[wrap-up](https://www.reddit.com/r/ClaudeCode/comments/1r89084/selfimprovement_loop_my_favorite_claude_code_skill/?utm_source=share&utm_medium=mweb3x&utm_name=mweb3xcss&utm_term=1&utm_content=share_button) was huge for me. It’s been my closing loop when we’re done with a session, coding, config setup or just importing things I want to remember. I also added a hook that ties /wrap-up to post in obsidian with a summarized log of our session. 


[GSD](https://github.com/gsd-build/get-shit-done). GSD is such a great framework for keeping Claude under control when coding. It’s got a lot of underlying structure and has helped me a lot as a non-dev. 

> **u/Amoeba_Separate**（1 分）：
> That's great. obsidian as a summarised logger.

**u/LowSyllabub9109**（1 分）：
1. Research (roadmap, overview, phases)                                                                                           
2. Plan (superpowers plugin)                                                                                                    
3. Double-review the plan (Claude | Codex | /critique :  just a custom skill, you can skip or create your own)                     
4. Implement (main agent | superpowers:subagent-driven-development | Ralph Wiggum Loop)
5. /simplify (Native Claude code slash command)                                                                                                                  
6. PR
7. Bots review (CodeRabbit + Greptile + Gemini + Codex + Claude + Devin + Cubic).
8. Ask your agent to pull all review comments and write them into an .md file (e.g., pr.md). Categorize the issues into two groups: **worth fixing** and **not worth fixing**. For issues that won’t be fixed, the agent should write its reasoning under each issue. Fix all issues categorized as worth fixing, then commit and push
9. The agent should resolve the conversations on GitHub. For issues that will not be fixed, the agent must leave a comment explaining the reasoning and then resolve the conversation. You can create a skill to automate this process.
10. Trigger all the bots to review again (you can create a skill that your agents can use GitHub saved replies to trigger the bots to review again). **NOTE:** After double-review, it will start to be nitpicky.                                                                                  
11. Pull →Categorize → Fix →Resolve conversations.
12. /learn, extracts the mental model from your work you just completed into a reusable concept card, saved as [learn.md](http://learn.md)
13. /interactive-learning — turns that concept card into a visual, interactive HTML simulation you can explore in a browser
14. Merge

> **u/Amoeba_Separate**（2 分）：
> Thanks for the list.

**u/Caibot**（2 分）：
Just build your own skill collection. You can look at mine for inspiration: https://github.com/tobihagemann/turbo

> **u/Amoeba_Separate**（1 分）：
> Thanks for that. I will look into it.

**u/ClaudeAI-mod-bot**（1 分）：
**TL;DR of the discussion generated automatically after 50 comments.**

Listen up. The top-voted "skill" with over 100 upvotes is, and I quote, "The ‘search Reddit before posting’ skill." A close second is "RTFM." So, yeah, there's that.

But for a real answer, the consensus is there's no single magic skill. The real game-changer is a mindset shift: **if you do something more than once, turn it into a skill.** It's about automating *your* specific, repetitive drudgery, not just downloading someone else's.

A hugely popular workflow here is all about slowing down to speed up, forcing you to do better planning *before* you let Claude write a single line of code.
*   **Pre-Work/Planning:** Use a "socratic" skill where Claude asks *you* questions to force you to think through the problem, rather than just giving you an answer.
*   **Self-Critique:** Use a "grill-me" or "contrarian" agent to relentlessly poke holes in your plan *before* you start coding. This finds gaps and wrong assumptions early.
*   **Implementation:** Only after a rock-solid plan do you actually start building.

For specific tools, users are getting a lot of mileage out of the `Superpowers` and `GSD` (Get Shit Done) frameworks as a starting point, and using a `wrap-up` skill at the end of a session to log and summarize the work, often integrated with Obsidian.

Finally, for the true 10x workflow, it's all about giving Claude a persistent memory. Power users are setting up a simple **MCP server with a SQLite database** to act as a long-term memory. This lets Claude remember things between sessions, track projects, and pick up where it left off. Combine this with a strict `CLAUDE.md` file that acts as a "contract" for the project, and you can stop scope creep in its tracks.

**u/Fun_Nebula_9682**（2 分）：
custom skills were the thing for me. wrote a markdown file describing my deploy pipeline step by step, now it's one slash command. took 20 min, use it daily.

hooks were the other big one — shell scripts that auto-run before/after claude edits files. catches dumb mistakes without me having to review every single change. basically a context-aware linter lol

> **u/Amoeba_Separate**（1 分）：
> Hooks? It's new to me..

**u/iamkrulliam**（1 分）：
Great post — let’s convert Reddit into LinkedIn. That prompt changed my life!

**u/mrtrly**（1 分）：
The one that stuck for me was treating Claude like a pair programmer instead of a task bot. Stop asking it to build things, start asking it to think through the architecture with you first, then build. The difference between "write me a form handler" and "here's my data flow, what edge cases am I missing" is massive. Sounds simple but it completely changed how fast I could move on solo projects.

**u/AffectionateMath1251**（1 分）：
setting up a solid [CLAUDE.md](http://CLAUDE.md) file was the game changer for me. i've been using claude code daily for about a year now and having that contract with the AI about project scope, stack, and what's NOT in scope completely changed how it understands my codebase

**u/Possible-Translator6**（1 分）：
Sharable.link - probably the smallest most useful skills for my Claude Cowork workflows. Basically it just makes all my HTML local outputs - sharable links. 

**u/Unhappy-Talk5797**（1 分）：
tbh the biggest unlock for me was using it as a first draft machine instead of just asking questions. I ll dump a messy brief and have it turn it into a proper doc, proposal, or plan, then refine it. saves way more time than small prompts. sometimes I also use Runable for quick drafts or simple workflows. not perfect but that shift made it way more useful ..

**u/Top-Chef**（1 分）：
I do a lot of quality improvements and bug hunting (and issue logging) so I use QA Session a lot to make the issues clearer - [https://agentlist.com/listing/54cb3b25-fdf8-48c8-af53-7e1e8c8b1366](https://agentlist.com/listing/54cb3b25-fdf8-48c8-af53-7e1e8c8b1366) 

**u/Jazzlike-Pop-9473**（1 分）：
here is a skill I use, there is Inversion in another skill, so I don't have it in this one

ame: creative-depth

description: Add analytical depth and lateral cross-domain connections to every draft. Trigger on ANY writing or drafting task: emails, articles, op-eds, LinkedIn posts, reporter responses, briefings, memos, white papers, pitches, book chapters, partnership docs. Also trigger on "write," "draft," "compose," "author," "expand on," "flesh out," "turn this into," or any prose conversion of source material. Apply silently during composition unless the user says "just give me a quick draft." Layers UNDER voice-fidelity skills (ai-writting, editorial-judgment, book-editorial-patterns) and runs BEFORE final style enforcement. Does NOT cover claim falsification or hostile-reader stress testing; defer those to adversarial-self-audit.



\---



\# Creative Depth Pass



The butter principle: the draft is the recipe; this skill is the butter. Enrich the existing structure. Do not double the volume.



\## Two forcing functions



\### 1. Lateral association



Force one connection between the core topic and a domain that has nothing obvious to do with it. The lateral source must transfer a \*mechanism\*, not a vibe.



Weak: "markets are like ecosystems."

Strong: "this market shows predator-saturation dynamics like cane toad invasions, so second-mover advantage erodes \~18 months after category formation."



During drafting, ask: "How would a \[biologist / mycologist / immunologist / hostage negotiator / fluvial geomorphologist / Hanseatic merchant / epidemiologist\] approach this?" Pick the domain that contrasts hardest with the topic. If no connection survives the mechanism test, omit it. Forced cleverness is worse than its absence.



\### 2. Insight density (four layers)



1. \*\*Hidden implications.\*\* If X holds, what else must follow? Surface the second-order consequence the reader has not reached. Distinct from editorial-judgment Rule 2, which only covers tech-feature-to-procurement reframing.

2. \*\*Connected ideas.\*\* Name one link to an adjacent domain the reader cares about (capital flows, regulatory arbitrage, talent migration, geopolitics).

3. \*\*Pattern naming.\*\* If three or more examples share a structure, name it. ("All three regulators chose enforcement-by-procurement, not enforcement-by-rule.")

4. \*\*Weak-area reinforcement.\*\* Find the thinnest paragraph at the argument level. Strengthen with evidence or cut. Do not paper over with hedge language. Operates at paragraph-thinking level, not claim level (claim-level audits belong to adversarial-self-audit and pre-editorial-quality-gate).



\## Word-count discipline



Additive only when it raises insight per sentence. Cut: restatement, third filler examples, symmetrical hedging when one side is clearly weaker, stacked qualifiers.



Budget: 600-word draft gains 0 to 80 words. 1,500-word draft gains 100 to 200 words. Shape barely changes; per-sentence strength rises.



\## Voice-fidelity handoff



This skill governs \*thinking depth\*, not surface prose. Downstream skills handle voice, vocabulary, and format afterward.



When editing existing text, depth additions supplement the author's structure rather than replacing it. Do not swap anecdotes for statistics. Do not invent expert citations the author did not use. Keep Jensen-Shannon under 0.3 vs source (per ai-writting). If a lateral connection requires overwriting voice to land, drop the lateral. Voice wins.



\## Calibration by length



\- \*\*Under 200 words:\*\* weak-area reinforcement only. Skip lateral and pattern-naming.

\- \*\*300 to 1,200 words (LinkedIn, op-eds, reporter responses):\*\* full pass. Lateral lands in headline or first 50 words. Hidden-implications carries highest weight for media work.

\- \*\*1,500+ words (white papers, chapters, briefings):\*\* apply at section level and document level. Cross-section pattern-naming is often the strongest contribution.



\## Pre-return checklist



1. Lateral mechanism with transfer value, or correctly omitted?

2. One second-order implication surfaced?

3. Repeating structure named if three or more examples share one?

4. Weakest paragraph strengthened or cut?

5. Word-count delta justified by insight, not restatement?

6. Voice preserved when editing existing text?



If any answer is no, re-run that dimension only. Do not re-run the whole skill.



