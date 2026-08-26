# writer brief: what-could-go-wrong/eliciting-latent-knowledge (01)

Inputs:
- `editorial-direction.md` (artifact root) — house standard, press voice, series prompt.
- `writing-coach/01/voice-guide.md` — how this piece should sound, with exemplar passages.
- `researcher/02/evidence.md` — the complete claim set (supersedes 01; 02 adds the required secondary source and is the record to draft from); draft only from what it opened.
- The initialized article: `.nb-work/what-could-go-wrong/eliciting-latent-knowledge/library/what-could-go-wrong/eliciting-latent-knowledge.html` — edit in place; do not recreate the skeleton.
- Effective template contract and furniture catalogs under `.nb-work/what-could-go-wrong/eliciting-latent-knowledge/.nb-context/`.

Output: `.nb-work/what-could-go-wrong/eliciting-latent-knowledge/agent-artifacts/what-could-go-wrong/eliciting-latent-knowledge/writer/01/draft-handoff.md` (and the edited article in place).

Proof (run from repo root `/home/user/the-nightly-build`):
`./nb check --series what-could-go-wrong --library /home/user/library-checkout .nb-work/what-could-go-wrong/eliciting-latent-knowledge/library/what-could-go-wrong/eliciting-latent-knowledge.html`
Iterate with `--no-check-links`; run the full command (links on) to `BLOCK: 0` before handing off. Run `nb stamp` on the article before the final check.

Evidence caveats you must respect (from the record):
- The central live tension is Burns et al. (CCS, the one empirical toe-hold, +4% avg over zero-shot) versus Farquhar et al. (CCS tracks the most salient feature, not truth). Present both; do not resolve it in CCS's favor.
- Some load-bearing quotes in the record are flagged "verify verbatim." Use a direct quotation only where the exact wording is the evidence and the record marks it confirmed; otherwise paraphrase and cite. Keep quotations minimal — the editor re-opens every citation.
- Keep reported fact, the authors' projection, and your synthesis distinct. ELK's strong claim ("we will not be able to tell what a superhuman AI knows") is a projection about systems that do not exist yet; say so.

Set the nb-meta writer model field to `claude-opus-4-8`.

Recent WCGW habits to break (do not inherit; the last three pieces were
concentration-of-power, algorithmic-monoculture, natural-selection):
- The opener mold "When people warn that X, they are pointing at something real and something imagined in the same breath. This lesson takes the most careful version..." — find a different way in.
- The why-bookend closer "By the end you will be able to..." — vary it.
- The takeaway staccato "X is here. Y is here. Z is not." and the closer phrasing "how worried to be tracks that one gap" — do not reuse either shape.
- The "the line cuts both ways / the booster... the dismisser..." device for weighing over- and under-confidence — make that contrast in a different sentence shape.
- Do not title a present-day section "Who makes the case now" verbatim.
- The phrase "doing the work" ("X, not Y, is doing the work") is a house tic across recent pieces; do not use it.
Name your one original-work sentence in the handoff.
