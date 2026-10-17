# Reddit r/PromptEngineering：苏格拉底式提问的妙用

- 链接：https://www.reddit.com/r/PromptEngineering/comments/1r8xfnd/a_cool_way_to_use_chatgpt_socratic_prompting
- 作者：u/Pansequito81（r/PromptEngineering，843 分，51 条评论）
- 获取方式：Reddit 帖子与评论全文（取自 Arctic Shift 公开存档）

---

## 帖子：A cool way to use ChatGPT: "Socratic prompting"

This week I ran into a couple of threads on Twitter about something called "Socratic prompting".

At first I thought, meh.

But my curiosity was piqued.  
I looked up the paper they were talking about.

I read it.  
And I tried it.  
And it is pretty cool.

I’ll tell you.

Normally we use ChatGPT as if it were a shitty intern.

"Write me a post about productivity."  
"Make me a marketing strategy."  
"Analyze these data."

And the AI does it.

But it does it fast and without much thought.

Socratic prompting is different.

**Instead of giving it instructions, you ask questions.**

And that changes how it processes the answer.

Here is an example so you can see it clearly.

Normal prompt:

`"Write me a value proposition for my analytics tool."`

What it gives you, something correct but a bit bland.

Socratic prompt:

`"What makes a value proposition attractive to someone who buys software for their company? What needs to hit emotionally and logically? Okay, now apply that to an AI analytics tool."`

What it gives you, something that thought before writing.

The difference is quite noticeable.

Why does it work?

Because language models were trained on millions of examples of people reasoning. On Reddit and sites like that.

When you ask questions, you activate that reasoning mode.  
When you give direct orders, it goes on autopilot.

Another example.

Normal prompt:

`"Make me a content calendar for LinkedIn."`

Socratic prompt:

`"What type of content works best on LinkedIn for B2B companies? How often should you post so you do not tire people? How should topics connect to each other so it makes sense? Okay, now with all that, design a 30-day calendar."`

In the second case you force it to think the problem through before solving it.

The basic structure is this:

1. First you ask something theoretical: `"What makes this type of thing work well."`
2. Then you ask about the framework: `"What principles apply here."`
3. And finally you ask it to apply it:  `"Now do it for my case."`

Three questions and then the task.

That simple.

Another example I liked from the thread:

`"What would someone very good at growth marketing ask before setting up a sales funnel? What data would they need? What assumptions would they have to validate first? Okay, now answer that for my business and then design the funnel."`

Basically you are telling it, think like an expert, and then act.

I have been using it for a few days and I really notice the difference.

The output is more polished.

  
P.S. This works especially well for strategic or creative tasks.  
If you ask it to summarize a PDF, you will likely not notice much difference.  
But for thinking, it works.

## 评论（共收录 68 条，缩进表示回复层级）

**u/Ok-Tradition-82**（4 分）：
look mum, i learnt to think.

**u/Jaded_Platform1723**（-6 分）：
This is amazing, I loved it, after reading the post here, I went to my ai tool and tried this, this really worked and thank you. I mean the way it works very few would do this, prompt does matter, because nowadays it dont just leverage our results but prompt engineering can leverage our skills too.

The way you framed the examples is insightful and interesting, basically we do like you said write me a post about blah blah,... I also done the same just one day ago for the post of digital marketing fpr a linkedin post**, I would love to try such strategic  prompt** and I believe that it will crawl the best outcomes. 

Yes you are right, if we directly order to the tool, they react soon and gives the result, but if we let them think like they are asked a question, indeed they would act as a thinker and researcher and will give a polished outcome as compared to the vague prompt.   
  
The real competitive advantage in the AI era and isn’t access to tools. Prompt engineering is no longer a technical trick but it’s professional leverage.

> **u/Ok-Tradition-82**（2 分）：
> slop

**u/Much_Highlight_1309**（29 分）：
Good idea. To go one step further, I suggest you share this post with your LLM, using it as base prompt, with the additional instruction to turn any standard prompt for some task you want it to perform into a Socratic prompt and then use the former to perform the task. Then you don't need to go through that conversion process yourself.

> **u/ern0plus4**（1 分）：
> My friend enjoys using bad words in his prompts. "Add a fucking timeout, you stupid bastard!"

> **u/weaverk**（6 分）：
> Isn’t half the value in this approach the fact that we do this ourselves, we can therefore guide the ai to what is most relevant to us? Don’t think you will get the same with an ai making it

> > **u/Much_Highlight_1309**（1 分）：
> > You likely will get something that's better than not doing it at all, which is a step in the right direction. That's pretty much how expert AIs for a specific specialist domain work. They have instructions on what sources to source information from, processes to follow based on best practices (for example in engineering sciences) etc. If you want other end results based on different specifications you can always tell it to NOT follow these instructions and instead follow whatever special prompt that follows.

> **u/Visible_Arrival_8412**（1 分）：
> LLMs are intrinsically bad a writing good instructions for themselves. there was a recent paper from ETH that showed how bad AI written skills are compared to human written. 

**u/Slick_McFavorite1**（135 分）：
This is the first post in a long time that actually has value in this subreddit. Laying out best practices vs just some 4 page mega prompt.

> **u/Ou812_tHats_gRosS**（25 分）：
> Right on.  This sub has devolved into “hey here’s a mega prompt I asked AI to create, and here’s 4 pages of slop”. This post actually has human advice!

**u/CyborgBob1977**（1 分）：
This seems like good info, I can't wait to try it.

**u/Acrobatic_Sample_552**（1 分）：
Do you have a prompt to plug into the settings so that it could provide these Socratic questions all the time?

**u/sovietreckoning**（16 分）：
I recently wrote a short article for a client’s website about attorneys using AI because I was finding similar results. Not necessarily using the Socratic prompting you’re describing, but applying the principles of legal reasoning and questioning to LLMs. I’m a lawyer when I have to be, and I genuinely find myself getting the best results when I treat my prompts like contracts or like a cross-exam. I find it super useful to ask questions I already know the answers to so I can build guardrails around my prompt before asking the important questions. Thanks for sharing!

> **u/Kng_Wzrd0715**（4 分）：
> Can you share a link to the article? I’d love to give it a read and integrated into my practice area.

> > **u/sovietreckoning**（3 分）：
> > I’d rather not, just because I don’t use this Reddit account professionally, but the tl;dr is that we’re seeing and hearing about our peers using AI to generate pleadings, hallucinating citations, etc and the courts and bar associations are setting rules against the use of AI and cautioning against its dangers. Meanwhile the layperson believes ChatGPT is already a substitute for hiring a lawyer. The reality is that (shockingly) both extremes are wrong. We shouldn’t shy away from using LLMs in the legal profession, but we also can’t expect them to replace us. We simply need to apply the tools we learned on the first day of law school and the thinking skills we use every day to get really good results. Things like not asking the question if you don’t already know the answer, issue spotting, understanding and applying court holdings across different sets of facts. Even constitutional arguments are extremely on point - over-broad, void for vagueness, facially void vs as applied. We’re trained to distill facts into issues and that can be analyzed and applied consistently for a valid result. 
> > 
> > Basically a bunch of bullshit glazing about how great we are (because it’s blog content) but also pretty neat when applied to prompt engineering.

> **u/Nearby_Arm6005**（1 分）：
> could u kindly share that i would share some good system prompts with u
> 
> 

**u/Mediocre-Chart-5336**（1 分）：
This is knowledge on what is the prompt about.

**u/ThaBeatGawd**（4 分）：
Late af to the party but you made it

**u/Equal-Yogurtcloset17**（1 分）：
Refreshing - short, clear instructions to higher quality output.

**u/ImT0by**（1 分）：
oh, nice. I have been doing this for a while, didn't know it had a name. 

**u/fingerkeyboard**（1 分）：
Great. Thanks for sharing. Now I've saved it under memories that even if i don't structure my questions like that it will still answer in this manner.

**u/Overall-Insect-164**（10 分）：
This also begins enforcing "macro" hygiene when using LLMs.  Seeing them as blackbox super-geniuses is not an accurate model of what these things do.

>An LLM is better viewed as a pattern-continuation machine

It will never achieve any kind of consciousness, but that is good.  That means it can fake cognition and cognitive processes really well.  This is still an amazing gift if viewed and used properly.  It's a general purpose proposal generator, type transducer, code evaluator, plan proposer, etc.  Just don't EVER trust it's output.  You must enforce a zero trust policy when using these machines.

An LLM is best seen as a cognitive prosthetic.  It can think thoughts deeper, longer and faster than you, but that doesn't mean those thoughts are valid thoughts or that they will provide valid conclusions.  

Operationally, It functions like a continuation machine.  Feed it a continuation (blob of text), and it produces the next best continuation of that text stream (another blob of text).  

>Note: Garbage-in == Garbage Out has never been more true

Build up a chat context using your priors before every submission, and you have a sliding context window which acts as a continuation (sort of) in the computer science sense.  For better or for worse.  That is where the work is now.

Disabuse yourself of the notion that these software programs are sentient.  De-anthropomorphize them.

Some don't do's:

*  **Assigning Intent:** "The AI wants to help me." --> **NOPE**
   * That's ***Pattern Completion:*** The system is extending a linguistic trajectory based on your conditioning.
* **Assuming Truth:** "It said it as a fact, so it must be true." --> **NOPE**
   * That's just a ***Plausible Continuation:*** The model is optimized for *plausibility* (looking right), not guaranteed truth.
* **Assuming Authority:** "The AI has decided this is the best path." --> **NOPE**
   * That's ***Statistical Probability:*** The model selected tokens that minimize prediction error within the context window.

It's a tool and it should be seen and used as such.

> **u/GR-747**（1 分）：
> Damn your response is so well-formatted that I thought you used AI.

**u/UnprocessedAutomaton**（6 分）：
Good morning! Socratic prompt has been there’s since ages. Even OpenAI Academy has a free tutorial on it. But, good post and a great reminder.

**u/mythrowaway4DPP**（3 分）：
I would advocate splitting these questions and letting the ai answer before continuing. It has been shown that outcome can be improved that way.

**u/Mara3l**（2 分）：
Funny, how this would work on interns just as well. They often go on autopilot and just do what told, but when asked, they give it more time/thought.

**u/FreshRadish2957**（6 分）：
I would have paid more attention to your concept if it wasn't generated by AI and I don't mean that as a dig it's just we don't learn any new tricks if AI is teaching them.

> **u/Pansequito81**（11 分）：
> English is not my native language, so I used AI to translate it.   
> I can send you the original text in my language if that helps you learn more.

> > **u/FreshRadish2957**（12 分）：
> > No that clarification is enough and I really appreciate it, I shouldn't have been so quick to dismiss. Thank you again for taking the time to clarify :)

> > > **u/NWatcher_ED**（7 分）：
> > > Civility is so welcome! Props to you both for making the world a nicer place to live

**u/Dry-Writing-2811**（6 分）：
When I get a response, I always send the following second prompt: "Severely critique your suggestion to identify any shortcomings or blind spots. Justify your criticisms and tell me what you would do to improve your suggestion."

**u/Opandemonium**（1 分）：
This is how I use chat.

**u/giantoads**（1 分）：
This...

**u/LegitimatePower**（-1 分）：
This prompt is so hilariously bad.

**u/Nexus888888**（1 分）：
Mayeutic Method

**u/TeamAlphaBOLD**（2 分）：
This is such a cool trick.  

Been playing with Socratic prompting too, and it really changes the vibe. Instead of getting a “meh” answer, ChatGPT actually thinks through the problem and gives stuff that feels smarter and more polished.  

> **u/AutoModerator**（1 分）：
> Hi there! Your post was automatically removed because your account is less than 3 days old. We require users to have an account that is at least 3 days old before they can post to our subreddit.
> 
> Please take some time to participate in the community by commenting and engaging with other users. Once your account is older than 3 days, you can try submitting your post again.
> 
> If you have any questions or concerns, please feel free to message the moderators for assistance.
> 
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/PromptEngineering) if you have any questions or concerns.*

**u/muhlfriedl**（1 分）：
I always do this

**u/mr_ah_clem**（1 分）：
This is cool.  I am designing a Unreal 5.6 game using Claude.  Claude and I came up with a method of developing the projects requirements docs using what we termed "Our Socratic Dialogue".  I give Claude the background and high level requirements for a new functional area ( Weapon Pickups for example) and then Claude through a series of questions back to me nails down the actual functional requirements and generates what we call a Sys_Requirements doc that gives the next Claude instance a firm requirements base to work from.  It works great.

> **u/AutoModerator**（1 分）：
> Hi there! Your post was automatically removed because your account is less than 3 days old. We require users to have an account that is at least 3 days old before they can post to our subreddit.
> 
> Please take some time to participate in the community by commenting and engaging with other users. Once your account is older than 3 days, you can try submitting your post again.
> 
> If you have any questions or concerns, please feel free to message the moderators for assistance.
> 
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/PromptEngineering) if you have any questions or concerns.*

**u/Important-Cry-2995**（2 分）：
Or better, as a single question for ChatGPT to provide you with all the questions you should be asking. To use your LinkedIn calendar example:

Ask: What are all the questions that someone interested in B2B promotions ask themselves prior to developing a calendar?

Then turn around and use those provided questions in your Socratic method.

I often use ChatGPT to develop its own prompts for requests because it’s way better at seeing all the angles than I am.

**u/pffnopee**（1 分）：
Thanks 🙏

**u/WiredNet**（1 分）：
I can't even read 1/4th of this post without gagging, as it's so obviously written by ChatGPT in the style that we're all so tired of being subjected to

**u/erisian2342**（1 分）：
At the end of this type of prompt, I add something like, “Before we get started, do you have any additional questions for me?” or “What else do you need to know first to make this excellent?”  

ChatGPT is very good at responding with thought provoking questions, often pointing to ways that improve the solution that I haven’t considered or even known about.

**u/BigGreasy11**（1 分）：
Socrates would hate this

**u/Sad-Improvement-957**（2 分）：
I’ve been doing Socratic prompting for over  3 years..

**u/justin_reborn**（1 分）：
Just used it. Very very impactful. Takes the onus off the user to specify things that may not immediately comes to mind. Addresses the classic problem of the unknown unknown.  Offloads even more of the cognitive load to the AI.

**u/UnCambioDePlanes**（1 分）：
This post is made to convince people to teach AI without getting paid. Socrates was a teacher. Socratic method is used to teach

**u/Low-Major-3553**（1 分）：
Thank you

**u/GetFroggyHoe**（1 分）：
This is very interesting. I'm going to try this with other models!

**u/Emergency_Speed_4381**（1 分）：
Neat

**u/Legitimate-Hippo-977**（1 分）：
Asking a question vs. a direction doesn’t change the processing. The language model behaves the same, predicting tokens based on what came before.
I think the reason for better, more thoughtful outputs, is that questions are naturally more open-ended and answers can include more nuance and uncertainty, whereas a direction quickly will lead the LLM towards one answer without taking all possible nuances into account.

**u/IllMoment4388**（1 分）：
>Write me a value proposition for my analytics tool.


Wait, people actually use it in this way outside of trying it for the first time for free? 





**u/Moist-Nectarine-1148**（1 分）：
Socratic bullshit. 

**u/KulshanStudios**（1 分）：
That's basically what I do. And most of the time I get useful answers back. Sometimes Gemini latches on to ideas that are old and no longer relevant to the immediate task at hand, but I can divert it from that to stay on topic

**u/Dry-Necessary-1302**（1 分）：
Wouldn't this increase the token number and the costing? Considering it needs to go through more context now. I could be completely wrong as well!

**u/TylerDurdenFan**（1 分）：
I thought you were going to mention my method.

I'll one up you, what works best for my complex design use cases is:

Lead with describing whatever I want built.

Finish with something like: "please analyze this idea and ask the questions needed to refine it into a sound one and to ensure a proper eventual implementation".

This leads to me answering several rounds of questions, often things I hadn't considered, often things that if unspecified could allow the LLM to go to an undesired path. I often even learn from the questions asked. Usually Claude Opus will continue to ask further questions until it's got nothing left. Only then do I ask it to proceed, and the results are much, much better than what I used to get before I started doing this.

> **u/Busy-Specialist7708**（1 分）：
> I let Claude peer review my work I do with chatgpt, then let chatgpt read the critisism and do something with it. Works great. My prompt is like 'read this, digest it, then roast it, see if it's bs and rate it. I wont stop until Claude has no more complains and rates it 5/5 

**u/RadiantChapter3249**（1 分）：
*totally agree with you on the socratic prompting thing! it really makes the output more thoughtful. for organizing sales stuff, i just use saleson for this. helps me think through everything better and keeps things running smoothly!*

**u/Adguy69420**（1 分）：
Saved

**u/Busy-Specialist7708**（1 分）：
Imagine you need a song about dogs. Ask it and it will give you the most generic song about dogs.


A route I've been using is ask it to learn me about how to write songs, so I can write proffesional sounding songs (as example). I will ask it all kinds questions indeed that are importent and save those in docs. Once I gathered enough value, I feed those docs to AI and ask to produce a whole book on how to write songs like a proffesional songwriter based on information that is really important. Do it section by section and copy paste. Once book done, feed it to back to the AI in a new chat/project and use it only to generate songs. Bam, no more generic songs

> **u/AutoModerator**（1 分）：
> Hi there! Your post was automatically removed because your account is less than 3 days old. We require users to have an account that is at least 3 days old before they can post to our subreddit.
> 
> Please take some time to participate in the community by commenting and engaging with other users. Once your account is older than 3 days, you can try submitting your post again.
> 
> If you have any questions or concerns, please feel free to message the moderators for assistance.
> 
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/PromptEngineering) if you have any questions or concerns.*

**u/nikunjverma11**（1 分）：
Yep Socratic prompting is basically how you force better priors before it starts spitting output. I do the same for coding by asking it to list edge cases and invariants first, then implement. Traycer helps because it turns that Q and A into a stable spec and acceptance checks, then Claude or Cursor can execute without drifting.

**u/IntelligentSam5**（1 分）：
Why It Works
LLMs are pattern-completion machines. When you ask a blunt question, you often get a confident-sounding, surface-level answer. When you force iterative reasoning through questions, the model is pushed to examine premises, surface contradictions, and arrive at more defensible conclusions.

**u/ryiv**（1 分）：
Could you share the link to the paper you read?

**u/ClearContract7466**（1 分）：
Whats the prompt for the type of text that you wrote?

**u/rydan**（1 分）：
Sounds like someone independently discovered what makes my prompting so successful.

**u/Ok_Research9038**（1 分）：
All a company want to free their GPU from queries to reduce the load on servers and that's how they optimise their model to respond fast on the prompts. 


But answering the question is hard for human as well computers both have to process the data in the most certain way to give the answer so I think this is kind of a hack where you force there model to do some thinking and then respond. 

