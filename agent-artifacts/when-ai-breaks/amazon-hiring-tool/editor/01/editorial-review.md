# Editorial review: when-ai-breaks/amazon-hiring-tool (editor/01)

## Skeptic

Thesis: the Amazon recruiting-tool story rests entirely on one anonymously
sourced 2018 Reuters investigation, but the failure it illustrates — a model
trained on a decade of biased hiring rebuilds the protected trait from proxies,
and neither deleting the field nor adding a human reviewer fixes it — is
established independently and is measurable in resume screeners running today.

The load-bearing claims, and how each held:

1. **Every Amazon-incident specific traces to one Reuters investigation, five
   anonymous sources.** Held. The prose carries this in-clause, not laundered:
   "Every specific that follows traces to those five people" (orientation), and
   "That timeline, and every figure in it, rests on one origin" (no-guarantee).
   Every figure I checked against researcher/02 — ~500 models, ~50,000 terms,
   1–5 stars, ten years of resumes mostly from men, the "women's" penalty, the
   two unnamed all-women's colleges, "no guarantee," disbanded by the start of
   2017, reported Oct. 2018 — matches the evidence record and is attributed to
   Reuters in the sentence that states it. The one directional quote ("taught
   itself that male candidates were preferable") is reproduced verbatim.

2. **The Reuters-vs-Amazon contradiction is carried, not resolved.** Held, and
   handled exactly as the brief requires. The piece states Amazon's on-record
   position ("never used by Amazon recruiters to evaluate candidates") against
   the sources' account (recruiters "looked at the recommendations ... but never
   relied solely on those rankings"), marks that the two "sit against" each
   other, and lands only on the point both share: the ratings were never the
   sole basis for a hire, the tool never became a live screen. The explicit
   bound is present and correct: "Nothing in the record says it rejected real
   applicants at scale," reinforced later by "Amazon's tool never went live." No
   claim implies harm at scale.

3. **The redundant-encoding mechanism is independently owned.** Held. Barocas &
   Selbst (2016, [4]) and Dwork et al. (2012, [5]) are cited as the mechanism's
   primaries, and the term is introduced only after its concrete stand-in (the
   word "women's," a women's college, a verb) is on the page as fact — the
   sequencing the voice guide licenses.

4. **The weakness lives today.** Held, and resting on the three primaries the
   brief names, not on the excluded marketing prevalence stats. EEOC four-fifths
   ([6]) with its worked example (80/40 applicants, 48/12 advance, rates 60% and
   30%, ratio 50% < 80% — arithmetic recomputed and correct); NYC Local Law 144
   ([7]); and the 2024 UW study ([8], 85/9/52/11, "never preferred" for
   Black-male names). No 83%/99% figures, no team headcount, no Edinburgh
   location. All excluded embellishments stayed excluded.

Display text checked descriptor by descriptor. Headline ("Amazon's resume
screener taught itself to penalize the word 'women's'") states the reported
finding with the actor named, in the present, with no duration mold and no colon
tell; the dek immediately supplies its evidentiary basis (single 2018 Reuters
investigation, five anonymous sources) so the headline's flat statement is
grounded rather than overclaimed. Dek is two clauses joined by ", and" — not a
comma triad, not a semicolon reversal, and it makes a claim about the world
(the state of the sourcing and where the flaw now lives), not a grade of the
article's method. The four subheads each name a step of the argument in the
piece's own nouns and reconstruct the argument when read alone; none is a
scaffolding slot, none repeats a comma-and cadence. Named scholars' names and
affiliations check out against the evidence.

`data-nb-kind` audit, all eight: [1] Reuters primary (origin report owning the
reporting — defensible, and the piece is explicit that its own basis is
anonymous); [2] Irish Times secondary and [3] VICE secondary (wire carriage and
carrier of Amazon's on-record statement respectively) — both correct; [4]
Barocas & Selbst and [5] Dwork et al. primary (foundational scholarship owning
the mechanism); [6] EEOC primary; [7] NYC DCWP primary; [8] UW News primary
(firsthand report of the authors' own study). No label hides a missing
independent source — the single-origin limitation is stated in the open, not
concealed behind a kind label.

Source [6] verified specifically, per the brief. The href is now the Wayback
capture `web.archive.org/web/20250125163154/https://www.eeoc.gov/.../select-issues-...`,
matching researcher/02 exactly. `data-nb-kind="primary"` is defensible: an
Internet Archive snapshot reproduces the EEOC's own text verbatim, so the
authoring party — and the owner of the Title VII interpretation — is still the
EEOC; an archive is a mirror of the document, not an outside author reporting on
it. The `data-nb-note` ("Internet Archive capture of the EEOC's own page;
eeoc.gov bot-gates the canonical URL") is factual and matches the evidence
record. I did not re-open eeoc.gov (bot-gated, as the brief noted); the archived
text was verified firsthand in researcher/02.

Every citation href was opened via the deterministic link check (read-only):
BLOCK 0, WARN 0. Every printed address resolves — the sole prior blocker (the
canonical eeoc.gov URL that returned a hard 404) is gone now that [6] is the
archived capture.

## Cut

One structural cut, and it is the flagged one. The `nb-note nb-note-strong`
"Verdict" block that closed the no-guarantee section is retired-template
furniture: `press/editorial.md` states plainly that the takeaway bookend is
where a lesson lands its judgment and that no body block may close with a
Verdict note or restate the finding. This block failed on every count I could
test it against. Its content ("The mechanism is settled; this particular
incident is not independently confirmed. Read Amazon's tool as a well-reported
illustration of a real failure, not as an audited finding") is the identical
judgment the takeaway already lands ("worth remembering for what is certain
about it, not for the details that are not ... The Amazon story may rest on five
people. The lesson does not rest on them at all"). It also duplicates the "What
to be careful about" column of the holds-up grid directly above it, which
already carries the single-origin caveat. It did no non-restating work, so it
cleared no bar that would justify keeping banned furniture. Cut. The section now
closes on the holds-up grid, which ends firmly on "Amazon disputes that
recruiters used the tool to evaluate candidates at all" — a stronger, non-
redundant close.

No prose leakage found on comparison with the writer brief: the single-origin
language in the body is reported fact about the sourcing, not a restatement of
the instruction or a claim that the assignment was fulfilled. The surviving
furniture earns its place: the holds-up grid is the article's central
evidentiary distinction made scannable, and the "Redundant encoding" definition
note fixes the one term the whole lesson turns on, tied to its concrete example.
Neither reads as a stack of blocks once the Verdict is gone. The one licensed
adjacent-domain hypothetical is marked illustrative and is not one of the
walled-off cases. Hedged contrasts in the piece ("not an Amazon bug but a
property of any model," "a reprint of the same report is not a second source")
each correct a real, named misconception central to the lesson and stay; cutting
the Verdict removed the weakest of them. No run-ons; the two body semicolons
(the EEOC rates/ratio, the UW race/gender stat pairs) each bind tightly
structured parallel clauses and do the semicolon's real job.

## Reader

Read straight through as the paper's declared reader — smart, no codebase — the
piece gives something the sources alone do not: a framework for judging any "AI
hiring bias" claim by separating the single-origin reported incident from the
independently established failure mode, then showing that same failure priced
into 2024 screeners and into law. Reuters, the two CS papers, the EEOC, NYC, and
UW do not connect themselves; the lesson connects them and shows on the page —
via the holds-up grid and the independent mechanism sources — that the teaching
survives even if every Reuters specific were wrong. That matches the
original-work sentence in draft-handoff.md, which is realized in the article
rather than merely asserted. The prose sits closer to the voice-guide exemplars
(Yglesias-plain, Dastin-graded attribution in the same breath as the claim,
concrete nouns) than to a median AI summary; attribution lives in-clause and the
hedges are sized to what each source supports. Re-reading the headline as the
largest claim: the piece defends it and never overclaims it beyond what Reuters
reported and the dek grounds.

## Edits

- Cut the `nb-note nb-note-strong` "Verdict" block that closed the no-guarantee
  section (restated the takeaway's judgment and duplicated the holds-up grid;
  banned by press/editorial.md as retired-template furniture).

## Required work

None. (Ran `./nb stamp` after the cut: words 1822, sources 8, reading_minutes 8.)

## Decision

approve — every brief-flagged issue resolves in the article's favor once the
banned Verdict block is cut: single-origin attribution stays visible and
in-clause, the Reuters-vs-Amazon contradiction is carried and weighed rather
than resolved, no claim implies harm at scale, source [6]'s note and primary
kind are defensible for an archived copy of the EEOC's own page, and the
read-only links-included proof is BLOCK 0 / PUBLISHABLE.
