# Editorial review: when-ai-breaks/meta-ad-delivery-discrimination (editor/01)

## Skeptic

Thesis: Facebook's ad-delivery system, optimizing for predicted engagement,
produced racially and sexually skewed delivery of job, housing, and credit
ads even when advertisers set identical, neutral targeting — a mechanism
distinct from (and harder to catch than) targeting-based exclusion — and the
government-mandated fix built in response worked only for the ad category it
was legally required to cover, partly by reaching fewer people.

Claims it stands on, each tested against the cited primary and, where I could
reach it, against the primary itself rather than the evidence record's
paraphrase:

1. **The controlled 2018–19 study isolates delivery from targeting.**
   Reread arxiv.org/abs/1904.02095 directly. Every skew figure the article
   states (lumber 90% male/72% white, cashier 85% female, janitor 65%
   female/75% Black, taxi 75% Black, the $1–$50 budget experiment's
   55%→45% male swing and rho=−0.88, bodybuilding >75% men, cosmetics >90%
   women) matches the paper's Introduction and §4.1–4.2 exactly. Held.
   Found and fixed two places where the article itself mischaracterized the
   study's own design as "identical ads" rather than identical
   targeting/budget on different ads — see Edits. This was the piece's most
   important thing to get exactly right, since the whole mechanism argument
   turns on that distinction, and it had drifted in the headline and one
   body sentence.

2. **HUD's charge and the two settlements, dated and named correctly.**
   Opened archives.hud.gov/news/2019/HUD_v_Facebook.pdf (resolves; the
   writer's swap from the dead hud.gov URL holds), the ACLU joint statement,
   and the Civil Rights Litigation Clearinghouse case page for the DOJ
   settlement. Every date, dollar figure ($115,054), and party held: March
   19/28, 2019; June 21–27, 2022; January 9, 2023. Confirmed independently
   via web search that Mobley (housing/employment/credit) and Riddick
   (housing/jobs/credit) support the timeline's "housing and employment ads"
   characterization. Held. One claim broke on close reading: the article
   said HUD's investigators worked "independently from Facebook's public
   platform documentation" when the evidence record itself states the
   opposite — HUD's charge draws its account of the mechanism from
   Facebook's own public statements, quoted and footnoted in the charge.
   Fixed directly from the evidence record already in hand (see Edits);
   the truer and still-standing independence claim is that HUD's charge
   (filed March 28, 2019) predates the CSCW paper's public posting
   (April 2019), so the two findings are genuinely independent of each
   other, just not of Facebook's own documentation.

3. **Facebook's contested denial, attributed and steelmanned.** Confirmed
   via ProPublica (opened directly) that the quoted "no evidence" line and
   the "taken significant steps to prevent" language are accurate and are,
   per the evidence record, the strongest available statement of Facebook's
   position. It stays in a Position block, attributed, never asserted as
   fact. Held.

4. **The 2025 audit shows the fix worked for housing, not yet for
   employment/credit, partly by reducing reach.** This is where the piece
   broke and I could not fix it myself. I downloaded and read the primary,
   Imana, Shen, Heidemann, and Korolova, "External Evaluation of
   Discrimination Mitigation Efforts in Meta's Ad Delivery" (FAccT '25,
   arXiv:2506.16560), §4.2.1 and Figure 3, rather than relying on the
   evidence record's paraphrase, because the record and the primary
   disagree. The paper's own text: "In the left figure for gender, variance
   is less than 5% even without VRS in 15 out of 18 cases... In the right
   figure for race, we see variance is more than 10% without VRS in all 18
   cases. VRS reduces variance to less than 10% in all cases, bringing it
   down to less than 5% in 15 of the 18 cases." That is a different, and in
   places a *stronger*, story than the article's stat strip: for race at
   Meta's own 10% compliance threshold, VRS moves 0/18 → 18/18, not
   "<5/18 → 15/18"; the 15/18 figure in the paper is the *stricter* 5%
   threshold for race with VRS on; and for gender, 15/18 cases were already
   under 5% *without* VRS, which the stat strip's shared "<5/18, system
   off" figure contradicts for that dimension. I did not alter the numbers
   myself — the record and the source I opened disagree, which the brief
   holds is the researcher/writer's fix, not mine. See Required work.

5. **The independent audit's scope.** The article states the 36 paired
   campaigns split "one copy declared a housing, employment, or credit ad."
   The primary (§4.1.1, §4.2.1–4.2.2) shows all 36 experiments are declared
   as housing; the employment/credit comparison is a separate, smaller set
   (the hair-product ad only, three audiences) run afterward and compared
   against the housing/no-VRS baseline. The −9.82% reach figure and the
   "those figures are for ads declared as housing" framing *are* accurate
   in scope (all 36 are housing-declared, confirmed against the primary) —
   only the "housing, employment, or credit" description of what triggered
   VRS in that pool of 36 is wrong. Routed with #4, same owner, same fix.

Display text checked descriptor by descriptor: headline, dek, all five
section headings, all five timeline dates/heads, the Position block's name
and date. One factual defect found and fixed (the headline's "identical job
ads"); one internal author-count error found and fixed ("five researchers"
→ six, checked against the article's own byline in Sources and Go deeper).
data-nb-kind audited against the primary/secondary test in
nb-researcher/SKILL.md for all eight sources plus the two furniture links —
all correct (s4 and s7 are the only secondary sources; both are genuinely
third-party). Every href opened as printed: all eight numbered sources, the
two DOI redirects (both correctly resolve to dl.acm.org for the right
paper), and the internal Background link, which pointed outside this
workspace into the checked-out library worktree — confirmed the linked
article and its exact title exist there.

## Cut

Ran the slop test sentence by sentence and the edge pass separately. Five
cuts/fixes landed:

- Cut "The job-listing results follow the same logic, across every category
  the study ran" — a weak, generic paragraph-closer that also overclaimed:
  the evidence record's own quote frames the cited figures as "the most
  extreme cases," so "every category" wasn't supported. Section now closes
  on the cosmetics figure, a checkable fact, per the voice guide's
  instruction to end sections on documented fact rather than a grading
  sentence.
- Cut the unsupported superlative "the most-studied case of algorithmic
  discrimination in advertising" (why-this-matters bookend) — puffery, not
  sourced anywhere in the record.
- One semicolon repaired to a period (two independent clauses not tightly
  bound enough to earn it, per the punctuation standard's default).
- One double-negative sentence rewritten for clarity ("isn't being weighed
  against nothing" → "has real evidence against it").
- One synonym-for-variety caught: the takeaway's "a cost nobody had to
  disclose" restated the body's "a cost the compliance metric doesn't
  count" in different words for no reason; reworded to the same term.

One repeated pattern found and broken: two section headings ("What the
advertiser chose, and what Facebook chose instead" and "What Facebook said,
and what would settle it") used the identical two-clause comma-and
construction spec/headlines.md names as a heading formula. Retitled the
second to "The data that would settle the dispute," which states the
section's actual argument step in the piece's own nouns.

Checked the one deliberate "X, not Y" heading ("The discrimination was in
the delivery, not the targeting") against the brief's instruction: the
piece does name the misconception it corrects (the why-this-matters
bookend's "someone wrote a rule" / "an advertiser chose who to exclude"),
and the section that follows is built to correct exactly that. Earned; left
it.

Checked authored text against the commission and writer brief for prompt
leakage: none found. The commission's own sentences about what the lesson
should teach do not appear reworded in the article; the six-step structure
is followed but not narrated.

Punctuation audit: no em-dashes in the article. 114 semicolon-looking
matches were almost all HTML entities/CSS; three were real, one fixed (see
above), two (a tight parallel budget comparison, and alt text used as a
list) left as earned or non-prose.

## Reader

Reading the surviving piece straight through as the declared reader (smart,
has never bought an ad or trained a ranking model): the piece gives a
causal chain — controlled study, to HUD charge, to two settlements three
years apart, to Meta's built fix, to an independent post-hoc audit of that
fix — that none of the four primary records states alone, and it leaves the
reader able to name the mechanism (engagement optimization reproducing
protected-class patterns at delivery) and recognize it in a feed or a match
list, not just in this one company's ad platform. That answer survives
comparison with draft-handoff.md's original-work sentence, which claims the
same causal-chain synthesis; the claim holds once required work #4/#5 is
fixed, since right now the last link in that chain (the audit "put a number
on it") is carrying numbers that don't match its own source.

The prose sits closer to the voice-guide's exemplars than to a median AI
summary: it gives denominators and periods with nearly every figure, lets
Facebook's own "no evidence" and "sometimes"-style hedge stand unglossed in
a Position block, and (after this round's cuts) closes its sections on
checkable facts rather than assessments. The headline, reread as the
largest claim after the fix below, now states exactly what the piece proves
and nothing more.

## Edits

- Rewrote the headline (title tag, h1, and nb-meta) from "Facebook sent
  identical job ads to audiences 90% male and 85% female" to "Facebook
  delivered identically targeted job ads to audiences 90% male and 85%
  female" — the original claimed the job ads themselves were identical;
  they were different ads (lumber vs. cashier) sharing identical targeting
  and budget, which is the article's actual, more important point.
- Rewrote the dek (h1 dekline and nb-meta, kept exact match) to drop the
  now-redundant "identical targeting" clause and add what the new headline
  doesn't cover: that the skew came from Facebook's own delivery system and
  stayed invisible until a controlled study isolated it.
- Fixed "five researchers" to "six researchers" (the study has six named
  authors, per the article's own Sources and Go-deeper citations).
- Rewrote "A nearly identical cosmetics ad" to "A cosmetics ad, with the
  same targeting and budget" — same error as the headline, on the
  bodybuilding/cosmetics pair; the two ads were not nearly identical, only
  identically targeted and budgeted.
- Cut "The job-listing results follow the same logic, across every category
  the study ran" (unsupported overclaim + weak closer).
- Cut "That failure sits behind the most-studied case of algorithmic
  discrimination in advertising" to "That failure produced the case this
  lesson covers" (unsupported superlative/puffery).
- Retitled the heading "What Facebook said, and what would settle it" to
  "The data that would settle the dispute" (repeated two-clause comma-and
  heading formula within the same article).
- Rewrote "That denial isn't being weighed against nothing" to "That denial
  has real evidence against it" (double negative, hard to parse on first
  read).
- Split one semicolon into two sentences ("...statistically significant
  skew; that design..." → "...statistically significant skew. That
  design...").
- Rewrote "HUD's own investigators, working independently from Facebook's
  public platform documentation" to "HUD's own investigators, drawing on
  Facebook's own public description of how its platform works... alleged
  the same two-stage mechanism independently of the study" — the evidence
  record shows HUD's charge draws on Facebook's own statements; the
  original had the relationship backwards.
- Reworded the takeaway's "a cost nobody had to disclose" to "a cost the
  compliance metric never counted," matching the term the body already
  established instead of a new synonym.

## Required work

- **Writer.** Reread Imana, Shen, Heidemann, and Korolova, "External
  Evaluation of Discrimination Mitigation Efforts in Meta's Ad Delivery"
  (source 8), §4.1.1 and §4.2.1, and Figure 3, and correct: (1) the
  stat-strip's "15/18" and "<5/18" figures, which currently misstate what
  the paper found for race at the 10% compliance threshold (0/18 without
  VRS → 18/18 with VRS, not "<5/18 → 15/18"; 15/18 is the paper's *stricter*
  5%-threshold figure for race) and conflate it with gender, where 15/18
  cases already passed *without* VRS; (2) the sentence describing the 36
  paired campaigns as split "one copy declared a housing, employment, or
  credit ad" — all 36 are housing-declared; the employment/credit
  comparison in §4.2.2 is a separate, smaller experiment. The −9.82% reach
  figure and its housing-only scope are correct as written and don't need
  to change. Check whether the correction changes anything in the takeaway
  bookend's summary of the audit. This is the piece's central quantitative
  claim about whether the government-mandated fix worked, so it needs to be
  exactly right, not just directionally right.
- **Orchestrator.** None — no missing commission context found.

## Decision

**Revise.** The mechanism claim, the timeline, and the operator's
attributed position all held under the primaries, and I fixed everything in
my remit directly. But the piece's own load-bearing evidence for "did the
fix work" — the 2025 audit's pass-rate figures — doesn't match what that
audit's own text says, and I can't settle a number a source I opened
disagrees with; that's the writer's fix before this can stand.
