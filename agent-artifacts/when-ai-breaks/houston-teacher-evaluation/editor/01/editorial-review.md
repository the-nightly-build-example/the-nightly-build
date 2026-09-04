# Editorial review: when-ai-breaks/houston-teacher-evaluation (editor/01)

## Skeptic

Thesis: Houston rated and pushed out teachers on a proprietary value-added score
they could not verify or recompute; a 2017 federal court held that firing on such
an unverifiable score violated procedural due process, without ruling the model
itself invalid; the same opaque-scoring design now sorts job applicants.

The claims it stands on, tested:

1. Teachers (and HISD itself) could not verify or recompute their EVAAS scores
   because SAS held the equations, source code, decision rules, and assumptions
   as trade secrets, and one teacher's score could not be recomputed without
   re-running the whole district. Held. The opinion quotes back this up
   descriptor by descriptor: the trade-secret refusal "to either HISD or the
   teachers themselves" (evidence p.12), the district's admission it does not
   verify or audit and its concession that replication "will necessarily fail"
   (pp.12-13), the "black box, impervious to challenge" language (p.17), and the
   HISD FAQ's own recompute admission (FAQ p.6). The article's quotations match
   the record.

2. The court's holding was procedural due process (verifiability and notice), and
   the court did NOT rule EVAAS invalid, biased, or volatile. This is the
   review-brief's first-read guardrail, and I pushed hardest here. The draft holds
   it. It states in two places that the court declined to decide the model's
   accuracy or stability, calling that question "disputed" and citing other courts
   that upheld value-added systems (matches evidence pp.19-23 and the
   Contradictions note). The main holding quote (p.18) is exact. No display-text
   descriptor or body claim upgrades the procedural holding into a finding of
   invalidity, bias, or volatility. Headline ("a score they could not check"), dek
   ("a score no one could recompute could not lawfully cost a teacher their job"),
   and every subhead stay on verifiability, never on the model being wrong.

3. Score volatility and the 1%-14% figure belong to the statisticians, not the
   judge. Held. Both are attributed only to the ASA statement (s5); the article
   reads "the American Statistical Association ... issued a warning" and carries
   the 1-14% figure, the correlation-not-causation line, and the
   large-standard-errors/unstable-rankings quotes there, never to the court. The
   categorical-cliff illustration (-2.01 vs -1.99 across the -2.00 line) is carried
   as "the plaintiffs' expert offered one illustration, which the court recorded"
   (matches p.18 n.45). Owner spelling "Education Value-Added Assessment System" is
   used.

4. SAS's defense and the plaintiffs' case are the unresolved dispute the court
   declined to settle. Held. SAS's position is stated at full strength in the
   position card (precise, reliable, unbiased; externally validated by four US DOE
   peer-review committees, GAO, RAND, WestEd), the plaintiffs' narrower claim (no
   one outside SAS could confirm it) sits beside it, and the article names what
   would settle it (the withheld equations) exactly as the court did.

5. Present-day parallel: HireVue scores applicants by an opaque proprietary
   algorithm. Held. Every HireVue figure and quote (opaque proprietary algorithm,
   no access to scores or to training data/factors/logic/techniques, "even HireVue
   is unaware of the basis," 700+ companies, 10-30% facial-expression weight, the
   Jan. 2021 facial-analysis withdrawal) matches the EPIC complaint (s8) and EPIC
   news account (s9).

Numbers, names, dates re-checked against the owning source: 2011-15 use; 50% then
30% appraisal weight; the five-tier TGI cutoffs (>=2 / >=1 / >=-1 / >=-2 / <-2);
-2.00 ineffective floor; 15% retention cap (Nov. 2012); 20.3/24.4/25.0% exits
2011-14; 12 HFT contracts terminated with 4 letters; over 6,100 members plus nine
individual teachers; $237,000. All reconcile with the evidence record. Harm is
worded as terminated / not renewed / resigned-retired-reassigned, never a flat
"fired," per pp.8-9.

One break, fixed directly. The sentence reporting the October 2017 settlement
carried citation [1], the court's May 4, 2017 opinion, which predates the
settlement and cannot own it. The opinion supports only the 2016 SAS-contract end
(p.3 n.8). I split the sentence so [1] carries the 2016 fact and s3 (AFT) + s4
(Education Week) carry the settlement date, terms, and $237,000 figure, which they
own and which double-source it. No wording of any fact changed.

data-nb-kind audit: all nine labels hold against the primary/secondary test. s1,
s2, s5, s6, s8 are the documents that own their claims (court opinion, HISD's own
FAQ exhibit, ASA's own statement, SAS's own fact sheet, EPIC's own filed
complaint) and are correctly primary. s4, s7, s9 are correctly secondary. s3 (AFT
press release) is primary for a party's own announcement of the settlement; the
independent confirmation the sensitive settlement claim needs is present as s4, so
no missing-independent-source is hidden behind a label.

Citation hrefs, opened as printed: seven resolve 200. s7 (journals.sagepub.com
DOI page) and s8 (epic.org/documents/in-re-hirevue/) return 403 to automated
requests even with a browser user-agent and via WebFetch. Both are Cloudflare
bot-blocks on the correct canonical pages, not dead links: the SAGE DOI page is
the article's authoritative home (its gating is documented in the evidence record,
and s7 is cited only for general framing, never a figure), and the EPIC page is
the complaint's document hub, the same landing-page-to-PDF pattern the accepted
s1 govinfo link uses. Left as printed; flagged below for the orchestrator's proof
step only.

## Cut

Two body sentences cut as self-narration/signposts, both failing the delete test
(their removal loses no fact, claim, or reasoning step):

- "and the vendor's case deserves its strongest statement" — the body telling the
  reader what it is about to do. The lesson body speaks to no one and never
  narrates itself; the steelman that follows in the position card carries the
  point. The remaining "Whether EVAAS was in fact accurate was never settled. SAS
  did not defend a crude tool." is concrete and does the work.
- "The parallel to Houston holds in the part that matters." — a signpost grading
  the parallel's relevance. The next sentence ("A person is ranked for a
  livelihood by a formula they cannot inspect...") states the parallel concretely,
  so the paragraph now opens on it.

Considered and kept: two negative-parallelism constructions ("was not that the
model was bad science. It was that..." and "That, and not the quality of the
statistics, is what the court found wanting.") are earned. Each corrects a real,
named misconception, the exact one the guardrail exists to prevent, so they stay
under the slop rule that protects a named contrast. The section-closing pairs ("An
estimate no one can inspect cannot be argued with. It can only be accepted." and
"The argument over the model's science stayed open. The due-process problem never
depended on resolving it.") each carry the reasoning step their section built, not
a punchline, so they stay.

Edge sentences, headings, dek checked against the recent-pattern notes. No
bare-reversal heading, no comma-triad dek, no colon-subtitle headline. The
where-it-lives-today closer ("One input changed. The design that Houston's
teachers ran into stayed in place.") is in this incident's own terms and carries a
real factual contrast (one input dropped, the opaque-scoring design intact); it is
close to the flagged house shape but not a copy of it, and it is not forming a
catchphrase. No furniture is decorative: the rating table, the score-to-job stat
strip, the HISD-FAQ quotation note, and the SAS position card each earn their
place. No Verdict block in the body; the judgment lands only in the takeaway
bookend, as the press direction requires.

No prompt leakage found. The reader-situation framing in the opener is the
reader's own situation reported as fact, not a lifted planning label. No em-dashes;
colons and periods used within the direction's punctuation standard. Grammar and
syntax clean throughout, display text and furniture included.

## Reader

Read straight through as the course's declared reader, I leave with what no single
source gives: the causal chain from an unverifiable proprietary score to a lost
job, built step by step (score formed by predicted-vs-actual growth, divided by
its standard error into a Teacher Gain Index, bucketed at hard cutoffs a hundredth
of a point can cross, unappealable because the computation is sealed), with the
court's procedural holding held distinct from the statisticians' separate account
of the score's noise the whole way, and carried into the present-day hiring
parallel. The draft-handoff's original-work sentence claims exactly this synthesis,
and the article delivers it; both answers survive. The prose sits closer to the
voice-guide exemplars than to a median summary: it teaches the structure before
judging it (Miller/Armstrong) and sets the vendor's steelman beside the
plaintiffs' case with flat attribution (Fink). The headline, reread as the largest
claim, is one the piece defends.

## Edits

- Split the settlement sentence: moved the October 2017 settlement (date, terms,
  $237,000) off citation [1] (the May 2017 opinion, which predates it) onto s3+s4,
  which own and double-source it; [1] now carries only the 2016 SAS-contract end.
- Cut "and the vendor's case deserves its strongest statement" (self-narration).
- Cut "The parallel to Houston holds in the part that matters." (signpost).

## Required work

None blocking. Note for the orchestrator (not a routed fix): s7 and s8 hrefs
return 403 to automated fetching (Cloudflare bot-block on the correct canonical
pages, not dead links); confirm they clear the proof's link check as the
draft-handoff proof reported, since both are the authoritative source homes and
resolve in a browser.

## Decision

approve — every holding, figure, name, and date reconciles with the owning source,
the legal-accuracy guardrail holds throughout, and the one miscitation and two slop
signposts were fixable and fixed in place, leaving no reporting or redraft for the
researcher or writer.
