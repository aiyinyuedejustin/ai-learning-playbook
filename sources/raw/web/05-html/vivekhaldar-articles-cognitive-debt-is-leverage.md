# Cognitive debt is leverage

- 链接：https://vivekhaldar.com/articles/cognitive-debt-is-leverage
- 作者：Vivek Haldar
- 获取方式：网页正文（trafilatura 提取）

---

# Cognitive Debt and the Future of Programming

By Vivek Haldar

(This blog post is derived from [this video on my YouTube channel](https://www.youtube.com/watch?v=KAySVbJoF0M).)

Geoffrey Litt recently gave a talk at AI Engineer called [“Understanding is the new bottleneck”](https://www.geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck.html). Simon Willison boiled its central phrase down to [“understand to participate”](https://simonwillison.net/2026/Jul/2/understand-to-participate/): if agents are writing more and more of our code, we still need enough understanding of that code to remain active participants.

I want to offer a different point of view, one I don’t see brought up very often when we talk about what agentic coding is doing to programming and programmers.

[Cognitive debt](https://margaretstorey.com/blog/2026/02/09/cognitive-debt/) is a lament: agents write code faster than we can absorb it. We no longer understand the code, the architecture, the design, or why the system evolved the way it did. We are more spectators than participants.

## Debt is leverage

The term “cognitive debt”, of course, evokes the familiar term “tech debt”.

I’ve been on both sides of the technical debt equation — first as an individual engineer, later as an engineering manager, including at startups where finding product-market fit fast mattered more than anything else.

Framing it as “debt” puts a thumb on the scale. It gives the term a negative connotation. But look around at the real world and debt is everywhere, used deliberately, by people who know exactly what they’re doing. We take on mortgages to buy houses decades earlier than we could with cash. Businesses borrow to fund operations and build-outs. Countries run on debt. Entire markets exist to trade it. Finance people don’t even call it debt — they call it *leverage*. The risk is that while it amplifies your gains, it can also crush you with losses.

Technical debt works the same way. If you’re a startup racing to find product-market fit, a pristine codebase is not the point. You need to try product ideas in the market, learn from customers, and move fast enough to survive. In that situation, you *want* technical debt: you’re buying speed and paying with future maintenance.

So when we talk about cognitive debt in agentic programming, the real question is: **what kind of leverage are we taking on, and do we understand the risk?** Just like when we make a trade-off in a design doc.

## Programming as theory building

This whole discussion reminded me of Peter Naur’s 1985 essay [“Programming as Theory Building”](https://pages.cs.wisc.edu/~remzi/Naur.pdf). (If you’re a compiler geek, you know Naur from the N in BNF — Backus-Naur Form, the notation we still use to describe the grammar of programming languages.)

Naur’s central claim is that the thing that matters about a program or system is not its source code but the *theory* of the program: the design, the architecture, the trade-offs, the reasons it’s shaped the way it is, and the understanding of how it can change. That theory lives in the minds of the programmers who built the system.

He had this evocative distinction between a living system and a dead one. A system is alive when the people who hold its theory in their minds are still around. A system can be running perfectly well in production and still be *dead* if nobody understands why it works or how to evolve it.

That’s the fear about agents that the term “cognitive debt” captures. If agents generate the code and no human ever develops a theory of the system, the code exists but the theory was never built in any human mind.

However, another concept in programming and system-building is in tension with theory-building, and it gets discussed less often: abstraction.

## Abstraction is a license to forget

Abstraction is the main arc of computer science. It might be the main arc of human knowledge and civilization.

A car is an abstraction. A bank account is an abstraction. Money is an abstraction. Underneath each one is an enormous tower of machinery, law, software, trust, and human coordination, built over centuries and kept running by millions of people. We don’t think about any of that when we drive to the store or transfer money. We just use the abstraction.

A good abstraction lets you think at a higher level *precisely because* it lets you safely forget the lower-level details.

Programming has been one long climb up the ladder of abstraction. We went from pulling wires on vacuum tubes, to punched cards, to assembly, to compiled languages, to garbage collectors, frameworks, cloud services — and now agents. [Every one of these transitions scared the programmers living through it](https://vivekhaldar.com/articles/when-compilers-were-the--ai--that-scared-programmers/). Every step up the stack hides something. Every useful abstraction creates a kind of forgetting.

The tension between theory-building and abstraction is that we have to be selective about what we hold in our heads. It is prohibitively expensive to maintain a theory of your entire stack. I can’t build an app in Swift or Python while also holding the compiler, the operating system, the processor, the memory hierarchy, the electrical engineering, and the quantum mechanics in my head.

But from another angle, they are not in tension at all. In fact, abstraction *enables* theory-building. A theory has to fit in a human brain. To reason about a system at all, you need a compressed model of it. You need to be able to say “this part behaves like this” and stop thinking about the gears underneath.

So the claim can’t be “understand everything.” Nobody has ever done that. The claim has to be subtler: understand the right layer, at the right time, with the right fidelity for the decision you’re making.

## Agents aren’t compilers (yet)

A very common objection is: agents are not compilers. They still make mistakes. You still have to supervise them and catch their bad choices.

For now, in most cases, you can’t treat agent-written code like compiler output — throw away the artifact, keep the spec, regenerate with confidence.

But for some classes of apps, we’re already past that point. The spec becomes the source of truth and the code becomes a generated artifact. Lose the binary, recompile. [We already treat compilers this way](https://vivekhaldar.com/articles/read-cognify-write/) — nobody inspects the assembly their compiler emits, and nobody audits their garbage collector’s memory-management decisions. We trust those layers, so we’ve moved up a level.

The problem is that, in this transitional phase, we’re using human experts as monitors, verifiers, and supervisors. There’s a 40-year-old paper explaining why that is a horrible idea.

## Humans make terrible monitors

Lisanne Bainbridge’s 1983 paper [“The Ironies of Automation”](https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf) ([I made a video about it](https://www.youtube.com/watch?v=YgKLOu9f0sI)) was written about industrial process control: machines that mostly ran themselves, with a human watching. The human was expected to jump in when the alarm went off.

The irony is that automation removes the easy, regular parts of the job and leaves the human with the rare, high-stakes, poorly practiced parts. You’re expected to sit there watching a mostly automated system, stay alert, keep your skills sharp — and then suddenly intervene, cold, when it fails. The paper is essentially a long catalog of the failure modes of using humans as monitors and verifiers.

And it’s exactly the role imperfect coding agents assign to us. The agent does the work; the human becomes the verifier. The human is supposed to maintain enough understanding to catch rare failures, while the automation removes the very activities through which that understanding used to get built.

*That* is why the cognitive debt conversation feels so urgent. The deep problem isn’t “AI wrote code I don’t understand.” The deep problem is that the automation is almost — but not quite — good enough, which turns the programmer into the operator of a mostly automated system. We’re stuck in the middle: **enough automation to create distance, not enough automation to create trust.**

## An old anxiety in a new form

Programmers have been wrestling with what it means to be a programmer for as long as [the tools around us have been climbing the stack](https://vivekhaldar.com/articles/programmers-climb/). Every new abstraction changes what must be understood, what may be forgotten, and what kind of work remains distinctly human. This angst is not new.

So no — don’t dismiss cognitive debt. Losing the theory of a system is dangerous, and Naur told us why in 1985.

But don’t treat all forgetting as failure, either. Forgetting is what abstractions are *for*. The entire history of programming is the history of finding higher levels at which humans can think productively.
