# Voice guide — the-evidence/the-bitter-lesson

## Directive

State Sutton's claim the way he states it: as a flat finding, not a hedge. Give
it a full, undiluted sentence or two before a single word of testing begins —
his cause (Moore's law compute), his mechanism (search and learning beat
built-in knowledge once compute grows), and one worked example, run all the
way through. Only after the claim stands at full strength does the weighing
start. A reader who stopped at the end of that statement should believe
Sutton has a real point, not sense the knife already coming out.

Keep the critique from tipping into a takedown by aiming it at the citation,
not the man. Sutton wrote a short essay and said so nowhere; the people who
cite it as settled law are the ones stretching it past what it holds. Land the
skepticism on that gap — what the text supports versus what it gets asked to
carry — never on Sutton's competence or motives. Where the essay is right
(hand-built chess and Go heuristics really did lose), say so as plainly as
where it overreaches. A critique that only ever finds fault reads as
score-settling; alternate a real concession with each real objection.

Anchor every comparison to a number the reader can hold: how many examples
Sutton's pattern rests on, how many data points Kaplan and Chinchilla ran,
how much of a transformer's or an RLHF pipeline's design is human-chosen
structure. Abstract framing ("the debate over scale") is where a thin
argument hides; a count or a parameter figure is where it can't.

State your own confidence the way you'd state anyone else's: not "arguably"
padding every sentence, but a plain claim followed by exactly how much
evidence stands behind it. When the evidence for a piece of the argument is
thin, say that it's thin instead of writing around it.

Recently used, do not reuse: the openers "The 20XX paper …" and "The
slogan … outgrew …"; the "X is not Y; it is Z" hedged-contrast thesis
construction; a colon-subtitle headline. The general move of showing a
headline claim resting on a smaller foundation than its citation implies is
this piece's actual subject and stays — vary only the opening line and
section cadence that carried it in recent pieces, not the move itself.

## Exemplars

```text
## Rich Sutton, "The Bitter Lesson"
Source: http://www.incompleteideas.net/IncIdeas/BitterLesson.html
Craft:
- cadence: one dense opening paragraph carries the entire thesis and its
  mechanism in maybe six sentences, clauses stacked with commas, almost no
  paragraph break until the examples start. Each example then gets its own
  short paragraph, same shape repeated: what the human-knowledge side tried,
  what beat it, who was unhappy.
- argument: the claim arrives in sentence one as an established finding —
  "The biggest lesson that can be read from 70 years of AI research is..." —
  no "I think," no "arguably." Confidence is stated, not earned on the page.
- evidence: four examples in series (chess, Go, speech, vision), each
  compressed to a few sentences, no numbers on how much compute changed or by
  what margin the approaches differed. The pattern is asserted, not measured.
- stance: dry and slightly needling toward the side that lost — "these
  human-knowledge-based chess researchers were not good losers" — one line,
  then he moves on without dwelling.
- notice: what's absent is louder than what's there. No citations, no dates
  on the speech and vision claims, no mention of a single case where the
  human-knowledge approach held. The essay's confidence comes from omission
  as much as argument.
- diction: "leverage computation," "in the long run," "massive" — set once,
  reused verbatim across the piece rather than varied for style.
- reader: assumes an AI-literate audience already inside the debate; defines
  nothing, glosses nothing.
- the move this piece needs: adopt his economy and his refusal to hedge the
  claim itself, and reject his unearned certainty about the pattern's size.
  His plainness is the register to borrow; his missing evidence is exactly
  what this article supplies instead of assuming.
Calibration: "The biggest lesson that can be read from 70 years of AI
research is that general methods that leverage computation are ultimately
the most effective, and by a large margin."
```

```text
## Scott Alexander, "Beware the Man of One Study"
Source: https://slatestarcodex.com/2014/12/12/beware-the-man-of-one-study/
Craft:
- cadence: an aphorism-length opening line, then the paragraph expands to
  set up the statistical picture before any criticism starts.
- argument: frames the caution as an extension of old wisdom ("Aquinas
  famously said... I would add...") rather than a novel takedown — this
  disarms the reader's instinct to defend the thing being questioned before
  the case against it even opens.
- evidence: one case worked all the way through in numeric detail (a bipolar
  drug, the spread of trial outcomes around a true effect) instead of a list
  of loosely connected instances. Depth over breadth.
- stance: neither dismissing the single study nor accepting it — he explains
  why studies on "the same question" often aren't (different populations,
  doses, diagnoses) before naming the danger of over-citing one result. The
  target is the citation practice, never the researchers who ran the study.
- notice: the essay never argues the cited study is wrong. It argues the
  study is being asked to prove more than one study can prove — a distinction
  the piece keeps returning to by naming, each time, exactly what a single
  result can and cannot settle.
- diction: plain, no statistics jargon without a plain-language gloss
  attached in the same sentence.
- reader: an intelligent reader with no statistics background; the bell-curve
  idea is taught inline, not assumed.
- the move this piece needs: the criticism lands entirely on how the result
  gets used afterward, not on the person who produced it. That's the exact
  shape this article needs for Sutton: no verdict on Sutton, a verdict on the
  citation.
Calibration: "Aquinas famously said: beware the man of one book. I would add:
beware the man of one study."
```

```text
## Dan Luu, "Which is faster, keyboard or mouse?"
Source: https://danluu.com/keyboard-v-mouse/
Craft:
- cadence: opens on a direct question, then two clean declarative sentences
  set the majority belief and the contested counter-claim back to back before
  either gets touched.
- argument: states the extreme version of the counter-claim plainly, then
  tests it with a reductio before any measurement begins — economy of logic
  before economy of data.
- evidence: concrete benchmark numbers appear within the first few sentences
  (typing speed against speaking speed) so every later comparison has
  something the reader can already picture.
- stance: refuses the binary the debate offers on both sides; reframes the
  question as "which tasks are faster with which tool" instead of picking a
  side of an all-or-nothing claim. He goes and finds the source of the
  contested claim (a supposed Apple study) and reports exactly what could and
  could not be verified about it.
- notice: the story turns out to be about a citation nobody can actually find
  the source of, not about keyboards or mice.
- diction: names the specific task, never "efficiency" or "productivity" in
  the abstract.
- reader: a working programmer who holds the folk belief already; the piece
  builds the case rather than assuming agreement.
- the move this piece needs: chase a citation to its root and report what's
  actually there. That is precisely this article's job with Sutton's own
  examples — check what the chess and Go record actually shows before
  letting the essay's summary of it stand.
Calibration: "Which is faster, keyboard or mouse? A large number of
programmers believe that the keyboard is faster for all tasks."
```

```text
## Matthew Yglesias, "It's Not Just Trade" (Slow Boring)
Source: https://www.slowboring.com/p/its-not-just-trade
Craft:
- cadence: short declaratives ("I did not sell any shares.") alternating with
  a longer sentence that supplies the reasoning behind them — never more than
  one qualifying clause stacked onto another.
- argument: opens by stating his own prior plainly and calibrating it out
  loud — what he believed, how confident he was, and why — before bringing in
  what actually happened.
- evidence: builds the case one piece of context at a time rather than
  posting a thesis sentence up top and backfilling it.
- stance: measured respect toward the people whose read on the situation
  turned out to be partly wrong; no gloating when he later shows the gap
  between their claim and events.
- notice: the calibration of his own certainty is the noticeable thing — he
  says exactly how sure he was, not just what he now believes.
- diction: contractions, short common words, zero unexplained jargon.
- reader: a generalist with no insider knowledge of the subject at hand;
  nothing is assumed that wasn't just supplied.
- the move this piece needs: narrate an update honestly — what a claim
  predicted, what the record since then shows, what that changes about how
  much to trust it — without narrating the article itself or addressing the
  reader directly. Model the update, don't announce that you're making one.
Calibration: "I was aware of Trump's extremely dubious ideas about trade
policy and thought it was definitely possible that he would implement them."
```
