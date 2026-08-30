# researcher brief: when-ai-breaks/mcdonalds-ai-drivethru (01)

Inputs:
- editorial-direction.md (house standard, citation rule, the reader, the When AI
  Breaks series prompt, which requires working from the record)
- this brief

Output: researcher/01/evidence.md

## Subject
McDonald's automated order taking (AOT) voice AI at drive-thrus, developed with
IBM, tested at ~100 US restaurants, and discontinued in 2024. Reconstruct the
incident from the record.

## Questions the evidence record must answer
1. The build, in order with dates and named parties: McDonald's 2019 acquisition
   of Apprente (and the McD Tech Labs unit it became); the 2021 sale of McD Tech
   Labs to IBM and the AOT partnership; the scale of the pilot (how many
   restaurants, which region). Name the companies and, where the record does,
   the people. Cite McDonald's and IBM's own announcements.
2. What it actually did wrong: document specific, verifiable failures (e.g. the
   order that ballooned to hundreds of McNuggets; bacon added to ice cream; other
   filmed mis-orders). Treat the videos as primary artifacts of the behavior and
   record what each shows. Distinguish widely-reproduced incidents from single
   unverifiable clips.
3. What the operator did afterward: the 2024 decision to end the IBM AOT
   partnership and remove the system from the test restaurants. Record the exact
   date and wording as reported (the internal memo carried by trade press such as
   Restaurant Business), and McDonald's stated position that it still intended to
   pursue voice ordering. Record the memo as the primary the reporting quotes.
4. The mechanism, to teach on the spot: why automatic speech recognition and
   order parsing are hard in a drive-thru specifically — engine and background
   noise, accents and disfluency, an open menu with modifications, and how a
   per-item error rate compounds across a full order. Anchor the ASR mechanism in
   a primary (the library uses the-evidence/whisper; source the general ASR
   difficulty to a credible primary). If any accuracy target or figure was
   reported (e.g. an ~85% order-accuracy goal), record it with its owner and note
   that McDonald's/IBM never published measured accuracy.
5. The human-in-the-loop reality: sourced evidence on how some voice-ordering
   deployments (McDonald's or peers) relied on remote human reviewers behind the
   "AI." Keep firmly to what is documented.
6. Where the weakness lives today: current peer deployments (e.g. Wendy's with
   Google, White Castle with SoundHound, and others) for the closing section.
   One sourced line each; these are context, not the subject.
7. Contradictions / disputed cause: McDonald's "end of a partnership, not a
   failure" framing versus the error record. Record both accounts and state what
   evidence would settle it.

## Source policy for this article
At least 8 sources; at least 4 primary, at least 1 secondary. Primaries:
McDonald's press releases (2019, 2021), IBM's statement, an earnings-call
transcript if it addresses AOT, and the failure videos as behavior artifacts.
Secondary: CNBC, The Verge, Restaurant Business, and similar reporting (including
where it carries the 2024 memo). Classify each and say why. Accusations of
specific failure need firsthand confirmation; two retellings of one clip count
as one.

## Source assets
Name any exact visual worth using (a still from a widely-reproduced failure
video, or a corporate statement excerpt), in the evidence asset shape. No crop
coordinates. Confirm every URL resolves to the source's own page.

## Focus / risk
Get the corporate chronology exactly right (Apprente -> McD Tech Labs -> IBM ->
2024 wind-down) with dates and owners, since it goes in display text. Separate
verified, widely-reproduced failures from unverifiable viral clips.
