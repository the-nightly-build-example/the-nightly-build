# editor review-brief: the-evidence/latent-diffusion (01)

Inputs:
- editorial-direction.md (house standard, slop/headline/punctuation rules, press voice, lesson identity, The Evidence prompt)
- commission.md (assignment, boundaries, original-contribution target)
- writer/01/brief.md (the exact writer brief)
- writing-coach/01/voice-guide.md (read first; register and the quoted exemplars the writer read)
- researcher/01/evidence.md (the claim set; reopen sources to try to break claims)
- writer/01/draft-handoff.md (open the original-work sentence only on the third read)
- the article at library/the-evidence/latent-diffusion.html
- template context under .nb-context/

Required fix (orchestrator-confirmed; you can make it directly):
- CLIP IS a taught lesson in this library (the-evidence/clip, on CLIP, Radford et al. 2021).
  The writer's brief wrongly said CLIP had no lesson (the researcher's nb history ran against
  an empty library), so the draft defines the CLIP text encoder inline as if new. House
  standard (press/editorial and lesson identity): link a taught lesson at first use and do not
  re-teach it. Add a Background reading row to the-evidence/clip and replace the inline CLIP
  re-teaching with a plain prose link at first use, keeping only the one clause the argument
  needs in place. This is prose + bookend-reading editing, within your scope; no new evidence
  needed. (denoising-diffusion, attention-is-all-you-need, and gans are the other taught
  Background links; confirm they are used as links, not re-taught.)

Round focus:
- Keep paper and product distinct: the CVPR paper's own experiments (LAION-400M text-to-image)
  versus the Aug 2022 Stable Diffusion release. The CSAM finding and the copyright litigation
  attach to the product's LAION-5B data, NOT the paper's method. Confirm the prose never blurs
  this, and states the UK High Court (Nov 2025) rejected the copying/storage theory while
  Getty's US complaint is an allegation (the UK judgment is sourced via secondary analysis;
  confirm attribution).
- Cost claim discipline: the compute saving is relative/architectural (pixel-space baseline;
  SD itself trained on 256 A100s). Confirm no sentence implies image generation became cheap
  in absolute terms, and that the "runs on a consumer/gaming GPU" capability is NOT stated as
  fact (no source supports it; the writer correctly left it out — do not add it without
  routing to the researcher).
- Numbers: recompute/compare FID and cost figures against the evidence Numbers section and the
  owning primary. FID table values came via an ar5iv HTML mirror (PDF gated); treat as the
  record gives them. Open each citation href; confirm it lands on the source itself.

My recent-pattern notes (catch formulas; compare against the recent library):
- Dek molds: the two-clause "claim, and/so the twist" (deepseek-r1's "...and the $5.6 million
  price tag belongs to a different model"); the comma-triad; the "The [thing] that..." opener.
- Closing body heading mold: recent evidence pieces end on a terse verdict-of-reach heading;
  avoid "The line the paper drew itself" (chain-of-thought used it). Keep the how-it-holds-up
  content; revise the heading if built to a recurring stamp.
- Furniture reflex: nb-note/nb-stat-strip/nb-table by habit. A cost or FID comparison may
  genuinely want a small stat strip or table; remove any component doing no work.
- Orientation heading should be its own concrete step, not a paraphrase of the headline.

You edit prose, structure, and documented furniture directly and log every change; route
numbers/claims/evidence gaps to the writer or researcher. The orchestrator stamps and
re-checks after your edits (your CLIP edit changes word count, so a fresh proof will run).
Decision: approve only when no publication-blocking work remains.
