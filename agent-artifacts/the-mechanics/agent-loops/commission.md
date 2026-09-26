# Commission: the-mechanics/agent-loops

## The behavior

An AI agent gets stuck repeating the same failed step. A coding agent reruns the
command that just errored; a browsing agent clicks the same dead link; an
autonomous agent retries the same broken approach turn after turn instead of
trying something else. Anyone who has watched an agent (a coding assistant, a
browsing agent, an AutoGPT-style runner) work for more than a few minutes has
seen it. This desk starts from one behavior and works backward to its cause.

## The assignment

Work backward from the loop to the mechanism, step by step. Each step names a
real part of the system and what it does, in plain words, with a small concrete
example where one makes the step land. Keep going until the reader hits ground:
a step below which nothing would change the answer. Mark which steps are settled
engineering and which are open questions even for the people who build these
systems. No code listings; explain the loop in prose, a numbered-steps
component, or a table.

The cause chain to teach (reach ground, do not stop early):
1. What an agent is: a language model in a loop. The model proposes an action,
   a harness outside the model executes it, the result is written back into the
   context as text, and the model is called again. (Link the-mechanics/tool-use
   and the-evidence/react-reasoning-and-acting; do not re-teach how one call
   works.)
2. The model is stateless between calls: each call re-reads the whole transcript
   and produces the next action from it. Its only memory of what it has already
   tried is whatever is written in that transcript. (Link
   the-mechanics/conversation-memory and the-mechanics/hangman; do not
   re-teach.)
3. The next action is the most probable continuation of that transcript. If the
   transcript still points at the same goal and the same apparent best action,
   the model re-derives the same action. An error appended to the context is
   weak evidence against a strong prior, and models frequently continue rather
   than revise on it.
4. Nothing in the base loop forces exploration or tracks a "already tried, do
   not repeat" list. Sampling temperature adds noise, not strategy (link
   the-mechanics/sampling-temperature).
5. The loop reinforces itself: repeated near-identical failed turns fill the
   context, and a transcript that shows the assistant trying the same thing
   makes trying it again the most in-pattern next move. Name the token-level
   cousin and draw the line to it (link the-mechanics/repetition-loops: that is
   decoding-level; this is action-level).
6. Ground: the agent re-conditions on a context that keeps making the same
   action most likely, and the harness keeps executing it. Below "the model
   predicts the next action from the transcript and the harness runs it,"
   nothing changes the outcome.

Then: what actually breaks the loop, and why that tells you where the cause sits
(explicit memory of attempts, a reflection/critique step, loop detection in the
harness, forcing a different action, a human interrupt). Mark clearly what is
settled (the architecture and that scaffolding helps) versus open (why models
under-weight their own error feedback; whether models can reliably self-correct
without an external signal).

## The one thing this article does that the sources do not

Put the loop where it belongs, in the plain architecture of an agent (a
stateless predictor re-reading a transcript and a harness executing what it
says), so the reader can see that the loop is not a bug in one product but the
default of the design, and can tell a real fix (changing the context or the
harness) from a cosmetic one (retrying, nudging, raising temperature).

## Angle refinement (post-research, orchestrator decision)

The record holds the angle (looping is the default of the stateless-predictor-
plus-harness design, not a one-product bug), with these refinements the writer
must draft to and must not overstate:

1. Do not round Huang et al. 2023 to "models cannot self-correct." The precise
   finding: with an external or oracle signal, self-correction improves accuracy;
   intrinsic self-correction (no external signal) often fails to help or
   degrades it. The loop is about the quality of the feedback signal, not an
   inability to revise in principle. Say it that way.
2. Statelessness is not the sole cause. ReAct's own authors (footnote 6)
   attribute part of the looping to greedy decoding, which is decoding-level and
   harness-addressable. So the honest framing is: the design makes looping the
   default, and decoding choices contribute. Draw the line to
   the-mechanics/repetition-loops precisely (some action-level looping shares the
   decoding-level cause), rather than declaring the two fully separate.
3. The "ground" proposition (below "the model predicts the next action from the
   transcript and the harness runs it," nothing changes) is the lesson's own
   synthesis, presented as its reasoning, not attributed to a single paper. The
   "temperature is noise, not strategy" point is taught in
   the-mechanics/sampling-temperature; link it and present it as synthesis.
4. Mark as an open question: why models under-weight their own error feedback.
5. Concrete example: lean on SWE-agent's described failure (an errant edit
   introduces a syntax error, then the agent repeatedly edits the same snippet;
   the failed-edit statistic; the edit-linting guardrail that helps). The
   AutoGPT user-log instance is vivid but a single unreplicated report; use only
   with that caveat, if at all.
6. If you mention a harness loop cap, use a current, correct number with its
   version caveat (LangGraph's default recursion limit is 1000 super-steps as of
   v1.0.6, not the older 25). Better to make the point without a fragile number.

## Boundaries — do not re-teach taught ground

Link at first use; do not re-teach:
- the-mechanics/tool-use — how a single tool call works (model writes text, a
  program runs it, result comes back).
- the-evidence/react-reasoning-and-acting — the reason-act loop as a paper.
- the-mechanics/conversation-memory, the-mechanics/hangman — statelessness / the
  transcript as the only memory.
- the-mechanics/repetition-loops — decoding-level looping; name the contrast.
- the-mechanics/sampling-temperature — why noise is not strategy.
- the-mechanics/losing-the-thread and lost-in-the-middle — context growth and
  the model attending unevenly to a long transcript; link if used, do not
  re-teach.
Teach any genuinely missing piece on the spot, briefly.

## Sources (the-mechanics policy: min 8, primary >=4, secondary >=1)

Primary should include papers that document agent failure/looping and the
mechanisms behind self-correction: ReAct (Yao et al. 2022); Reflexion (Shinn et
al. 2023); Huang et al. 2023 "Large Language Models Cannot Self-Correct
Reasoning Yet"; and an agent-evaluation or failure-analysis primary (e.g.,
Kapoor et al. 2024 "AI Agents That Matter"; AgentBench, Liu et al. 2023; or
SWE-bench/SWE-agent). A documented concrete loop instance (from a paper's error
analysis or a well-attested public report) is required so the example is real,
not invented. Cite figures to the document that owns them.

## Recent shapes to break (compare against the recent library)

- Do not default to the "You have probably ..." opener or the "By the end you
  will know A, B, and C" closer.
- Check the dek and headings against recent the-mechanics pieces (hangman,
  answer-length-bias, false-premise-questions, output-diversity). Recent
  mechanics deks often state the mechanism as a compact causal sentence; make
  this one its own, not a copy of hangman's shape.

## Production record

Profile balanced. Models "capable" for all roles. Effort targets: researcher
high, writer medium, editor high, writing-coach low. Roles run as isolated
subagents on a capable model (Claude Opus-class); per-role reasoning-effort not
separately dialed in this harness (recorded deviation). No `required` directive
traded down.
