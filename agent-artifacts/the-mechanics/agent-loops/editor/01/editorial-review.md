# Editorial review: the-mechanics/agent-loops (editor/01)

## Correct

Thesis from the draft alone: a stuck agent repeating a just-failed step is the
default behavior of a stateless model re-reading a transcript while a harness
executes what it returns, so the reader can tell a real fix (change the
transcript or the harness) from a cosmetic one (retry, nudge, raise temperature).
The claims under it: (1) an agent is a model in a four-step loop with a harness;
(2) the model is stateless, so the transcript is its only memory and the next
action is the most probable continuation of that text; (3) an appended error is
weak signal because a model cannot reliably judge its own reasoning; (4) greedy
decoding also pushes toward the repeat, a cause shared with token-level
repetition loops; (5) below the transcript and the harness nothing changes the
outcome; (6) fixes work by supplying a better signal or a harder stop.

I tried to break each and read past the quoted passages. Where each held:

- Huang et al. is the claim I most wanted to check, because the source title
  invites the "cannot self-correct" rounding the refinement forbids. The article
  does not round it. It states both settings, gives the intrinsic drop (GPT-4
  GSM8K 95.5 to 91.5 to 89.0, Table 3) beside the oracle lift (GPT-3.5
  CommonSenseQA 75.8 to 89.7, Table 2), and lands it as signal quality: "The
  finding is not that a model cannot revise. It is that a model cannot reliably
  judge whether its own reasoning was correct." Both figures and the §3.3
  mechanism match the record. Held.
- Greedy decoding and the line to repetition-loops. The article credits ReAct's
  footnote 6 for "part of their loop" and draws the line as "Some action-level
  looping shares that decoding-level cause," not two separate phenomena and not a
  claim that decoding is the whole cause. Matches the record and the refinement's
  sanctioned wording ("attribute part of"). Held, not overstated.
- The ground proposition and the temperature point read as the lesson's own
  synthesis. The reduction ("Nothing below that line changes the outcome") carries
  no citation; the temperature knob links the-mechanics/sampling-temperature in
  prose rather than citing it as a numbered source. Correct.
- The SWE-agent case is faithful: repeated edits after an errant edit introduces a
  syntax error, 1185 of 2942 (51.7%) trajectories with a failed edit, 12.47%
  resolved against 3.8% prior, the edit guardrail as a harness fix. All match the
  Numbers section and §5.2/§3. The AutoGPT #1994 instance carries its single
  "one unreplicated report, not a rate" caveat. The LangGraph cap carries its
  version caveat (1000 as of v1.0.6, 25 earlier) and no fragile cap number is
  leaned on.
- No code listings: the loop is carried by a numbered-steps component, a stat
  strip, prose, and one table. Series rule met.
- The open question is marked in its own note block (why a model under-weights
  the error in its transcript; whether reliable self-correction is possible with
  no outside signal), and the settled/open split is stated at the close.

Break found and fixed: the orientation section said AgentBench "scores models as
agents across eight environments." No input supports the count eight; the
evidence record (s3) says only "across many environments." Narrowed to "across a
range of environments." The 82.5% TLE figure is correctly framed as the whole
finish-reason category (which includes repeated generations), not as a looping
rate, and the ReAct 47% is explicitly flagged as a reasoning-error row the loop
is only part of, per the record's instruction not to report 47% as the loop rate.

Labels checked against their owning documents: headline, dek, and the five body
headings carry no figure, title, date, or affiliation that the record does not
own. Every citation href was read against the evidence URLs and matches
source-for-source; the full proof (links included) resolved them all.
data-nb-kind audited row by row: s1-s4, s6-s9 primary and s5 secondary, matching
the record exactly (AutoGPT #1994 recorded as primary firsthand report, Vectara
as the one secondary aggregator). 8 primary, 1 secondary, 9 total meets the
series policy. data-nb-section labels are the house short-slug convention, the
same shape as repetition-loops and the other recent pieces.

## Reads well

I ran the placeholder test on every edge and read the piece once as someone
arriving cold from a link. Nothing failed the test outright and nothing had to be
cut for slop. The antithesis constructions (the stuck agent "is not a broken
product," "The finding is not that a model cannot revise," "A cap is not a way out
of the loop") each correct a misconception that is real and stated in the piece,
which is the one condition under which the form stays; none is decorative. The
"By the end you can look at any proposed fix..." opener closer is one concrete
capability, not the banned "A, B, and C" list mold, and it is the template's
required promise. No em-dashes, no leaked briefing phrasing (I read commission.md
for clause order; the cause-chain sentences are rewritten in the article's own
words, not lifted), and no borrowed clause from the voice-guide exemplars.

Against the recent record: the dek leads with a definition of an agent rather than
hangman's "X stops doing Y because Z, so" causal mold, so it is its own line. The
headings are built differently from one another and do not repeat the recent
comma-and heading shape.

Where the draft ran flat: nothing needed lifting. The prose already follows the
voice guide's register (one mechanism per sentence, a named part given a job at
first mention, numbers at the joints: 51.7%, 130 of 134, 95.5 to 89.0). I made no
rewrite-for-register edits, which the standard prefers over inventing a better
sounding sentence.

## The experience

The rendered page reads top to bottom as the argument it claims: the SWE-agent
opener makes the behavior concrete before any mechanism, the numbered steps carry
the loop without code, the stat strip and the fixes table each show a comparison
faster than a paragraph would, and the table sorts every fix by where it acts,
which is the exact tool the piece promises. Nothing drags and the weight sits at
the ground reduction and the fixes table, where it belongs. What the piece gives
beyond its sources: it places the loop in the plain architecture (stateless
predictor plus harness) and reduces it to the floor below which nothing changes,
so a reader can sort a real fix from a cosmetic one, work none of the individual
papers does. That matches the original-work sentence in draft-handoff.md, and it
is visible on the page in the ground section and the sorted fixes table.

## Edits

- Narrowed "scores models as agents across eight environments" to "across a range
  of environments" (the count eight is supported by no input; the record says
  "many environments").
- Re-stamped the article (words 2195 to 2197) to match the edit.

## Decision

approve. It is correct, it reads in the guide's voice, and the rendered page does
the teaching the commission asked for; the one unsupported figure was narrowed to
the record and the full proof passes with links included.
