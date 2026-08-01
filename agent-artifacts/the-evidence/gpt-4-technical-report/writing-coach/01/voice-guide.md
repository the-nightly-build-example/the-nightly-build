# Voice guide — the-evidence/gpt-4-technical-report

Register: a plain, declarative reader-briefing, not an indictment. The writer
has read the document closely and is reporting what is in it and what is
missing, the way a careful colleague would if you asked "so what does this
report actually say." No outrage, no relish in catching OpenAI out.

Reader relationship: a smart peer who has heard the report cited and never
opened it, being handed the receipts, not a lecture. Never address the reader
directly or narrate the piece's own project.

Moves that will change sentences in this article:

- Quote the document's own language for both halves of the argument: the
  disclosure disclaimer and any claim you are checking. Do not paraphrase a
  sentence you can lift. A paraphrase softens exactly the wording that is the
  evidence.
- Keep three things typographically distinct in every paragraph that turns on
  this: what the report states, what a separate primary source found, and
  your own synthesis connecting them. A reader should be able to tell, sentence
  by sentence, which one they are reading. Do not let a summary of the report
  blur into a claim about the world.
- When you give OpenAI's own stated reason for withholding detail, quote it
  and stop. Do not extend the quote into a motive ("because they wanted to")
  the sentence didn't earn. Attribute the reasoning to the report; do not
  supply the report's psychology.
- Balance is a sentence-level habit, not a closing caveat. Put one thing the
  report gets right next to the thing it fudges in the same stretch of prose,
  each with its own citation, so the fairness is visible in the structure and
  not asserted in a summary line.
- Let a named, sourced voice or a specific quoted line carry the harder
  judgments instead of the writer's own adjectives. The document's own
  sentence, quoted plainly, does more work than a writer calling it evasive.
- Prefer the concrete unit of evidence (the report's own sentence, a specific
  table entry, a specific percentile) over a general description of the
  document's posture ("OpenAI has been secretive"). Secrecy is a pattern the
  reader assembles from particulars you show them, not a label you hand them.

Recently used, do not reuse: no colon-subtitle headline; no hedged-contrast
dek (X is not Y, it is Z); no three-scenario cold open; no retired Verdict
block; do not open by narrating the document's fame in generic terms.

---

## Katharine Sanderson, "GPT-4 is here: what scientists think"
Source: https://www.nature.com/articles/d41586-023-00816-5
Craft:
- cadence: Short scene-setting opener, then a fast handoff to sourced voices.
  Each paragraph carries one named speaker and one claim; the piece never
  editorializes in its own voice for more than a sentence before returning to
  a quote.
- argument: Built entirely from attributed statements arranged for contrast:
  excitement from one researcher, frustration from another, on the same page,
  neither softened to make room for the other.
- evidence: Every judgment is pinned to a name and a title ("Sasha Luccioni,
  a research scientist specializing in climate at HuggingFace"), so the
  reader can weigh the source, not just the claim.
- stance: Fair by construction. The piece includes a red-teamer who found the
  model genuinely useful right beside a scientist who calls closed models "a
  dead end," and does not referee between them.
- notice: The frustration is not with GPT-4's abilities but with what cannot
  be checked: "You don't know what the data is. So you can't improve it."
  The piece keeps returning to that specific gap, not to secrecy in general.
- diction: Plain, no jargon left unglossed; technical terms (red-team,
  hallucinate) are defined in the clause where they first appear.
- reader: Treated as someone who wants to know what practitioners actually
  think, not what the writer thinks of practitioners.
- the move the axes miss: the headline judgment ("essentially dead ends in
  science") is never the writer's sentence. It is always someone else's,
  quoted exactly, which is what keeps the piece reporting rather than arguing.
Calibration: "All of these closed-source models, they are essentially dead
ends in science... for the community at large, it's a dead end."

## Timothy B. Lee, "Why it's getting harder to measure AI performance"
Source: https://www.understandingai.org/p/why-its-getting-harder-to-measure
Craft:
- cadence: Measured and conversational; short declarative sentences anchor
  longer explanatory ones, and each section deepens the same problem rather
  than introducing a new one.
- argument: A lifecycle structure — a benchmark works, then saturates, then
  the replacement benchmark shows its own new limitation. The structure
  performs the point: measurement keeps failing to keep up with capability.
- evidence: Specific numbers doing the work (a task completion time, a
  confidence interval), each tied to a named source or study, never offered
  as color.
- stance: Neither dismissive of the concern nor alarmed by it; treats a
  genuine measurement problem as worth explaining slowly rather than
  resolving quickly.
- notice: The inversion that when models start solving the hardest
  benchmark tasks, the tool measuring them gets noisier, not more precise, so
  the noise itself becomes evidence of progress.
- diction: Plain phrasing carries technical content ("gets a little crazy
  when it saturates") instead of a term of art standing in for an explanation.
- reader: Addressed as informed but not a practitioner; jargon is named and
  translated in the same breath ("In industry jargon, MMLU has saturated").
- the move the axes miss: he never announces that the number is misleading;
  he shows the specific mechanism (score compression near the ceiling) that
  makes it misleading, so the reader reaches the conclusion a beat ahead of
  being told it.
Calibration: "In industry jargon, MMLU has saturated."

## Melanie Mitchell, "Thoughts on a Crazy Week in AI News"
Source: https://aiguide.substack.com/p/thoughts-on-a-crazy-week-in-ai-news
Craft:
- cadence: Builds through a sequence of specific claims, each one checked in
  turn, before the piece widens to what the pattern means.
- argument: Separates what a paper asserts from what it can be shown to
  demonstrate, then asks a third question: could an outside reader verify
  it at all. That third question is the one most critiques skip.
- evidence: Names the specific access problem rather than gesturing at
  "lack of transparency" — no version of the model, no training data,
  therefore no way to rerun the experiment.
- stance: A working scientist's skepticism, applied evenly. She holds her
  own reluctance to the same bar she holds the hype, asking whether she
  herself is "putting my head in the sand."
- notice: That a result can be honestly obtained and still not support the
  size of claim being built on it, because the size of a claim depends on
  who else can check it.
- diction: Direct, occasionally wry, never hedged into vagueness; a strong
  verb ("un-probe-able") replaces a paragraph of qualification.
- reader: A thinking peer being walked through a chain of reasoning, not
  handed a verdict.
- the move the axes miss: she indicts the claim's unfalsifiability, not the
  authors' honesty. The critique never becomes about motive, only about what
  a reader outside the building can and cannot confirm.
Calibration: "The experiments described in the paper are unreproducible and
un-probe-able, since researchers outside Microsoft or OpenAI don't have
access to either the version of GPT-4 that was tested, or data used to train
it."
