# Commission — when-ai-breaks/google-flu-trends

## Assignment
Teach one real, deployed failure: Google Flu Trends (GFT). Google built a model
that predicted regional flu prevalence from search queries, launched it in 2008,
was praised in Nature, then watched it drift badly wrong, most visibly missing
the 2009 swine-flu wave and then overestimating the 2012-2013 season by roughly
double the CDC's later figure, before Google quietly retired the public product
in 2015. Tell it in order, name names and dates, then explain why this class of
system fails this way, and where the same weakness lives today.

## Angle
Order the narrative: what it was built to do (nowcast influenza-like illness ~2
weeks ahead of CDC's lagged reports, from aggregated search terms), who built it
(Google.org / Google researchers; Jeremy Ginsberg et al., Nature 2009), what it
actually did (the drift: over-prediction, the swine-flu miss), who it affected
(public-health users who might have relied on it; and the broader "big data
hubris" lesson), and what the operator did after (updated the model repeatedly,
then shut the public site in Aug 2015 and moved to giving data to partners).

Then the mechanism, taught on the spot (the reader may not have it): the model
correlated search terms with CDC flu rates over a training period, but (a) the
relationship was not stable — search behavior changed, partly because media
coverage of flu drove flu-related searches independent of actual illness; (b)
Google's own search algorithm changed (autocomplete, recommended searches) during
the model's life, altering the inputs underneath a frozen relationship; (c) the
model was tuned on a small number of seasons and picked up seasonal correlates
(some terms correlated with winter, not flu). This is distribution shift plus
overfitting plus a feedback loop. Connect to the-mechanics/knowledge-cutoff
(a model's fitted relationship is frozen while the world moves) — link, don't
re-teach. The Lazer et al. 2014 Science paper "The Parable of Google Flu: Traps
in Big Data Analysis" is the definitive post-mortem; use it as the analytical spine.

Close where the weakness lives now: any deployed model whose inputs are generated
by a world that reacts to the model or drifts from training — recommender systems,
predictive-policing and fraud scores fit on historical data, LLMs relying on a
frozen training distribution, "AI nowcasting" of the economy. Keep this concrete
and cited, not a generic moral.

Where the cause is discussed, present the strongest account: Google's own updates
vs the outside critique. The Lazer critique and Google's responses/other analyses
(e.g., Cook et al. 2011 on the 2009 revision; Santillana et al. on later fixes)
give the disputed-cause material the desk wants.

## Intended reader
House reader who has heard "big data can predict flu from searches" as a success
story and does not know it failed or why.

## Required contribution
The reader can explain why a model that fit search terms to flu rates went wrong
even though nothing was "broken," and can recognize the same distribution-shift /
feedback-loop failure in systems they use.

## Source obligations (when-ai-breaks: min 8; primary >=4, secondary >=1)
Work from the record: the papers, the post-mortems, the reporting that held up.
- PRIMARY: Ginsberg et al., "Detecting influenza epidemics using search engine
  query data", Nature 2009 — the original design and claims. Read the method and
  the reported accuracy.
- PRIMARY: Lazer, Kennedy, King, Vespignani, "The Parable of Google Flu: Traps in
  Big Data Analysis", Science 2014 — the definitive critique; read the exact
  over-estimation figures (e.g., the ~2x / 100%+ over CDC across the 2011-2013
  interval, and the 100 of 108 weeks it overshot).
- PRIMARY: Cook et al. 2011 (PLoS ONE) on GFT's 2009 (swine flu) failure and the
  model revision — firsthand.
- PRIMARY: Google's own record — the 2009/2013 model-update posts / the 2015
  shutdown announcement (Google Research blog) — for what the operator did.
- PRIMARY candidate: Santillana et al. or Lazer's follow-ups for later analysis.
- SECONDARY: contemporaneous reporting that held up (e.g., a 2014-2015 piece in a
  reputable outlet) for context only.
- Verify every number against the owning primary. The "overestimated by ~double"
  and "missed swine flu" claims must trace to Lazer/Cook exactly, not to retellings.
  Seek contradiction: defenders argued GFT was never meant to replace CDC and that
  post-2013 fixes improved it — represent that fairly.

## Starting sources
Ginsberg 2009 (Nature); Lazer 2014 (Science, "Parable of Google Flu"); Cook 2011
(PLoS ONE); Google Research blog shutdown post (2015). Researcher verifies/completes.

## Relevant prior coverage (link, do not re-teach)
- the-mechanics/knowledge-cutoff — a fitted/frozen relationship while the world
  moves. Natural Background link for the distribution-shift mechanism.
- when-ai-breaks/zillow-offers and /epic-sepsis-model are neighbors: both are
  distribution-shift/overfit deployment failures. Do NOT reuse their structure or
  their framing lines; GFT's distinctive twist is the feedback loop (media and
  Google's own algorithm changing the inputs). Foreground that to stay distinct.

## Structures NOT to repeat
- when-ai-breaks headlines lean on a single stark number or a name+harm ("A Cruise
  robotaxi... dragged her 20 feet", "spent 30 hours in a jail cell"). A number is
  fine if it is the story (the ~2x overestimate), but do not copy the victim-harm
  cadence; GFT's harm is epistemic, not bodily — be honest about that, do not
  inflate it into physical harm.
- No colon-subtitle headline; no hedged-contrast dek; no scenario-triad open.

## Neighboring articles tonight
This is the only failure-incident piece and the only one centered on distribution
shift / prediction drift. Distinct from the four AI-language-model pieces.

## Template / mode / paths
- template: lesson; mode: open; order: null; date: 2026-08-01.
- article: .nb-work/when-ai-breaks/google-flu-trends/library/when-ai-breaks/google-flu-trends.html

## Harness / model
writer: claude-code-routine / claude-sonnet-5 / medium. researcher high, editor
high, coach low; all claude-sonnet-5.

## Tags
Suggest: ["distribution-shift", "big-data", "public-health", "overfitting"]. Writer finalizes.
