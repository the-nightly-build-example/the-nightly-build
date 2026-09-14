# Editorial review: the-evidence/imagenet-database (editor/01)

## Skeptic

Thesis: the 2009 CVPR paper that introduced ImageNet is a database paper (a
WordNet-backed hierarchy filled with web images and crowd-verified labels), and
the accuracy result the name now evokes belongs to a different paper, a
different team, and a competition subset three years later. The claims it stands
on: (1) the 2009 paper contains no competition and no accuracy score; (2) the
reported 2009 scale is 5,247 synsets and 3.2 million images across 12 subtrees,
against a stated goal of roughly 50,000 synsets and 50 million images; (3) the
labeling method is a per-category vote threshold that reached 99.7% precision on
80 sampled synsets; (4) the famous 15.3% top-5 error is AlexNet's ILSVRC-2012
result, not a 2009 measurement.

I read the controlling primary (Deng et al. 2009) in full and checked each claim
against it. The scale figures, the average of over 600 images per synset, the
~80,000 noun synsets, the ~10% raw search accuracy and >10,000 candidates per
synset, the four query languages, the "at least 10 users" initial vote, the
confidence-table threshold, the Burmese-cat example (Fig. 7: two agreeing votes
give 0.97 for "cat" and 0.83 for "Burmese cat"), the 99.7% on 80 mammal/vehicle
synsets verified by an independent group (Fig. 4), and the Section 4 experiments
arguing that cleaner and more data help recognition all match the paper exactly.
The three angle distinctions the round asked me to protect are held: the piece
says plainly the 2009 paper was not silent on the value of data and confines the
correction to the 2012 jump it did not show; it holds the 99.7% (presence
verification) and the ~6% (single-label error on the ILSVRC validation set)
apart as measurements of different objects; and it attributes the
49,000-workers / 167-countries / 160-million-candidate figures to later
retrospectives, never to the document.

One claim broke against the primary. The article stated the ~50,000-synset,
50-million-image goal "would cover around a tenth of WordNet's nouns." The paper
says the opposite: its abstract aims "to populate the majority of the 80,000
synsets of WordNet," and the "∼10%" figure in Section 5.1 describes the 2009
build, not the goal. Fifty thousand is the majority of eighty thousand, not a
tenth. The right source was already cited on the sentence (s1), so I corrected
it in place to "the majority of WordNet's noun synsets," which the abstract
states directly and which also sharpens the section's ambition-versus-outcome
point. No number, name, or citation target changed.

I opened all seven citation hrefs as printed. s1 (the 2009 PDF), s3 (Wikipedia
ImageNet, which confirms 14.2M/21,841 and attributes the worker figures to a
2017 retrospective), s4 (Russakovsky ILSVRC), s5 (Krizhevsky AlexNet), s6
(Northcutt label-error audit), and s7 (Yang person-subtree audit) all resolve
and land on the source itself. s2 (wordnet.princeton.edu) returns HTTP 403 to
automated agents only, the Cloudflare human-check gate the evidence record
documents; it is WordNet's own homepage and resolves for a human reader, so it
is not a broken link. Every data-nb-kind is correct under the primary/secondary
test: the six primaries own their claims firsthand, Wikipedia is the one
secondary and is used only for the eventual-size and popular-framing context, and
the construction figures that have no primary are presented as secondary
retrospectives rather than smuggled in as the paper's own.

On the round's asset question: the verification method is taught as a prose
scene (disagreement on "Burmese cat" to a per-category threshold), following the
voice guide's model. Fig. 7 would show the same vote panel and confidence table
the prose already walks through. It would not let the reader test the argument
better than the scene does, and the piece's central argument is the
document-versus-shorthand correction, not the voting mechanics. The figure is
not required; I did not request it. AlexNet and top-5 accuracy are linked in
prose as taught ground and appear only as Background rows, not numbered sources,
as the commission requires.

## Cut

Two sentences failed on this pass. One was a body signpost, "The rest of this
lesson is what those three moves produced, how large it really was, and how the
labels were made worth trusting," which both previews structure and refers to
"this lesson" from the body. The lesson template confines self-reference to the
two bookends and holds the body to speaking to no one, and the slop standard
cuts signposts that describe where the piece will go. The three moves were just
named and the following sections deliver them, so deleting it lost no fact; I
cut it and let the paragraph end on the concrete third move. The other was the
false "a tenth" clause, recorded under Skeptic; it is a correction rather than a
slop cut, but it also could not stay.

I ran the delete test on the edge sentences, which is where this piece could
have collected slop. The section openers ("Gathering candidate images was the
easy half," "None of this is why most people have heard of ImageNet") and the
short declaratives the voice guide invites ("That leap is real," "That gap is
the jump," "Both can be true at once") each carry a fact or a reasoning step
tied to the subject's own nouns, so they survive the placeholder test and stay.
The negative constructions ("data, not just algorithms," "not the idea itself,"
"It is not a claim about anything a later program would do") each correct a real,
named misconception the piece is built around rather than a strawman, so they are
the earned kind. I checked the draft against the voice guide's quoted writers and
found no borrowed phrasing, and against the briefing files and commission and
found no leaked instructions or planning labels. No em-dashes, no punctuation
reflexes to repair.

I made two small prose repairs while here. The 2009-scale sentence used "among
them" twice; I changed the second to "in all." And the scale table separated
thousands with spaces (5 247, ~50 000, 21 841) while the body uses commas, so I
aligned the table to commas for within-piece consistency. No values changed.

Against the recent-pattern notes: the headline is a plain finding, not the
named-authors opener or the claim-plus-reversal mold; the dek (after my rewrite)
is neither the number-plus-reversal nor the everyone-quotes-X-not-Y build; no
heading joins two clauses with a comma and "and." The furniture is one scale
table earning its place by putting the reported count, the goal, and the eventual
size side by side, which is the piece's core move; it is not a stacked block.

## Reader

Read straight through, the piece hands the declared reader something the source
papers alone would not: the three things people fuse under the name "ImageNet,"
pulled apart and each set at its true size. I finish knowing the 2009 paper is a
database, not the accuracy result; that it argued data helps but did not show the
2012 jump; that the 99.7% and the ~6% audit measure different objects; and that
the famous construction figures are retrospective, not in the document. The
draft-handoff's original-work sentence claims exactly this disentangling, and the
article delivers it. The prose sits closer to the voice-guide exemplars than to a
median summary: plain committed sentences, numbers placed where the reader can
see what they count, and the verification method taught as a scene. The headline,
read last as the largest claim, is true and defended: the paper contains no
accuracy score, which I confirmed against the document itself.

## Edits

- Rewrote the dek to remove a dangling referent. "The paper it comes from is a database..." had no clear antecedent for a reader arriving from a link; now "That paper is a database: 3.2 million web images hung on a hierarchy borrowed from a dictionary of English, their labels checked by crowd vote, finished three years before the record fell." Updated both the rendered dekline and the nb-meta dek so they stay identical.
- Corrected a factual error against the primary: "which would cover around a tenth of WordNet's nouns" to "enough to fill the majority of WordNet's noun synsets" (the 2009 abstract aims to populate "the majority of the 80,000 synsets"; the paper's "∼10%" describes the 2009 build, not the goal).
- Cut the body signpost sentence "The rest of this lesson is what those three moves produced, how large it really was, and how the labels were made worth trusting."
- Changed the second "among them" to "in all" in the 5,247-synsets / 3.2-million-images sentence.
- Aligned the scale table's thousands separators to commas (5,247; ~50,000; 21,841) to match the body.

## Required work

None. Every issue was fixable within editing against the primary already cited;
no new reporting, redraft, source asset, or chart provenance is owed to the
researcher or the writer.

## Decision

approve — the piece is accurate at honest scale and holds its three distinctions
cleanly; the one broken claim was a mischaracterization I corrected in place
against the cited primary, with no new prose owed.
