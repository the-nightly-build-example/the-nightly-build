# Voice guide: the-evidence/alexnet (01)

## Directive

Register: warm, patient, and admiring, in the temperament of a teacher who
respects the paper on the table and still means to correct what people say about
it. This is the opposite of the desk's recent instinct. The last several Evidence
pieces land their finding as a clever deflation ("never mentions," "no further
details," "zero citations"). This lesson must not. AlexNet's result was real and
large; the shorthand credits it with more than it showed. Both are true, and the
prose holds them together without ever resolving into a debunk. When you correct
the myth, the sentence still honors the paper.

Reader: a smart, widely read person who has absorbed "the 2012 ImageNet moment"
and "AlexNet proved deep learning works" and wants to know what is actually true.
You are teaching them, not scoring a point off the paper or off the thing they
half-believed. No wink, no gotcha, no smugness at anyone's expense.

The moves that will change sentences in this article:

1. Hold both truths in the same passage. The result was a real ~10-point win; the
   shorthand credits AlexNet with inventing or proving deep learning. State the
   real thing and the overclaim close together, and let the piece stay generous.
   A passage that reads as "here is what they got wrong" has left the register.

2. Let humble, dated numbers carry the scale. Two GTX 580 cards with 3GB each,
   roughly five to six days, about 1.2 million images. Give each a comparison a
   2026 reader already holds, and let the smallness do the work on its own. Do not
   announce that the numbers are small or that this is striking; a number the
   reader can measure against something they know makes the point without a nudge.

3. Credit superseded engineering as the right call under its constraints. The
   two-GPU split, local response normalization, overlapping pooling were later
   dropped. Present each as a sensible answer to a real 2012 constraint — 3GB of
   memory forced the split — never as a quaint mistake the field grew out of.

4. Teach each borrowed term by building the picture in plain words before any
   formula: what a convolution slides over, what "top-5 error" counts, what
   overfitting is. Set the picture first, name the term once, then reuse it
   exactly. Everything the reader needs to follow a paragraph is taught before
   that paragraph, in this lesson or a linked one.

What this needs that the house default does not supply: the default (plain
claims, no hype) gives clarity and restraint, but not this article's particular
combination of admiration and correction. The recent desk output shows the
default drifting toward the clever negative reveal; this piece needs the reverse
temperament — generous, unhurried — while still landing the correction. That,
plus the teacherly build-up and the humble numbers carrying the scale argument,
is the sound the default will not produce by itself.

## Licenses

form: direct second-person address inside a worked mechanism
move: Olah and Alammar put the reader inside a step before naming it — "we slide
  the filter," a running example the reader does the calculation on — so the
  mechanism is felt before it is formalized.
bar:  each "you" sits inside an actual step the reader is being walked through: a
  calculation, a slide of the filter across the image, the rule for scoring a
  top-5 guess. Cut any "you" that is rapport, a rhetorical "you might think," or a
  polite stand-in for "one."

form: one physical analogy carrying one mechanism
move: Olah lets a single image ("conveyor belt") carry an entire concept; the
  analogy is load-bearing, and the reader keeps the mechanism by it, not by the
  notation.
bar:  at most two in the whole piece, each mapping cleanly onto the real
  mechanism (a small stencil slid across the image for a convolution, and the
  like). Name it once, cash it out in the paper's own terms, and drop it once the
  mechanism is taught. No analogy for scale, for importance, or for the era — only
  for a mechanism the reader must picture to follow the next paragraph.

form: the credit-then-correct sentence
move: Karpathy shows a real success and its real failure in the same breath, and
  the admiration is believable precisely because the limit sits beside it.
  Transferred here: the shorthand is corrected without the paper losing its due.
bar:  the sentence names the specific thing proved and the specific thing
  overclaimed, both concrete, and credits before it qualifies. If the correction
  could be lifted out and quoted alone as a gotcha, it fails — rewrite until the
  credit and the correction cannot be separated.

## Recently used, do not reuse

- The negative-reveal / absence dek: "X, not Y," "never mentions," "no further
  details," "zero citations," "without ever showing." The commission names this
  mold and the writer must break it. Land the finding in a shape that states what
  the paper did, not what it lacks.
- The "collapsed / overshoots once inspected" gotcha reveal (BERT's score
  "collapsed once the shortcut was closed," AlphaFold's test the prize citation
  overshoots). Same temperament as above; avoid it.
- The word "shorthand" as the dek's or headline's pivot, and the "before the
  shorthand runs past it" / "where the shorthand overshoots" framing. AlphaFold
  (2026-08-03), the immediately prior Evidence piece, is built on exactly this.
  The gap between claim and record needs different words here.
- The heading mold "What X actually says / proved / measures," and the reflexive
  "actually." Three of the last four pieces used it ("What the prize citation
  actually says," "What each document actually proved," "What the report measures
  itself").
- The paired-phrase heading "A [noun] in, a [noun] out" ("A sequence in, a shape
  out").
- Any heading or dek that joins clauses with a comma and closes on "and," and the
  suspended trailing clause ("...by a margin worth understanding before X"), both
  flagged in spec/headlines.md and both present in the recent deks.

## Chris Olah, "Understanding LSTM Networks"
Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/
Craft:
- cadence: a short declarative claim opens a paragraph, then one or two longer
  sentences expand it; rarely more than two or three clauses in a sentence.
- argument: delays the "how." Several sections establish why the problem exists
  before any mechanism appears, and each section is a prerequisite for the next.
- evidence: one relatable scenario per abstraction (a sentence needing the earlier
  word "France," a pronoun needing a gender from earlier context), chosen so the
  example parallels the exact mechanism being explained.
- stance: names the difficulty out loud ("look pretty intimidating," "seem kind of
  mysterious") and tells the reader plainly when not to worry about a detail yet.
- notice: opens on ordinary experience — reading this sentence, using the previous
  words — so the technical problem feels natural rather than arbitrary.
- diction: one load-bearing physical image carries a whole concept (state as a
  conveyor belt, gates that let information through); notation is held back until
  the intuition is set.
- reader: "we" and "let's go back to our example" — the reader walks alongside as
  a collaborator, not an audience being lectured.
- the move the axes miss: the mental picture is the argument, not an illustration
  of it. The reader understands by seeing the structure before reading any math.
  In a text-only lesson this transfers as: build the picture in words first, then
  name the formula for the reader who already sees the shape.

## Jay Alammar, "The Illustrated Transformer"
Source: https://jalammar.github.io/illustrated-transformer/
Craft:
- cadence: short declaratives set a pattern, broken by a question that voices the
  reader's own ("What are the query, key, and value vectors?"), giving a beat of
  breathing room before the answer.
- argument: nested scale. Black box, then components, then vector-level mechanics,
  then the matrix form — intuition before formalism, the reverse of the paper's
  own order.
- evidence: one running example reused across sections ("The animal didn't cross
  the street because it was too tired"), plus a toy vocabulary small enough to
  hold in the head while a calculation is walked through.
- stance: names his own simplifications ("we will oversimplify," "don't be fooled
  by me throwing around 'self-attention'") and his prior ignorance, so the reader
  trusts a guide who admits what he is glossing.
- notice: numbers get their reason, not only their value ("8, the square root of
  the key dimension"), so a constant stops feeling arbitrary.
- diction: specific over atmospheric ("multiply the embedding by three matrices we
  trained," "multiplying them by tiny numbers like 0.001"); analogy is rare and
  strictly functional.
- reader: promises a cumulative payoff and forward-references what is coming, which
  relieves the anxiety of reading something not yet fully explained.
- the move the axes miss: explains the same mechanism two or three times at rising
  resolution without announcing it. Repetition with more precision reads as the
  reader's understanding deepening, not as redundancy.

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"
Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/
Craft:
- cadence: a punchy declaration pulls the reader in, a longer explanation sustains
  it; fragments after a colon break dense ideas into beats; tempo speeds at a
  surprising result and slows for the mechanism behind it.
- argument: fascination, then theory, then escalating evidence (Paul Graham prose,
  Shakespeare, Linux source, LaTeX), then honest reflection — each experiment
  evaluable before the next arrives.
- evidence: shows the actual generated output with its warts (the awkward
  sentence, the undefined variable, the mismatched tag), so the reader sees the
  promise and the failure in the same view.
- stance: tempers his own excitement and separates proof from speculation out loud
  ("forget I said anything," "these conclusions are slightly hand-wavy"); never
  claims the model "understands."
- notice: the failures are central examples, not a limitations footnote. Showing
  what broke is what makes the successes credible.
- diction: concrete specifics ("opens and closes brackets correctly and indents
  its code well"); humor that arises from the data rather than being forced onto
  it; "magical" used as honest puzzlement, not as hype.
- reader: a personal anecdote and a driving question ("how is that even
  possible?") set the through-line; warm without being chummy.
- the move the axes miss: the enthusiasm is licensed by the honesty. The
  admiration is believable because the limits sit in the same breath. This is the
  exact model for crediting AlexNet fully while correcting what people say it
  proved.
