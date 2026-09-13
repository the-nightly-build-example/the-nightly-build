# writer brief: when-ai-breaks/retinopathy-field-study (01)

Inputs (all under the artifact root unless noted):
- ../../editorial-direction.md — house standard, slop/headline standards, the paper's voice, the lesson template identity, the series prompt
- ../../writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting
- ../../researcher/01/evidence.md — the complete set of claims and figures available to you; use its recorded URLs and Numbers exactly
- ../../commission.md — the assignment and the desk's order, but read the correction below first
- the initialized article to edit: /home/user/the-nightly-build/.nb-work/when-ai-breaks/retinopathy-field-study/library/when-ai-breaks/retinopathy-field-study.html
- template context: /home/user/the-nightly-build/.nb-work/when-ai-breaks/retinopathy-field-study/.nb-context/

Output: draft-handoff.md (in this directory)

Proof (run from /home/user/the-nightly-build, iterate with --no-check-links, then final with links until BLOCK: 0):
  ./nb stamp .nb-work/when-ai-breaks/retinopathy-field-study/library/when-ai-breaks/retinopathy-field-study.html
  ./nb check .nb-work/when-ai-breaks/retinopathy-field-study/library/when-ai-breaks/retinopathy-field-study.html --series when-ai-breaks --library /tmp/claude-0/-home-user-the-nightly-build/1fc763aa-f362-5066-bfeb-fee58939daaf/scratchpad/library-checkout

Correction to the commission (the evidence record establishes this; follow the record):
- Do NOT claim field diagnostic accuracy collapsed. It held up (about 94.7%, Ruamviboonsuk 2022, Lancet Digital Health). What failed was throughput and patient experience: a conservative image-quality gate rejected roughly a fifth of real-world images in the first months at the studied clinics, and the surrounding system (clinic lighting, cameras, internet, referral distance, patient volume) was not the graded test set. Teach that sociotechnical gap as the lesson, not an accuracy failure.
- Attribute the deployment to Google / Google Health working with Rajavithi Hospital and Thailand's Ministry of Public Health, NOT Verily. Give every named person the role the source states.
- The spine source (CHI 2020) is Google's own, qualitative, and small after deployment (about 5 nurses, 1 technician, ~50 patients observed, 3 clinics); the 21% ungradable figure covers the first six months at three Pathum Thani clinics. State scope with each figure and weigh that it is Google's own study.

Decisions the inputs do not settle:
- Distribution shift is the reader's existing ground (link `when-ai-breaks/waymo-recall` in Background); teach the medical-screening, quality-gate version here rather than re-teaching the concept from zero.
- Set nb-meta tags to concrete topical tags (e.g. medical-ai, deployment, distribution-shift). Fill nb-meta date 2026-09-13, harness, and the writer model you actually ran on.

Recent habits not to inherit (from the recent When AI Breaks record):
- Keep the desk discipline of a named actor, a hard number, and a date up front, but find this piece's own claim, not a recent one's shape.
- Keep the order (built to do / did / who / operator / why / where it lives) but name sections for this incident; no stock labels.
