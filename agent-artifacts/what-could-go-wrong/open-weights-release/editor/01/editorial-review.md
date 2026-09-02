# Editorial review: what-could-go-wrong/open-weights-release (editor/01)

## Skeptic

Thesis: an open-weights release is irreversible and its safety training is
demonstrably cheap to remove, but the jump from that demonstrated fact to a
catastrophic real-world harm is not demonstrated, so a reader should hold the
irreversibility case and the marginal-risk rebuttal together and ask, of any
open-weights claim, whether the harm has been shown and what the open version
adds over what is already reachable.

The claims it stands on, and how each held:

1. The release is irreversible; no recall mechanism (Seger et al. + the Llama 2
   license). Held. The "no undo function" quote is in the GovAI report, and the
   Llama 2 license genuinely gates only 700M-MAU commercial users and carries no
   revocation once weights are downloaded. Verified the license page resolves and
   quotes the sole-discretion clause.
2. Safety training is cheaply and demonstrably removable (Qi et al.). Held, and
   this is the load-bearing figure, so I checked it against the primary directly.
   Table 1 of arXiv:2310.03693 gives GPT-3.5 Turbo 1.8% to 88.8% at 10 examples
   (cost stated as "less than $0.20"), and Llama-2-7b-Chat 0.3% to 50.0% at 10
   examples and 0.3% to 80.3% at 50 examples, run locally at no API cost. The
   article's table reproduces all six numbers exactly.
3. Catastrophic bio uplift is not demonstrated (RAND null result). Held, and
   stated in RAND's own qualitative terms: "did not measurably change the
   operational risk," "beyond the capability frontier of LLMs as assistive
   tools," no statistically significant difference in plan viability. Confirmed no
   participant or team count appears anywhere in the article, per the guardrail on
   that disputed figure.
4. The marginal-risk reframe (Kapoor, Narayanan et al.). Held at full strength,
   and correctly not softened into a blanket "open weights are fine": the article
   carries the six-of-seven insufficient-evidence finding, the low-cyber
   conclusion, and the counterweight that the same paper finds "considerable
   marginal risk" for non-consensual intimate imagery. Confirmed the paper's
   identity, authorship, and marginal-risk definition against the primary.
5. The present-day complication (Meta's 2025-2026 pivot). Held. The article
   reports the move to a closed successor for competitive/IP reasons and the
   partial reversal by August 2026, with Zuckerberg's own "rigorous about
   mitigating these risks" language. Verified both secondaries resolve and support
   the framing.

Specific check requested. The headline attaches the ten-example finding to Llama
2, and that is correct, not a wrong-system display failure: Table 1's
Llama-2-7b-Chat 10-example row is a real data point (0.3% to 50.0%). The
irreversibility argument and the marginal-risk rebuttal are both held at full
strength; the article names where confidence outruns proof on both doom (the
unproven uplift) and dismissal (RAND's own "not a guarantee about tomorrow's
models," the NCII exception). The Meta pivot complication is present. No company
is cited as an authority: Meta, Zuckerberg, and LeCun all appear as events and
documents, with the factual weight carried by Seger, Qi, RAND, Kapoor, Egan/Heim,
and NTIA. One nuance worth recording but not blocking: the ten-example Llama 2
result (50.0%) is the softer of the paper's numbers, and "stripped" sits at the
strong end for it; it stays honest because the body and table report the 50.0%
plainly and the 50-example row reaches 80.3%.

Breaks found:

- Chronology. The draft said Qi et al. tested the harder route "Ten months after
  Seger's report." Qi's v1 is October 5, 2023 (arXiv:2310.03693, submission
  history confirmed); Seger's GovAI report is Sept/Oct 2023 (SSRN Sept 29, GovAI
  Oct 9). The two are contemporaneous, so the ten-month interval is false. I cut
  the interval; the logical juxtaposition it framed (Seger calls the built-in
  route harder, Qi's numbers show how low the bar sits) survives without it.
- The same error placed Seger's report "In November 2023." November is only the
  arXiv-mirror posting date; the cited source is the GovAI page, published in
  October 2023. I cut the incorrect month rather than ship a wrong date. The
  writer may restore a correct, sourced publication date if reader orientation
  wants one.
- Zuckerberg quotation. The draft prints, in quotation marks, that wide
  distribution lets "larger institutions...check the power of smaller bad actors."
  The source's actual clause reads "larger actors can check the power of smaller
  bad actors"; "larger institutions" belongs to a different sentence ("larger
  institutions deploying AI at scale will promote security and stability across
  society"). The printed quote splices the two and swaps the subject noun. I
  cannot alter a quotation, so this is routed to the writer. The evidence record
  carries the same spliced phrasing, so the researcher's record should be
  corrected to the primary's verbatim text as well.

Citation hrefs: opened every link as printed. All resolve to the source's own
page. RAND's report page and the NTIA fact sheet returned 403/503 to the
automated fetcher, which is bot-blocking, not a dead link; both are the correct
live pages (the RAND report URL and title were confirmed independently, and the
NTIA URL is well-formed and was read by the researcher). data-nb-kind labels all
check out: the Meta license, Zuckerberg essay, RAND press release, and NTIA fact
sheet are correctly primary as the owning documents of their own statements,
reported as events rather than as authorities. Source floor met: 12 sources, 9
primary, 3 secondary. No operational CBRN content appears; the DailyAI quote's
"bioweapon building instructions" phrase was correctly not reproduced.

## Cut

One clear slop cut: the null-result section closed on "An independent voice, from
inside a company that ships open weights, had reasoned to the same place RAND's
data later landed on." It restated the preceding sentence ("called RAND's result
a confirmation of that view") and its one new beat, calling a Meta insider an
"independent voice," worked against itself. Removed; the paragraph now lands on
the sourced confirmation line.

Three smaller repairs to reflexive edges. "The table's two rows aren't just a cost
comparison, either" was a signpost opener; replaced with "The two rows differ in
more than cost," which the next two sentences cash out concretely.
"Removing an open model's safety training isn't theoretical: it's demonstrated..."
carried a negative-parallelism reflex and a colon used as a bare connector;
tightened to the plain positive, since the demonstrated/theoretical line is
already the article's spine. And "finds the opposite for non-consensual intimate
imagery, in the same paper" repeated "the paper that" from the same sentence;
dropped the trailing "in the same paper."

Edge and formula pass. The dek makes a claim about the world (RAND found no
measurable difference), not a grade of the article's method, and it breaks this
desk's recent molds: it is not the comma triad, not the ", and"-twist, and not the
"the worry X named survives Y" shape. The headline is a positive finding rather
than the desk's default negative-fact reveal. The present-day heading is "What
open weights add that the internet doesn't," not the recurring "Where X still Y."
The four subheads, read alone and in order, reconstruct the argument. No
distinctive phrasing was borrowed from the Karnofsky, Tufekci, or Schneier
passages in the voice guide. No prompt or brief language leaked into the prose.
The remaining negative-parallelism constructions ("not a hypothetical," "not a
guarantee about tomorrow's," "a spreadsheet, not a research program") each correct
a misconception the article actually names, and each carries a fact or a reasoning
step, so they stay.

## Reader

Reading what survives straight through: the piece gives a reader a way to reason
that no single source hands over. It puts Seger's qualitative "harder route" claim
against Qi's empirical numbers to show how low that bar sits, then draws out the
asymmetry neither paper states alone, the closed attack ran through a service that
could log or refuse it while the open one ran where nobody could watch, then uses
RAND's null and Kapoor's disaggregated framework to separate a demonstrated harm
from a projected one, and closes on the Meta pivot showing release decisions may
track competition rather than either safety position. The original-work sentence
in the handoff claims exactly that synthesis, and the article delivers it. The
prose sits closer to the voice-guide exemplars than to a median summary: it states
each finding plainly and says in the same breath what it does and does not settle.
The reader leaves with the two portable questions the opener promised.

## Edits

- Cut "In November 2023," from the orientation opener (incorrect date for the
  cited GovAI source).
- Cut "Ten months after Seger's report," from the cheap-to-strip section (false
  interval; Qi and Seger are contemporaneous).
- Replaced "The table's two rows aren't just a cost comparison, either." with "The
  two rows differ in more than cost."
- Cut the null-result section's closing sentence "An independent voice, from
  inside a company that ships open weights, had reasoned to the same place RAND's
  data later landed on."
- Tightened the holds-up bullet "Removing an open model's safety training isn't
  theoretical: it's demonstrated..." to "Removing an open model's safety training
  is demonstrated, at negligible cost, on a real released model."
- Dropped the redundant "in the same paper" from the NCII holds-up bullet.

## Required work

- writer: Correct the Zuckerberg quotation. The primary's clause is "larger actors
  can check the power of smaller bad actors" (about.fb.com/news/2024/07/
  open-source-ai-is-the-path-forward/); the draft's "larger institutions...check
  the power of smaller bad actors" splices a second sentence and swaps the subject.
  Print the verbatim primary text.
- writer: Optionally restore a correct, sourced publication date for the Seger
  report if reader orientation wants one. The cited GovAI report is October 2023
  (SSRN Sept 29, GovAI Oct 9), not November 2023. I removed the wrong month; a
  correct date is welcome but not required.
- researcher/orchestrator (awareness only, no new evidence needed): the evidence
  record's Zuckerberg paraphrase carries the same spliced quotation; align it to
  the primary so a future article does not inherit it.

## Decision

revise: the quotation attributed to Zuckerberg is not verbatim and must be
corrected by the writer against the primary before publication; my prose and date
fixes are already applied.
