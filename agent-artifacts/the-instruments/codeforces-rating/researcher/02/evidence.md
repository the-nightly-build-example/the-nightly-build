# Evidence: the-instruments/codeforces-rating (02)

Round 02 preserves round 01 in full and adds one source: a major-press report
(VentureBeat) that carries o3's 2727 Codeforces figure into circulation without
its estimated/simulated qualifier, comparing it to a named human's rating. That
is the eighth source and the concrete instance of the launch gloss the article
discusses. Nothing from 01 is retracted.

The evidence supports the commission's core mechanism firsthand. Codeforces' own
post defines the rating as an Elo generalization scored against the other people
in a contest, so any single number is a standing inside a live human field.
Every AI "Codeforces rating" in circulation is traced to the document that owns
it, with its exact conditions: AlphaCode's top 54.3% and estimated 1238 rating
(Li et al., DeepMind), and OpenAI's series from GPT-4o at 808 to o3 at 2724, all
from simulated contests. Two conditions the headline numbers drop are documented
by the producers themselves: AlphaCode used up to a million samples per problem
before filtering to ten submissions, and OpenAI's o1 rating moves from 1673 to
2214 depending on hand-crafted test-time strategies. The evidence is thin in one
place the commission may lean on: the "contamination inflated a Codeforces
rating" story does not hold for the frontier case. The one primary that looked
for contamination on Codeforces (LiveCodeBench) found the inflation signal on
LeetCode and not on Codeforces. And the angle that these numbers never touched
the real judge is partly wrong: AlphaCode did submit to the live Codeforces
judge, on past contests. Both are recorded under Contradictions.

## Sources

```text
URL:         https://codeforces.com/blog/entry/20762
Kind:        primary — Codeforces defines its own rating system here; author is
             the site's founder.
Establishes: How a Codeforces rating is produced. It generalizes Elo to contests
             with many participants; each contestant's rating change depends on
             how their actual place compares to their expected place (seed).
Paraphrase:  The rating generalizes Elo to games with multiple participants.
             A 200-point gap implies the stronger player beats the weaker with
             probability about 0.75; a 400-point gap, about 0.9. Before a round,
             each contestant's seed (expected place) is computed by summing win
             probabilities against every other entrant. After the round, the
             rating rises if the actual place beats the seed and falls if it is
             worse. The number is therefore a position relative to the specific
             field that showed up.
Locators:    Opening section "General ideas"; author MikeMirzayanov; post updated
             October 2015.
Quote:       "The basic idea of Codeforces rating system is to generalize Elo
             rating to support games with multiple participants." "if the
             difference of ratings is equal to 200 then stronger participant will
             win with probability ~0.75. If the difference of ratings is equal to
             400 then stronger participant will win with probability ~0.9."
Note:        codeforces.com sits behind a Cloudflare interstitial that blocks
             direct fetch (returns the challenge page, not the article). The
             address above is the document's own page; its text was read through
             a reader transport. The article resolves for a human browser.
```

```text
URL:         https://codeforces.com/blog/entry/20638
Kind:        primary — Codeforces' founder setting the title/color thresholds.
Establishes: The rating bands and their titles, as set in this post.
Paraphrase:  The scheme in this post: Newbie 0–1199, Pupil 1200–1399, Specialist
             1400–1599, Expert 1600–1899, Candidate Master 1900–2199, Master
             2200–2299, International Master 2300–2399, Grandmaster 2400–2599,
             International Grandmaster 2600–2899, Legendary Grandmaster 2900+.
             The post announces the cyan band and shifts colors upward.
Locators:    Body table; author MikeMirzayanov; post from ~2013.
Note:        These are the thresholds as of this 2013 post. Codeforces has since
             adjusted the top bands (the site now uses International Grandmaster
             2600–2999 and Legendary Grandmaster 3000+, and Master 2100–2299).
             An article stating a single canonical threshold set must date it;
             the exact top-band cutoffs depend on the year. Read through a reader
             transport for the same Cloudflare reason as above.
```

```text
URL:         https://codeforces.com/blog/entry/68288
Kind:        secondary — hosted on Codeforces but authored by the user EbTech
             (author of the Elo-MMR rating method), not Codeforces staff. It
             reports one snapshot of the distribution, it does not own the rating
             definition.
Establishes: That a Codeforces rating is read as a percentile of the active
             player pool, and the size of that pool at one date.
Paraphrase:  EbTech tabulates rating against percentile of players active in the
             past six months, computed over 99,832 such players as of 30 May
             2021. "Percentile" here means the fraction of that active pool below
             a given rating. This confirms the relative-standing framing the
             AlphaCode and OpenAI papers both rely on for their percentile
             claims: the denominator is recently active contestants, not all
             humans or all programmers.
Locators:    Distribution table near the top; author EbTech; dated 30 May 2021.
Quote:       Bands are labeled as "subsets of the 99832 players who've competed on
             Codeforces in the past 6 months."
Caution:     EbTech's table uses his own binning (e.g. it lists a "Pupil" band at
             1000–1199 and an "Apprentice" band at 1200–1399), which does NOT
             match Codeforces' official titles from entry/20638. Do not present
             EbTech's bands as Codeforces titles. Use it only for the
             rating→percentile idea and the active-pool denominator.
```

```text
URL:         https://arxiv.org/abs/2203.07814
Kind:        primary — the AlphaCode authors' own report (Li et al., DeepMind).
             This is the open preprint of the paper published as Li et al.,
             Science 378, 1092 (2022), doi:10.1126/science.abq1158; the top
             54.3% figure is identical to the Science abstract.
Establishes: AlphaCode's Codeforces result and every condition attached to it.
Paraphrase:  AlphaCode averaged a ranking in the top 54.3% across 10 Codeforces
             contests, each with more than 5,000 participants, held 2021/12/01
             to 2021/12/28. From those placements the authors estimate a
             Codeforces rating of 1238, which they say is within the top 28% of
             users active in the last six months (equivalently, greater than 72%
             of them). The system generated up to roughly a million candidate
             programs per problem, then filtered and clustered to at most 10
             submissions (the "10@k" setting), averaging 2.4 submissions per
             solved problem. Crucially, the authors did submit the selected
             candidates to the real Codeforces judge and computed placements
             against the real standings; they call this "simulated running
             AlphaCode live" because the contests were already over. The rating
             is their estimate, the percentile ranks use a simulated time
             penalty, and the paper gives upper/lower bounds depending on how
             many accelerators were used to sample.
Locators:    Abstract; Section 1 (Figure 1 and footnotes 3–4); Section 5.1
             "Codeforces competitions evaluation"; the 10@k definition in the
             metrics section.
Quote:       "In simulated evaluations on recent programming competitions on the
             Codeforces platform, AlphaCode achieved on average a ranking of top
             54.3% in competitions with more than 5,000 participants." "we
             estimate that our system has achieved a Codeforces rating of 1238
             which is within the top 28% of users who have participated in a
             contest in the last 6 months." "We submitted these selected
             candidates to the Codeforces platform, and computed AlphaCode's
             placement in each contest." "scale to millions of samples per
             problem." "an actual average of 2.4 submissions for each problem
             solved."
```

```text
URL:         https://arxiv.org/abs/2502.06807
Kind:        primary — OpenAI's own paper, "Competitive Programming with Large
             Reasoning Models." It owns the o1/o1-ioi/o3 Codeforces numbers and
             restates the o1 figure first published on OpenAI's o1 blog.
Establishes: The full model rating series and the conditions that move it.
Paraphrase:  Ratings, all from OpenAI's simulated Codeforces contests: GPT-4o
             808 (11th percentile); o1-preview 1258 (62nd); o1 1673 (89th);
             o1-ioi 1807 (93rd), rising to 2214 (98th) with the full hand-crafted
             test-time strategy; o3 2724 (99.8th). OpenAI states the contests
             were simulated under conditions that mirror real ones, using each
             problem's full test suite and real time and memory limits, and that
             ratings were fit by maximizing the likelihood of the observed
             rankings. The paper's central comparison: o1-ioi relied on
             IOI-specific, hand-engineered test-time strategies (clustering and
             reranking, similar to AlphaCode), while o3 surpassed it without
             them, its test-time reasoning emerging from end-to-end RL. The same
             base model o1 therefore reports as 1673 or 2214 depending on the
             scaffolding wrapped around it.
Locators:    Abstract; results (Figure 3 and surrounding text); conclusion.
Quote:       "Further training pushed o1's rating to 1673 (89th percentile)."
             "o1-ioi reached a CodeForces rating of 1807, outperforming 93% of
             competitors ... attaining a rating of 2214 (98th percentile)." "the
             transition from the o1-ioi model to o3 resulted in a rating increase
             from 2214 (98th percentile) to 2724 (99.8th percentile)." "o3
             outperforms o1-ioi without relying on IOI-specific, hand-crafted
             test-time strategies." "We simulated CodeForces contests under
             conditions that closely mirrored real competitions."
```

```text
URL:         https://arxiv.org/abs/2403.07974
Kind:        primary — the LiveCodeBench authors' own contamination analysis
             (Jain et al.). Firsthand for the measurements it reports.
Establishes: What the contamination signal looked like, and where it did NOT
             appear. This is the source that tests the commission's contamination
             sub-angle.
Paraphrase:  LiveCodeBench collects problems from LeetCode, AtCoder, and
             Codeforces with release dates, then checks whether a model does
             worse on problems released after its training cutoff. For
             DeepSeek's instruction-tuned model the authors find a sharp drop on
             problems released after its cutoff, but they state the drop occurs
             on LeetCode problems specifically and that performance is smooth
             over time for the other platforms, including Codeforces. For
             GPT-4-Turbo, Gemini-Pro, Claude-3, and Mistral they report no
             drastic time-based variation.
Locators:    Contamination section, with the DeepSeek/LeetCode figure and the
             cross-platform comparison.
Quote:       "DeepSeek-Instruct performs considerably worse on problems released
             since September 2023." "This drop in performance primarily occurs
             for the LeetCode problems only and ... the model performance is
             relatively smooth across the months for problems from other
             platforms."
```

```text
URL:         https://arxiv.org/abs/2409.05824
Kind:        primary — Roy and Roy (University of Saskatchewan) report their own
             experiment; published as doi:10.1145/3674805.3686689, ESEM '24.
Establishes: How general-purpose LLMs perform when actually run through
             Codeforces contests, judged by the real online judge.
Paraphrase:  The authors ran ChatGPT, Gemini, and Meta AI on 126 Codeforces
             problems and entered nine virtual contests across Codeforces and
             LeetCode, submitting to the real judges. In the harder Codeforces
             contests (Division 1 and Division 2) the models did poorly; they did
             better in the easier Division 4 (outperforming 63.32% of
             participants) and Division 3 (69.76%), and struggled in the
             Educational contest. On LeetCode weekly/biweekly contests they beat
             an average of 53.7% of users. This is an independent grading through
             contest conditions, and it lands well below the frontier estimated
             ratings, on a different (non-reasoning) model generation.
Locators:    Abstract; RQ3 results (virtual-contest standings) and Table 3.
Quote:       "they struggled in virtual contests, especially on Codeforces."
             "they outperformed an average of 53.7% of users [on LeetCode] ...
             their performance was poor in the more challenging Codeforces
             contests (Division 1 and Division 2)."
```

```text
URL:         https://venturebeat.com/ai/openai-confirms-new-frontier-models-o3-and-o3-mini/
Kind:        secondary — VentureBeat reports OpenAI's December 2024 o3
             announcement. It does not own the figure; it relays the launch
             number and frames it against a named human's rating. This is the
             evidence that the o3 number entered general circulation stripped of
             its estimated/simulated condition.
Establishes: That major tech press carried o3's Codeforces rating as a flat
             2727 and glossed it by human comparison, without the caveat that it
             is an estimate from OpenAI's simulated contests.
Paraphrase:  VentureBeat reports o3's Codeforces rating as 2727 and immediately
             compares it to a specific person's rating, calling it a rating that
             beats OpenAI's chief scientist. The article gives the number and the
             human comparison without stating that the rating was estimated from
             simulated contests. This is the launch gloss the article critiques,
             in a reputable outlet: the 2727 also differs from the 2724 OpenAI's
             own paper reports.
Locators:    Body, in the o3 benchmark rundown; authors Emilia David and Carl
             Franzen; dated 20 December 2024.
Quote:       "achieves a Codeforces rating of 2727, outperforming OpenAI's Chief
             Scientist's score of 2665."
```

## Contradictions

- The "these numbers never went through the real judge" framing is partly false.
  AlphaCode submitted its selected programs to the live Codeforces judge and
  read real placements (arxiv 2203.07814, Section 5.1). What is estimated is the
  rating derived from those placements and the time penalty, not the pass/fail of
  each submission. The honest distinction is live-contest entry in one sitting
  versus retroactive submission to a finished contest, not judged versus
  unjudged.

- The contamination sub-angle does not hold for Codeforces in the one primary
  that looked. LiveCodeBench found the memorization-driven inflation on LeetCode,
  and explicitly reported that Codeforces performance was smooth over time for
  the same model (arxiv 2403.07974). If the article claims a Codeforces rating
  was inflated by training-data contamination, this source cuts against it. The
  contamination concern is real for code benchmarks in general; the clean
  Codeforces-specific example is not in hand.

- OpenAI states its simulated contests "closely mirrored real competitions" with
  full test suites and real time/memory limits (arxiv 2502.06807). A reader could
  take that as evidence the estimates are trustworthy. It cuts against a blunt
  "simulations are unrealistic" claim. The load-bearing caveats survive it
  anyway: the rating is still fit to simulated rankings rather than earned live,
  and it depends heavily on test-time scaffolding (1673 vs 2214 for the same
  model).

- The o3 figure is quoted two ways. OpenAI's paper reports 2724 (99.8th
  percentile) from simulated contests (arxiv 2502.06807). VentureBeat's launch
  report gives 2727 and compares it to a named human's rating, with no
  estimated/simulated qualifier (venturebeat.com, 20 Dec 2024). The widely
  repeated "175th best competitive programmer" gloss traces to the December 2024
  o3 livestream and its coverage; treat 2724 as the verified figure, 2727 as the
  circulated launch number, and "175th" as a livestream gloss not owned by a
  primary document I could open.

## Numbers

```text
Figure: probability ~0.75 (200-point gap), ~0.9 (400-point gap)
Owner:  Codeforces (entry/20762)
Scope:  Win probability between two contestants by rating difference; defines the
        Elo generalization.
```

```text
Figure: AlphaCode top 54.3% average ranking
Owner:  Li et al., DeepMind (arxiv 2203.07814 / Science 2022)
Scope:  Averaged over 10 Codeforces contests, each >5,000 participants, held
        2021/12/01–2021/12/28; up to ~1M samples/problem filtered to ≤10
        submissions; submitted to the real judge on finished contests.
```

```text
Figure: AlphaCode estimated rating 1238 = top 28% (> 72%) of active users
Owner:  Li et al., DeepMind (arxiv 2203.07814)
Scope:  Estimated from the 10-contest placements; denominator is users active in
        the last 6 months. Rating is an estimate, not a live-earned rating.
```

```text
Figure: GPT-4o 808 (11th pct); o1-preview 1258 (62nd); o1 1673 (89th);
        o1-ioi 1807 (93rd) → 2214 (98th) with full strategy; o3 2724 (99.8th)
Owner:  OpenAI (arxiv 2502.06807)
Scope:  Estimated from OpenAI's simulated Codeforces contests (full test suite,
        real time/memory limits); percentiles fit to simulated rankings. o1's
        number moves 1673→2214 with hand-crafted test-time strategies.
```

```text
Figure: o3 = 2727, compared to a rating of 2665 (OpenAI's chief scientist);
        "175th best competitive programmer" in the launch gloss
Owner:  VentureBeat report of the o3 announcement (2727, human comparison);
        "175th" from the December 2024 livestream via secondary coverage
Scope:  Launch/circulated figures; the 2727 differs from the paper's 2724, and
        both the human comparison and "175th" gloss omit the estimated/simulated
        condition.
```

```text
Figure: Codeforces active-pool size 99,832 players (past 6 months)
Owner:  EbTech (entry/68288)
Scope:  Snapshot as of 30 May 2021; the denominator behind percentile readings.
```

```text
Figure: LLMs (ChatGPT/Gemini/Meta AI) beat 63.32% (Div 4), 69.76% (Div 3) of
        participants; poor in Div 1/Div 2
Owner:  Roy & Roy (arxiv 2409.05824 / ESEM '24)
Scope:  Nine virtual contests on Codeforces/LeetCode, real judge; non-reasoning
        model generation; harder divisions are where top-rated humans compete.
```

Preserved series for a possible chart (model, estimated Codeforces rating,
percentile, all from OpenAI arxiv 2502.06807): GPT-4o 808 / 11th; o1-preview
1258 / 62nd; o1 1673 / 89th; o1-ioi 1807 / 93rd; o1-ioi full strategy 2214 /
98th; o3 2724 / 99.8th. AlphaCode's comparable point (Li et al., 2203.07814):
1238 / top 28%. A rating axis anchored to Codeforces titles (Pupil 1200,
Expert 1600, Grandmaster 2400) lets a reader place each model.

## Source assets

```text
Asset: AlphaCode Figure 1 — (a) AlphaCode's ranking in 10 contests against the
       rating-vs-ranking curve of participants; (b) its estimated rating on the
       Codeforces rating distribution. In arxiv 2203.07814, Section 1.
Shows: Visually, that "top 54.3%" and "1238" are a placement inside a real
       human field, and where AlphaCode sits on the active-user rating curve.
Crop:  Keep both panels' axes and the AlphaCode marker; a crop must retain the
       rating scale so the placement is legible. Do not crop away the axis
       labels.
```

```text
Asset: OpenAI Figure 3 — the o1-ioi / o3 Codeforces rating comparison. In arxiv
       2502.06807.
Shows: The jump across models and the effect of test-time strategy, in one
       image.
Crop:  Retain the rating axis and every model label; the point is the spread
       from ~800 to ~2700, so no single bar can be cropped out.
```

```text
Asset: Codeforces title/color table. In entry/20638.
Shows: The named bands a rating maps to, so a reader can read 1238, 1673, 2724
       as Pupil/Expert/International-Grandmaster territory.
Crop:  If used, reproduce as a small labeled table rather than a screenshot;
       date it, because the top-band cutoffs have shifted since the 2013 post.
```

## Discarded

```text
https://openai.com/index/learning-to-reason-with-llms/: OpenAI's original o1
  blog (source of "1673, 89th percentile"). Returns HTTP 403 to every fetch
  transport tried; not opened. The same figure is stated in OpenAI's own paper
  (arxiv 2502.06807), which was opened, so the number is cited from there.
https://openai.com/12-days/ and the OpenAI o3 launch page: returns HTTP 403 to
  every transport tried; not opened. The launch figure is carried instead by the
  VentureBeat report cited under Sources.
https://www.science.org/doi/10.1126/science.abq1158: canonical AlphaCode page,
  paywalled. The identical text (same authors, same 54.3% abstract) was read in
  the open preprint arxiv 2203.07814, cited above.
https://arstechnica.com/ai/2024/12/openai-announces-o3-and-o3-mini-its-next-simulated-reasoning-models/:
  read via reader transport; it names the Codeforces benchmark but gives no o3
  rating number and no "175th" framing, so it does not support the point.
https://arxiv.org/html/2501.01257 (CodeElo): a separate LLM Elo benchmark, not
  needed for tracing the specific claims the commission names.
```
