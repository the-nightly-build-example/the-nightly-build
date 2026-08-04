# writer brief: the-evidence/alexnet (02) — revision

Apply the two publication-blocking items in editor/01, both owned by you. The
editor already fixed the Recht content error by direct cut and re-stamped
(words 2131); preserve that. Do not expand the claim set or re-litigate settled
work.

Inputs:
  ../../editor/01/editorial-review.md — the review to apply (the two writer items)
  ../01/brief.md — the original writer brief (round 01)
  ../../commission.md, ../../editorial-direction.md, ../../writing-coach/01/voice-guide.md, ../../researcher/01/evidence.md — unchanged context
  ../../../../library/the-evidence/alexnet.html — the article to revise (with chart-1.py / chart-1.png beside it)
Output: ./draft-handoff.md
Proof (links included, until BLOCK: 0):
  ./nb check .nb-work/the-evidence/alexnet/library/the-evidence/alexnet.html --series the-evidence --library /home/user/library-checkout

Required items:
1. Chart honesty (blocking). chart-1 plots only 2010/2012/2014 and connects them
   with a straight line, asserting a continuity the record lacks — the 2011
   (~26%) and 2013 winners are omitted, flattening AlexNet's 2012 break. Rebuild
   the chart with every annual ILSVRC top-5 winner 2010–2014 (values from the
   evidence record / Russakovsky et al. 2015, s2 — verify each against the
   owning primary), or use a form that does not imply the missing years. Keep
   axes labeled and the zero baseline. Re-render with `nb chart`, inspect the
   PNG as a reader (the 2012 break must read honestly), and commit the updated
   chart-1.py provenance.
2. Byline placeholder (blocking, display). The visible byline reads literal
   "N min read"; `nb stamp` writes only nb-meta (reading_minutes=9). Fill the
   byline with the stamped value ("9 min read") so display text is honest.

Then run `nb stamp` and prove with links included until BLOCK: 0, and redo the
display-text pass on anything you touched.
