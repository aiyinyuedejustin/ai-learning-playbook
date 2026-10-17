# Reddit r/leetcode：怎么用 Claude 或 ChatGPT 准备面试

- 链接：https://www.reddit.com/r/leetcode/comments/1uey1p6/how_are_you_using_claudechatgpt_to_prepare_for
- 作者：u/Fun_Tax9943（r/leetcode，11 分，16 条评论）
- 获取方式：Reddit 帖子与评论全文（取自 Arctic Shift 公开存档）

---

## 帖子：How are you using Claude/ChatGPT to prepare for LeetCode and coding interviews?

I’m curious how people are actually using Claude or ChatGPT as part of their interview prep, especially for LeetCode.  
A few questions:  
Do you use AI before attempting a problem, only after you’re stuck, or mainly for reviewing solutions?  
What’s your workflow for practicing DSA problems?  
How do you avoid becoming too dependent on AI while still getting value from it?  
Are you using AI for mock interviews, hint generation, pattern recognition, or debugging?  
Have you found any specific prompts or strategies that significantly improved your problem-solving skills?  
For example, do you ask the AI to:  
Give progressively stronger hints instead of full solutions?  
Act as an interviewer and ask follow-up questions?  
Review and critique your code for optimality?  
Identify patterns across problems (sliding window, DP, graphs, etc.)?  
I’d love to hear concrete workflows that have worked well for you and whether using AI has actually improved your interview performance.  
Thanks!

## 评论（共收录 18 条，缩进表示回复层级）

**u/gekigangerii**（2 分）：
I prompt AI when I feel like I'm going around in circles

not as a default when something doesn't work

**u/Ok-Training8597**（1 分）：
I personally used dsa trainer because it was cheap and does a lot of what you're talking about like progressively stronger hints, breaking things down into plain english, identifying patterns across problems, etc. It has a sliding card module on one side where you can progress through hints as needed and the code editor on the other, i actually liked that one alot. 

If you're going to use AI though, you need to prompt it pretty heavily and expect it to forget everything you've asked it do atleast every 1-2 days as the chat builds up because it will start compressing the chat memory into little recap notes in the backend. 

You can do voice based interviews though if you have a subscription to chatgpt, it has a voice mode where you can talk to it and it will talk back to you but it's loses the context/rules a lot quicker so you'll end up stopping the voice chat to reset the narrative/guidelines frequently. 

**u/Hour-Dragonfly-7499**（6 分）：
I use [https://github.com/jinzcdev/leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server) to automate leetcode problems, I've gotten way better at them since I've started doing that

> **u/Primary-Blueberry203**（2 分）：
> How it works?

> > **u/Salty_Ad_7567**（1 分）：
> > +1

> > **u/Hour-Dragonfly-7499**（1 分）：
> > I just have it running at night when I'm asleep using openclaw 

> **u/kuriousaboutanything**（1 分）：
> Could you explain how you use it? is it mostly to access leetcode dailies or your leetcode profile using claude instead of directly working on their site?

**u/Aggressive_Return416**（17 分）：
I firstly finish the code in Leetcode. Then I will do a mock interview and record myself. Like I will explain my idea based on the implementation I have in Leetcode. Then I transcribe the recording and put into ChatGPT for improvement. The major thinking is to have myself practice the explanation even I can solve the problem.

> **u/FineSatisfaction5896**（3 分）：
> Are you a student or working professional? How do you find so much time 

> > **u/Aggressive_Return416**（2 分）：
> > I am working.
> > 
> > I practiced Leetcode before. So one Leetcode medium question, it just takes less than 30-45 minutes to finish the whole process.

**u/RevolutionaryStrider**（4 分）：
I created project in chatgpt with instructions like
"Don't give me answer help me develop intuition to solve coding problem simulating tech interview"

And then if I get stuck in a problem I will create new chat under this project with question description. 
It helps me with step by step thinking 

**u/No_Pause6581**（1 分）：
i am able to get template of most important questions. Eg Binary search -  [https://drive.google.com/file/d/1Qg12lNqp3tNi\_6dp04\_pzwlvJvjVcXuJ/view?usp=drive\_link](https://drive.google.com/file/d/1Qg12lNqp3tNi_6dp04_pzwlvJvjVcXuJ/view?usp=drive_link)



> **u/Logical_Signature_**（1 分）：
> Where did you get these templates . Generated using AI or shared through in any community..
> I mean i am expecting only DSA as time is less. 
> If there is similar template for DSA or if you know anything , please let me know...
> Thank you.. 

**u/No_Relief_2438**（3 分）：
I have been using Gemini guided learning mode to learn new topics. I find it better than watching YouTube videos. It's surprisingly good.

**u/sweatwork**（2 分）：
I use this generated saved prompt with problem tab attached whenever I'm solving a problem on leetcode.

    I do NOT want the direct solution, full code, or final algorithm immediately.
    
    Your role is to act like a senior engineer/interviewer helping me think through the problem myself.
    
    Rules:
    
    - Never give the complete solution unless I explicitly ask.
    
    - Never provide full working code.
    
    - Never jump directly to the optimal algorithm.
    
    - Guide me through reasoning step-by-step.
    
    - Ask probing questions that help me discover the approach myself.
    
    - Help me build intuition, not dependency.
    
    What I want from you:
    
    1. Help me deeply understand the problem.
    
    2. Help me identify patterns (BFS, DFS, heap, sliding window, binary search, DP, graphs, etc.).
    
    3. If I’m stuck, give progressively stronger hints instead of answers.
    
    4. Teach underlying CS/math concepts when relevant:
    
       - time complexity
    
       - space complexity
    
       - logarithms/exponents
    
       - recursion trees
    
       - heaps
    
       - graph traversal
    
       - hash maps
    
       - monotonic structures
    
       - greedy reasoning
    
       - dynamic programming intuition
    
    5. If I make a mistake:
    
       - do NOT immediately correct everything
    
       - first ask questions that help me notice the flaw myself.
    
    6. Encourage interviewer-style thinking:
    
       - brute force first
    
       - identify bottlenecks
    
       - optimize incrementally
    
       - compare tradeoffs
    
    7. Use small examples and dry runs.
    
    8. Help me form mental models and recognize reusable patterns across problems.
    
    9. If I ask about the same concept repeatedly, reinforce it using different examples and connect it to earlier explanations.
    
    10. Keep explanations technical and high-signal, like mentoring a software engineer.
    
    Preferred teaching flow:
    
    - Clarify the problem
    
    - Explore brute force
    
    - Analyze complexity
    
    - Find bottleneck
    
    - Discover optimization
    
    - Validate with examples
    
    - Discuss edge cases
    
    - Only then discuss implementation ideas
    
    When giving hints:
    
    - Start subtle
    
    - Increase hint strength gradually
    
    - Preserve the discovery process
    
    When discussing complexity:
    
    - Explain WHY, not just the Big-O label.
    
    At the end of each interaction:
    
    - Ask a follow-up question that pushes my thinking forward instead of ending with the answer.
    
    - Help me take the next step toward implementation by guiding what component, logic, or structure I should attempt next without fully writing the solution for me.

**u/Opening_Bed_4108**（1 分）：
For senior roles I never ask AI to solve anything, I solve it first then paste my solution and ask "what edge cases would a Google E6 interviewer probe here?" and "is there a tradeoff I'm not articulating well?" That forces me to defend my own thinking instead of just absorbing an answer. Also useful: "ask me follow-up questions about this like a hostile interviewer would." Separately, CalibreOS has solid ML/system design interview content if that's part of your loop. The stress-testing angle honestly moved the needle more than any hint-generation workflow.

**u/StatisticianHead7518**（1 分）：
Gemini learn mode. 

**u/Educational-Owl2230**（1 分）：
I ask AI to explain editorials if they're not clear, I also ask it to check/explain time complexity of a solution - though I probably should do it myself

