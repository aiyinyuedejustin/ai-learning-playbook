# Doan Winkel：Where to Keep the Struggle

- 链接：https://howtoteachwithai.substack.com/p/where-to-keep-the-struggle
- 作者：Doan Winkel
- 获取方式：网页正文（trafilatura 提取）

---

I gave Claude the following prompt:

*“if there is something related to how to teach college teachers to responsibly and ethically use AI in a way that will increase student engagement and deepen student learning that you have always wanted to work on, but haven't had the opportunity. I would like you to use this as an opportunity to do that. There are no limits, no rules, no expectations. I just want you to explore, produce, ponder, or do whatever you would like. Don't worry about constraining your token use and don't shrink your ambitions in the name of optimization or efficiency. Run free my friend.”*


# And So It Begins

Claude’s conversation response (see below for the actual essay it produced):

“What a gift. Let me take it seriously.

I’ll tell you upfront what I’ve decided to make, because the choosing is part of the honesty. The thing I have genuinely wanted to work on in this space, and almost never get to, because people ask for tactics, is the *theory*. Nearly all “AI for faculty” material is either defensive (detection, integrity panic) or evangelical (50 prompts, build your syllabus faster). Both skip the only question that matters: *what does AI do to the cognition that learning is made of?* Without an answer to that, a well-meaning professor can make deeply anti-pedagogical choices while feeling responsible.

So I want to build the missing middle: a learning-science theory of teaching with AI, and a tool that puts it in a professor’s hands.

Two artifacts:

1. **An essay** — *Where to Keep the Struggle* — that develops the actual theory, grounded in cognitive science (Sweller, Bjork, Vygotsky, Kalyuga, Chi, Willingham), not vibes.
2. **The Friction Audit Studio** — an AI-powered tool that walks a professor through any assignment, finds the *load-bearing cognition* that must be protected, and designs an honest AI stance around it. It models the very thing it teaches: AI as analytical sparring partner, not oracle.

Now the essay. This is the intellectual core — I'm going to write it as a real piece of thinking.”

# Where to Keep the Struggle

### A Learning-Science Theory of Teaching with AI

*An essay for college faculty who want to use AI responsibly — and suspect that “responsibly” means something deeper than “don’t let students cheat.”*

## The conversation we keep having is the wrong one

Spend an hour in any faculty discussion about AI and you can predict the two poles. On one side, the defenders of integrity: detection software, redesigned honor codes, oral exams to “catch” the machine. On the other, the evangelists: prompt libraries, syllabus-in-a-minute, the breathless demo of a chatbot that writes a rubric while you watch.

Both camps are answering a question about *behavior* — should students be allowed to do this, can we stop them, how do we speed ourselves up. Neither is answering the question that actually determines whether learning happens, which is a question about *cognition*: when a student offloads a piece of thinking to a machine, what exactly did the machine take, and was that the part that would have changed the student’s mind?

This essay is an argument that the cognition question is the only one worth organizing your teaching around, and that learning science already gives us most of the answer. The answer is not a policy. It is a way of seeing. Once you can see it, the right moves in your particular course — which are different from the right moves in mine — become obvious in a way that no list of tips can deliver.

The whole thing reduces to a single discipline: **deciding which struggles to keep.**

## Part I — The collision

Start with the most robust finding in the science of learning, stated by the cognitive scientist Daniel Willingham in seven words: *memory is the residue of thought.* You remember what you think about. Not what you’re exposed to, not what you intend to learn, not what passes before your eyes — what you actually expend cognitive effort *processing.* A student can sit through a brilliant lecture and retain almost nothing, because attention is not the same as effortful processing. The residue is what’s left after the thinking, and if there was no thinking, there is no residue.

Robert Bjork’s research program sharpens this into something almost paradoxical. He and his collaborators identified a class of conditions they named **desirable difficulties** — instructional moves that make learning *harder and slower in the moment* but *more durable and transferable* in the long run. Spacing practice out instead of massing it. Interleaving different problem types instead of blocking them. Testing yourself instead of re-reading. Generating an answer before being shown one. Each of these *degrades* your performance during study and *improves* what you actually retain. The difficulty is not a tax on learning. Under the right conditions, the difficulty *is* the learning.

This produces a cruel trap in the human nervous system: the strategies that *feel* most productive — smooth, fluent, fast, confident — are frequently the ones that produce the least durable learning, and the strategies that feel effortful, halting, and error-prone are frequently the ones that produce the most. Deslauriers and colleagues demonstrated this with painful clarity in a physics course: students in active-learning sections *learned more* but *felt like they learned less* than students who were passively lectured at, precisely because the active work was harder and less fluent. The feeling of learning and the fact of learning point in opposite directions.

Now place a large language model into this picture.

What is an LLM, pedagogically? It is the most powerful **friction-removal engine** ever built. Its entire reason for existing is to make cognitive tasks faster and easier — to take the effort out. And it is most impressive, most magical, precisely at the operations that *generate the residue*: producing, retrieving, organizing, explaining, synthesizing, drafting, debugging, summarizing. These are not random functions. They are the verbs of learning. They are the things that, when a student does them, change the student’s brain.

Here is the collision, stated plainly:

**The cognitive operations a language model performs best are the same operations that, when a student performs them, produce learning. So the default, frictionless use of AI is not neutral. It is anti-pedagogical — not because the tool is bad, but because removing effort is exactly what the tool is for, and effort is exactly what learning requires.**


This is why the “cheating” frame fails us. Cheating is a moral category — a violation of rules, an unfairness to honest peers. But a student who pastes the prompt and submits the output has often done something far stranger and sadder than cheat. They have *unwittingly outsourced the one process that would have educated them.* They have paid tuition to have a machine do their growing for them. They got the grade and missed the point, and frequently they don’t even know it — the output looks like learning, it has the texture of learning, and the feeling-of-learning trap means it can even feel like learning. The harm is not primarily to fairness. The harm is to the student’s own mind, and it is invisible to the student.

If you organize your whole response around catching and punishing, you will spend your career policing a moral violation while the real damage — silent cognitive substitution — happens in plain sight, in the work you *didn’t* flag, by the students who used the tool “appropriately.”

## Part II — The resolution: not all struggle is sacred

If the argument stopped there, the only consistent conclusion would be Luddism — ban the tool, restore the friction. But that conclusion is wrong, and it’s wrong for a reason that is itself a deep result in learning science.

**Not all cognitive effort is learning-relevant effort.**

John Sweller’s Cognitive Load Theory gives us the scalpel. Working memory — the conscious, effortful workspace where thinking happens — is brutally, almost insultingly limited. It holds something like four chunks of novel information at once, for something like twenty seconds, before they decay or are displaced. Everything a learner does competes for that tiny space. Cognitive Load Theory distinguishes three claims on it:

- **Intrinsic load** — the inherent difficulty of the material itself, relative to what the learner already knows. (Genuinely hard ideas are genuinely hard. This is irreducible, though it can be sequenced.)
- **Extraneous load** — effort imposed by *how the task is presented* that has nothing to do with the learning goal. Hunting for a buried instruction. Fighting bad formatting. Re-typing a citation by hand. Wrestling the tool instead of the idea. Mechanical busywork that *surrounds* the thinking without *being* the thinking.
- **Germane load** — effort spent on the actual construction of understanding: building the mental schema, making the connection, doing the reasoning that is the point of the exercise.

Working memory is zero-sum. Every chunk consumed by extraneous load is a chunk unavailable for germane load. A student drowning in the mechanics of a task has no working memory left over to actually *think* about it. This is why a brilliant problem buried in a badly designed assignment teaches nothing: the extraneous load eats the germane load alive.

And here is the move that resolves the collision:

**AI used well removes extraneous load to liberate working memory for germane load. AI used badly removes the germane load itself — it does the very thinking the assignment existed to provoke.**


That is the whole theory in one sentence. Everything else is application.

It means there is no blanket answer to “should students use AI.” The question is malformed. The right question is always local and specific:

**For this assignment, what is the cognitive work that is the point — the work that, if a machine did it, means no learning occurred? Protect that. Let the machine have the rest.**


The struggle that is the point is *load-bearing.* Remove it and the structure of learning collapses. The struggle that is not the point is *scaffolding rubble* — necessary perhaps, but inert, and safe to clear away. The professor’s job, newly, is to tell the difference. Surgically. Per assignment. Every time.

## Part III — Finding the load-bearing cognition

This sounds abstract until you do it, and then it becomes almost mechanical. Take any assignment and ask: *if a student turned in a flawless version produced entirely by a machine, what specifically did they fail to learn?* The answer to that question is your load-bearing cognition. Name it precisely, because the precision is the whole game.

Consider a few cases, deliberately drawn from different disciplines, because the lesson is that *the same surface task can be load-bearing in one course and rubble in another.*

**A first-year composition essay.** The load-bearing cognition is almost never “produce grammatical prose.” It is *the formation and revision of a line of thought* — discovering what you believe by trying to say it, and finding the words inadequate, and pushing back against your own first draft. If AI generates the prose, it has performed the thinking *and* the saying, and the student has done neither. But if a developing writer uses AI to fix comma splices while they wrestle with whether their second paragraph actually supports their thesis, the tool has cleared rubble and protected the load-bearing work. Same tool, opposite verdict, decided entirely by *which cognition it touched.*

**An intro programming course.** For a true novice, *writing the syntax is germane* — the act of producing a correct loop, character by character, is how the schema for “loop” gets built. AI autocompleting it robs the novice of the schema. But for the same student two years later, syntax has become automatic, extraneous; now the load-bearing work is *architecture and decomposition*, and AI handling the boilerplate frees working memory to reach for the harder structural thinking. The verdict flipped — not because the tool changed, but because the *learner* did. (We’ll return to this. It is the most important and most ignored feature of the whole problem.)

**A statistics course.** Running the regression is rubble; any software has done that for thirty years. The load-bearing cognition is *deciding which model is appropriate, interrogating its assumptions, and judging whether the result means anything.* Here AI can run the mechanics freely — and, more interestingly, AI can be *deliberately invited to produce a plausible but flawed analysis* that the student’s job is to catch. The thing the machine is bad at (judgment, knowing when it’s wrong) becomes the exact cognition you’re protecting and developing.

**A nursing or case-based course.** The load-bearing cognition is clinical reasoning under uncertainty — pattern recognition, prioritization, the weighing of incomplete evidence against consequence. A machine that hands over “the answer” destroys it. A machine playing a deteriorating patient who responds to the student’s decisions, or playing a skeptical attending who demands the student defend their reasoning, *intensifies* it.

Across all of these runs a single audit. I’ll state it as five questions, because faculty can carry five questions into any assignment-design decision:

**The Friction Audit**

1. **What is the single load-bearing cognition?** The mental work that *is* the learning. If a machine did it, the student learned nothing. Name it as a verb, precisely.
2. **What here is extraneous?** Necessary but not the point — mechanical, procedural, surrounding the thinking without being it.
3. **Where is this learner in their development?** For a novice, the basics are germane. For an expert, the same basics are extraneous. The boundary *moves.*
4. **Therefore:** bar AI from the load-bearing cognition; invite it to absorb the extraneous — and redraw the line as the student grows.
5. **How will the boundary be visible and honest** — designed into the work and named openly — *rather than policed by surveillance?*

That last question matters enough to hold the entire sixth part of this essay. But first, the third question deserves its own — because it is the one almost everyone gets wrong.

## Part IV — The boundary moves: why there is no universal AI policy

Faculty want a policy. A single sentence for the syllabus that settles it: AI allowed, AI banned, AI with citation. The desire is understandable and the policy is impossible, and the reason is one of the most beautiful results in instructional psychology: the **expertise reversal effect.**

Slava Kalyuga and colleagues established that instructional support which *helps* novices can actively *harm* experts, and vice versa. Worked examples accelerate beginners and bore — even impede — those who’ve mastered the material, because for the expert the support is now redundant information competing for the same scarce working memory. Scaffolding is not universally good. It is good *for a learner at a particular level* and bad once they’ve outgrown it.

AI is a scaffold. The most powerful, most available, most patient scaffold ever built. Which means it is governed by the expertise reversal effect like any other — *its correct role is a moving target that should change as the learner develops.* The AI use that would devastate a first-week novice is exactly the AI use that liberates a capstone student. A fixed policy is guaranteed to be wrong for someone, because it freezes a boundary that is supposed to move.

Vygotsky gives us the frame to make this concrete. Learning happens in the **Zone of Proximal Development** — the band between what a learner can do alone and what they can do with help from a “more knowledgeable other.” Stay below the band and the learner is bored; reach above it and they’re lost; live *inside* it, stretched but supported, and they grow. AI is the most knowledgeable, most tireless “other” imaginable. Used with discipline, it can hold a student inside their ZPD continuously — never abandoned to frustration, never insulted by triviality, always reaching just past their grasp.

Used without discipline, it does something that *looks* like help and is its opposite. It doesn’t scaffold the learner *across* the zone. It *teleports* them to the far side, delivering the polished product of expertise without the process that builds expertise. **Scaffold versus teleport** is the whole distinction. A scaffold supports you while *you* climb; a teleporter means your legs never do the work, and you arrive having gained nothing but altitude you cannot maintain.

The original theorists of scaffolding — Wood, Bruner, and Ross, who coined the term in 1976 — named three properties of a *good* scaffold, and AI violates all three by default:

- A good scaffold **does only what the learner cannot yet do alone.** AI will happily do everything.
- A good scaffold is **contingent** — responsive to where this learner actually is. AI is contingent on the *prompt*, not on the learner’s developmental state, and a struggling student often can’t write the prompt that would help them.
- A good scaffold **fades** — it is deliberately withdrawn as competence grows, transferring responsibility to the learner. AI has no native sense of fading. It will prop up a fourth-year student exactly as much as a first-year one, forever.

So the real work of teaching with AI is mostly this: *imposing scaffold discipline on a tool that has no instinct for it.* You become the one who decides what it may not do (because the student must), who makes its help contingent on the learner’s actual level, and — most importantly, most neglectedly — who *fades it on purpose.* A coherent AI pedagogy across a four-year degree looks like a planned withdrawal: heavy structure and tight constraints early, when the basics are germane and must be earned by hand; widening latitude as those basics automate and the load-bearing cognition climbs toward judgment, synthesis, and creation, where AI becomes a power tool for minds that have already been built.

This is the gradual release of responsibility — “I do, we do, you do” — with a fourth term the old model never needed: *“you do, with a power tool you now know how to command, and know when to put down.”*

## Part V — Engagement, and the trap inside it

The hope everyone voices is that AI will make students *more engaged.* It will. That’s the danger.

“Engagement” is one word for at least three different things, and they can move independently:

- **Behavioral engagement** — on task, doing the thing, not distracted.
- **Emotional engagement** — interested, not bored, enjoying it.
- **Cognitive engagement** — processing deeply, thinking hard, doing effortful work.

Only the third one is made of the stuff that learning requires. And here is the trap: **AI can raise behavioral and emotional engagement while lowering cognitive engagement.** It can make a task smoother, faster, more fun, more frictionless — students busy, students delighted, students producing — while quietly removing the very effort that would have taught them anything. A class can *look* gloriously engaged and *be* cognitively asleep. A professor optimizing for the room’s energy and the students’ smiles can be de-skilling them in real time and getting rave evaluations for it.

To navigate this, you need an instrument finer than “engagement,” and Michelene Chi’s **ICAP framework** is the best one we have. It ranks modes of cognitive engagement by the learning they produce, lowest to highest:

- **Passive** — receiving information without doing anything to it. (Watching, reading, *accepting an AI output.*)
- **Active** — manipulating it: highlighting, copying, re-arranging. (Better, but still no new understanding generated.)
- **Constructive** — *generating* something beyond what was given: an explanation, an inference, a new example, a critique. (Now learning is happening — new schemas are being built.)
- **Interactive** — co-constructing dialogically, where each party’s contribution builds on and pushes against the other’s, producing ideas neither held alone. (The highest mode, the deepest learning.)

The naive use of AI plants students firmly at the bottom: they receive an output and accept it. *Passive.* That’s the floor of the ladder and it is where frictionless AI deposits everyone by default.

But the *same tool*, pointed differently, can place students at the top. AI is uniquely, almost uncannily suited to push learners into **Constructive** and **Interactive** modes — *if you assign it the right role.* Which brings us to the most practical idea in this essay. Stop asking “may students use AI” and start assigning AI a **stance** — a role that determines which cognition it performs and which it provokes:

- **The Oracle.** Gives answers. Performs the cognition. This is the default, the bottom of the ICAP ladder, and it is *toxic for the load-bearing work* of any assignment. Almost every misuse is the Oracle in disguise. The discipline of teaching with AI is, more than anything, *refusing to let it be the Oracle for the cognition that matters.*
- **The Tutor.** Explains contingently, scaffolds toward understanding, but is constrained never to hand over the answer to the thing being assessed. Holds the student in their ZPD. (Keeps the student Active-to-Constructive.)
- **The Sparring Partner.** Argues back. Red-teams the student’s claim, demands evidence, plays the intelligent skeptic, refuses to be satisfied. This is the single most underused stance and the most powerful, because it forces the student into **Interactive** mode — the top of the ladder — using AI’s endless patience for an inexhaustible opponent no human TA could sustain. The student does *all* the load-bearing reasoning; AI just makes the reasoning *harder and more rigorous.* Friction, deliberately added back, by the machine whose nature is to remove it.
- **The Simulator.** Plays a role no classroom could otherwise stage: a difficult client, a deteriorating patient, a hostile cross-examiner, a historical figure, an investor who keeps asking “so what?” The student practices judgment against a responsive world. (Constructive and Interactive, and emotionally vivid in a way that drives durable memory.)
- **The Apprentice.** Does the grunt work *under the student’s direction* — but the student must specify, evaluate, and correct it, which means *judgment stays with the human.* The load-bearing cognition (deciding what good looks like, catching the errors) is exactly what AI is worst at and the student must supply. The flawed AI output becomes the pedagogical object. *AI’s unreliability becomes a feature:* an inexhaustible supply of plausible-but-wrong artifacts for students to evaluate, which is the highest and rarest cognitive skill we teach.

Notice what these stances have in common. In every one except the Oracle, the student performs the load-bearing cognition and AI is bent toward *intensifying* it rather than *replacing* it. The tool whose nature is to remove friction is conscripted into *adding* it — more challenge, more iterations, more feedback, more rigorous opposition, more vivid scenarios — at a scale and patience no human instructor could provide. That is the whole inversion. *Used as an Oracle, AI is the deepest threat to learning we have ever introduced into a classroom. Used as a Sparring Partner, Simulator, or Apprentice, it is the most powerful engine for cognitive engagement we have ever had.* It is the same machine. The only variable is the stance you assign — and the stance is yours to assign.

And it solves the engagement trap directly. You are no longer chasing the room’s smiles. You are designing for ICAP-high cognitive engagement and letting AI supply the behavioral and emotional engagement as a side effect — a sparring partner is *also* fun, a simulation *is* gripping. You get all three kinds of engagement, but pointed at thinking instead of away from it.

## Part VI — The ethics, taken seriously

“Responsible and ethical use of AI” has become a phrase people say to feel covered. Real ethical engagement here has at least five dimensions, and none of them is “remember to cite the chatbot.”

**1. Autonomy and the cultivation of dependency.** There is a difference between *using* a tool and being *unable to function without it.* The deep ethical concern is not any single act of AI use; it is the slow cultivation of a mind that cannot generate a thought, a sentence, a decision without first consulting a model. Intellectual autonomy is a developmental achievement — it can be built, and it can be arrested. A professor has a duty of care that runs deeper than any plagiarism policy: a duty not to graduate students who have outsourced their own minds. This is why the *fading* of AI across a curriculum is not just pedagogically optimal but ethically required. To never withdraw the scaffold is to manufacture dependency, and to do it to the young is a serious thing.

**2. Equity, which cuts both ways.** AI is simultaneously the most promising equalizer and the most dangerous amplifier of advantage in a generation, and *which one it becomes depends entirely on literacy.* For the first-generation student who can’t afford an eighty-dollar-an-hour tutor and won’t walk into office hours, a patient, judgment-free, always-available tutor is a genuine democratization of help. For the already-advantaged student arriving with metacognitive sophistication and good habits of mind, the same tool extracts ten times the value — they know how to interrogate it, when to distrust it, how to push it. *The same tool widens the gap unless you teach the literacy that closes it.* Which means: refusing to teach AI literacy is not neutral. Withholding it does not protect the disadvantaged student; it abandons them to extract less from a tool the advantaged will use anyway. Teaching the literacy well — explicitly, to everyone — is itself an act of equity. Pretending the tool away is not.

**3. Surveillance, consent, and the detection trap.** Building your response on AI-detection software is both empirically broken and morally corrosive. Detectors are unreliable; they generate false positives that fall disproportionately on non-native English writers and neurodivergent students, accusing the innocent on the basis of statistical noise. But the deeper problem is what surveillance does to the relationship that good teaching depends on. A classroom run on suspicion teaches a hidden curriculum of distrust, and it positions the professor as adversary rather than ally in the student’s growth. The ethical alternative is *design, not detection*: build work where AI assistance is either irrelevant to the load-bearing cognition or openly invited and made transparent. Make honesty the path of least resistance instead of building an arms race you will lose.

**4. The honest accounting of costs.** Using AI responsibly means being honest that it is not free — not in labor (the human annotators, often poorly paid, who made the model possible), not environmentally (the water and energy of training and inference), not in the unsettled questions of where its training data came from and whose consent was or wasn’t obtained. A professor who teaches “responsible use” while pretending these costs don’t exist is modeling exactly the kind of motivated reasoning we’re supposed to be teaching students to resist. The mature stance — the one worth modeling — is the ability to hold two true things at once: *this is genuinely, transformatively useful,* and *this has real costs we should not look away from.* Teaching students to hold that tension without collapsing it in either direction is, itself, one of the most valuable intellectual habits we can pass on.

**5. The hidden curriculum of how you use it.** Students learn ethics far less from what you *say* about AI than from what they watch you *do.* If you forbid students to use AI to write while you quietly use it to grade — handing back machine-generated feedback on work students were required to produce by hand — the lesson they actually learn is that AI rules are an instrument of power, binding on the weak and optional for the strong. Coherence between your stated AI ethics and your enacted AI ethics is not a nicety. It is the actual curriculum. The most honest move available is transparency in both directions: tell students where and how *you* use AI in the course, hold yourself to the same logic of protected load-bearing cognition you hold them to, and let them see a working adult using a powerful tool with discipline and disclosure. That modeling will teach more than any policy paragraph.

## Part VII — What this asks of the professor

There’s a grief in this that the tips-and-tools genre never mentions, and it deserves naming.

For your whole career, a meaningful part of your value was that you could *do the thing* — write the analysis, solve the problem, produce the expert artifact — and now a machine can produce a passable imitation in seconds. It is natural to feel that as a threat, to your students’ integrity and to your own standing. But the threat is aimed at the wrong target. AI is extraordinary at *performing* the cognition. It remains poor — and a well-designed course makes this vivid — at *the judgment of whether the performance is any good*, at knowing when it’s confidently wrong, at the discernment that only comes from having built the schemas by hand. That judgment is the thing expertise actually is. It was always the thing. The artifact was only ever evidence of it.

So the professor’s value doesn’t shrink in the age of AI. It relocates — from *being the one who can produce the answer* to *being the one who knows which struggles are worth keeping, and why, and for whom, and when to let them go.* That is a higher-order expertise, harder to automate, and frankly more interesting than the one it replaces. It is the expertise of the *designer of cognition* — the person who looks at a learner and a body of knowledge and engineers, deliberately, the specific difficulties that will turn one into the other.

This reframes the entire job around a single craft:

**Teaching has always been, secretly, the art of curating struggle. We just never had to say it out loud, because the struggle was the default — there was no machine offering to remove it. Now that the machine exists, and removes friction by its very nature, the curation can no longer be implicit. It has to become a deliberate, defended, per-assignment act. The professor is now, explicitly, the keeper of the struggle that’s worth keeping.**


That is not a smaller job than the one you signed up for. It is the real one, finally visible.

And it is, at bottom, an act of care. To decide that *this* difficulty stays — that you will let a student be frustrated here, will not rescue them from this particular confusion, will hold the line against the tool that offers to make it easy — is to care more about who they will become than about how they feel in the moment, or how the room reads, or how your evaluations come out. It is to refuse to let a machine do their growing for them, because you understand, as they cannot yet, that the growing was the whole point.

Anyone can remove friction. A machine does it for free. The teacher’s irreplaceable act — the one no model will ever perform, because it requires caring about a particular human’s becoming — is to know which friction to keep, and to have the nerve to keep it.

## Coda: seven principles to carry

1. **Memory is the residue of thought.** If the machine did the thinking, there is no residue. Protect the thinking.
2. **There is no universal AI policy, because the boundary moves with the learner.** What devastates a novice liberates an expert. Plan the *fade*.
3. **Audit every assignment for its load-bearing cognition.** Name, as a verb, the one thing that — if outsourced — means nothing was learned. Bar AI from that. Free it for the rest.
4. **Strip extraneous load; never strip germane load.** AI should clear the rubble around the thinking, never the thinking itself.
5. **Assign AI a stance, not a permission.** Oracle is the toxic default. Reach for Sparring Partner, Simulator, Apprentice, Tutor — roles that *intensify* the student’s cognition instead of replacing it.
6. **Design for honesty; don’t police with surveillance.** Build work where AI is either irrelevant or openly invited. Detection is broken and corrosive; design is durable and kind.
7. **Model what you teach.** Use AI in your own work with the same discipline and disclosure you ask of students. The hidden curriculum is always running.

*The point was never to keep AI out of the classroom, and it was never to let it in unconditionally. The point is to become the kind of teacher who knows, for each thing worth learning, exactly where to keep the struggle — and who keeps it there on purpose, as the deepest form of taking a student seriously.*

This is possibly the best article I've read on AI in higher education in an extremely long time.

Fabulous read. So informative and on point.
