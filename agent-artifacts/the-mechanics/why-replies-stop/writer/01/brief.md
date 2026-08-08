# writer brief: the-mechanics/why-replies-stop (01)

Inputs:
- .nb-work/the-mechanics/why-replies-stop/agent-artifacts/the-mechanics/why-replies-stop/editorial-direction.md — governing standard, headline standard, press voice, lesson identity, series prompt
- .nb-work/the-mechanics/why-replies-stop/agent-artifacts/the-mechanics/why-replies-stop/commission.md — subject, angle, required contribution, boundaries
- .nb-work/the-mechanics/why-replies-stop/agent-artifacts/the-mechanics/why-replies-stop/writing-coach/01/voice-guide.md — craft standard and licenses (state the trained behavior flatly; keep model and serving-layer as two named actors)
- .nb-work/the-mechanics/why-replies-stop/agent-artifacts/the-mechanics/why-replies-stop/researcher/01/evidence.md — complete claim set; use its Numbers/example exactly
- .nb-work/the-mechanics/why-replies-stop/library/the-mechanics/why-replies-stop.html — the initialized article to EDIT in place
- .nb-work/the-mechanics/why-replies-stop/.nb-context/ — effective contract, runtime assets, furniture catalogs

Output: .nb-work/the-mechanics/why-replies-stop/agent-artifacts/the-mechanics/why-replies-stop/writer/01/draft-handoff.md

Proof (from /home/user/the-nightly-build): iterate with
`./nb check .nb-work/the-mechanics/why-replies-stop/library/the-mechanics/why-replies-stop.html --series the-mechanics --library /home/user/library-checkout --no-check-links`
then `./nb stamp` and the same command WITHOUT `--no-check-links` until `BLOCK: 0`.

nb-meta: date `2026-08-08`, harness `claude-code-routine`, model `claude-opus-4-8`;
keep nb-meta `dek` identical to the rendered dekline.

Precision the evidence requires (the editor will check):
- Do NOT say base models "never stop" or "can't stop." Precisely: a base model
  emits a document-end token (e.g. Llama's `<|end_of_text|>`, Qwen's
  `<|endoftext|>`), just not a turn-end token at a helpful boundary; post-training
  teaches the turn-end token (Llama's `<|eot_id|>`, Qwen's `<|im_end|>`). State it
  that way.
- The two causes (the model samples a stop token vs a length cap truncates) are the
  MAIN case, not the whole enumeration. You may note in one clause that a serving
  API lists other stop reasons (refusal, context-window-exceeded, tool_use); do not
  pad the piece with them.
- The stop-token probability micro-example is a DEFENSIBLE ILLUSTRATION on a real
  documented readout method (HF `compute_transition_scores`), not a captured
  measurement. Label it as illustrative in the prose/caption; do not attribute the
  specific numbers (~0% -> ~3% -> ~92%) to a named model as measured fact.
- If you print a verbatim quote for the serving cap, use the Anthropic Messages API
  wording (verified in the record); re-read the Gemini page live before quoting its
  `finishReason` wording. Use `<code>` only for literal token strings the reader
  would match character-for-character (e.g. `<|eot_id|>`, `max_tokens`), not for
  ordinary terms.

Recent the-mechanics shapes to break: no "watch a product appear one line at a
time" table framing or that heading cadence; a small token/probability table may
serve the illustration. Link (plain prose link) to the-mechanics/autoregressive-
generation and the-mechanics/sampling-temperature rather than re-teaching next-token
prediction or sampling. No code.

This round's focus: the reader can say a reply ends either because the model sampled
a learned stop token or because a length cap truncated it, and can tell a natural
finish from a truncation.
