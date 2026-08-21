# writer brief: when-ai-breaks/arup-deepfake-fraud (01)

Inputs:
- Editorial direction: ../../editorial-direction.md — house standard, paper voice, series prompt.
- Voice guide: ../../writing-coach/01/voice-guide.md — how this piece should sound, with exemplar passages.
- Evidence record: ../../researcher/01/evidence.md — your complete claim set (add no facts it lacks). Read its Contradictions section carefully.
- The initialized article: ../../../../library/when-ai-breaks/arup-deepfake-fraud.html (edit; do not recreate the skeleton).
- Template context: ../../../../.nb-context/ — effective contract, furniture catalogs, runtime assets.

Output: ./draft-handoff.md (writer/01/draft-handoff.md)

Proof: run from repo root /home/user/the-nightly-build —
`./nb check .nb-work/when-ai-breaks/arup-deepfake-fraud/library/when-ai-breaks/arup-deepfake-fraud.html --series when-ai-breaks --library /tmp/claude-0/-home-user-the-nightly-build/b1bf3c94-3553-5519-8a12-b9ebb7eba930/scratchpad/library-checkout`
New slug; no `--revision`. Use `--no-check-links` while iterating; run it links-on until `BLOCK: 0`.

## IMPORTANT correction to the commission (from the researcher's record)

The authoritative primary — the Hong Kong government's Legislative Council reply
(LCQ9, 26 Jun 2024) — says the deepfake video conference was **pre-recorded**,
that there was **no real interaction** between the employee and the fraudster,
and that the instructions to transfer came **afterward, over instant messaging**.
So correct the commission where it says "interactive" and "a live video image was
the proof of identity":

- The honest account: the employee joined what looked like a live video meeting;
  the "colleagues" and "CFO" on it were pre-recorded deepfake video and audio, not
  a two-way conversation; the actual transfer instructions came by message.
- The popular reporting framed it as a live interactive call. The primary record
  is more specific. Tell the record's version, and you may note the gap between
  the widely-repeated "interactive call" story and what the government stated —
  that gap is itself worth the reader's attention.
- The general claim "real-time, two-way deepfakes are cheap and convincing
  enough" is defensible as an EMERGING capability (NSA/FBI/CISA 2023; Europol
  2022; Nightingale & Farid, PNAS 2022), but this incident is NOT clean proof of
  a two-way real-time video deepfake. Keep the capability claim and the incident
  claim separate; do not use Arup as proof of two-way real-time deepfaking.

The core lesson is intact: a convincing fake of colleagues the employee saw and
heard defeated the human identity check, and the defense is out-of-band
verification (call-backs, code words, authenticating the transaction not the
face), not detection.

## Verified figures (from the record; do not alter)

HK$200 million (~US$25.6 million); 15 transfers to 5 bank accounts; a single
finance employee in Arup's Hong Kong office; report lodged 29 Jan 2024; police
account from Acting Senior Superintendent Baron Chan Shun-ching (4 Feb 2024
briefing); Arup confirmed "fake voices and images were used," one Hong Kong
employee, about $25M, its systems were not compromised (CNN, 16 May 2024). Check
each figure's owner in the record before using it.

## Recent patterns to break (when-ai-breaks tics)

- Dek: avoid the "Named actor + past act + then/until [ironic reversal]" mold.
- Headings: avoid fragment noun-phrase headings with a comma-appended antithesis;
  the wh-bank ("What happened...," "Who ended up...," "Where this kind of X lives
  now"); and the stock final "where the same failure lives on" heading form. You
  MUST still close on where the weakness lives today — just not under that stock
  heading.
- Opener (hard tic): do NOT open with the dated "On [day-of-week], [Month DD,
  YYYY], ..." scene-set.
- Closer: avoid the persist-kicker ("still there," "still online") plus a
  reader-directed numbered-questions close.
- Diction: avoid "still working / still there / outlived / lives now," "the same
  [trick/call/play/gap]," "only as good as the examples it was shown."
- Cross-series: no "By the end you will be able to..."; no "The next time..., ask"
  close; "honest" as a virtue word.

Link, do not re-teach: `when-ai-breaks/biden-deepfake-robocall` (voice cloning);
`the-mechanics/image-generation` if a deepfake-generation mechanic needs grounding.
