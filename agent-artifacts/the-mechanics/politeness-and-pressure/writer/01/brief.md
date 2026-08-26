# writer brief: the-mechanics/politeness-and-pressure (01)

Inputs:
- `editorial-direction.md` (artifact root) — house standard, press voice, series prompt.
- `writing-coach/01/voice-guide.md` — how this piece should sound, with exemplar passages.
- `researcher/01/evidence.md` — the complete claim set; draft only from what it opened.
- The initialized article: `.nb-work/the-mechanics/politeness-and-pressure/library/the-mechanics/politeness-and-pressure.html` — edit in place; do not recreate the skeleton.
- Effective template contract and furniture catalogs under `.nb-work/the-mechanics/politeness-and-pressure/.nb-context/`.

Output: `.nb-work/the-mechanics/politeness-and-pressure/agent-artifacts/the-mechanics/politeness-and-pressure/writer/01/draft-handoff.md` (and the edited article in place).

Proof (run from repo root `/home/user/the-nightly-build`):
`./nb check --series the-mechanics --library /home/user/library-checkout .nb-work/the-mechanics/politeness-and-pressure/library/the-mechanics/politeness-and-pressure.html`
Iterate with `--no-check-links`; run the full command (links on) to `BLOCK: 0` before handing off. Run `nb stamp` before the final check.

No code in this article. Work backward from the behavior to its cause, marking each
step as settled engineering or open question.

Evidence caveats you must respect (from the record):
- Confirmed figures are safe to use (e.g. Yin et al. GPT-3.5 MMLU 60.02 / 59.44 / 51.93 across polite/neutral/impolite). Some exact decimals were summary-sourced and are flagged approximate — prefer stating the direction and rough size over a shaky decimal, and never present an unverified decimal as exact.
- The steelman (EmotionPrompt's large BIG-Bench gain; Bsharat's tip/penalty principles) runs on 2023-era or small models; address it as the strongest counter-evidence and weigh it. The cross-source pattern is that the effect shrinks as models get stronger, and at least one study ("Mind Your Tone") reverses the sign on GPT-4o. Keep reported fact, estimate, and your synthesis distinct.
- The settled half: output is a prediction conditioned on all the prompt's text, so tone/stakes shift it. The open half: no specific trick reliably produces the claimed improvement on modern models. Do not overclaim either.

Set the nb-meta writer model field to `claude-opus-4-8`.

Recent Mechanics habits to break (do not inherit; the last three pieces were
text-in-images, first-token-latency, false-confidence):
- The opener mold "You [do a small thing], and [the failure]. This is the one failure everyone notices... This lesson takes a single X and traces it back... By the end you can..." — find a different way in, and do not use "By the end you will/can...".
- The device "It is tempting to say X. That goes too far." — do not use it.
- Do not close the takeaway on a posed diagnostic question ("Is the model failing to X, or failing to Y?"); the last Mechanics piece already ended that way.
- The phrase "doing the work" ("the framing, not the content, is doing the work") is a house tic across recent pieces; do not use it.
Name your one original-work sentence in the handoff.
