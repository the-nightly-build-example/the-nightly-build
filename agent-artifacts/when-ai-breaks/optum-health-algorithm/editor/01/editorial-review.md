# Editorial review: when-ai-breaks/optum-health-algorithm (editor/01)

## Skeptic

Thesis: a commercial risk-scoring tool trained to predict next-year medical
cost scored equally sick Black patients as lower-risk, because cost is a
biased stand-in for health need, and that failure is a general property of
proxy labels, not a health-care quirk. The claims it stands on: the tool's
label was cost, not illness; at equal score Black patients were sicker
(4.8 vs 3.8 conditions); cost and need come apart by race through unequal
spending ($1,801 wedge); race was never an input; and label choice alone
swings the outcome (14.1% vs 26.7% Black in the top-risk group).

I pushed hardest on the three figures the brief flagged as easy to conflate,
opened the owning primary (s1, the Obermeyer et al. paper PDF) as an
opponent, and confirmed each against the paper's own text:

- Observed study-sample gap: paper reads "4.8 versus 3.8 distinct conditions;
  P < 0.001," "26.3% more chronic illnesses." The article prints exactly this,
  framed as the 97th-percentile study-sample figure. Holds.
- Simulated vs observed share: paper's abstract gives the counterfactual "from
  17.7 to 46.5%," and separately "The enrolled individuals are 19.2% Black."
  The article keeps these in distinct frames: 19.2% is labeled observed
  enrollment, 17.7 to 46.5% is labeled a simulation ("not a change anyone
  made"), and the stat strip carries the 17.7% baseline so no reader reads
  19.2 to 46.5. Holds. This is the piece's cleanest save.
- Manufacturer replication: paper says the manufacturer "independently
  replicated our analyses on its national dataset of 3,695,943 commercially
  insured patients," where "Black patients had 48,772 more active chronic
  conditions." The article attributes both numbers to the manufacturer's own
  3.7M-patient dataset, never to the study sample. Holds.

Also verified against the primary: race excluded ("the algorithm specifically
excludes race"), the cost label ("total medical expenditures ... as the
label"), and the $1,801 wedge ("$1801 less per year, holding constant" the
number of chronic conditions). The 49,618 / 100,009 sample denominators sit in
Table 1 (extraction dropped the tokens; the evidence record read them
firsthand and they are not contested).

Vendor naming (brief focus 2) is exact. The article states the study named no
vendor and cites the paper's own "no contact with the manufacturer until after
the analysis" reticence; attributes "Optum's Impact Pro" to reporting (s4) and
the NY DFS/DoH letter (s5), never to the paper. I opened s5 and confirmed the
letter names "Optum's data analytics program, Impact Pro," calls the results
"unlawful in New York," and is signed by Superintendent Lacewell and
Commissioner Zucker to CEO Wichmann. All display attributions land.

I checked the one quote the evidence record did not itself carry: the repo's
"our health system partner" (s3). I opened the raw README and confirmed the
exact phrase is present and that the repo names no vendor. Citation is honest.

data-nb-kind audit: s1 (paper), s2 (SOA report), s3 (authors' repo), s5 (DFS
letter), s7 (Playbook) all correctly primary; s4 (Science News), s6 (govtech),
s8 (Berkeley notice) all correctly secondary. The vendor defense quote is cited
to the secondary that carries it (s6), and the Playbook framing quote is
double-cited to the primary and the secondary that verifies its wording (s7,
s8). No mislabeled source, no independent-source gap hidden by a label.

No break survived. No claim routed to the researcher.

## Cut

One direct cut. The orientation section closed on "This lesson is about what
that score actually measured," a self-narrating signpost of the banned
"this dossier / what follows" family. Removed; the paragraph now lands on the
flat declarative "The score decided who the program reached," which carries the
stakes without narrating the piece.

Worst tell hunted for and not found: the shelf's recent "Where the same
weakness lives today" closing mold and its nb-figure + nb-note pairing. The
closing heading is "When the label is a proxy," named from this incident's
mechanism, and the piece carries no figure at all, so the formula is absent.
Furniture earns its place: the stat strip keeps the observed and simulated
shares side by side (the exact anti-conflation job), the table shows cost
near-equal at equal score while illness is not, and the two nb-notes serve
distinct purposes (the vendor's own words, then a plain-language distillation).

Register and no-villain check (brief focus 3) held throughout: the vendor's
defense is quoted as restating the mechanism, the replication and 84% reduction
read as engagement, and the regulator's "unlawful" language is a cited fact,
not the article's indignation. The hedged-contrast count runs high (the tool
"was not broken," label "was not illness," "not whether it is accurate"), but
each corrects a real misconception the lesson is built to dispel rather than a
strawman, so each is earned. No moralizing to cut.

## Reader

What the piece gives beyond its sources: the paper reports these results in
scattered sections; the article recasts them into one "hold the risk score
fixed" walkthrough that a reader can follow to the flaw, and turns the
label-choice swing into a transferable proxy rule the paper never states in one
place. Read straight through, it teaches how a race-blind score produced a
racial gap and equips the reader to ask the transferable question. The
original-work sentence in the handoff claims exactly this recasting and the
distinct-frames discipline, and both survive the read. The prose sits closer to
the Obermeyer/Mullainathan exemplars, forensic calm with one exact figure per
paragraph, than to a median AI summary. The headline, reread as the largest
claim, is accurate and defended.

## Edits

- Cut "This lesson is about what that score actually measured." from the
  orientation section (self-narrating signpost).
- Ran `./nb stamp`: words 1734 to 1725, reading_minutes 8, sources 8.

## Required work

None blocking.

- Optional (writer): the mechanism's root, at equal illness less is spent on
  Black patients, is the one place a source figure (paper Fig. 3B,
  cost-vs-conditions by race) would let the reader see the gap open rather than
  read it. The table carries the calibration argument adequately, so this is an
  enhancement, not a gap. Available via `./nb asset` from s1 if pursued.

## Decision

approve. Every load-bearing figure verified against the owning primary, the
three conflatable figures held in distinct and correctly attributed frames, the
vendor naming and no-villain register exact, and the one self-reference cut.
