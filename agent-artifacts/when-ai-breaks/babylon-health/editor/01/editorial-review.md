# Editorial review: when-ai-breaks/babylon-health (editor/01)

## Correct

Thesis, from the draft alone: Babylon sold its symptom checker as "as good as a
doctor," but that number came from a curated vignette test the company built, and
the presentations that actually failed were the serious, uncommon ones such a
test underweights, with no real-world under-triage rate ever measured. The claims
under it: (1) the marketing outran Babylon's own paper, which said only
"comparable" and "safer on average" and warned its results "cannot be directly
interpreted with respect to real-world accuracy and safety"; (2) the comparable
number rests on 100 scripted vignettes scored by one judge on conditions the
system was built to recognize, and is fragile (drop the weakest of the seven
doctors and humans win every measure; move from the judge's range to the
strictest in-house GP and triage safety falls from 97.0 to 81.0 percent); (3)
documented under-triage, a distinct safety failure, is real but rateless (the
female-profile heart attack read as panic attack, the missed DVT, chest pain
routed to gastritis, two MHRA-logged incidents); (4) Babylon answered by calling
its critics trolls while RCGP and MHRA sided with them, and the company collapsed
in 2023.

I checked each claim against the evidence record and the owning documents. The
two failures stay distinct: the oversold claim lives in orientation and the
vignettes section, the under-triage in "What the vignettes left out," and no
sentence blurs them. The load-bearing figures all trace: recall 80.0 vs 83.9,
top-1 70.0 vs 75.3, top-3 96.7 vs 90.3, triage 97.0 vs 93.1, and the 81.0 against
the strictest in-house GP are the study's Tables 1-3. The "81%" the piece uses is
that Table 3 triage-safety figure, not the marketing MRCGP composite the evidence
flags as never stated in the paper; the only exam reference is the RCGP's own
rejection and the paper's "above 72%" line. The seven-doctor count is the paper's
(Doctors A to G), with Coiera's "six" noted in the parenthetical. The Lancet
quote carries the paywall note as written, and the citation and conclusion match
the Crossref record and Coiera's review. Babylon's defenses are quoted in its own
words beside the counter-evidence (the troll line, Grimes on "safe information,"
the "we stand by our original science" note, "millions of uses, no reported
harm"). The retinopathy field study is linked at first use, not re-taught.
data-nb-kind holds throughout: study, Coiera, Lancet, the gov.uk notice and the
SEC filing primary; the news pieces secondary, including the TechCrunch report
that reproduces the MHRA letter rather than being it.

One break. The head-to-head table's caption claimed "on the diagnosis itself the
doctors led or matched," but its own "Right answer in top three" row shows
Babylon ahead, 96.7 to 90.3. A scanning reader meets a label its table
contradicts. Fixed to "the doctors led on the top single diagnosis, and the
triage-safety lead was scored against one judge's range," which is true of the
top-1 row and hides neither Babylon's top-3 lead nor the judge-dependence of the
triage number. Under-triage as the costly error, the gender split, the names and
roles (Watkins the consultant oncologist; Fraser, Coiera, Wong; MHRA), the
valuations and the 2023 administration date all held against the record.

## Reads well

The vignettes section opened on "The comparable-to-doctors result came from one
specific kind of test," which survives the placeholder test as "the X came from
one specific kind of Y" and left the actual test to the next sentence. I folded
the two together so the sentence names the test it promises: "came from a test
Babylon's researchers built: a 'semi-naturalistic, role-play' exam of 100
clinical vignettes." Nothing else read as filled-in pattern or as lifted from the
commission or the voice guide; the "fluency is the easy part" close reworks the
commission's framing into the piece's own Babylon-grounded argument rather than
borrowing its clause. The register already matches the guide: claims stated
plainly, the numbers carried beside the protocol that produced them, Babylon's
answers quoted at length before they are tested, the way STAT sets IBM's words
beside the documents and ProPublica sets Northpointe's letter beside the
analysis.

Recent-pattern checks passed. The close, "That number is still the one today's
symptom checkers and chatbots find hard to get and easy to skip," resolves the
opener's promise and is not the "the same X, wherever Y" or "did not end with"
relocation mold. The nb-note heading is "Babylon on its own study," not a mirror
of the Waymo "Perception, then prediction" pair. The dek is one lean sentence
with concrete detail and closes on no triad. The five headings each name a
distinct step of the argument and reconstruct it in order when skimmed.

## The experience

The rendered page reads top to bottom as the record in order: what Babylon built
and claimed, where the number came from, what the vignettes left out, how Babylon
answered, and where the weakness lives now. The one table earns its place by
setting the four test-set results side by side so the reader sees the closeness
and the judge-dependence at once; the caption edit was the only thing keeping it
from misreporting its own rows. The nb-note holds Babylon's "we stand by our
original science" line where the reader can weigh it against the findings.

What the piece gives beyond its sources: it puts the study's own hedged words and
its explicit real-world caveat next to the marketing, then shows the number's
fragility from the record itself (97.0 against the judge, 81.0 against the
strictest GP; humans winning once the weakest doctor is dropped), and holds that
apart from the separate, rateless safety failure. That is the draft-handoff's
original-work sentence, and the article does the work, not just assert it.

## Edits

- Table caption: replaced "on the diagnosis itself the doctors led or matched"
  with "the doctors led on the top single diagnosis" so no row contradicts the
  label while the triage judge-dependence stays flagged.
- Vignettes section lead: merged "came from one specific kind of test. Babylon's
  researchers built a 'semi-naturalistic, role-play' exam:" into "came from a
  test Babylon's researchers built: a 'semi-naturalistic, role-play' exam of 100
  clinical vignettes," cutting a sentence that named no test.
- Re-ran nb stamp (words 2196) and nb check with links (BLOCK 0, WARN 0).

## Decision

approve: the argument is sound and sourced, the two failures stay distinct with
no rate claimed, and the two remaining defects (a self-contradicting caption, a
hollow lead sentence) were fixable in place.
