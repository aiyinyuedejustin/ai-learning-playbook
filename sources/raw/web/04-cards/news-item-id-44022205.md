# HN：用 MCP 把卡写进 Anki

- 链接：https://news.ycombinator.com/item?id=44022205
- 作者：TechDebtDevin
- 获取方式：Hacker News 帖子与评论全文

---

## （TechDebtDevin，0 分）

（讨论共收录 30 条评论，缩进表示回复层级）

Pro Tip , if you're using LLMs to learn, create an MCP tool for them to insert Anki cards on topics you're discussing in a csv on google drive, then sync that with you anki decks on your phone.

This was a game changer for me and working with LLMS, while I still think they make you dumb, and we essentially use them to offload critical thinking (almost only find myself using them when tired lazy, and just cant), if you must use them use them as a study tool.

**maxwellg**：
ChatGPT 4o's voice mode has been mindblowing for me for learning basic Mandarin. I'm sure I will hit the limits of the model sooner or later, but it has been so much fun bouncing around my apartment and asking what various objects are called / if words are related to other words. It is phenomenal for putting together short little sentences and getting immediate validation on grammar too.

No MCP on ChatGPT yet, but I can ask chat to generate an output of what we reviewed in a structured format.

**MostlyStable**：
I created a python script that checks my anki deck for the cards that I'm scheduled to review the next day and asks an LLM to generate new sentences for the cards, so that every time I see them, I see them in a new context.

I did this because I realized I was hitting an issue where I theoretically "knew" a word (would get it always correct on the card), but wouldn't always recognize it in a novel context.

I'm hoping that having the context be variable when I'm learning it will help fix this issue.

> **AlchemistCamp**：
> > *”I realized I was hitting an issue where I theoretically "knew" a word (would get it always correct on the card), but wouldn't always recognize it in a novel context.”*
> 
> Some of the problem is due to the specificity of the training effect. I.e., if you mostly practice something through flash cards then you’re going to be training your ability to work with that on flash cards.
> 
> With language, there’s an additional challenge—many if not most words have different meanings in different contexts.

> > **MostlyStable**：
> > Yeah, I'm trying to spend a lot more of my language learning time just reading/listening to content in my target language, but it's actually pretty difficult to find enough content that is in the right difficulty band where it has some words/grammar etc. that I am still learning but not so much that I just can't understand it at all.

> > > **mrbombastic**：
> > > Check out if there are comprehensible input sites for your target language if you haven’t already, for example fo spanish there is: https://www.dreamingspanish.com/ which puts out videos labeled with various difficulties of speaking and listening

> > > > **TechDebtDevin**：
> > > > How well does this work?

> > > > > **mrbombastic**：
> > > > > Pretty well in my experience if you are trying to build listening comprehension and pronunciation. But it is just one tool in tool belt would recommend just as augmenting other language learning tools.

> > > > > **AlchemistCamp**：
> > > > > Very well, but it's very slow compared to what you can do if you mix it up with some higher effort activities.

> > > **sasjaws**：
> > > I'm building a reader app that tries to solve this exact problem by providing a range of gradually simplified versions of each article to match your proficiency. So you can stay in the sweet spot, or work your way up version by version.
> > > 
> > > If your target language happens to be Chinese then you can give it a try at https://reader.longyan.io/landing
> > > 
> > > No login required, love your feedback.

> > > > **AlchemistCamp**：
> > > > Sure. This kind of project seems to be pretty common. I'd strongly suggest using traditional characters as a base because it's very easy to map multiple characters into simplified forms but much harder to disambiguate simplified forms into the traditional versions.
> > > > 
> > > > Related comment on another app: https://news.ycombinator.com/item?id=43769831

> > > > > **sasjaws**：
> > > > > Thanks for having a look, I actually started out from traditional characters, but once I realized >90% of the students only do simplified I switched.
> > > > > 
> > > > > I also tend to believe to just convert between them is not the best approach. Better to find different content for both. If student wants to learn traditional script, they usualy want content from Taiwan and not from China, and the other way round.

> > > > > > **AlchemistCamp**：
> > > > > > Almost anybody serious about learning Chinese is going to want to read *some* things written before the 1960s and for those things, people are reading the exact same books, essays, poems, speeches, etc. The simplified versions of all of those works are literally converted from the traditional versions. Ditto for all kinds of popular content that originated in HK, TW and overseas Chinese communities.
> > > > > > 
> > > > > > There is no long-term gain from storing "hair" and "emit" under the same entry in your database. Storing 髮 and 發 separately, along with 发 as the simplification of both is a small effort now that will constrain you a lot less in the future. I've literally seen this pitfall happen with about 40 different Chinese learning apps over the last 15 years. Only a few (like Du Chinese and Pleco) got it right early on.

> > > **AlchemistCamp**：
> > > That's a great idea. I was an early Anki contributor and ended up wasting a lot of time with SRS. Basically every language blogger I knew in 2008 was obsessed with it.
> > > 
> > > If I were to go back and learn Japanese again, (which I may do since I haven't spoken it in 20 years), I'd use Anki for the following:
> > > 
> > > - drilling the sounds, single syllables, 2-3 syllables, and identifying pitch accents in sentences
> > > 
> > > - relearning hiragana and katakana
> > > 
> > > After that initial phase, I'd probably make the core of my practice listening to podcasts for foreign learners while reading the transcripts at home and then re-listening to those same podcasts later while outside for practice. It's way easier and more helpful to recall words in a context you already understand.
> > > 
> > > I'd also use Anki for learning kanji if I hadn't spent years reading traditional Chinese. Since I have that background and Japanese character simplifications were so modest, I think I'd just read some audio books while listening to the audio and see if I could figure out all the kanji from context. TV series are also great once you can access them because they tend to use similar vocabulary and revisit similar throughout a season arc.

> > **echan00**：
> > Shameless plug of my language app, dangerous.
> > 
> > Our language app is largely based on using LLMs and spaced-repetition. We explain the context behind every word and phrase, provide additional usage examples and cultural notes, and also use speech recognition to test recall and pronunciation.
> > 
> > We're invite-only at the moment, but happy to pass along invite codes to anybody who may find it useful.
> > 
> > https://apps.apple.com/us/app/dangerous-language-skills/id6741348848

> > > **fivestones**：
> > > Sounds very interesting. I’d love an invite. I’d love to be able to navigate conversations better next time I’m in China.
> > > 
> > > I’m also working on learning Nepali which is hard as far as language apps go because none of the apps take on smaller languages like this. I’m hoping this will change with LLMs in the mix. My experience (and that of my Nepali friends) is that ChatGPT’s written and spoken Nepali language skill is too-notch.

> > > > **echan00**：
> > > > for sure, email me erik at getdangerous.app

> > > **j0r0b0**：
> > > Very curious to try this app too, if you dont mind sending an invite code.

> > > > **echan00**：
> > > > will email you via your profile

> > > **AJayWalker**：
> > > Also interested if you have an invite!

> > > > **echan00**：
> > > > will email you via your profile

> > > **xenostar**：
> > > I’m also very interested in an invite, this sounds like a very novel concept!

> > > > **echan00**：
> > > > for sure, email me erik at getdangerous.app

> **Llamamoe**：
> That sounds like a really useful project!! Have you considered publishing it?

> > **MostlyStable**：
> > I don't think what I wrote would be very generally useful, other than the basic idea of it. I wrote it with some pretty narrow assumptions about card layout etc that work for my exact deck, and it's not designed to be flexible. It wouldn't be hard to adjust it I don't think, but also it's such a simple script, that once you have gotten to the point of changing it, you aren't much beyond writing it from scratch either.

> **bspammer**：
> That’s a really clever use for LLMs, I have the exact same problem with my Anki deck. Do you store all the historical sentences for each card or is it just a destructive overwrite each time?

> **bryanhogan**：
> This sounds useful. Maybe someone could create an Anki plugin that does this.
> 
> Or is there something similar already available?

**udit99**：
> f you're using LLMs to learn, create an MCP tool for them to insert Anki cards on topics you're discussing in a csv on google drive, then sync that with you anki decks on your phone.

Speaking for myself, I’d love to see a blogpost detailing how this is done. At the very least, I’d love to know:
How are you syncing csvs to anki cards and how does the MCP interaction look like for an LLMs response to the CSV creation

> **collyw**：
> Ask chatgpt how to do it

> **TechDebtDevin**：
> If I get time this week, I'll drop a README here that shows how to do it. Not too hard tho, read up how to build mcp with https://github.com/mark3labs/mcp-go
> 
> AnkiDroid has settings for linking a csv from google drive. Then just look up how to sync a local file/directory with Drive. Its just a matter of making sure the LLM knows the MCP Anki tool is available in every prompt (well I have a learning/Q&A prompt that uses this), then In the system prompt I tell it to make Anki cards whenever it seem like I'm having trouble with a concept, like asking a question twice, and to make sure the card doesn't exist already.

> > **udit99**：
> > Thank you!

