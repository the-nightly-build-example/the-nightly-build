# Draft handoff: the-instruments/glue (01)

## Original work

The article converts a scattered record of surpass dates and artifact findings
into a working audit of the "human-level" claim by staging one mechanism the
reader watches happen: MT-DNN clears the GLUE human line only after its single
failing task, WNLI, is lifted off the 65.1 majority-vote floor (human 95.9),
which shows a nine-task average can read as human while a model performs at
chance on one ninth of it. The evidence holds each of these facts separately;
the article assembles them into the "which tasks, whose baseline, what leaks"
test the reader leaves with.

## Proof result

`nb check ... --series the-instruments --library /home/user/library-checkout`
with links: **BLOCK: 0, WARN: 0, PUBLISHABLE.** No warnings left standing.

Sources: 9 total (8 primary, 1 secondary), meeting the min-8 / >=4-primary /
>=1-secondary policy. All source URLs resolve, including the internal Background
link to the published mmlu lesson.

## Framing decisions honored

- The "misleading" is located in reception and shorthand, never in the benchmark
  or model authors: GLUE's authors read saturation as a reason to build
  SuperGLUE, and the DeBERTa team's own caveat ("by no means reaching the
  human-level intelligence of NLU") is quoted directly. Bender & Koller carry
  "saturation is not comprehension."
- Exact dates and baselines used (87.1 passed 6 Jun 2019 at 87.6; 89.8 passed
  6 Jan 2021 at 89.9/90.3), plus the two-week gap between the baseline's late-May
  2019 publication and MT-DNN's pass.
- Artifact reliance framed as model-specific (BERT leans on COPA cues, RoBERTa
  does not); the standing claim is that a high score is *consistent with*
  shortcut exploitation, using the hypothesis-only NLI (~67% / ~53% vs ~33%) and
  COPA cues-only (59.6% vs 50%) figures exactly.
- "Annotation artifact" defined in plain words at first use; mmlu linked as
  Background and re-linked once in prose, not re-taught.

## Open question

Reception is carried by a single secondary (The Gilbane Advisor); the record's
other reception sources were discarded as unreadable (403 / nav-only chrome). If
the editor wants a second downstream data point on how the surpass was framed
publicly, it would need a new researcher artifact, as the current record does not
open one.
