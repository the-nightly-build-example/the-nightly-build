# Evidence: the-instruments/brier-score (01)

The evidence supports the full commissioned argument. Brier's own 1950 paper
was read in full (via a public-domain scan of the original journal issue, not
a summary), and it hands over a clean worked example, the exact 0-to-2
original scale, and the forecaster's-own explanation of why the score cannot
be gamed by hedging. Halawi et al. 2024 was read in the primary, with every
number below pulled from its own sentences and tables, not from coverage of
it. Two independent later studies (Lu 2025, and Karger/Halawi/Tetlock's
ForecastBench 2025) extend the record past 2024 and supply the "same
question set" comparison the commission wants readers to demand. The critique
(AI Alignment Forum, Sept. 2024) targets Halawi et al. by name and gives a
sourced, quotable version of the "misleading aggregate" case. The one gap:
Murphy 1973 and Metaculus's own scoring page could not be opened in full text
despite repeated attempts (see Discarded); the Murphy decomposition is
instead sourced to a peer-reviewed 2012 paper that reproduces Murphy's
equations and citation exactly, and the platform-methodology requirement is
met by Good Judgment Open's FAQ instead of Metaculus's. Both substitutions
are sourced, not guessed, and are flagged for the editor below. A second,
unplanned finding surfaced in the reading: Good Judgment Open still scores on
Brier's original two-term, 0-to-2 scale, not the one-term, 0-to-1 scale used
by Halawi, Lu, and ForecastBench. That is a second, genuine comparability trap
beyond the question-set one the commission named, and it is documented fully
in Contradictions and Numbers for the writer and editor to weigh.

## Sources

```text
URL:         https://archive.org/details/sim_monthly-weather-review_1950-01_78_1
Kind:        primary — Glenn W. Brier, U.S. Weather Bureau, is the paper's sole
             author and the score's originator.
Establishes: The original 1950 definition of the "verification score" P, its
             worked numerical example, and its own stated range (0 to 2).
Paraphrase:  Brier proposes scoring a set of n forecasts, each stating a
             probability for each of r mutually exclusive, exhaustive
             categories, by P = (1/n) * sum over occasions and categories of
             (forecast − outcome)^2, where outcome is 1 or 0. He states P
             is minimized (0) by perfect forecasting and maximized (2) by
             stating certainty for the event that did not occur. He shows
             that if a forecaster has no ability to discriminate one occasion
             from the next, the best constant forecast is the true class
             frequency, and demonstrates this on his own 10-forecast
             rain/no-rain example.
Locators:    Monthly Weather Review, vol. 78, no. 1 (Jan. 1950), pp. 1-3.
             "Verification Formula" section (formula 2, p. 1) through
             "Conclusions" (p. 3). Table 1 (p. 2, 10-forecast example);
             Table 2 (p. 3, 85-forecast reliability table).
Quote:       "A number of interesting observations can be made about a
             vertification [sic] score P... it is obvious that the score P
             has a minimum value of zero for perfect forecasting and a
             maximum value of 2 for the worst possible forecasting."
             Also: "a forecast of 0.3 probability for rain on every occasion
             would give a score P'=1-(0.3^2+0.7^2)=0.42. If for these same 10
             forecasts a climatological probability of say 0.2 for rain had
             been used on every occasion the corresponding score is 0.44."

URL:         https://arxiv.org/abs/2402.18563
Kind:        primary — Halawi, Zhang, Yueh-Han, and Steinhardt (UC Berkeley)
             built the system and ran the evaluation themselves.
Establishes: The exact Brier numbers behind the "LLMs approach human-level
             forecasting" claim, the question set, the resolution window, and
             the authors' own characterization of what counts as a "large"
             margin.
Paraphrase:  A retrieval-augmented LM pipeline (search, rank, summarize,
             forecast, aggregate by trimmed mean) is evaluated on 914 binary
             questions, held out from training/validation and all published
             after June 1, 2023, drawn from Metaculus, GJOpen, INFER,
             Polymarket, and Manifold. The full system scores .179 against a
             ".149" human-crowd aggregate on that set (accuracy 71.5% vs.
             77.0%). Separately, raw (non-retrieval) LLM forecasts are graded
             against an ".25" unskilled baseline; only the GPT-4 and Claude-2
             model series clear that baseline "by a large margin (>.02)." The
             paper's "in some settings surpasses" claim (its abstract) refers
             to a selective subset — questions where the crowd's own forecast
             sits between .3 and .7 — where the system scores .238 against a
             .240 crowd score, a .002 gap.
Locators:    Read via https://arxiv.org/html/2402.18563 (arXiv's own HTML
             rendering of the same paper, not a third-party mirror).
             Section 3.2 (baseline results, Table 2b) for the .25 baseline
             and the ">.02" language; Section 6.1 and Table 4 for the system
             (.179) vs. crowd (.149) result and the .03 gap; Section 4/6.1
             for the selective-subset ".238 vs .240" figures; Table 5 for the
             retrieval ablation (removing retrieval costs .027 Brier).
Quote:       "As the main result, our averaged Brier score is .179, while the
             crowd achieves .149, resulting in a difference of .03." Also:
             "Only the GPT-4 and Claude-2 series beat the unskilled baseline
             by a large margin (>.02)." Also: "As a baseline, an (unskilled)
             forecast of .5 attains a Brier score of .25."

URL:         https://arxiv.org/abs/2507.04562
Kind:        primary — Janna Lu (George Mason University) ran this evaluation
             independently of Halawi et al.
Establishes: A 2024-25 Brier comparison of frontier LLMs against a Metaculus
             question set and against a separate panel of expert forecasters,
             and an explicit statement that beating a "crowd" baseline is not
             the same as matching experts.
Paraphrase:  On 334 test questions from Metaculus (published/resolved July
             4-Sept. 30, 2024) plus a 130-question hold-out set (Oct. 1-Dec.
             1, 2024), the best model (o3) scores a median Brier of .1352
             (.1307 on the hold-out set). A separate panel of 157 questions
             scored by expert forecasters gives a median Brier of .0225 (mean
             .1573) — far below any model tested. Calibration plots (Section
             5.5) show specific overconfidence: "Qwen-32B... would predict
             close to certainty for an event that has an observed frequency
             of 50%." The paper's own headline comparison mixes question
             sets: it compares its .1352 directly against Halawi et al.'s
             .149 "crowd" figure, which was computed on a different,
             non-overlapping question set from different platforms and a
             different year.
Locators:    Read via https://arxiv.org/html/2507.04562v3. Abstract; Section
             5.1 (Table 3, direct-prediction Brier scores) for the .1352
             figure; Section 5.3 for the hold-out .1307 figure; Section 5.4
             (Table 8) for the .0225/.1573 expert figures; Section 5.5 for
             the calibration-plot quote.
Quote:       "Frontier models achieve Brier scores that ostensibly surpass
             the human crowd but still significantly underperform a group of
             expert forecasters." Also: "o3 achieves a Brier score of 0.1352,
             outperforming the crowd baseline of 0.149 but underperforming
             the 0.121 reported in Halawi et al. (2024) and Karger et al.
             (2025) respectively."

URL:         https://arxiv.org/abs/2409.19839
Kind:        primary — Karger, Bastani, Yueh-Han, Jacobs, Halawi, Zhang, and
             Tetlock (Forecasting Research Institute et al.) designed and ran
             this benchmark themselves; Danny Halawi is a co-author on both
             this paper and the 2024 paper it partly answers.
Establishes: What a same-question, same-period comparison of LLMs, the
             general public, and superforecasters actually shows, once the
             question-set problem this lesson teaches is deliberately
             engineered away.
Paraphrase:  ForecastBench draws forecasting questions daily from nine
             sources and obligates every LLM to forecast on the full set, "to
             ensure comparability of scores across models and human-based
             aggregates." On a shared 200-question subset, forecast by the
             general public, by 39 superforecasters, and by LLMs in the same
             window, the superforecaster median forecast scores a mean Brier
             of .096 (95% CI [.076, .116]); the general-public median forecast
             scores .121 (CI [.101, .141]); the best LLM configuration
             (Claude-3.5-Sonnet, "freeze values" scratchpad prompting) scores
             .122 (CI [.099, .146]), with other Claude-3.5-Sonnet prompting
             variants and other models scoring .127 to .143 or worse. The
             abstract states plainly that expert forecasters beat the
             top-performing LLM at p<.001.
Locators:    Read via https://arxiv.org/html/2409.19839v5 (v5, revised Feb.
             28, 2025; ICLR 2025). Abstract; Section 3.3 (question-set design
             quote); Section 4 (Table with superforecaster/public/LLM Brier
             scores and CIs); Section 5.2 ("Comparing humans and LLMs").
Quote:       "there is no framework for evaluating the accuracy of ML systems
             on a standardized set of forecasting questions... expert
             forecasters outperform the top-performing LLM (p-value <0.001)."
             Also: "we obligate all LLMs to forecast on all questions to
             ensure comparability of scores across models and human-based
             aggregates."

URL:         https://www.gjopen.com/faq
Kind:        primary — Good Judgment Open's own FAQ states its own scoring
             rule.
Establishes: A working forecasting platform's own Brier definition, worked
             example, and stated range, used as the required "platform
             methodology" primary. Read directly, not via search snippet.
Paraphrase:  Good Judgment Open scores each active day of a forecast by
             summing the squared error over every answer option, not just
             one: for a yes/no question forecast at 70% rain that resolves
             yes, the score is (1-0.7)^2+(0-0.3)^2=0.18. The stated range is
             0 (best) to 2 (worst) — Brier's original two-term convention,
             not the one-term, 0-to-1 convention used by Halawi et al., Lu,
             and ForecastBench above. A question's overall score is the mean
             of its daily scores.
Locators:    "Score Range and Interpretation" and worked-example sections of
             the FAQ page.
Quote:       "The best (lowest) possible Brier score is 0, and the worst
             (highest) possible Brier score is 2." "For a yes/no question
             where you forecasted 70% and the event happened, your score
             would be (1-0.7)^2+(0-0.3)^2=0.18."

URL:         https://www.alignmentforum.org/posts/uGkRcHqatmPkvpGLq/contra-papers-claiming-superhuman-ai-forecasting
Kind:        secondary — the authors (nikos, Peter Mühlbacher, Lawrence
             Phillips, and dschwarz) did not run Halawi et al.'s study; they
             re-read and re-argue its published numbers, and three other
             papers' numbers.
Establishes: A named, dated critique that a claim was made and disputed, and
             the specific arithmetic the critique uses against Halawi et al.
Paraphrase:  The post argues four 2024 papers (Schoenegger et al., Halawi et
             al., Hsieh et al., Phan et al.) oversell "superhuman" or
             "human-level" AI forecasting. On Halawi et al. specifically, it
             notes the paper's own ">.02" threshold for a "large" Brier
             margin (used there for raw models vs. the unskilled baseline)
             and points out that the full system's shortfall against the
             crowd — .03 — is larger than that threshold, in the wrong
             direction for the "approaching human-level" framing. It also
             flags, for the other three papers, data contamination (already-
             resolved questions), missing internet access for 9 of 12 tested
             models, a small sample (n=31) behind one claim, and a post-hoc
             adjustment needed before one model beat the human crowd.
Locators:    Sections "On Halawi et al." and the paper-by-paper breakdown;
             posted Sept. 12, 2024, cross-posted to LessWrong under the same
             URL slug.
Quote:       "Today's autonomous AI forecasting can be better than average,
             or even experienced, human forecasters, but it's very unlikely
             that any autonomous AI forecaster yet built is close to the
             accuracy of a top 2% Metaculus forecaster, or the crowd."

URL:         https://empslocal.ex.ac.uk/people/staff/ferro/Publications/ferro-fricker2012copyright.pdf
Kind:        secondary — Ferro and Fricker (University of Exeter / National
             Centre for Atmospheric Science) extend and critique Murphy's
             1973 decomposition; they did not originate it. Used because
             Murphy 1973 itself could not be opened (see Discarded).
Establishes: The plain content of Murphy's three-term decomposition, with
             Murphy's own equations reproduced and cited.
Paraphrase:  The Brier score B decomposes as B = REL - RES + UNC. REL
             (reliability) is a weighted average of the squared gap between
             each stated probability and how often that probability class
             actually verified — zero when forecasts match observed
             frequencies. RES (resolution) is a weighted variance of those
             observed frequencies across forecast classes — zero if the
             outcome frequency is the same no matter what was forecast,
             meaning the forecasts carried no information. UNC (uncertainty)
             is the base-rate variance of the event itself, x̄(1-x̄), and is
             not something a forecaster controls. The paper is a preprint
             accepted at the Quarterly Journal of the Royal Meteorological
             Society (published version behind a paywall at
             onlinelibrary.wiley.com/doi/10.1002/qj.1924).
Locators:    Section 1 ("The Brier score and its decomposition"), equations
             1-4 and the paragraph immediately following, which names and
             defines REL, RES, and UNC and cites "(Murphy, 1973)" directly at
             the point the decomposition is introduced.
Quote:       "Then the Brier score can be decomposed (Murphy, 1973) as
             B = REL - RES + UNC... The first term (REL)... measures the
             reliability of the forecasts... The second term (RES)... measures
             the resolution of the forecasts... The third term (UNC) is a
             measure of uncertainty or climatological variation in the event
             occurrence."

URL:         https://en.wikipedia.org/wiki/Brier_score
Kind:        secondary/tertiary — a reference article, used only to
             corroborate the historical wrinkle already confirmed firsthand
             in Brier 1950 itself (above); not relied on for any number the
             primary does not also support.
Establishes: That the "modern," one-term, 0-to-1 Brier score in wide current
             use is a later simplification of Brier's own two-term, 0-to-2
             formulation for the binary case, with the standard citation.
Paraphrase:  "For binary forecasts, the original formulation of Brier's
             'probability score' has twice the value of the score currently
             known as the Brier score," because Brier's own formula sums the
             squared error over both outcome classes rather than one.
Locators:    "History" / definition section, citing Brier, G.W. (1950).
             Monthly Weather Review, 78(1): 1-3.
```

## Contradictions

**The case against "LLMs approach human-level forecasting":**

Halawi et al.'s own headline result is a .03 Brier gap in the crowd's favor
(system .179, crowd .149) on their full test set — the system did not beat
the crowd there. The abstract's "in some settings surpasses" claim survives
only on a selective subset (questions where the crowd itself was near .3-.7,
i.e., genuinely uncertain), and there the margin is .238 vs .240 — .002, an
order of magnitude below the ">.02" bar the same paper sets elsewhere for
what counts as a "large" Brier margin (that bar was set for a different
comparison — raw model vs. the unskilled baseline — so applying it to the
system-vs-crowd gap is the critique's own inference, not something the
authors said outright; it is nonetheless the critique's central, checkable
argument). The AI Alignment Forum critique (Sept. 2024) makes exactly this
argument against Halawi et al., and separately documents that three sibling
2024 papers making similar claims relied on stale/contaminated questions, LLMs
without internet access, a 31-question sample, or a post-hoc adjustment to
reach their result.

A year later, the picture had not changed in the AI system's favor relative
to real experts. Lu (2025) finds the best model (o3, Brier .1352) beats a
"crowd" figure but still loses badly to a panel of expert forecasters (median
Brier .0225) — nearly a six-fold gap. ForecastBench (Karger et al. 2025,
co-authored by Halawi himself and by Philip Tetlock), built specifically to
give LLMs, the general public, and superforecasters the same questions in the
same window, states plainly in its abstract that "expert forecasters
outperform the top-performing LLM (p-value <0.001)": superforecaster median
Brier .096 vs. the best LLM configuration around .122-.130.

**The strongest case for it:** Halawi et al.'s test set was built specifically
to rule out the cheapest ways to fake a good score. It restricts the 914 test
questions to those published after June 1, 2023 — after every tested model's
training cutoff — so the system cannot have memorized outcomes, and it
time-restricts retrieval so search results from after a question's start date
cannot leak the answer. An ablation (Table 5) shows removing retrieval costs
.027 Brier, meaning the system's skill is not simply reciting climatology; a
model without retrieval does measurably worse. And on the general public,
progress is real and not merely claimed: ForecastBench's own numbers put the
best LLM's Brier (~.122-.130) close to or better than the general-public
median (.121) — a genuine capability gain versus ordinary human forecasters,
even though the same paper shows superforecasters remain clearly ahead.

**A second, unplanned comparability trap:** Good Judgment Open's FAQ confirms
it still scores on Brier's original two-term, 0-to-2 scale (a .18 in their
worked example) rather than the one-term, 0-to-1 scale every AI-forecasting
paper above uses. A raw score copied from one convention into the other, with
no unit check, would misread a mediocre forecast as roughly twice as bad (or
good) as it is. This was not in the commission's original list of traps; it
is the same underlying fact (Brier's 1950 multi-category formula) surfacing a
second time, and the editor should decide whether it belongs alongside the
question-set trap or is one trap too many for this lesson's scope.

## Numbers

```text
Figure: 0.25 (Brier score of always forecasting p=.5 on a binary question)
Owner:  Halawi et al. 2024 (states it directly; also a direct algebraic
        consequence of the one-term modern formula, invariant to any
        binary question's actual base rate)
Scope:  Any single binary yes/no question, one-term (0-to-1) convention;
        does not depend on the true frequency of the event.

Figure: P'=0.42 (Brier score of a constant 0.3/0.7 climatological forecast)
        and P'=0.44 (constant 0.2/0.8 forecast), against 3 rain / 10 total
Owner:  Brier 1950, worked example, Table 1 and following text
Scope:  n=10 forecasts, r=2 categories (rain/no-rain), Brier's own two-term
        0-to-2 convention (so these are not directly comparable to the
        .149/.179/.25 figures elsewhere in this record, which use the
        one-term 0-to-1 convention — see Contradictions).

Figure: System Brier .179 vs. human-crowd Brier .149 (a .03 gap)
Owner:  Halawi et al. 2024, Table 4 / Section 6.1
Scope:  914 held-out binary questions, all published after June 1, 2023,
        across Metaculus, GJOpen, INFER, Polymarket, and Manifold; system
        evaluated with full retrieval pipeline and trimmed-mean aggregation.

Figure: Raw LLM Brier .208 (GPT-4-1106-Preview), .215 (Claude-2.1), vs.
        unskilled baseline .25
Owner:  Halawi et al. 2024, Section 3.2 / Table 2b
Scope:  Same 914-question test set, zero-shot/scratchpad prompting without
        the retrieval system; "only the GPT-4 and Claude-2 series beat the
        unskilled baseline by a large margin (>.02)."

Figure: Selective-subset system Brier .238 vs. crowd .240 (a .002 gap, the
        basis for the paper's "in some settings surpasses" claim)
Owner:  Halawi et al. 2024, Section 6.1
Scope:  Subset of the same test set restricted to questions where the crowd's
        own forecast fell between .3 and .7.

Figure: o3 Brier .1352 (median, direct prediction)
Owner:  Lu 2025, Table 3 / Section 5.1
Scope:  334 Metaculus binary questions published/resolved July 4-Sept. 30,
        2024. A 130-question hold-out set (Oct. 1-Dec. 1, 2024) gives o3 a
        Brier of .1307 (Section 5.3).

Figure: Expert-forecaster Brier: .0225 (median), .1573 (mean)
Owner:  Lu 2025, Table 8 / Section 5.4
Scope:  157-question subset scored by a panel of expert forecasters
        (distinct panel from the Metaculus "crowd" used elsewhere).

Figure: Superforecaster median-forecast Brier .096 (95% CI [.076,.116]);
        general-public median-forecast Brier .121 (CI [.101,.141]); best LLM
        configuration (Claude-3.5-Sonnet, "freeze values" scratchpad) .122
        (CI [.099,.146])
Owner:  ForecastBench (Karger et al. 2025), Section 4 / Section 5.2 table
Scope:  A shared 200-question subset, all three groups (39 superforecasters,
        ~500 general-public respondents averaging 49 responses/question, and
        multiple LLMs) forecasting the same questions in the same window —
        the standardized comparison the commission's angle calls for.

Figure: 0.18 (Good Judgment Open's worked Brier example: forecast 70% rain,
        rain occurs)
Owner:  Good Judgment Open FAQ
Scope:  Single yes/no question, Good Judgment Open's own two-term, 0-to-2
        scale — equal to 0.09 on the one-term, 0-to-1 scale used by every
        AI-forecasting paper above.
```

## Source assets

```text
Asset: Brier 1950, Table 2, "Verification of a series of 85 forecasts
       expressed in terms of the probability of rain" (p. 3)
Shows: A binned table of forecast-probability ranges against the observed
       proportion of rain in each bin — a reliability diagram in tabular
       form, from the founding paper itself, 76 years before the term
       "reliability diagram" was common usage.
Crop:  Must keep both columns (forecast-probability bin and observed
       proportion) and enough bins to show the relationship is imperfect,
       not just the two extreme bins.

Asset: Halawi et al. 2024, Figure 3, calibration curves for (a) base models
       zero-shot, (b) the system on validation data, (c) the system on test
       data
Shows: How closely stated probabilities track observed outcome frequency,
       and that fine-tuning visibly tightens this relationship between (a)
       and (c) — a direct, current-day illustration of the "reliability"
       component Murphy's decomposition names.
Crop:  Any single panel must keep its axis labels and the diagonal
       reference line; do not crop to just the curve without the diagonal,
       since the deviation from the diagonal is the entire point.

Asset: Lu 2025, Section 5.5 calibration plots, "(a) Calibration plot for
       direct prediction (b) Calibration plot for narrative prediction"
Shows: Specific, named overconfidence — e.g., Qwen-32B forecasting near
       certainty on events that actually resolve near 50/50 — a concrete,
       attributable instance of the "confident wrong calls" pattern the
       commission asks for, not just an aggregate score.
Crop:  Keep the model label with its curve if multiple models share one
       panel; a crop that drops which line belongs to which model loses the
       finding.

Asset: ForecastBench (Karger et al. 2025), Section 4/5.2 results table
       (superforecaster/general-public/LLM Brier scores with 95% CIs)
Shows: The same-question, same-period comparison the whole lesson argues
       for, with confidence intervals attached to each figure rather than a
       bare point estimate.
Crop:  Keep the CI columns; a version with only the point estimates re-
       introduces the false precision this lesson warns against.

None found — Halawi et al. 2024, Table 5 (retrieval ablation) is a table of
numbers, not a chart, and Good Judgment Open's FAQ carries no chart or table
beyond its one worked-example line.
```

## Discarded

```text
URL: https://journals.ametsoc.org/view/journals/mwre/78/1/1520-0493_1950_078_0001_vofeit_2_0_co_2.xml
     — this is the American Meteorological Society's own hosting of Brier
     1950. A direct fetch returns an AWS WAF "human verification" challenge
     (confirmed via response header x-amzn-waf-action: challenge); a
     browser-user-agent request returns only the site's navigation shell,
     with no article text (confirmed by inspecting the returned HTML); and a
     reader-proxy fetch returns a CAPTCHA page. The article itself was read
     instead from a public-domain scan of the same journal issue on the
     Internet Archive (see Sources), which is the identical text, freely
     readable, and does not require solving a bot challenge.

URL: https://journals.ametsoc.org/view/journals/apme/12/4/1520-0450_1973_012_0595_anvpot_2_0_co_2.xml
     (Murphy, A.H., 1973, "A New Vector Partition of the Probability Score,"
     Journal of Applied Meteorology 12: 595-600) — same AMS gate as above,
     confirmed by the same three methods. No Internet Archive scan of
     Journal of Applied Meteorology exists (checked via the Archive's own
     advancedsearch API, zero results for the title and for the year).
     ResearchGate's copy (researchgate.net/publication/234395762) returned
     HTTP 403. Not opened in full text; used only at one remove, via Ferro &
     Fricker 2012, which reproduces Murphy's equations and cites him
     directly at the point of use (see Sources). This is a genuine gap: no
     source in this record has read Murphy's own prose, only his equations
     as another peer-reviewed paper states them.

URL: https://www.metaculus.com/help/scores-faq/ — returned HTTP 403 on two
     direct fetches and a Cloudflare "Just a moment..." interactive
     challenge via a reader-proxy fetch. Not opened. Good Judgment Open's own
     FAQ was read instead and used to satisfy the "a forecasting platform's
     own methodology" requirement; it happens to also surface the two-term/
     one-term scale difference documented in Contradictions above.

URL: https://www.researchgate.net/publication/234395762_A_New_Vector_Partition_of_the_Probability_Score
     — HTTP 403, no preview text served. See the Murphy 1973 entry above.

Papers characterized only through the AI Alignment Forum critique, not opened
directly, and therefore not treated as read sources in this record:
Schoenegger et al. 2024 ("Wisdom of the Silicon Crowd"), Hsieh et al. 2024
("Reasoning and Tools for Human-Level Forecasting"), and Phan et al. 2024
("LLMs Are Superhuman Forecasters"). Their numbers are not cited directly
anywhere above; only the critique's characterization of them is used, and
only in Contradictions, attributed to the critique.
```
