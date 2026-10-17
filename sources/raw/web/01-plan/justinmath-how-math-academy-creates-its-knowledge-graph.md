# How Math Academy creates its knowledge graph

- 链接：https://justinmath.com/how-math-academy-creates-its-knowledge-graph/
- 作者：Justin Skycak
- 获取方式：网页正文（trafilatura 提取）

---

# How Math Academy Creates its Knowledge Graph

*Want to get notified about new posts? Join the [mailing list](https://justinmath.com/mailing-list) and follow on [X/Twitter](https://x.com/justinskycak).*

Been getting the following question a lot:

*“How do you create your knowledge graph? How do you map out the topics at the appropriate level of granularity and set the connectivity (prerequisite & encompassing relationships)?”*

The answer is actually pretty simple but it tends to frustrate the kinds of people who are always searching for some “secret trick” to avoid work that feels difficult and tedious.

**The answer: We handcraft it.**

Let me be clear: we do use tools to ease the load where possible, like a carpenter uses a hammer, a drill, a band saw.

But the secret sauce is really just doing a shit-ton of work to accumulate domain expertise in math and teaching and then doing a shit-ton more work to encode that domain expertise into our knowledge graph structure.

Whenever we plan out a course we take a look at numerous other textbooks and online resources, but ultimately it just comes down to our own best judgement based on our own teaching/tutoring experience and knowledge of the subject matter.

This might feel challenging and tedious at the beginning, but in my/our experience it comes easier as you gain experience with it.

You just kind of get a “feeling” for what the right chunk size is and what level of detail needs to be addressed within a single chunk.

We’ve also spent years refining the chunks, sometimes realizing that a chunk needs to be split, and after enough of that we’ve gotten to the point where we can pull it off really well on the first try.

How about the connectivity? Each of our \~2500 topics has 3-4 knowledge points, and each knowledge point is linked to one or more (typically several) prerequisites. Each prerequisite has an encompassing weight that says what fraction of the prerequisite topic is encompassed, on average, by solving a problem in the post-requisite topic – in other words, how much “credit” should a simpler topic get for doing an advanced topic where the simpler topic is a component skill.

Yes, that’s a lot of connectivity. It was and still is quite a bit of work, but not a prohibitive amount of work. “Right at the edge of human scale” as Jason likes to say.

By the way, the “edge of human scale” does not mean “the edge of what you can do in a day” or “the edge of when you get tired/bored.”

When we were first encoding encompassings into the knowledge graph (after already building up a hefty content base) I spent about 8 hours per day setting encompassings, for a month. No joke, I basically did domain-expert data entry full time for a month:

```
1500 topics at the time
x 5 prereq relationships per topic
x 2 minutes to estimate the encompassing value for each of those relationships
= 15000 minutes
= 250 hours
~ 8hr/day for 30 days
```
This was pre-ChatGPT, so I didn’t have a single tool to ease the load. Like a carpenter without a drill.

And yeah, it suuuuuucked! 🤮

But guess what? At the end of that month the task selection model started working really, really well because it had such accurate and comprehensive data to go off of. It was not a fun month but it was 100% worth it.

Like “picking gold off a mountain” (a Jason phrase) where there’s a ton of gold scattered around, and it’s tedious to load it up into the wagon and come up and down the mountain, but it’s insanely valuable and you’d be an idiot not to just go collect it even if it’s not super fun.

In other words… just because something’s tedious doesn’t mean it’s low ROI. Sometimes the highest-ROI things are extremely tedious and you just have to suck it up and do it because it’s a sure path to get you to where you need to be in a reasonable time frame.

Okay okay, so the topics and connectivity are handcrafted… what about the questions and solutions?

Yeah, those too. Handcrafted. All of our content, metadata, and exercises are created in-house, carefully crafted by a team of math experts.

There was a time in my life when I was attracted to the idea of creating general-purpose solutions to a wide class of problems, but I’ve come to realize that the real edge – and, at least for me, the real satisfaction – typically comes from

1. using your human brain / accumulated experience to grapple with the microstructure of a seemingly intractable problem,
2. finding an exploit that you can pry open just wide enough to shove yourself through with some elbow grease, and
3. doing that over and over again on each successive problem, continually noticing/capturing efficiency gains, and periodically looking up to see that despite how intractable it seemed at the outset, you're making serious progress in the direction that you're trying to go.

Like Matt Damon in the movie The Martian: [“You solve one problem and you solve the next one and then the next. And if you solve enough problems, you get to come home.”](https://youtu.be/0EhbvQSx6Dk)

**Further Reading:** [Knowledge Graph Engineering: Mental Models & War Stories - Math Academy Podcast #4, Part 2](https://justinmath.com/math-academy-podcast-4-part-2)


*Want to get notified about new posts? Join the [mailing list](https://justinmath.com/mailing-list) and follow on [X/Twitter](https://x.com/justinskycak).*
