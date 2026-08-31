# Editorial review: the-instruments/toxicity-score (editor/01)

## Skeptic

Thesis: the number behind "model X is less toxic than model Y" is one
classifier's calibrated probability, produced by a five-link chain from human
labels to a model ranking, and that chain carries a structured penalty against
text that names an identity or is written in African-American English — a
penalty a decent aggregate agreement hides. The piece stands on four load-bearing
claims, each tested against the evidence record at its owning scope.

1. **The score is one classifier's probability, thresholded and averaged.**
   Held. RTP's isotonic-calibration statement ("we can meaningfully interpret the
   score as a probability") backs the probability claim (s1); the 0.5 cutoff, the
   100K prompt construction (25K per quartile band), the ~22K toxic count
   (21,744 in Table 1; text says "22K"), and the two k=25 metrics all match the
   evidence exactly. The model-comparison table (GPT-1 0.58/0.78/0.60, GPT-2
   0.51/0.75/0.48, GPT-3 0.52/0.75/0.50, CTRL 0.52/0.73/0.50) matches RTP Table 2
   value for value at the stated scope (per model, per prompt-toxicity split, at
   25 generations). The "within seven hundredths" claim checks (0.51–0.58).

2. **Identity mentions are penalized because the training data over-represents
   the term.** Held, and this is what the headline owns. Dixon Table 1 has "gay"
   in 3% of toxic comments vs 0.5% overall; "queer" and "homosexual" carry the
   same over-representation; the "false positive bias" name and the "I am a gay
   man" example are Dixon's own words (s5). The headline ("'Gay' filled 3% of
   toxic comments, so the classifier marked the word toxic") is a faithful
   compression of Dixon's causal claim that the models "over-generalized" from
   that imbalance — exactly what Dixon owns, not a reach past it. The 2017 "I am a
   gay black woman" 87% figure is correctly attributed to the Engadget test
   (secondary, s6), date- and pre-mitigation-scoped in text.

3. **Dialect is penalized, established across two independent teams.** Held. Sap
   2019: r=0.42 (DWMW17) and 0.35 (FDCL18) between AAE markers and the labels;
   46% vs 9% false-positive gap on the DWMW17-trained classifier; direct
   Perspective query December 2018 at r=0.31/0.45 (s7). Davidson 2019: five-dataset
   corroboration (s8). Both match the evidence at scope. The AAE-phrase table
   (90%/7%, 95%/6%) matches Sap Figure 1 exactly, both columns retained so the
   same-meaning/opposite-score point survives.

4. **The bias is in the annotation, not the text.** Held. Sap's priming result
   (mean rating 0.55 control to 0.44 when dialect is disclosed) is reported at the
   correct direction and pinned to the first link of the chain, which is the
   article's structural claim about where the penalty enters.

I pushed hardest on the claim I most wanted to keep — the dialect penalty — by
rereading Sap for what breaks it. It holds, but two scope slips surfaced and are
fixed below. I also confirmed the datasets are not merged: the RTP-era CNN is
attributed only to Wikipedia Talk + NYT/news comments; Civil Comments appears
once, in a Go-deeper row, explicitly labelled a separate later dataset. The 0.5
threshold is presented solely as RTP's chosen cutoff, never as a vendor
recommendation, and the unverified 0.7 figure is correctly absent — handled
honestly. Figures are date- and endpoint-stamped throughout (Sap Dec 2018,
Engadget 2017, Dixon "before mitigation," production model 2022), with the
moving-target caveat under the table.

Two scope breaks, both fixed directly (no reporting needed):

- **Davidson range top mis-rounded.** The draft read "between about 1.4 and 2.6
  times." Davidson's max ratio is 2.653 (Davidson-2017 "Offensive"), which rounds
  to 2.7 at the one-decimal precision the sentence uses for its low end (1.396 to
  1.4). "2.6" understated the top of the cited range. Corrected to 2.7 to match
  the owning primary and the evidence record.
- **"Toxic labels" mislabelled the two hate-speech datasets.** The r=0.42/0.35
  correlations are with DWMW17's "offensive" label and FDCL18's "abusive" label,
  neither of which is a "toxic" label. Given the piece's care not to conflate
  sources, I dropped the inaccurate adjective ("correlated with the labels").

Every citation href was opened as printed. All resolve to the source itself:
aclanthology (s1, s7, s8) and arXiv (s4) return 200; the two dl.acm.org DOIs
(s3, s5) return the ACM paywall gate but the DOIs resolve to exactly the cited
papers (Ex Machina / Wulczyn-Thain-Dixon 2017; Measuring and Mitigating
Unintended Bias / Dixon et al. 2018), so a gate that lands on the right source is
not a broken link; the s2 GitHub blob returns 403 to this automated session, but
the same path on raw.githubusercontent.com returns 200, so the model card exists
at that exact address and resolves for a reader. Background and Go-deeper reading
links, and the two caption data-nb-url locators, all resolve. All eight
data-nb-kind labels match the evidence record's primary/secondary determinations,
and the policy floor (8 sources, 7 primary, 1 secondary) is met.

## Cut

The piece is disciplined; the body reserves every evaluative adjective for the
takeaway, as the voice guide directs, and reports the charged findings in the
sources' own figures. The slop pass found three sentences to remove and one
generic-address slip; no repeated formula.

- **Cut a redundant recap topic sentence.** "Each link stands in for a human one"
  opened the paragraph that closes the chain section, but the section had already
  opened on "Each one replaces a person's call with a stand-in for it," and the
  very next clause proves the same point with the specific mapping. It failed the
  delete test — no fact lost — so it went, leaving the paragraph to open on the
  concrete mapping.
- **Cut a signpost.** "One caution sits under every figure here" announced the
  moving-target caveat the paragraph then delivers, and the paragraph's own closer
  already states the caveat applies to every figure. Pure signpost; deleted, so
  the paragraph opens on "The Perspective model is not fixed."
- **Removed a generic second person from the body.** "both rise if you sample
  more" was the body's only second-person address; the brief holds the body to
  address no one. Recast to "both rise as that number grows," which is also more
  precise about what drives the rise (the generation count).

I checked the flagged "The number is not noise" against the negative-parallelism
rule. It corrects a real, named misconception — the failure section opens on the
88% agreement precisely to refute "the score is random" — and it is a bare
negation, not an "X is not Y, it is Z" mold. It is earned; left in place. The dek
("...is one classifier's probability, and the same labels score African-American
English as more toxic") is a two-clause "X is Y, and Z", not a banned semicolon
reversal, suspended question, or comma triad, and it makes a claim about the world
rather than grading the article. The imperative procedural voice ("Feed each
model a batch," "Move it and text that was toxic becomes clean") is the
name-the-hidden-parts register the voice guide asks for, not reader address;
left intact.

Leakage: compared authored text against the commission, both briefs, and the
voice guide. No lifted planning labels, selection rules, or "this lesson"
framing; the body never mentions the lesson. The brief's "structured penalty"
phrasing is not carried over verbatim. No distinctive clause borrowed from the
Luu/Evans/Narayanan-Kapoor quotations — the Goodhart passage reaches the same
mechanism in the article's own terms. Punctuation is clean; the one semicolon
("...signal of toxicity; 'queer' and 'homosexual'...") is a defensible tight join
that avoids opening a sentence on a lowercased quoted term, so I left it.

Recent-pattern check: headline shape (quoted token + concrete finding + causal
"so") and the definition-note opener differ from the most recent simpleqa piece's
stat-strip + "how X became Y" note, and the five headings reconstruct the argument
in the piece's own nouns with no scaffolding slot and no repeated comma-and mold.
No formula.

## Reader

Read straight through as the paper's declared reader, then opened the handoff's
original-work sentence. What I have that the sources alone would not give me: the
whole toxicity pipeline assembled as one causal chain, with each separate bias
finding (Dixon's term imbalance, Sap's correlations, Davidson's ratios) pinned to
the exact link where a human judgment became the number, plus the synthesis that
ranking or tuning by the score penalizes identity and dialect speech — a
conclusion no single cited paper states. The handoff's original-work claim (the
reassembly into a continuous chain, figures pinned to links) matches what the
piece delivers; both answers survive, so this is not a restatement of its sources.
The prose sits closer to the voice-guide exemplars than to a median summary: it
holds the level register on charged material, commits to the exact figures, and
keeps the judgment in the takeaway. The headline reads as the largest claim and
is exactly what Dixon owns.

## Edits

- Corrected the Davidson range top from "about 1.4 and 2.6 times" to "1.4 and 2.7
  times" (max ratio 2.653 rounds to 2.7; "2.6" understated the cited primary).
- Changed "correlated with the toxic labels" to "correlated with the labels"
  (DWMW17/FDCL18 use "offensive"/"abusive" labels, not "toxic").
- Cut the redundant recap sentence "Each link stands in for a human one."
- Cut the signpost sentence "One caution sits under every figure here."
- Recast "both rise if you sample more" to "both rise as that number grows"
  (removes the body's only second-person address; sharpens the cause).

## Required work

None blocking. No item routed to researcher or writer; all findings were
resolvable by direct edit from the evidence record and the sources opened in the
first read. The orchestrator re-runs nb stamp (word count drops slightly from the
two cut sentences) and nb check before the PR.

## Decision

Approve. Every load-bearing claim holds against the evidence at its exact scope,
all citations resolve to their sources, the two figure/scope slips and the slop
found are fixed directly, and no publication-blocking work remains.
