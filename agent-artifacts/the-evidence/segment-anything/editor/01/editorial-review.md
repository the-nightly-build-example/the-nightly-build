# Editorial review: the-evidence/segment-anything (editor/01)

## Skeptic

Thesis: Segment Anything's "foundation model" reputation rests on a segmenter
that returns masks with no names, drew 99.1% of its own training set, was
checked on only 500 of its 11 million images, and loses zero-shot to the very
detector whose boxes it is handed. The piece states this cleanly, and the four
claims it stands on are all in the display text and the two tables.

Claim 1 — SAM outputs a mask, never a class label. Held. The paper (Sec. 3, 5)
and the SA-1B page both say masks are class-agnostic; the SA-1B page confirms
"class agnostic mask annotations." The headline, the orientation section, and
the discussion quote all carry it, and the boundary stays sharp: the piece never
lets the mask acquire a name.

Claim 2 — SA-1B is ~1.1B masks on 11M images, 99.1% fully automatic, via a
three-stage engine. Held against the evidence Numbers and the SA-1B page (1.1B
masks, 11M images, ~100/image, fully automatic). Per-stage counts (4.3M / 20→44
/ 34s→14s / 6 retrains; 5.9M / 44→72 / 10.2M cumulative; 1.1B / ~100) all match
the record. The 99.1%-automatic and 0.9%-human-touched split checks out.

Claim 3 — the only quality check is Meta's own 500-image study (94% of pairs
>90% IoU), with no independent audit of the 1.1B. Held; the article reports the
thinness plainly rather than writing around it, which is the honest state of the
record.

Claim 4 — handed a detector's boxes, zero-shot SAM still trails the specialist
on mask AP (COCO 46.5 vs 51.0, LVIS 44.7 vs 46.6). Held against the paper's
Sec. 7.4 table as recorded. The framing is fair: it carries both the number and
the paper's own contest of the metric, then makes the deeper point the setup
conceded — SAM never picked an object; the detector supplied every box and class.

One break. The object-proposal concession read "even while it leads on the rare
and large ones." On large objects the paper's table gives AR 86.9 (SAM) vs 87.0
(ViTDet-H) — the record calls this "essentially tied," and SAM is in fact
marginally behind, so it does not lead there. The claim rested on the paper's
prose summary, not its table, in a sentence that explicitly tells the reader to
read the table. I changed "large" to "medium" (81.6 vs 80.8, a real lead in the
record), so the named slices are ones the table actually supports. No number
altered; the citation still points at the same Sec. 7.3 table.

Citations: I opened all six hrefs as printed. s1 (arXiv 2304.02643) is the SAM
paper; s2 is the SA-1B page; s3 is Meta's release blog (confirms the "first
foundation model" framing, 400x, 6.5x); s4 is the Roboflow breakdown (confirms
foundation-model framing, "GPT-esque moment," text prompting not shipped); s5
(arXiv 2304.14660) is Huang et al. and confirms the COSMOS "1050K images / 6033K
masks" — the 58.52% Dice sits in the full text the evidence record read. s6 is
the Nature MedSAM page; it answers with Nature's standard cookie 303 that
resolves back to the article, so it lands on the source for a browser (the record
already noted this and read the abstract numbers from the arXiv twin). All three
`data-nb-kind` labels I could test (s1–s3 primary, s4–s6 secondary) match the
primary/secondary test: the paper and Meta's own pages own their claims; Roboflow
and the two medical evaluations are outside authors reporting on SAM. Internal
Background links to vision-transformer, clip, and denoising-diffusion all resolve
to existing library files.

Brief focus confirmed: the class-agnostic / 99.1% / 500-of-11M synthesis and the
handed-the-boxes AP loss both hold against the owning primaries; CLIP and the
vision transformer are linked as Background (CLIP as the class-from-text
contrast, ViT as the image encoder), not re-taught.

## Cut

Four sentences failed the slop or reader-address test and were fixed in place.

- The data-engine paragraph opened "A billion machine-drawn masks are only as
  useful as they are accurate, and here the evidence thins out." The first clause
  is an interchangeable truism and the second a signpost about the article's own
  evidence. Rewrote to a concrete sentence that keeps the reasoning step (the
  accuracy of the automatic masks rests on a single check) and leads straight
  into the 500-image study.
- In the specialist section, "Both things are true, and the reader should hold
  them together" both signposts and addresses the reader — the lesson body speaks
  to no one, and the sentence does no reasoning the next one ("The number favors
  the specialist; the paper contests what the number measures") does not already
  do. Cut.
- "But notice what the setup already conceded" opened on the lecturing imperative
  the slop file rules out (the Note/Consider/Imagine family). Recast as "But the
  setup had already conceded the real point," keeping the pivot without the
  imperative.
- "The other tests land the same way when you read the table rather than the
  prose" leaned on a flat "land the same way" and a generic reader-you. Rewrote
  to "The same gap between prose and table shows up in the other tests," which
  keeps the analytical point (the paper's prose runs ahead of its tables) and
  drops the address.

Formula check against the recent-pattern notes. Heading "Three stages, and the
people drop out" was the comma-and join the notes flag; retitled to "The people
drop out over three stages," concrete and single-clause. The opener does not
inherit the "what X is counting" / "the paper that..." mold — it walks one prompt
(click a dog, drag a box). The piece closes on the required takeaway bookend, not
a bare assessment heading or a leftover Verdict block. The dek states a finding
with one number but avoids all three banned molds (no comma-triad, no
semicolon-reversal, no suspended question) and adds what the headline leaves out
rather than restating it; I left it.

No borrowed phrasing from the voice-guide exemplars (Alammar, Olah, Weng) — the
worked prompt, the data-engine walk, and the box-filling image are the article's
own. No prompt leakage: "foundation model" and "segmentation is solved" reach the
reader as attributed discourse (Meta's launch, independent coverage), not as the
commission's instruction. Furniture is right-sized: two tables for the two
load-bearing numeric comparisons, one quotation note for the paper's own
boundary. No component is doing decorative work.

## Reader

Read straight through, the declared reader ends able to say what SAM takes in (a
point, box, or rough mask — a place, not a phrase), what it returns (a mask with
no name), where the billion masks came from (a three-stage engine that sheds
human effort until 99.1% is the model's own work, audited on 500 of 11M images),
and why "segmentation is solved" claims more than the paper measured (handed a
detector's boxes, zero-shot SAM still trails on AP; the medical gains arrived only
after fine-tuning). What the piece gives past its sources is the join: three facts
the record keeps apart become one case that the "foundation model" reputation
rests on a segmenter that never names or picks its objects and was audited only by
its makers. That matches the draft-handoff's original-work sentence, and both
survive — this is synthesis, not restatement. The prose sits with the voice-guide
exemplars: concrete instance before the abstract term, each term of art glossed
where it enters, limits reported in the same flat voice as the headline count.
The headline holds as the largest claim the body defends.

## Edits

- Retitled section heading "Three stages, and the people drop out" to "The people
  drop out over three stages" (broke the flagged comma-and join).
- Rewrote the data-engine paragraph opener, cutting the "only as useful as they
  are accurate ... the evidence thins out" truism-plus-signpost to a concrete
  sentence leading into the 500-image study.
- Cut "Both things are true, and the reader should hold them together" (signpost
  and reader-address, no reasoning of its own).
- Recast "But notice what the setup already conceded" as "But the setup had
  already conceded the real point" (dropped the lecturing imperative).
- Rewrote "The other tests land the same way when you read the table rather than
  the prose" to "The same gap between prose and table shows up in the other tests"
  (kept the point, dropped the flat signpost and the reader-you).
- Corrected the object-proposal slice from "the rare and large ones" to "the rare
  and medium ones" (the table has SAM behind on large, 86.9 vs 87.0; medium is a
  real lead, 81.6 vs 80.8). No number changed.

## Required work

- orchestrator: my edits changed prose, so the stamped word count and reading
  time are now slightly stale. Run `nb stamp` then `nb check` before the PR; the
  piece stays well inside the 1200–2200 band.

No work for the researcher or the writer: the evidence settled every claim, and
no reporting, redraft, asset, or chart provenance is needed to publish.

## Decision

approve — the load-bearing synthesis holds against the primaries, every citation
lands on its source, and the one factual slip (the "large" slice) plus four slop
or reader-address sentences are fixed in place; a fresh stamp is all that remains.
