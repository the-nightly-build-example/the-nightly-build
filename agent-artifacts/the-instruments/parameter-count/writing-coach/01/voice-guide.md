# Voice guide: the-instruments/parameter-count (01)

## Directive

Write as a measurement explainer who does the counting in front of the reader.
The house voice already gives you plain claims and concrete stakes. What this
lesson needs on top of that is the metrologist's discipline: before you judge a
number, say exactly what physical thing it tallies, and when a number misleads,
show the arithmetic that misleads people rather than asserting that it does.

Register: unhurried and exact, never brisk. This is the one desk where slowing
down to count is the point, so a sentence that walks a small sum is doing the
work, not padding. Keep the authority quiet. The reader has repeated "175
billion parameters" without knowing what it counts, and so has almost everyone;
the tone toward that reader and toward the people who got the MoE math wrong is
correction without condescension. You are handing them a caliper, not catching
them out.

The three moves that will change sentences here:

- Ground the number in the objects it counts before you say anything about what
  it means. A parameter is one learnable weight, a single number the model
  multiplies into an activation and freezes after training. Name the weight
  matrices the count is made of before the count becomes an argument.
- Do the misleading arithmetic in the open. The "8x7B = 56B" error and its fix
  (attention is shared, so the experts do not simply multiply) is the spine of
  the misled case. Put the wrong sum and the right one where the reader can see
  the step between them.
- Isolate one variable when two systems sit side by side. The advertised total
  and the active count differ by exactly one thing the headline hides: how much
  of the stack fires per token. Make that the only thing moving in the
  comparison.

## Licenses

form: arithmetic worked in the prose
move: the measurement debunkers put the plausible wrong number and the correct
  number in the reader's view and walk the one step between them (shared
  attention, activated fraction). when a figure misleads because people compute
  it wrong, the correction is the computation, shown.
bar:  the use shows the actual figures read off the model's own paper and the
  specific step that resolves them; it corrects an error a real reader makes,
  never a sum invented to be knocked down.

form: naming the physical thing the number counts
move: strong explainers of a spec (what a megapixel is, what a clock tick is)
  say what is literally being tallied before complicating it, so the abstract
  figure has a body. here that is the weights in the attention and MLP blocks
  and the embedding table.
bar:  the sentence names the actual counted objects, not "the network" or "the
  model's size"; it earns its place by making a later claim about the number
  concrete.

form: an isolated side-by-side of two systems' figures
move: the clock-speed writers set two processors equal on the headline number
  and unequal in output, so the reader sees the headline number is not the work.
  the parallel here is total-vs-active across a dense model and an MoE, or across
  two MoEs.
bar:  each figure is primary-sourced, and the comparison holds everything fixed
  except activation, so the reader can attribute the gap to one cause. If it
  reaches for rhythm or reversal it has become the banned dek mold; keep it a
  plain table or plain parallel sentences.

## Recently used, do not reuse

- The "same X, two numbers" reversal, in the dek and anywhere else. The recent
  desk deks lean on it ("both are true"; "0.3 by one measure and 2.9 by
  another"; "scored X and Y, and only the compute changed"). Total-vs-active is
  genuinely a two-number story, which is exactly why this mold is the trap. The
  reveal must not be staged as a matched pair snapping into contrast.
- Heading cadence that joins two clauses with a comma and "and" ("The scale, and
  what it is compounding against"). Vary the shape across the piece.
- Do not re-teach training-compute (link the-instruments/training-compute) or
  the Chinchilla result (link the-evidence/chinchilla). Their prose lives in
  those lessons; reaching for it here repeats them.

## Tim Harford, "Statistics, Fast and Slow"
Source: https://timharford.com/2018/05/statistics-fast-and-slow/
Craft:
- cadence: alternates a large number with a thing the reader can picture, and
  lets the picture land before returning to the figure.
- argument: a number and lived experience disagree, and the resolution is
  understanding what the number is actually measuring, not distrusting numbers.
- evidence: one concrete case carries the abstraction (the average bus holds 17
  people, yet every bus feels full because empty buses are seen only by their
  drivers).
- stance: a fellow learner who admits when a figure confused him, which buys
  trust before he corrects the reader's intuition.
- notice: the gap between what you observe and what the average says — directly
  transferable to advertised total versus what runs per token.
- diction: plain, borrows a technical term only with its plain-words gloss in
  the same breath.
- reader: treated as capable and curious, never lectured; the misconception is
  named as a natural one, then explained.
- the missed move: he explains why the wrong intuition felt right, so the
  correction teaches instead of scolding.

## Lisa Eadicicco, "Why a Phone's Megapixels Don't Matter As Much As You Think" (Time)
Source: https://time.com/4192833/smartphone-camera-megapixels/
Craft:
- cadence: definition, then contradiction, then the ignored variable, in short
  steps that each spend the last.
- argument: the marketed number measures one real thing (resolution) but not the
  thing buyers think it measures (image quality).
- evidence: states what a megapixel literally is before complicating it, then
  hands the ignored variable a physical picture (larger pixels gather light like
  bigger buckets catch rain).
- stance: matter-of-fact; concedes the number is sometimes right before showing
  when it is not.
- notice: a single spec stands in for quality it cannot capture — the same
  substitution the parameter count invites.
- diction: accessible, one worked analogy doing the load rather than adjectives.
- reader: assumed smart and misled by marketing, not foolish.
- the missed move: it separates "what the number counts" from "what people read
  into it" as two distinct sentences, which keeps the correction clean.

## XDA, clock speed / the megahertz myth
Source: https://www.xda-developers.com/everyone-obsesses-over-this-one-spec-but-it-barely-affects-performance/
Craft:
- cadence: methodical — define the myth, show the counterexample, then say when
  the number still means something.
- argument: a spec that once tracked performance stopped tracking it as
  architecture changed, so equal on the headline number no longer means equal in
  work.
- evidence: the side-by-side where two chips are locked to the same clock and
  core count and still differ, isolating architecture as the cause.
- stance: a practical guide, not an authority performing expertise.
- notice: the number did not become wrong, it became incomplete once a new
  design (here, sparse activation) broke the old proportionality.
- diction: specific without jargon; names the hidden variable plainly.
- reader: respected, assumed to have obsessed over the wrong spec in good faith.
- the missed move: it grants the number its old validity before showing what
  severed it, which is why the correction reads as teaching rather than
  gotcha — the dense-model count was a fair proxy until MoE, and saying so earns
  the MoE reveal.
