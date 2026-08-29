## How this piece should sound

This lesson has to grade three separate repairs (guess rate, label noise,
prompt sensitivity) rather than deliver one verdict on MMLU-Pro, and Ben
Recht's habit of separating a term from its neighbor is the model for making
each grade land. His distinction between "axiom" and "theorem" states a
technical fact in one plain sentence and lets that sentence carry the
paragraph. The piece's own hinge terms, guess rate and the reasoning-tilt
chain-of-thought gap, want that same flat treatment: state the mechanism
first (ten options instead of four means a one-in-ten baseline instead of a
one-in-four baseline), then say what that buys, in the same unhurried
register Recht uses for "we don't have theory for that."

The piece's central difficulty is holding a compliment and a limit in the
same sentence without either one swallowing the other. Anna Rogers' sentence
on BERT does exactly this: she credits it plainly, then states the specific
condition under which that credit holds, and neither clause cancels the
other. Each of the three MMLU-Pro repairs can take that shape: what TIGER-Lab
fixed, stated as a fact, followed by the condition that still limits it,
stated as a second fact rather than a reversal of the first.

Where the lesson has to walk through how a repair was actually built, the
filtering pass on trivial and mislabeled items, the tilt toward
reasoning-heavy questions, Melanie Mitchell's order of operations is the one
to borrow: she lays out Greenblatt's prompting, generation, and voting steps
in full before she reaches for the chess comparison that judges them. The
comparison earns its place because the mechanism is already on the page. Any
comparison this lesson reaches for (a guess floor, a widened gap between
reasoning and direct answers) should wait the same way.

Rogers' two-sentence description of what leaderboards are supposed to do,
followed by "Or do they?" on its own line, is the model for the one turn this
piece is built to make: after MMLU-Pro's construction is on the page, a
single plain question can pivot from what it was designed to fix to whether
it worked, and the question alone should carry the pivot.

For the piece's closing claim, what a given MMLU-Pro gap between two models
does and does not support, Mitchell's paragraph on Goodhart's Law is the
direction: name the specific way a repaired measure still gets gamed or
misread, tied to a mechanism the reader could check against the TIGER-Lab
paper's own numbers, rather than a general warning about scores.

The reader has the MMLU lesson but no background in how a benchmark is
scored, so guess rate, label noise, and prompt sensitivity each need the
plain-word treatment Recht gives "axiom": defined once, in the sentence that
first needs it, then used exactly that way for the rest of the piece.

## Ben Recht, "Benchmark Studies"

Source: https://www.argmin.net/p/benchmark-studies

> "In machine learning, the price of admission is a belief that pattern
> recognition is possible and the conviction that it's too hard to write a
> function describing these patterns from first principles. Generalization
> is an axiom, not a theorem. It would be nice if we could say one algorithm
> is better than another at finding these prediction functions, but we don't
> have theory for that."

This sentence separates two words that get blurred in casual talk about
machine learning: axiom and theorem. Recht states plainly that generalization
is assumed rather than proven and lets that one distinction carry the
paragraph. The flat "but we don't have theory for that" is his own voice: a
working researcher naming a gap most writers smooth over.

> "On the other hand, machine learning has some shockingly robust practices
> that other fields should emulate. The train-test paradigm is fascinating.
> How can I know which method is best? I check my answer on some leaderboard.
> Despite statistical arguments declaring it fundamentally flawed, the
> culture of competitive testing on benchmarks has driven and still drives
> the engine of what the field defines as progress. We still can't explain
> much about why it works as well as it does."

The sentence "I check my answer on some leaderboard" names the field's actual
method without dressing it up. Recht then grants the practice real credit,
"shockingly robust," in the same breath he calls it theoretically
unexplained, and he leaves both statements standing rather than resolving
them into a single judgment.

> "Although some argue that we need to move beyond the benchmarking paradigm,
> I would counter that the benchmarking paradigm defines the field. Believe
> that pattern recognition is possible. Specify your metric at the population
> level. Gather two samples representative of this population and use one
> for play and one for benchmarking, trying to maximize your metric. Once you
> get bored with the benchmark, make a new one. That's machine learning in a
> nutshell."

The four short imperatives turn an abstract definition into steps anyone
could follow, which is the clearest way Recht has of showing what he means by
"the benchmarking paradigm." Ending the list on boredom rather than on a
methodological limit is where his particular sense of humor about the field
comes through.

## Melanie Mitchell, "On the 'ARC-AGI' $1 Million Reasoning Challenge"

Source: https://aiguide.substack.com/p/on-the-arc-agi-1-million-reasoning

> "Oh yeah, they also rebranded ARC as 'ARC-AGI', which I'm not a fan of,
> since I don't love the term 'AGI,' and I don't think that solving ARC is
> necessarily the golden ticket to achieving AGI, whatever AGI is. But no one
> is asking me for naming advice."

Mitchell states her objection to the rename in one plain sentence, then
immediately marks the limit of her own standing to insist on it: "But no one
is asking me for naming advice." She says exactly what she thinks and moves
on rather than leaving the aside to hang unresolved.

> "To me, this is reminiscent of the comparison between computer and human
> chess players. Computer players get a lot of their ability from the amount
> of look-ahead search they can do, applying their brute-force computational
> powers, whereas good human chess players actually don't do that much
> search, but rather use their capacity for abstraction to understand the
> kind of board position they're faced with and to plan what move to make.
> The better one is at abstraction, the less search one has to do."

She spends the paragraphs before this one narrating Greenblatt's method step
by step, prompting, generating, revising, voting, so the chess comparison
lands on facts the reader already has rather than standing in for them. The
comparison itself states a tradeoff with a direction, more abstraction means
less search, instead of leaving the analogy to gesture at a similarity.

> "As with any other AI benchmark that gets a lot of attention, we need to
> worry about Goodhart's Law: 'When a measure becomes a target, it ceases to
> be a good measure.' ARC now is a $500,000 target where everyone is aiming
> at the bullseye. The problem is that when people focus on a specific target
> (e.g., top score on the ARC private evaluation set), they sometimes lose
> sight of what the benchmark is actually trying to measure (e.g., capacities
> for few-shot abstraction based on core knowledge concepts), and the methods
> developed to hit the target might miss the original motivation altogether."

Mitchell names the exact mechanism of failure: people optimizing for the
score stop tracking the capability the score was built to stand in for. She
states this as a risk to a competition she has already said she is
"genuinely excited about," holding both the enthusiasm and the worry on the
page at once.

## Anna Rogers, "How the Transformers broke NLP leaderboards"

Source: https://hackingsemantics.xyz/2019/leaderboards/

> "A big reason why NLP is such an actively developed area is the
> leaderboards: they are the core of multiple shared tasks, benchmark systems
> like GLUE, and individual datasets such as SQUAD and AllenAI datasets.
> Leaderboards stimulate competitions between engineering teams, helping them
> to develop better and better models to tackle human language.
>
> Or do they?"

The two sentences describing what leaderboards are supposed to do are stated
as settled fact, no hedging. Then "Or do they?", three words as their own
paragraph, turns the whole setup into an open question. The turn is carried
by where the sentence sits, not by any word announcing that a reveal is
coming.

> "The chief problem with the huge models is simply this: 'More data &
> compute = SOTA' is NOT research news. If leaderboards are to highlight the
> actual progress, we need to incentivize new architectures rather than teams
> outspending each other. Obviously, huge pretrained models are valuable, but
> unless the authors show that their system consistently behaves differently
> from its competition with comparable data & compute, it is not clear
> whether they are presenting a model or a resource."

The boxed line states her finding as an equation and a verdict at once, short
enough to quote from memory. The sentences right after it do the actual
argument, spelling out exactly what a paper would need to show for a result
to count as more than that equation, so the quotable line is not asked to
substitute for the reasoning.

> "Let me stress that huge pretrained models like BERT are an undeniable
> achievement, and did help to push the state-of-the-art on numerous tasks.
> Obviously, there is nothing wrong methodologically with using any
> `<muppetName>` as pretrained representations, as long as the paper is about
> something else and does not rest on any properties of `<muppetName>` that
> have not been fully validated."

This is the passage where Rogers grades the exact method she has spent the
whole post criticizing. She credits BERT by name, then states the specific
condition under which reusing it is fine, and both statements stand
side by side rather than one qualifying away the other. The running
placeholder for BERT, ERNIE, and the rest is her own device: dry rather than
cute, and it keeps the point general without losing the precision of naming
an actual condition.
