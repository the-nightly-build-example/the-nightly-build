# Editorial review 02 — what-could-go-wrong/jailbreaks (re-review after correction)

## Skeptic

Skeptic: thesis unchanged from 01 (optimizer-found jailbreaks transfer and
demonstrated defenses stay partial; robust-refusal impossibility is
conjectured, not proven), now carrying a second, explicitly separate live
debate the revision adds — how much a demonstrated jailbreak's marginal
capability matters, given that the same information may already be public;
tested 6 claims (Kapoor et al.'s marginal-risk framework and its own worked
example's scope; RAND's Table 3 numbers and its red-teamer quote; Soice et
al.'s one-hour MIT demonstration; Peppin et al.'s "field's working position"
characterization; whether the both-directions rule holds for the new
argument; whether the DEMONSTRATED-vs-CONJECTURED spine stays intact); broke:

- A scope mischaracterization. The draft called Kapoor et al.'s pathogen
  example "the jailbreak case." I fetched the paper directly (both the arXiv
  abstract and the ar5iv full text): the paper's subject is open-weight
  models, where the relevant bypass is retraining on released weights, not
  prompting a closed API — the evidence record's source 14 entry says this
  explicitly and warns the draft against exactly this conflation. Fixed:
  "Their own example, about open-weight models rather than a prompt
  jailbreak: a model can produce pathogen information that is..."

Everything else held. RAND's HTML landing page returned HTTP 403 to WebFetch
for me too, matching the evidence record's account; I retrieved the PDF
directly with `curl` and a browser user-agent (also matching the evidence
record's documented workaround) and read all relevant pages firsthand. Table
3's −0.22/t=−0.49/p=0.64, the design (45 red-teamers, 15 cells, 12-cell main
comparison, 7 weeks, 80 hours/member), and the exact red-teamer quote — "had
more success using the internet" but when they could "jailbreak [the model,
they] got some information," and it "wasn't being specific about
[operational] vulnerabilities — even though it's all public online" — all
match the article's rendering (which correctly keeps both clauses together,
as the evidence record's own contradiction note required). Soice et al.'s
"in one hour," the four capabilities the chatbot supplied, and Peppin et
al.'s Section 3.1.1/3.1.3 language and the NSCEB quote all checked out
against the primaries directly.

The both-directions rule holds. The new section's closer — "'No one has
shown a model meaningfully beats a skilled searcher' is not proof it never
will, just as 'no defense has been proven complete' is not proof defense is
futile" — names the gap in both directions explicitly, mirroring rather than
duplicating the Vassilev section's own hedge. The DEMONSTRATED-vs-CONJECTURED
spine is untouched: the new material sits in its own paragraphs, clearly
framed as a second question ("how much it matters," not "whether it
happened"), and the takeaway's added clause keeps the two questions separate
rather than merging them.

## Cut

Cut: 6 sentences/clauses; worst tell: "Zero, then one, against the same
system" and "The two sit side by side without colliding" — both fully
restate a fact or conclusion the immediately preceding sentence already
stated, the same "manufactured punchline" pattern flagged in 01 but missed
there on those two. Also cut "Both sides can be right," "His caveats matter
as much as the theorems," and "Reaction split" (three topic-sentence
signposts whose payload the following sentences already carry), and trimmed
"on AI and biological-attack planning" from the RAND appositive (redundant
with the linked neighbor article's own anchor text).

**Length is not fully resolved and I am recording why.** These cuts move the
count from 2588 to 2557 — an honest 31 words, all I could defend under the
delete test. That leaves the piece roughly 357 words over the 1200-2200
band. I looked hard for more: the pre-existing DEMONSTRATED-band prose (GCG,
Wei, many-shot, constitutional classifiers, Attacker Moves Second, poetry)
was already cut tightly in round 01 and is protected there as load-bearing
for the cross-paper "resistance flips by attack family" thread; the new
steelman section is explicitly protected by this round's brief and was
already trimmed once by the writer (draft-handoff reports ~500 words cut to
~330). What remains in both is prose that already passes the delete test —
removing more of it would either cut a fact, a citation-bearing number, or a
reasoning step the commission specifically required (the RAND design context,
the "both directions" closer, the Vassilev caveats). Closing the remaining
gap would require condensing sentences into fewer words, not deleting
material outright — that is writer-level rewriting, past what a clause-sized
surgical fix covers. I am letting W-LENGTH-HIGH stand with this reason
recorded rather than cutting further into protected content.

## Reader

Reader: this now gives me two cross-source syntheses no single cited paper
states — the 01 finding (which model resists a jailbreak best flips by
attack family, not a fixed ranking) plus a new one: which population a
jailbreak's marginal risk gets tested against (an expert red-teamer given
seven weeks vs. a first-time non-scientist searcher) is what decides whether
the "it's already public" argument or its rebuttal looks right, a distinction
built by connecting RAND's own design choice to Soice et al.'s different
population, which neither paper states as connected to the other. The
takeaway now resolves both threads it opened. Prose register holds; the new
paragraphs read at the same Carlini-short-declarative register as the rest.

## Direct edits made

1. Fixed the Kapoor et al. scope mischaracterization ("the jailbreak case" →
   "about open-weight models rather than a prompt jailbreak") in the
   proof-not-measurement section.
2. Cut "Zero, then one, against the same system" (short-of-zero) and "The
   two sit side by side without colliding" (short-of-zero), reattaching
   citations to the sentence before each.
3. Cut "Both sides can be right," "His caveats matter as much as the
   theorems," and "Reaction split" (proof-not-measurement, three topic-
   sentence signposts).
4. Trimmed "on AI and biological-attack planning" from the RAND sentence
   (proof-not-measurement).
5. Updated `nb-meta` "words" from 2588 to 2557 (recomputed by stripping
   tags/scripts from the rendered article). `reading_minutes` stays 13
   (2557 still rounds up to 13 at ~200 wpm); visible byline unchanged.

No markup, script, style, asset, or citation URL was touched. The new
steelman's substantive content, the RAND link, and the both-directions
closer were left exactly as the writer wrote them.

## Required work by owner

None publication-blocking. The one open item is the recorded, honest
W-LENGTH-HIGH warning above — closing it further would need the writer to
condense (not cut) the DEMONSTRATED-band prose or the new section's prose
into fewer words while preserving every number, citation, and reasoning step,
which is a legitimate future ask but not one I can execute as surgical cuts,
and not one that blocks publication on its own: the word count is honestly
reported, the warning is not a BLOCK, and the content it's carrying is
exactly what 01 required.

## Decision

Not publication-blocking. The 01 gap is closed and verified firsthand
against every new primary. One factual mischaracterization was found and
fixed. Length remains over the nominal band after all defensible cuts;
recorded above rather than forced.
