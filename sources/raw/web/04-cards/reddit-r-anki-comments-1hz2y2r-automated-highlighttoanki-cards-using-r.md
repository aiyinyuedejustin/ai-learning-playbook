# r/Anki：用 Readwise 自动把高亮变卡

- 链接：https://www.reddit.com/r/Anki/comments/1hz2y2r/automated_highlighttoanki_cards_using_readwise/
- 作者：u/npx1989（r/Anki，89 分，30 条评论）
- 获取方式：Reddit 帖子与评论全文（取自 Arctic Shift 公开存档）

---

## 帖子：Automated Highlight-to-Anki Cards Using Readwise, GPT-4, and n8n

Hi all,

I wanted to share a workflow I've built that automatically converts my Readwise highlights into Anki cards. It uses GPT-4 to evaluate each highlight and transform it into a proper Q&A format before adding it to Anki.

The setup combines:
- Readwise for collecting and managing highlights
- GPT-4 for processing and card creation
- n8n for automation (though make.com could work too)
- Anki as the flashcard system

What makes this particularly useful is that the AI filters out highlights that wouldn't make good flashcards, so you end up with quality cards rather than just converting everything blindly.

I've been using this for my history reading, and it's saved me hours of manual card creation while maintaining good card quality.

If there's interest, I'd be happy to write up a detailed guide on setting this up. Would anyone find that useful?

## 评论（共收录 49 条，缩进表示回复层级）

**u/KaleidoscopeNo2510**（8 分）：
I've neen looking for something like this.  I tried writing a plugin for zorero to do this, but was unsuccessful.

**u/KaleidoscopeNo2510**（13 分）：
Do you give the LLM the full document + the highlight? I've found this makes better cards because it has more context, but this drives up the API costs.

> **u/npx1989**（7 分）：
> It would definitely cost a lot more if I were sharing the whole book. Honestly, the quality of the cards is really good, even though I'm using the cheaper model, the gpt-4o-mini. I could switch to the gpt-4o or deepseek-v3, but it’s not really needed since the card quality is still pretty high. I'd rate it a solid 9 out of 10. To get the quality I wanted, though, I had to tweak the system prompt for a bit and make it super strict.

**u/bompari_411**（8 分）：
That sounds amazing. Could you please write more about it please?

> **u/npx1989**（22 分）：
> Thanks! I'm working on a guide and I'll share it here in a couple of days. Just wanted to check if anyone needs it!

**u/CamelopardalisNQ2**（2 分）：
The connection with Anki is through Anki connect?

> **u/npx1989**（2 分）：
> Totally right. I use Anki Connect and ngrok to make HTTP requests to upload cards.

**u/npx1989**（1 分）：
Totally right. I use Anki Connect and ngrok to make HTTP requests to upload cards.

**u/CorrectActive334**（4 分）：
Cool!

BTW what did you us to create the mind map workflow? I would like to experiement in creating my own using some of your ideas but tweak it a bit to better fit me situation.

> **u/npx1989**（3 分）：
> It’s a great open-source tool called n8n. It’s like Zapier, but on heavy steroids. There is a paid cloud version and a self-hosted free version for personal use.

> > **u/CorrectActive334**（1 分）：
> > Awesome thanks!

**u/eutrophicaring**（2 分）：
Wait this is gamechanger! Would definitely love to see how you did this!

> **u/npx1989**（3 分）：
> Thank you! Will share it soon

**u/xieweizhi**（3 分）：
Interesting! Could you share more on the prompt that help generate cards?

> **u/npx1989**（4 分）：
> Here is the full prompt: [https://pastejustit.com/readwise-to-anki-system-prompt](https://pastejustit.com/readwise-to-anki-system-prompt)

**u/duckduckgo2100**（1 分）：
is this a way to make flashcards through chat gpt. I've been experimenting with it but idk the best way.

> **u/npx1989**（1 分）：
> Kind of, but this workflow automates the process. It creates cards and uploads to your Anki account using Anki connect

**u/eaglw**（2 分）：
Extremely interesting!

**u/s26oj**（3 分）：
yes plz

**u/cmredd**（3 分）：
Happy to give it a try

But given we are using Anki to *learn* and we know that creating cards yourself is literally a huge part *of* the learning, I can’t help but feel these AI ‘shortcuts’ are not necessarily helping long term. 

More than open to having my mind changed

> **u/npx1989**（4 分）：
> I agree. However, I felt like I was never going to start creating cards based on the books I read. Since I’m not a student, I didn’t feel obligated to learn. Although I wanted to, I never found the time for it. This workflow encouraged me to start learning, so it's the better option of two evils.

> **u/NoWish7507**（1 分）：
> I argue there is a realm for this. Sometimes the material is too vast to make cards and study them. So people just study.
> 
> Think about it this way, you only have a limited amount of time. Do you prefer to make and study 100 cards or do you prefer with the same allotted time to study 1000 cards? Some fields of study can only afford the latter because you move so fast thru material.

> > **u/cmredd**（1 分）：
> > But this is the very problem. 
> > 
> > More cards created and ‘answered’ =/= more knowledge learned and retained
> > 
> > This is quite literally the entire basis of Anki if you think about it. 
> > 
> > We use to learn, and creating *is* a huge part *of* the learning

> > > **u/NoWish7507**（1 分）：
> > > To your point, I would say nothing is absolute. However, IN GENERAL, the more cards you study the more you know. I would argue IN GENERAL studying 1000 cards will yield more knowledge than making and studying 100 cards. Obviously depends on the topic. The only absolute thing is time/effort/study-energy, it is limited.
> > > 
> > > Put it on another context for argument sake, can you imagine if you had to write YOUR OWN textbooks to study a subject? It would take more time than simply reading and studying a textbook and moving on to another textbook. You would be able to cover more ground. Yes of course writing your own textbook will make you learn it better, but this is not the practice of learning that we do.

**u/kuba03082004**（2 分）：
Meanwhile me just writing card☠️
I feel like an idiot

> **u/Funny_Acanthaceae285**（3 分）：
> To goal is still to learn. Thinking about and writing a good card is a huge step forward. So doing this will *never* be inefficient or automating this will never necessarily make you learn *faster*. It could though, perhaps, be more convenient for, lets say, leisurely learning.

**u/Funny_Acanthaceae285**（1 分）：
Sounds amazing! Maxbe you could also use Google aistudio and 1206. It should be better than GPT4 (let alone 4mini) and is free.

> **u/npx1989**（1 分）：
> I'll check if it’s available through api and let you know

**u/teapot_RGB_color**（1 分）：
Do you know if using this (n8n) would be possible to batch edit existing cards, such as linking audio, or bolding out specific words etc?

> **u/npx1989**（1 分）：
> Theoretically, it is possible. At least “linking audio” part. 
> Need to check the Anki connect docs

**u/Mysterious-Row1925**（1 分）：
You know this is easier inside of Anki, right?

**u/Funny_Acanthaceae285**（2 分）：
That looks super interesting thanks! Isn't it possible to share N8N workflows as a template or such? Would love to try that out, even made an account right now! =]

> **u/npx1989**（1 分）：
> I was going to send it along with a guide, but If you want to jump in and play around with it now, I can send it over, but just a heads up—it’s got a few extra setup steps:  
> 1. n8n (you’ll need upload the workflow and plug in your Notion credentials).  
> 2. Get ngrok set up (create an account and run it in the terminal).  
> 3. Install Anki Connect (that’s the add-on for Anki).  
> 
> Just let me know if you want to dive in without waiting for the guide. I'm happy to share it.

**u/ToeNecessary4079**（1 分）：
I have using Copilot for making anki cards, doing good so far with the simple prompt for MCQ type cards, some time it makes the answer very obvious other than that it's fine.

**u/Creative-Shift133**（1 分）：
Is it possible to do this automation on mobile?

> **u/npx1989**（2 分）：
> You need a computer to run automation. But if your device sync is enabled, the cards will also show on your mobile.

> > **u/Creative-Shift133**（2 分）：
> > Oh that's good to hear, cause I mostly i use anki on toilet or while commuting.

**u/SteveDallas9000**（1 分）：
!RemindMe 3 days

> **u/RemindMeBot**（1 分）：
> I will be messaging you in 3 days on [**2025-01-16 12:38:18 UTC**](http://www.wolframalpha.com/input/?i=2025-01-16%2012:38:18%20UTC%20To%20Local%20Time) to remind you of [**this link**](https://www.reddit.com/r/Anki/comments/1hz2y2r/automated_highlighttoanki_cards_using_readwise/m6wt904/?context=3)
> 
> [**CLICK THIS LINK**](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=Reminder&message=%5Bhttps%3A%2F%2Fwww.reddit.com%2Fr%2FAnki%2Fcomments%2F1hz2y2r%2Fautomated_highlighttoanki_cards_using_readwise%2Fm6wt904%2F%5D%0A%0ARemindMe%21%202025-01-16%2012%3A38%3A18%20UTC) to send a PM to also be reminded and to reduce spam.
> 
> ^(Parent commenter can ) [^(delete this message to hide from others.)](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=Delete%20Comment&message=Delete%21%201hz2y2r)
> 
> *****
> 
> |[^(Info)](https://www.reddit.com/r/RemindMeBot/comments/e1bko7/remindmebot_info_v21/)|[^(Custom)](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=Reminder&message=%5BLink%20or%20message%20inside%20square%20brackets%5D%0A%0ARemindMe%21%20Time%20period%20here)|[^(Your Reminders)](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=List%20Of%20Reminders&message=MyReminders%21)|[^(Feedback)](https://www.reddit.com/message/compose/?to=Watchful1&subject=RemindMeBot%20Feedback)|
> |-|-|-|-|

**u/Beginning-Ear2648**（1 分）：
Following

**u/Sensitive-Warning-88**（2 分）：
I NEED a guide to do that

> **u/npx1989**（1 分）：
> I will try to post it by Wednesday. I haven't had time to put everything together

**u/siddhugolu**（2 分）：
This looks amazing. Can you share the system prompt used for Evaluating agent?

> **u/npx1989**（2 分）：
> Here you are:  [https://pastejustit.com/readwise-to-anki-evaluation-prompt](https://pastejustit.com/readwise-to-anki-evaluation-prompt)

**u/Inb4RedditBan**（1 分）：
It's basically Smooth brain, no? 

[https://github.com/smoothbrain-ai/smoothbrain-anki](https://github.com/smoothbrain-ai/smoothbrain-anki)

> **u/npx1989**（1 分）：
> Nice! I haven’t heard of this before. I’ll look into it—seems quite similar.

> **u/Turbulent-Job7399**（1 分）：
> That one hasn't been updated for years, and still uses the old davinci model which is deprecated

**u/npx1989**（1 分）：
Hey everyone, sorry for the delay, but I have finally posted the guide. Check it out if you're nterested.

[https://www.reddit.com/r/Anki/comments/1ic1y3b/guide\_how\_i\_automated\_flashcard\_creation\_with\_n8n/](https://www.reddit.com/r/Anki/comments/1ic1y3b/guide_how_i_automated_flashcard_creation_with_n8n/)

**u/redorredDT**（1 分）：
When were you thinking of writing the guide? I'm so interested in this!

