# Voice guide — when-ai-breaks/google-flu-trends

Register: plain, factual, unhurried. Report the sequence like an investigator
retracing what happened, not like a prosecutor building a case. The reader
already believes the success story; your job is to walk them, step by
verifiable step, to the place where it stopped being true, then hand them the
mechanism as something they now understand rather than something they were
told.

Moves that will change sentences in this article:

- Open on a single concrete moment of discovery, not a claim. Someone
  compares a number to another number and the gap is the story: a CDC report
  lands next to a GFT estimate, or Lazer's tally of overshot weeks. State the
  comparison plainly before you name what caused it. Withhold the mechanism
  until the reader has felt the gap.
- Write the mechanism as a causal chain, one link per sentence: this changed,
  which meant this stayed fixed, which meant this drifted. Do not summarize
  the feedback loop in one abstract sentence ("the model and the world
  influenced each other"). Show the specific chain: media covers flu, media
  coverage drives flu-word searches independent of illness, the model was
  trained to treat those searches as illness signal, so the signal now
  answers a different question than the one it was fit on. Name each actor
  in the chain (Google's algorithm, the CDC's lagged reports, the search
  terms themselves) so the loop has moving parts, not a label.
- Build the ~2x figure the way a precise number earns its place: state the
  baseline first (what CDC later measured), then the GFT figure, then the
  ratio, once, in a single clean sentence. Do not restate the ratio as a
  refrain. One earned number beats three approximate mentions of it.
  Stack figures so each new one is comparable to the last (weeks overshot,
  out of weeks measured; seasons trained on, out of seasons available), never
  a number that arrives without something to measure it against.
- Locate the failure in the design and the assumptions, not in a villain.
  Ginsberg's team is not the target; the target is what a model like this
  cannot know about itself while it is running. Keep blame off individuals
  even where a choice reads clearly wrong in hindsight; the point is that the
  system had no way to notice its own drift, which is the transferable
  lesson.
- Where Google's account and Lazer's critique disagree, give each its
  strongest form in its own sentences before you weigh them. Say plainly
  where the record does not settle it, rather than smoothing the disagreement
  into a single balanced-sounding sentence.
- For the closing turn to where this lives today, do what a chain of named,
  concrete instances does better than a general claim: name the actual
  system, name what its frozen relationship is, name what in the world moves
  under it. Two or three real ones beat one abstract sentence about "systems
  like this."
- Vary sentence length by function: short sentences to land a fact or a
  number, longer ones only when tracing a causal chain that must stay in one
  breath to keep the order clear. Never lengthen a sentence to sound
  authoritative.

Recently used, do not reuse: the victim-harm cadence of recent
when-ai-breaks headlines (a name plus a bodily injury) — this failure's harm
is epistemic, a wrong number treated as true, and should read as exactly
that scale of harm, not inflated toward physical stakes. No colon-subtitle
headline. No hedged-contrast dek ("X is not Y; it is Z" or its cousins). No
scenario-triad open (stacking three illustrative cases before the real one).
Also avoid the zillow-offers/epic-sepsis-model shape of centering the
overfitting alone; this piece's distinctive engine is the feedback loop
(media and Google's own algorithm changing the inputs underneath a frozen
model), so the causal chain should foreground that, not just "the model was
overfit."

## Kim Zetter, "How Digital Detectives Deciphered Stuxnet, the Most Menacing Malware in History"
Source: https://www.wired.com/2011/07/how-digital-detectives-deciphered-stuxnet/
Craft:
- cadence: short declaratives to open a scene, then sentences lengthen as
  investigators accumulate detail, then short again to land a finding.
- argument: builds by withholding. The reader learns the mystery (centrifuges
  vanishing at an abnormal rate) before any explanation, and the explanation
  arrives only as the researchers themselves earn it.
- evidence: dated, attributed findings from named researchers (Falliere,
  Chien, Langner), each credited with the specific piece of the puzzle they
  solved, in the order they solved it.
- stance: reports the technical unraveling as a detective story without
  editorializing; judgment appears late and only after the evidence supports
  it ("the consensus is that it failed").
- notice: uses one concrete analogy to carry a hard technical idea — the
  malware masking its own commands is explained as a heist film's looped
  camera feed, not as protocol description.
- diction: plain nouns for technical objects (a PLC is "essentially small
  computers, generally the size of a toaster") defined the moment they
  appear, then reused exactly.
- reader: assumes intelligence, not expertise; every acronym is cashed out in
  one clause before the story moves on.
- the move the axes miss: it ends without full resolution. Two encrypted
  files are still uncracked, the cost-benefit is called into question rather
  than settled, and the piece states this as fact rather than smoothing it
  into a tidy close.
Calibration: "The question was, why? Iran wasn't required to disclose the
reason for replacing the centrifuges and, officially, the inspectors had no
right to ask."

## Doug Seven, "Knightmare: A DevOps Cautionary Tale"
Source: https://dougseven.com/2014/04/17/knightmare-a-devops-cautionary-tale/
Craft:
- cadence: opens with the scale of the outcome in one sentence before any
  cause is given, then moves in dated, numbered steps toward the mechanism.
- argument: each paragraph adds exactly one fact the next paragraph needs;
  the reader always has what the next sentence assumes.
- evidence: cites the SEC filing directly and quotes its exact language
  rather than paraphrasing the regulator's finding.
- stance: refuses to blame the technician even while naming the exact human
  error, and states directly why: "the process...was not appropriate for the
  risk they were exposed to."
- notice: stacks numbers so each is legible against the one before it ($365
  million in cash, then a $460 million loss, then 45 minutes) so the reader
  always has a comparison, never a bare figure.
- diction: plain, almost procedural language for what should have been
  routine ("the update was intended to replace old, unused code"), which
  makes the eventual failure land harder by contrast.
- reader: a practitioner who has deployed software, addressed without
  jargon overload; every system term (SMARS, Power Peg) is defined in the
  sentence that introduces it.
- the move the axes miss: it narrates the response as it happened, including
  the mistake made while trying to fix the mistake (removing the working
  code instead of the broken code), rather than skipping straight to the
  clean postmortem version.
Calibration: "During the first 45-minutes of trading Knight's executions
constituted more than 50% of the trading volume, driving certain stocks up
over 10% of their value."

## Dan Luu and Yao Yue, "A decade of major cache incidents at Twitter"
Source: https://danluu.com/cache-incidents/
Craft:
- cadence: dense, clause-by-clause causal sentences during the mechanism,
  broken by one short sentence that closes a phase ("The total time for
  everything combined was about two months.").
- argument: treats the general failure class (a feedback loop that becomes a
  runaway feedback loop) and the specific incident as two things to hold at
  once, moving between them rather than picking one register.
- evidence: quotes the engineer's own contemporaneous ticket comment instead
  of restating the finding in the authors' words.
- stance: openly flags what it does not know ("the fix was never widely
  rolled out for reasons that are unclear") instead of papering over a gap in
  the record.
- notice: tracks second-order failures, where the fix for one incident
  caused or masked another, and states that pattern as a named lesson rather
  than letting it sit implicit in the timeline.
- diction: technical terms (shard, ejection, IRQ affinity) are used exactly
  once introduced and never swapped for a synonym, even across a long
  passage.
- reader: technically literate but not assumed to know this system, so every
  piece of internal vocabulary gets one clause of plain definition on first
  use.
- the move the axes miss: it names the abstraction (feedback loop, death
  spiral) before or after the concrete instance, never instead of it, so the
  reader gets both the general mechanism and the specific case that
  instantiates it.
Calibration: "It turned out that hosts with this BIOS version were
triggering the BMC to run a very expensive health check every 20 hours and
40 minutes which interrupted the kernel for the duration, preventing any
packets from being processed, causing packet drops."
