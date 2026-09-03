# Evidence record: the-instruments/task-time-horizon (01)

This record supports a lesson on how METR's 50%-task-completion time horizon is
built and where it gets over-read. The construction is well documented from the
primary paper (Kwa et al. 2025): 170 timed tasks across three suites, model
success scored as binary pass/fail, a logistic fit of success against log human
task time, and the 50% horizon read off as the human task length where the
fitted success probability crosses 0.5. The headline figures are firm and
sourced to the paper: Claude 3.7 Sonnet at 59 minutes (rounded to "around 50
minutes" in the abstract), and a doubling time of 212 days with a 95% bootstrap
interval of 171-249 days. The paper's own limits are stated plainly in its text
and are strong: the 50% threshold is not reliability (Claude 3.7 Sonnet's
80%-horizon is 15 minutes), the tasks differ systematically from real work, and
the authors say external-validity and future-trend uncertainty carry "the
majority of our uncertainty." Two things are well evidenced as contested: the
2024-2025 acceleration (the authors call the gap "difficult to distinguish from
noise," and METR's own 2026 update attributes part of it to task composition),
and whether the trend extrapolates to dated milestones. The over-read is
documented: AI Digest converts the doubling into "A new Moore's Law for AI
agents" with year-stamped milestones (1 work month by 2029). The record is thin
in one place: individual per-model horizon values are read off Figure 1 and the
paper's text does not tabulate them, so only a handful of exact per-model numbers
could be pulled from prose. That gap is flagged in Numbers.

Source-obligation status: 8 distinct sources read, all URLs resolve. Primary: 7.
Secondary: 1. Note that the two Toby Ord entries are one origin (his paper and
his own restatement of it), so they count as one independent critic, not two.

## Sources

```text
URL:         https://arxiv.org/abs/2503.14499
Kind:        primary. This is the paper that defines the metric and owns every
             construction figure and headline number. Full readable text at
             https://arxiv.org/html/2503.14499v1 (also resolves); abstract page
             recorded as the canonical address.
Establishes: The metric, the method, the headline horizon and doubling figures,
             and the paper's own stated limits.
Paraphrase:  METR proposes the "50%-task-completion time horizon": the human
             completion time of tasks a model completes with 50% success.
             Humans with domain expertise were timed on RE-Bench, HCAST, and 66
             new shorter tasks. Frontier models such as Claude 3.7 Sonnet reach a
             50% horizon of around 50 minutes; the horizon has doubled roughly
             every seven months since 2019, possibly faster in 2024. The gain is
             attributed mainly to greater reliability and error-recovery, plus
             better reasoning and tool use.
Locators:    Abstract; body sections on task suites, logistic fit, results, and
             limitations (Sections 3-7 of the v1 HTML).
Quote:       "we propose a new metric: 50%-task-completion time horizon. This is
             the time humans typically take to complete tasks that AI models can
             complete with 50% success rate."
             "If these results generalize to real-world software tasks,
             extrapolation of this trend predicts that within 5 years, AI systems
             will be capable of automating many software tasks that currently
             take humans a month."

URL:         https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
Kind:        primary. METR's own announcement of its own result. Owns the public
             framing METR chose.
Establishes: METR's headline framing and its forward extrapolation in its own
             voice, plus the caveat METR attaches to the projection.
Paraphrase:  METR states the metric has increased exponentially for six years
             with a ~7-month doubling, gives Claude 3.7 Sonnet a horizon of
             about one hour (where its fitted logistic curve crosses 50%), and
             projects that "in under a decade" agents will complete a large
             fraction of software tasks that now take humans days or weeks. METR
             adds that the projection ignores future trend changes and external
             validity, "which are responsible for the majority of our
             uncertainty."
Locators:    Summary and the trend/extrapolation section of the blog post.
Quote:       "this metric has been consistently exponentially increasing over the
             past 6 years, with a doubling time of around 7 months"
             "Claude 3.7 Sonnet ... has a time horizon of approximately one hour,
             as this is where its fitted logistic curve intersects the 50%
             success probability threshold."

URL:         https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains/
Kind:        primary. METR's own follow-up measuring the metric on other task
             suites. Owns the cross-domain numbers.
Establishes: The horizon is task-suite dependent: the same method yields very
             different horizons and doubling rates on different task
             distributions.
Paraphrase:  Measured on visual computer-use suites (OSWorld, WebArena), 50%
             horizons run 40-100x shorter than on the software-and-reasoning
             cluster; Tesla FSD improves at only ~0.6 doublings per year. METR
             says the original ~100-minute horizon and ~4-month doubling on its
             software/reasoning tasks are "likely not an outlier," while showing
             the number moves substantially with the task distribution.
Locators:    Cross-domain results section; per-domain figures.
Quote:       "Visual computer use (OSWorld, WebArena) time horizons are 40-100x
             shorter than the software and reasoning cluster"

URL:         https://metr.org/blog/2026-1-29-time-horizon-1-1/
Kind:        primary. METR's own revision of the original measurement.
Establishes: Which original figures moved on re-measurement, and METR's own
             caution that the trend depends on task composition.
Paraphrase:  METR expanded the suite from 170 to 228 tasks (8h+ tasks from 14 to
             31) and moved from in-house Vivaria to the open-source Inspect
             framework. Under the update, some older models' horizons fell (GPT-4
             1106 down 57%, GPT-4 0314 down 35%) and frontier ones rose; the
             most capable current models reach 50% horizons of roughly 320 min
             (Claude Opus 4.5), 214 min (GPT-5), 121 min (o3). The post-2023
             doubling estimate moved from 165 to 131 days, which METR partly
             attributes to a different task-difficulty distribution rather than
             pure capability gain. Human baselines were measured for only 5 of
             31 long tasks; the rest are estimates.
Locators:    Update summary; methodology-change and revised-estimate sections.
Quote:       "the trend in time horizon is somewhat sensitive to task
             composition"

URL:         https://arxiv.org/abs/2505.05115
Kind:        primary. Toby Ord's own paper; he owns the constant-hazard model and
             the human/AI divergence finding. It re-analyzes METR's data, so it
             is a critique/refinement, not METR reporting.
Establishes: A simpler alternative model of the same data, and a documented way
             the 50% horizon can mislead about longer tasks.
Paraphrase:  Ord (author of the paper; the arXiv listing shows no affiliation,
             he is a philosopher at Oxford) shows that within METR's tasks, agent
             performance on longer tasks fits a constant per-human-minute failure
             rate, giving each agent an exponentially declining success rate with
             task length and a characteristic "half-life." Under this model the
             50% horizon implies fixed ratios to stricter thresholds (T80 about
             1/3 of T50, T99 about 1/70), so a 50% horizon overstates what a
             model does reliably.
Locators:    Abstract; model derivation and threshold-ratio section.
Quote:       "the performance of AI agents on longer-duration tasks can be
             explained by an extremely simple mathematical model -- a constant
             rate of failing during each minute a human would take to do the
             task."

URL:         https://www.tobyord.com/writing/half-life
Kind:        primary (same origin as the entry above; counts as one independent
             critic). Ord's own restatement, used only for figures the arXiv
             abstract omits.
Establishes: The concrete human/AI divergence numbers and the 59 vs 15 minute
             threshold gap.
Paraphrase:  Ord notes Claude 3.7 Sonnet reaches 50% success up to 59 minutes but
             only 15 minutes at 80%. He then shows humans do not follow the
             constant-hazard decay his model assumes for agents: human baseliners
             at ~50% success on 1.5-hour tasks would fall to 6.25% at 12 hours
             under constant hazard, but stayed above 20%. A later note flags that
             the constant-hazard assumption likely fails on closer inspection.
Locators:    Sections on the threshold gap and on human vs AI decay; update note.
Quote:       "the humans were still above 20% success rate at that point" (versus
             the 6.25% a constant hazard rate predicts).

URL:         https://theaidigest.org/time-horizons
Kind:        primary for the over-read it commits: AI Digest (a project of Sage)
             owns this forecast and framing. Secondary as reporting on METR.
Establishes: A public, dated over-extrapolation of the doubling trend that treats
             the metric as a law.
Paraphrase:  AI Digest headlines the result "A new Moore's Law for AI agents" and
             converts the doubling into calendar milestones: a 1-work-day (8h)
             horizon in 2027, 1 work week (40h) in 2028, 1 work month (167h) in
             2029, with month-long tasks possibly in 2027 on the faster trend.
             The page notes single-year estimates are less robust and the trend
             could slow or speed up.
Locators:    Headline and the projected-milestones timeline.
Quote:       "A new Moore's Law for AI agents"
             "2029: 1 work month (167 hours)"

URL:         https://emptysqua.re/blog/review-measuring-ai-ability-to-complete-long-software-tasks/
Kind:        secondary. An independent review by A. Jesse Jiryu Davis (April 1,
             2026). Reports on and assesses the paper from outside METR.
Establishes: An outside reading of the benchmark-to-reality gap and the
             human/AI testing asymmetry, useful for the lesson's "where it
             misleads" turn.
Paraphrase:  Davis accepts the headline finding but stresses that real software
             work lacks an automatic referee, that the human baseline's
             representativeness is uncertain (a person who knows the codebase is
             faster; one ignorant of a technique is slower), and that METR timed
             humans under an eight-hour cap while giving AIs no time limit. He
             cites METR's own finding that about half of SWE-bench pull requests
             passing automated tests would be rejected by human maintainers.
Locators:    Sections on messiness, human baselines, and testing asymmetry.
Quote:       "METR tests humans and AIs differently" (humans faced eight-hour
             limits while AIs had none).
```

## Contradictions

- Claude 3.7 Sonnet's 50% horizon: the abstract says "around 50 minutes" and the
  METR blog says "approximately one hour," while the paper body and Ord give the
  fitted value as 59 minutes. This is rounding, not disagreement. The precise
  fitted figure is 59 minutes; the abstract rounds down and the blog rounds up.
  Record 59 minutes as the number, ~50-60 min as the rounded public phrasing.

- The paper's title differs across versions. The v1 arXiv HTML and METR's March
  blog both read "Measuring AI Ability to Complete Long Tasks"; the arXiv
  abstract page (and NeurIPS 2025 listing) read "Measuring AI Ability to Complete
  Long **Software** Tasks." The paper was retitled to scope it to software after
  v1. Use the software-scoped title as the current one and note the metric was
  built and validated on software/ML/cyber tasks, not general knowledge work.

- Doubling time is not one number. Full period 2019-2025: 212 days (~7 months),
  95% CI 171-249. The 2023-2025 subset: about six months in the paper's text,
  and METR's blog and AI Digest cite a ~4-month rate for 2024-2025. METR's 2026
  update revises the post-2023 figure to 131 days. The authors say the fast-trend
  gap is "difficult to distinguish from noise," and the 2026 update attributes
  part of the change to task composition. Settled: the ~7-month full-period
  doubling with its CI. Contested: the 2024-2025 acceleration.

- Ord's constant-hazard model contradicts itself on humans and he says so: if
  agents fail at a constant per-minute rate, humans on the same tasks should too,
  but the human baseliners decayed far more slowly (>20% at 12h vs the 6.25% the
  model predicts). Ord's later note concedes the constant-hazard assumption
  probably does not hold. So the "half-life" reframing is a useful intuition, not
  a settled mechanism.

- The paper's forward extrapolation ("within 5 years ... a month") sits against
  its own external-validity caveat in the same document. The over-reading the
  commission targets is partly seeded by the authors' own projection and then
  amplified by AI Digest into dated, law-like milestones. The lesson should not
  present the extrapolation as purely an outside misreading.

## Numbers

```text
Figure: 50%-task-completion time horizon = human completion time of tasks a
        model succeeds at 50% of the time
Owner:  Kwa et al. 2025 (arXiv:2503.14499)
Scope:  Defined over the 170-task suite (software, ML research eng., cyber)

Figure: Claude 3.7 Sonnet 50% horizon = 59 minutes (public rounding: ~50-60 min)
Owner:  Kwa et al. 2025; restated with the exact minute figure by Ord
Scope:  On METR's task suite, at the 50% success threshold

Figure: Claude 3.7 Sonnet 80% horizon = 15 minutes
Owner:  Kwa et al. 2025 (and Ord)
Scope:  Same suite, 80% success threshold. Shows 50% is not reliability.

Figure: Doubling time (full period) = 212 days, 95% bootstrap CI 171-249 days
Owner:  Kwa et al. 2025
Scope:  2019-2025 frontier trend of the 50% horizon

Figure: Doubling time (recent subset) = ~4-6 months (2023/2024-2025); revised to
        131 days post-2023 in Time Horizon 1.1
Owner:  Kwa et al. 2025 (text/blog) and METR 2026 update
Scope:  Recent-years subset only; authors call the acceleration hard to
        distinguish from noise

Figure: Task suite = 170 tasks: HCAST 97, RE-Bench 7, SWAA 66
Owner:  Kwa et al. 2025
Scope:  Task durations span <1 second (SWAA) to ~30 hours (HCAST/RE-Bench)

Figure: HCAST human baselines = 286 successful baselines from ~460 attempts;
        task time = geometric mean of successful baselines
Owner:  Kwa et al. 2025
Scope:  Skilled professionals (~5 yrs domain experience); RE-Bench durations
        from baseliners who spent 7-9 hours; SWAA baselined 3-4x by METR staff

Figure: Logistic fit p_success = sigmoid((log h_model - log t_task) * beta_model)
Owner:  Kwa et al. 2025
Scope:  h_model is the fitted 50% horizon; t_task is the task's geometric-mean
        human time; success is scored binary per task

Figure: Messiness scale = 0-16 across 16 properties; suite mean ~3.2/16; a task
        like "write a good research paper" would score ~9-15/16; +1 messiness
        point reduces mean success by ~8.1%
Owner:  Kwa et al. 2025 (Appendix on messiness)
Scope:  Rated on HCAST/RE-Bench tasks; quantifies the benchmark-vs-real gap

Figure: Cross-domain spread = visual computer-use horizons 40-100x shorter than
        the software/reasoning cluster; Tesla FSD ~0.6 doublings/year
Owner:  METR, "How Does Time Horizon Vary Across Domains?" (2025-07-14)
Scope:  Same method, different task suites

Figure: Current frontier 50% horizons (2026 update) = Claude Opus 4.5 320 min
        [170-729], GPT-5 214 min [117-480], o3 121 min [74-201]
Owner:  METR, Time Horizon 1.1 (2026-01-29)
Scope:  228-task revised suite; wide confidence intervals

Figure: Over-read milestones = 1 work day (8h) 2027, 1 work week (40h) 2028,
        1 work month (167h) 2029
Owner:  AI Digest (theaidigest.org/time-horizons)
Scope:  Straight-line extrapolation of the doubling; the over-read the lesson
        examines
```

Unverified from text: exact per-model 50% horizon values for the full model list
(GPT-2, davinci-002/GPT-3, GPT-3.5-turbo-instruct, GPT-4 0314/1106, Claude 3
Opus, Claude 3.5 Sonnet, o1-preview, o1) with release dates. These are plotted in
Figure 1 and not tabulated in the v1 body text, so only approximate prose values
could be recovered: GPT-2 and GPT-3 near zero (fail tasks over ~1 minute), Claude
3 Opus in a 5-30 minute range, o1 around 39 minutes. Treat individual points as
Figure-1 readings with wide error bars, per the paper's own caution; the trend,
not any single point, is what the paper defends. If the writer needs an exact
per-model table, the live results plot at metr.org/blog is client-rendered and
was not machine-readable here; the numeric table would need to be pulled from the
paper's figure data or appendix directly.

## Source assets

```text
Asset: Figure 1, the log-scale scatter of 50% time horizon versus model release
       date with the fitted exponential trend line (Kwa et al. 2025, arXiv HTML
       v1)
Shows: The whole argument in one image: horizon on a log axis climbing a straight
       line from GPT-2 (seconds) to Claude 3.7 Sonnet (~1 hour), which is what
       "doubling every 7 months" looks like.
Crop:  Must keep the log y-axis label and the release-date x-axis so the reader
       sees the scale is logarithmic; must keep the trend line and its data
       points. Do not crop to only the recent, steeper points, which would
       misrepresent the fast-trend claim the authors themselves hedge.

Asset: The 50%-vs-80% horizon comparison for Claude 3.7 Sonnet (59 min vs 15 min)
       (Kwa et al. 2025; restated by Ord)
Shows: A single model's horizon shrinking as the reliability bar rises, the
       clearest illustration that the 50% number is not "can do."
Crop:  Retain both thresholds and both minute values; omitting either loses the
       point.

Asset: Per-domain horizon chart from "How Does Time Horizon Vary Across Domains?"
       (METR, 2025-07-14)
Shows: The same metric landing 40-100x apart across task suites, the visual case
       that the headline number is suite-dependent.
Crop:  Keep the domain labels and the log axis; the spread only reads on a log
       scale.

Asset: AI Digest projection timeline with year-stamped milestones (1 day 2027,
       1 week 2028, 1 month 2029) (theaidigest.org/time-horizons)
Shows: The over-read itself, a straight line extended past its data into calendar
       predictions.
Crop:  Keep the dated milestone labels; this is the artifact the lesson critiques,
       so present it as a claim being examined, attributed to AI Digest.
```

## Discarded

```text
URL: https://arxiv.org/pdf/2505.05115 — same content as the abstract/writeup
     entries; the PDF returned binary and is not the address a reader should get.
URL: https://x.com/IntuitMachine/status/1902672941159960712 — a social post
     restating the paper's author list; adds nothing the primary does not own.
URL: https://techxplore.com/news/2025-03-metric-quantify-capabilities-ai-terms.html
     — general-press restatement of the METR abstract; superseded by the primary.
URL: https://medium.com/@AIchats/are-ai-time-horizon-doubling-every-seven-months-...
     — self-published critique; its points on the acceleration are better sourced
     to METR's own 2026 update, which concedes the task-composition caveat.
URL: https://medium.com/@divyanshbhatiajm19/the-half-life-paradox-... — blog
     retelling of Ord; two retellings of one origin count as one, and Ord is
     already cited primary.
URL: https://www.themoonlight.io/en/review/is-there-a-half-life-... — auto-
     generated literature review of Ord; no independent standing.
URL: https://www.forethought.org/research/is-there-a-half-life-... and
     https://www.alphaxiv.org/abs/2505.05115 — mirrors of Ord's paper; the
     primary is cited directly.
```
