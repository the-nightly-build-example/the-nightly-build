# writer brief: what-could-go-wrong/lethal-trifecta (02, revision)

Apply the required items in editor/01/editorial-review.md. Both are writer-owned citation
fixes; the editor already made its prose edits in place. Change nothing else except what these
items logically require.

Inputs:
- editor/01/editorial-review.md (the review to apply; its Required work section is the task)
- researcher/01/evidence.md (the claim set and the owning sources)
- editorial-direction.md (citation standard)
- the article at library/what-could-go-wrong/lethal-trifecta.html (already carries the editor's prose edits)

The two required fixes:
1. s2 (Invariant) misquote: the article prints "GitHub alone cannot resolve through
   server-side patches"; the source reads "GitHub alone cannot resolve this vulnerability
   through server-side patches." Restore the dropped words, or mark the elision with an
   ellipsis without changing the meaning.
2. EchoLeak "a crafted email was enough": this is cited to s3 (the CVE), but the CVE
   establishes only the no-interaction rating ("over a network"), not the email delivery
   channel. The email vector is owned by Willison's EchoLeak post (s4). Re-cite to the source
   that establishes it, or recast the sentence so the cited source supports exactly what it
   claims.

Output: writer/02/draft-handoff.md (one line per item resolved).

Proof (run from /home/user/the-nightly-build), to BLOCK: 0 with links:
  ./nb stamp .nb-work/what-could-go-wrong/lethal-trifecta/library/what-could-go-wrong/lethal-trifecta.html
  ./nb check --series what-could-go-wrong --library /home/user/library-checkout .nb-work/what-could-go-wrong/lethal-trifecta/library/what-could-go-wrong/lethal-trifecta.html

Do not independently expand the claim set or re-edit settled prose. Rerun the complete proof.
