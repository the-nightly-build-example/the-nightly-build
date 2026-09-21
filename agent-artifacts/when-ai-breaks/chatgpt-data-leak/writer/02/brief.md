# writer brief: when-ai-breaks/chatgpt-data-leak (02) — CI link repair only

Inputs:
- ../01/draft-handoff.md — the approved draft's original-work sentence and notes
- ../../editor/01/editorial-review.md — the approving review (no prose changes are owed)
- ../../researcher/01/evidence.md — what each Garante document establishes
- ../../../../library/when-ai-breaks/chatgpt-data-leak.html — the article to edit in place
Output: ./draft-handoff.md
Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/when-ai-breaks/chatgpt-data-leak/library/when-ai-breaks/chatgpt-data-leak.html --series when-ai-breaks --repo /home/user/the-nightly-build

Scope: a link-resolution fix ONLY. Do not change prose, claims, structure, headings, the dek, source kinds, or which documents are cited. The editor already approved the content.

The problem: four cited sources point at `www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/<ID>` pages. That site serves a hard HTTP 404 to script clients (urllib) from GitHub's CI runners, so the proof's link checker marks all four B-SOURCE-DEAD and blocks the Article PR (CI run showed BLOCK: 4). The pages are real and readable in a browser; only automated probes from CI get the 404. The checker blocks only on 404/410 or a non-resolving domain; a 200 or a 403 never blocks.

The fix: replace each of the four Garante source `href`s (and any matching `data-nb-url`) with a Wayback Machine snapshot of the exact same Garante page, so CI's checker reaches a resolvable address. A real snapshot returns 200 (or a non-blocking 403); only a missing snapshot 404s, so every replacement must be a snapshot that actually exists and captured the real document.

The four docweb IDs and the snapshots already found (verify each still resolves; a plain urllib probe must not get 404/410):
- 9870847 → http://web.archive.org/web/20260904190957/https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9870847
- 10085432 → http://web.archive.org/web/20260917130924/https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10085432
- 9881490 → http://web.archive.org/web/20260831071752/https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/9881490
- 9870832 → NO snapshot found via the availability API. Create one with web.archive.org/save using the pre-installed Chromium/Playwright browser (PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers; do not run `playwright install`), then confirm the captured snapshot shows the actual 30 March 2023 Garante order (docweb 9870832) — its grounds (legal basis for training data, information notice, data accuracy, age verification), not a bot 404 page.

Verify, before swapping, that each chosen snapshot renders the same document the citation makes claims about (open it in the browser and confirm the content). Keep the source kind (primary — an archived copy of the Garante's own page is the same primary) and the citation label unchanged. In `draft-handoff.md`, record only the four address swaps and confirmation each snapshot shows the right document.

If 9870832 cannot be archived cleanly (the crawler captures a 404 or the wrong page), do NOT substitute a different document for the claim — stop and report exactly that back to the orchestrator.

Then run the exact proof above with links until BLOCK: 0 (one W-SENTENCE-DENSITY warning on a verbatim quotation is expected and non-blocking).
