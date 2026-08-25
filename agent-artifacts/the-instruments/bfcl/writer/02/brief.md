# writer brief: the-instruments/bfcl (02)

Single-owner repair. Apply the editor's one blocking item using the new
evidence; change nothing else the editor already settled.

Inputs:
- editor/01/editorial-review.md (artifact root): the Required work items. The
  editor already fixed the dek label and split a citation directly in the
  article; your job is only the remaining s5 / secondary-source item.
- researcher/02/evidence.md: the repaired secondary source, its verified
  passage, and a fully-verified fallback (option b).
- The current article (with the editor's edits in place):
  .nb-work/the-instruments/bfcl/library/the-instruments/bfcl.html
- editorial-direction.md and writer/01/brief.md for the standing rules.

Output: agent-artifacts/the-instruments/bfcl/writer/02/draft-handoff.md
(add one line per editorial request resolved; do not overwrite writer/01).

Proof (from /home/user/the-nightly-build; final with links):
  ./nb check .nb-work/the-instruments/bfcl/library/the-instruments/bfcl.html \
    --series the-instruments \
    --library /tmp/claude-0/-home-user-the-nightly-build/795ad1d0-7e30-55f8-9f00-32962f849f5d/scratchpad/library-checkout
Run `./nb stamp` before the final check. Drive to BLOCK: 0.

The fix:
- The framing sentence's truth rests on the primary (ICML paper) already
  cited in the same paragraph. Prefer the cleaner option b from
  researcher/02: keep the claim on the primary and attach the single secondary
  to what it genuinely and durably supports. If you instead use the new
  "agentic chasm" analysis (s5'), note it carries no named author, so cite it
  only as an outside overview that echoes the shape (a repetition), never as
  the owner of a figure or of the claim's truth.
- Keep exactly one legitimate secondary so the >=1-secondary composition floor
  holds. Preserve first-citation source numbering order; renumber only if the
  swap requires it, and keep data-nb-kind labels honest.
- Do not expand the claim set or touch settled prose beyond this citation fix.
