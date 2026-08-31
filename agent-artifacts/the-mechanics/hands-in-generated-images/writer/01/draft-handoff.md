# Draft handoff: the-mechanics/hands-in-generated-images (writer 01)

## What this draft does to the evidence

The article turns the evidence record's separately-sourced claims into one
behavior-to-cause explanation: it reframes the six-fingered hand as the
predictable output of a denoising objective that never verifies anatomy, holds
the two distinct step-3 causes apart (data scarcity, from the model's maker;
distributional diffuseness from few pixels plus high articulation, from
FoundHand and HanDiffuser), and marks precisely where the account is settled
(the cause) against where it stays soft (no measured base rate, and "solved" as
a moving target) — a separation none of the sources makes on its own.

## Proof result

`./nb check ... --series the-mechanics` (links included): **BLOCK: 0, WARN: 0**,
verdict PUBLISHABLE. `nb stamp` wrote words=1774, reading_minutes=8, sources=8
(6 primary, 2 secondary; series floor of 8 / 4 / 1 met). Word count sits inside
the lesson band (1200-2200). The two `W-SENTENCE-DENSITY` warnings from the
first pass were fixed by splitting the two flagged sentences, not waived.

The check notes that library state was not provided, so open-mode dedupe and
commission cross-checks are skipped locally (the published library is not in
this checkout). The two in-lesson links to `the-mechanics/image-generation`
(Background band and body prose) resolve against that library, not this
worktree.

## Warnings intentionally left

None. Final proof is clean.

## Precision corrections applied (from the brief)

- Frequency kept qualitative throughout. The only prevalence figure used is
  HanDiffuser's 27% "plausible or better," explicitly framed as human-rater
  judgment on one model, not a malformed-hand rate.
- HandRefiner's "97 of 100" is not used anywhere.
- The two step-3 causes are presented in separate paragraphs with separate
  sources, not blurred.
- The failure is marked as receding (scale, data, pose/mesh guidance), not a
  permanent limit; settled-vs-open is carried by the holds-up grid and prose.
- The 16-joint / 27-DOF figure is attributed in prose to ElKoura & Singh 2003
  and cited to HandRefiner (s7) as where it is read, since the researcher did
  not open ElKoura & Singh directly.
- Diffusion denoising is linked (the-mechanics/image-generation), not re-taught,
  and appears as a plain prose link, never a numbered source.

## Furniture

Two components, each discharging an explicit requirement: an "In plain language"
note landing the pivot (the objective scores appearance, never finger count),
and a holds-up grid marking settled cause against soft/open frequency. No source
asset was used: the six-fingered hand is the reader's own premise, so showing
one would be closer to decoration than evidence, and the voice guide leans on
prose and concrete figures.

## Open questions

None for the editor. The "no anatomy/counting step" claim is presented as an
argument from the objective as written (with the steelman that a large model
learns an implicit, imperfect statistical prior), matching the evidence record's
framing note rather than asserting a measured negative.
