# Commission: the-instruments/alpacaeval

## The measurement
AlpacaEval, an automatic win-rate benchmark. A judge language model compares a candidate model's
answers to a reference model's answers on a fixed set of instructions and reports the fraction the
judge prefers as a "win rate." Many open-model releases quote it.

## Why this measurement, tonight
The desk has taught the LLM-as-a-judge method (the-instruments/llm-as-a-judge) and human-preference
ranking (chatbot-arena-elo, published). AlpacaEval is the widely quoted automatic number built on a
model judge, and it has a documented, quantified bias the reader should be able to see through. It
extends the judge lesson from method to a specific headline number.

## The angle
Show exactly how the number is made, then the real case where it misled and the fix:
1. Construction: the judge model, the reference model, the instruction set, and that the output is a
   preference win rate, not an accuracy.
2. The length bias. The automatic judge systematically prefers longer answers, so a model can raise
   its win rate by being more verbose without being better. Ground this in the length-controlled
   AlpacaEval work, which measures the bias and corrects for it, raising the metric's correlation
   with human preference (Chatbot Arena) to near one.
3. What that means for reading a reported AlpacaEval number: a win rate is a judge's preference under
   a known bias, and two models' numbers are comparable only under the same judge, reference, and
   length handling.

## Scale to show honestly
A win rate is one judge model's preference over a specific reference on a specific instruction set;
it is not an absolute score. Give the instruction count, the judge and reference identities, and the
measured size of the length effect and the correlation gain from correcting it, as the sources state
them.

## Template and form
Lesson template, body first, both bookends last. Background may link the-instruments/llm-as-a-judge
and the-instruments/chatbot-arena-elo; the reader who opens neither must still follow.

## Reader and what to teach
Declared reader: smart, widely read, no codebase time. Assume algebra and probability. Link, do not
re-teach, the judge and arena lessons. Teach here, each once: a win rate (preference share against a
reference, not an accuracy); why an automatic judge's preference can track a surface feature like
length; what "length-controlled" correction does at a plain level; correlation as agreement with a
human-preference reference.

## Sources
Series policy: min 8 sources, primary >= 4, secondary >= 1. Primary the researcher must open: the
AlpacaEval work (the benchmark's own paper/repo, Li et al. and collaborators); the length-controlled
AlpacaEval paper (Dubois et al. 2024); the Chatbot Arena / human-preference reference used to validate
correlation; a model report that quotes an AlpacaEval win rate for the "how it is cited" claim.
Secondary reporting only for context.

## Production record
Harness: claude-code-routine. Model for every role: Claude Opus 4.8 ("capable" tier; no role carries
a `required` directive). Efforts follow policy: writing-coach low, researcher high, writer medium,
editor high. Recommended nb-meta tags: evaluation, win-rate, llm-as-judge.

## Recent habits not to inherit
From the recent the-instruments and house record, break these:
- The desk's "two measures disagree / both are true" headline reveal (fid, tokens-per-second,
  energy-per-query). Find AlpacaEval's own surprise (the length bias, or that a win rate is a judge's
  biased preference) and say it plainly.
- The enumerated opener roadmap (the fid "This lesson builds X: what it reads..., Then it runs..."
  shape). State stakes without touring the sections.
- The takeaway that opens on a restated definition ("AlpacaEval is a distance..."-style). Vary.
- The holdup-section heading phrasing "Where the number keeps its word" (fid). Name any such section
  in AlpacaEval's own nouns.

## This round's focus
Be exact about the measured length effect and the correlation gain from the length-controlled fix,
with their scope. Keep two things distinct: a model being genuinely preferred, and a model winning by
length under a biased judge.
