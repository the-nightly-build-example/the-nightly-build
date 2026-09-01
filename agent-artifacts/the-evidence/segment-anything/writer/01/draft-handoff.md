# Draft handoff: the-evidence/segment-anything (01)

## Original work

The article joins three facts the evidence records separately — that the model
drew 99.1% of its own training set, that the only check on those masks covers
500 of 11 million images, and that on the standard AP score the model loses to
the very detector whose boxes it is handed — into one case that Segment
Anything's "foundation model" reputation rests on a segmenter that never names
its objects, never chooses them, and was audited only by the team that built it.

That work is visible in the article: the data-engine section ties the 99.1%
automatic share to the 500-image quality study, and the "Handed the boxes"
section ties the instance-segmentation AP loss to the fact that the detector
supplied every box and class while the model only filled the mask.

## Proof result

`nb stamp` then the full brief command (links included):

```
BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

Stamped: words 1927, reading_minutes 8, sources 6 (3 primary: SAM paper, SA-1B
dataset page, Meta release blog; 3 secondary: Roboflow, Huang et al., MedSAM).
No warning left standing. Em-dash count 0; no banned terms triggered.

## Notes for the editor

- Every body-section claim cites the source that owns it. The two scale/boundary
  tables and the "paper draws its own line" note all cite the SAM paper (s1)
  with section locators from the evidence record. The "400x / 6.5x faster"
  comparison is Meta's own launch framing, cited to the blog (s3), and flagged
  in-prose as Meta's framing.
- The contradiction the evidence flagged (SAM's AP loss vs. the paper's own
  argument that COCO ground truth is low-quality and raters preferred SAM's
  masks) is carried in prose in the "Handed the boxes" section: both framings
  reach the reader, then the section makes the deeper point that SAM never
  picked an object.
- Background links go to the published `vision-transformer`, `clip`, and
  `denoising-diffusion` lessons; they are linked, not re-taught, per the
  commission's boundary. The masks-not-labels spine is kept sharp against
  CLIP's class-from-text output.

## Open questions

None. The evidence settled every claim the draft rests on. The mask-quality
thin spot (500-image internal study, no independent audit of the 1.1B) is
reported as such in the data-engine section, which is the honest state of the
record rather than a gap to resolve.
