# writer brief: what-could-go-wrong/ai-moral-status (02) — revision

Inputs:
- editorial-direction.md (house standard, the paper's voice, the What Could Go
  Wrong prompt: original documents, no company as an authority)
- writing-coach/01/voice-guide.md (unchanged)
- researcher/02/evidence.md (the NEW evidence record — supersedes 01; see the
  updated source 6 / Birch entry and its CAUTION)
- editor/01/editorial-review.md (apply its Required work → writer item)
- writer/01/draft-handoff.md
- library/what-could-go-wrong/ai-moral-status.html (the article — it ALREADY
  carries the editor's own two direct edits; build on them, do not revert)
- .nb-context/

Output: writer/02/draft-handoff.md
Article: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/ai-moral-status/library/what-could-go-wrong/ai-moral-status.html
Proof: ./nb check .nb-work/what-could-go-wrong/ai-moral-status/library/what-could-go-wrong/ai-moral-status.html --series what-could-go-wrong --library /home/user/library-checkout

## Apply exactly the one required change — nothing wider
The editor's block: source 6 (Birch, *The Edge of Sentience*, gaming problem) had
an href that resolved to a marketing page, not the chapter, and the concept had
been read only via source 1. researcher/02 has now resolved this: the book is
open access and Birch's own gaming-problem definition is established firsthand
from the chapter's authoritative published abstract. So s6 is legitimate — fix
the citation, keep the count at 8, do not re-cite to s1.

Do exactly this:
1. Update the source 6 entry's URL to the canonical, resolvable chapter address
   the record gives: the chapter DOI `https://doi.org/10.1093/9780191966729.003.0017`
   (resolves to the Oxford Academic chapter page). Update any `data-nb-url`/href
   for s6 accordingly.
2. Confirm the article cites s6 only for what the record establishes firsthand:
   the gaming-problem CONCEPT and its remedy (deep computational markers, not
   behavioural markers; the "sentience candidate" idea). Do NOT attribute to
   Birch any page-specific body quotation beyond that abstract wording — if the
   draft has one, recast it to the concept as the record supports, or cut it.
3. Preserve the editor's two direct edits and all other settled work.

Run the full proof with links. If the DOI href fails the link check because the
open-access host is behind a bot-verification wall (a 403/paywall is gated, not
dead — record the address where the source lives), try the alternate open-access
addresses the record lists (the OAPEN book page or the PhilArchive PDF) and use
whichever resolves for the checker while still being the source's own page. If
none resolve for the automated checker, keep the canonical DOI and report that
clearly so the orchestrator can decide.

Then re-run the display-text self-test, nb stamp, and the full proof until
BLOCK: 0. Write writer/02/draft-handoff.md: the s6 URL you landed on and why, how
you confirmed the Birch citation is concept-only, the proof result, and any open
question.
