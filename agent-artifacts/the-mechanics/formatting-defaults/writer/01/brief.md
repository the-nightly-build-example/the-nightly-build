# writer brief: the-mechanics/formatting-defaults (01)

Inputs (under the article's agent-artifacts root unless noted):
- `editorial-direction.md` — house standard, paper voice, lesson identity, series prompt.
- `writing-coach/01/voice-guide.md` — how this piece should sound, with exemplars.
- `researcher/01/evidence.md` — the complete claim set. Draft only from it.
- Article to edit: `.nb-work/the-mechanics/formatting-defaults/library/the-mechanics/formatting-defaults.html` (initialized from the lesson template).
- Template context: `.nb-work/the-mechanics/formatting-defaults/.nb-context/`.

Output: `.nb-work/the-mechanics/formatting-defaults/agent-artifacts/the-mechanics/formatting-defaults/writer/01/draft-handoff.md`

Proof: `./nb check .nb-work/the-mechanics/formatting-defaults/library/the-mechanics/formatting-defaults.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/4555dd06-1325-5643-8ae1-70035fc82956/scratchpad/library-checkout`
(Use `--no-check-links` while iterating; run the full command, links included, until `BLOCK: 0`. Run `nb stamp` before the final check.)

This round's focus, from the evidence record:
- The chain must be marked honestly at each link. Settled: preference tuning and LLM-judges reward structure and length substantially independent of correctness (numbers exist); the markdown default is a learned, steerable policy, shown by lab docs (OpenAI Model Spec's interactive-markdown default; Anthropic's published system prompts suppressing lists/headers). Open/undisclosed: the pretraining contribution (no dedicated primary; inferred from autoregressive mechanics) and the exact formatting makeup of instruction-tuning data. The mechanics desk requires marking which steps are settled engineering and which are open — do this explicitly.
- One precision the record insists on: length dominates markdown once both are controlled (length coefficient ~0.249 vs ~0.019–0.031 per markdown element in the LMSYS style-control analysis); much of the raw "bullets win" effect is length riding along. Frame it as structure-and-length together, length the heavier half, and say "substantially content-independent," not "wholly content-free" — LMSYS calls its own analysis observational.
- End at ground: the format is a learned output policy, not a task requirement, which is why an instruction or system prompt turns it off. No code.

Reach the reader's own terms: work backward from the visible bulleted-list/bold-header answer to tokens sampled one at a time (link the-mechanics/autoregressive-generation), then instruction tuning, then preference tuning. Link the-instruments/chatbot-arena-elo for the style-vote result and the-mechanics/sycophancy and the-evidence/instructgpt for preference tuning rather than re-teaching them.

Recent the-mechanics habits not to inherit:
- Differentiate hard from the-mechanics/prompt-sensitivity (input formatting changing accuracy). This piece is output formatting and its origin; link it, do not echo its framing.
- Avoid the recurring "X is all the system ever does" opener/closer shape (image-generation) and the single-mechanism "the behavior is really just Y" reveal — this behavior has several contributing stages, so do not flatten it to one cause.
- Vary dek and heading construction; recent deks state a mechanism as one plain surprising fact. Fine to be plain, but build the dek in this piece's own nouns and do not stamp a mold.

Original work: name in one sentence, in draft-handoff.md, what this article does to the evidence that the evidence does not do itself.
