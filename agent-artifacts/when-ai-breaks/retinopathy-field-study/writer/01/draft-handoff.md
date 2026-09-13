# Draft handoff: when-ai-breaks/retinopathy-field-study (01)

## Original work
The article sets the model's lab pedigree, its 94.7% field accuracy from the
2022 Lancet follow-up, and the CHI study's 21% ungradable rate beside one another
(in prose and in Fig. 1) to show the failure was a quality-gate and workflow gap
rather than an accuracy collapse. That reconciliation appears in no single source:
the accuracy result and the ungradable rate live in two different papers, and the
piece is what puts them in the same frame and reads distribution shift off the gap.

## Proof
`nb stamp` then `nb check ... --series when-ai-breaks --library <checkout>` with
links: BLOCK: 0, WARN: 0, verdict PUBLISHABLE. words 2160 (band 1200-2200),
sources 8 (5 primary / 3 secondary, series floor met). No warning left standing.

## Notes for the editor
- Followed the brief's correction throughout: no accuracy-collapse claim. The
  lesson is the sociotechnical / image-quality-gate gap. Field diagnostic accuracy
  held (94.7%, ~ retina specialists). Deployment attributed to Google / Google
  Health with Rajavithi Hospital and Thailand's MoPH; Verily is not named. Each
  figure carries its scope (the 21% is the first six months across the three
  Pathum Thani clinics, from Google's own CHI study).
- Distribution shift is linked, not re-taught: a one-clause plain definition plus
  an inline prose link to `when-ai-breaks/waymo-recall`, which is also the first
  Background row. `epic-sepsis-model` is the second Background row as the contrast
  case (a model that really was inaccurate).
- Fig. 1 is a committed chart (`chart-1.py` beside the article), inspected. Two
  accuracy bars in one color, the 21% ungradable share in a distinct color and a
  separate legend series so the share is never folded into an accuracy number; the
  caption states the two bars measure grading on accepted images and the third is
  the share never graded. Cites Lancet 2022 (s7) and CHI 2020 (s1).

## Open questions
- Source-link robustness (no change needed unless CI link-checks more strictly):
  s1 (CHI 2020) uses the canonical dl.acm.org DOI URL from the evidence record,
  which gates automated bots (403) but resolves for a reader; s2 (JAMA) and s4/s7
  (Lancet) gate bots similarly. `nb check --check-links` passed on all of them.
  If CI's link check is stricter, the evidence record also opened an author-hosted
  CHI landing page (research.google/pubs/pub48768) as an alternative for s1.
- No open voice questions.
