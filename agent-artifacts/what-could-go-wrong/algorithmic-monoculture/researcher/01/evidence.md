# Evidence: what-could-go-wrong/algorithmic-monoculture

The record supports the argument the commission wants to teach: Kleinberg and
Raghavan's PNAS 2021 paper does formally establish that a monocultural, more
accurate algorithm can be a dominant strategy for firms and yet leave social
welfare strictly lower than a market of independent, less accurate human
evaluators. Bommasani, Creel, Kumar, Jurafsky, and Liang (NeurIPS 2022) supply
the first formal metric of "outcome homogenization" and show shared training
data reliably increases individual-level systemic failure on three fairness
datasets, though their model-sharing experiments produce mixed results
(training from scratch on CelebA was the most homogeneous). Toups, Bommasani,
Creel, Bana, Jurafsky, and Liang (NeurIPS 2023) audit nine commercial APIs
from Google, Microsoft, Amazon, Baidu, IBM, and Face++ across eleven datasets
and find systemic-failure rates that always exceed the independent-model
baseline, with year-over-year model improvements barely reducing them.
Bommasani, Bana, Creel, Jurafsky, and Liang (FAccT 2026) provide the record's
strongest deployment evidence: 4,197,168 real applications from 3,372,132
applicants through the pymetrics vendor, with systemic-rejection rates that
significantly exceed an independence baseline (chi-square 18,481, p < 0.001)
and adverse impact against Black applicants at 10.62% of 1,746 positions.

The record is thin, and by design should be, on the strong strict-monoculture
premise. Peng and Garg (NeurIPS 2024) build the matching-markets extension of
Kleinberg-Raghavan and prove that while polyculture achieves "wisdom of the
crowds" (only the highest-value applicants match, as m grows), on average
applicants are matched to firms they prefer *more* under monoculture, and
monoculture is more robust to differential application access; they explicitly
say their model "does not pose a greater risk of systemic exclusion overall."
Jo, Garg, and Raghavan (2026) formally show that monoculture claims are only
meaningful relative to a chosen null model of independence, and that reasonable
alternative nulls (e.g. those that account for item difficulty) can absorb
apparent excess correlation and drive it to zero. Hedden and Raghavan (2026)
philosophically defend monoculture against several standard objections and
argue the Braess effect is a "modest gap" whose price-of-anarchy is bounded.
The commission's angle survives these correctives so long as it teaches them
alongside the primary result, rather than presenting the Braess paradox as the
last word.

Two commonly cited illustrations turn out weaker than headlines suggest.
Amazon's scrapped recruiting tool (2014-2017) is a single-firm training-data
bias case, not a monoculture case: it never scored any candidate at any other
firm. The 2024 CrowdStrike outage is a shared-software-update failure in a
cybersecurity kernel driver, not a shared-scorer case, and involved no ML
model at all. Both are analogies for correlated-failure risk, not evidence for
correlated-scoring harm. The FAccT 2026 pymetrics dataset is, to the
researchers' explicit knowledge, "the first study to observe real algorithmic
outcomes for the same applicant across multiple employers" and it also finds
that "very few applicants apply to positions at different employers served by
the same underlying pymetrics model" — so even in the strongest empirical
case, total monoculture is rare and the harm operates through *partial*
sharing.

## Sources

### 1. Kleinberg and Raghavan, "Algorithmic monoculture and social welfare" (PNAS 2021)

```text
URL:         https://www.pnas.org/doi/10.1073/pnas.2018340118
Kind:        primary. The paper that names and formalizes the concept.
             Kleinberg (Cornell CS) and Raghavan (then Cornell CS, now MIT
             Sloan/EECS) own the theorem. arXiv mirror at
             https://arxiv.org/abs/2101.05853.
Establishes: (a) The formal model: n candidates with intrinsic values
             x_1 > x_2 > ... > x_n; two firms each rank candidates via a
             randomized mechanism R drawn from a "noisy permutation family"
             F_theta with accuracy parameter theta; human evaluators have
             accuracy theta_H and produce independent rankings; the
             algorithm has accuracy theta_A and produces one shared ranking
             for every firm choosing it; firms hire in random order.
             (b) Definition 2 (Preference for the first position) and
             Definition 3 (Preference for weaker competition) as the two
             conditions on the noise family.
             (c) Theorem 1: "Suppose that a given candidate distribution D
             and noisy permutation family F_theta satisfy Definition 2
             (preference for the first position) and Definition 3
             (preference for weaker competition). Then, for any theta_H,
             there exists theta_A > theta_H such that using the
             algorithmic ranking is a strictly dominant strategy for both
             firms, but social welfare would be higher if both firms used
             human evaluators."
             (d) Theorem 2 proves the conditions hold under Random Utility
             Models with Gaussian or Laplacian noise for n = 3 candidates;
             Theorem 3 proves they hold under the Mallows Model for any
             candidate distribution.
             (e) Braess'-paradox framing: introducing a more accurate
             algorithm "can drive the firms into a unique equilibrium
             that is worse for society than the one that was present
             before the algorithm existed."
             (f) A worked numeric bound: for three candidates drawn i.i.d.
             from uniform on [0,1] with Gaussian noise, at equilibrium
             both firms use the algorithm and welfare is "approximately
             4% less than it would be had both firms used human
             evaluators instead." For a candidate distribution allowing
             negative qualities, the model can produce equilibria whose
             welfare is negative while the social optimum is positive.
             (g) Two negative results that scope the claim: under the
             Plackett-Luce (Gumbel RUM) model, U_AH = U_AA for any D, so
             monoculture "never meets Definition 2" and has no effect.
             The Definition-2 conditions can also be violated for
             Laplacian noise with n=15 candidates from certain D. The
             authors call generalization beyond n=3 for RUMs an open
             question.
             (h) The dominant application throughout is "algorithmic
             hiring" (Section 2 title); lending is named alongside.
Paraphrase:  The paper is about firm competition under noisy ranking, not
             about correlated errors as such. Its central point is that
             the second-mover firm is *strictly better off* if the
             first-mover used an independent ranking rather than the same
             one, because after the top choice is taken, an independent
             evaluator's top remaining choice is expected to be better
             than the same evaluator's second choice. This "preference
             for independence" (their Equation 2) drives everything. The
             harm to overall accuracy, not the harm to any particular
             group, is the paper's contribution; the authors explicitly
             separate their result from the systemic-exclusion concern
             ("[our result] shows that it would be a mistake to view the
             harm to particular applicants as necessarily balanced against
             the gains in overall accuracy").
Locators:    Abstract; Section 2.1 (Modeling ranking, Definitions 1-3);
             Section 2.3 (Stating the main result: Theorem 1); Section 3
             (Instantiating with Ranking Models: Theorems 2-3); Section
             3.1 (four-percent example, Plackett-Luce negative result);
             Section 4 (models with multiple firms).
Quote:       "The introduction of a more accurate algorithm can drive the
             firms into a unique equilibrium that is worse for society
             than the one that was present before the algorithm existed."
             (Section 1, second paragraph after Figure 1 caption in the
             arXiv v2.)
```

### 2. Bommasani, Creel, Kumar, Jurafsky, and Liang, "Picking on the Same Person: Does Algorithmic Monoculture Lead to Outcome Homogenization?" (NeurIPS 2022)

```text
URL:         https://arxiv.org/abs/2211.13972
             (NeurIPS proceedings page:
             https://proceedings.neurips.cc/paper_files/paper/2022/hash/17a234c91f746d9625a75cf8a8731ee2-Abstract-Conference.html)
Kind:        primary. The paper introduces and defines "outcome
             homogenization" and runs the empirical tests. Authors: Rishi
             Bommasani (Stanford CS), Kathleen A. Creel (Northeastern
             Philosophy/CS), Ananya Kumar (Stanford CS), Dan Jurafsky
             (Stanford Linguistics/CS), Percy Liang (Stanford CS).
Establishes: (a) Formal definitions:
                  FAIL(h^i) = E_{x ~ D^i}[F^i(x)]
                  SYSTEMIC_FAILURE(h^1,...,h^k) = E_j[prod_i F^i(x_j^i)]
                  H^{individual} = SYSTEMIC_FAILURE / prod_i FAIL(h^i)
                  H^{group}_G = sum_g W(g) prod_i FAIL_g(h^i) / prod_i FAIL(h^i)
             The measure is the ratio of the observed rate of systemic
             failure to the rate expected from independent draws; > 1
             means outcome homogenization beyond what underlying failure
             rates would produce.
             (b) Component-sharing hypothesis: "If deployed algorithmic
             systems share components, outcome homogenization will
             increase (i.e. there will be more systemic failures)."
             (c) Data-sharing experiments on three algorithmic-fairness
             datasets - German Credit (1,000 records, 2 tasks), ACS PUMS
             (3.6 million individuals, 3 tasks), and LSAC (Appendix C) -
             using logistic regression, SVMs, gradient-boosted trees, and
             small neural networks. In the "fixed" (fully shared)
             training set, individual-level homogenization is reliably
             higher than in the "disjoint" (same distribution, different
             samples) setting across three datasets and four model
             families. Individual-level homogenization consistently
             exceeds group-level homogenization on ACS PUMS racial
             groups (group-level values near 1, with "little change as a
             function of dataset size").
             (d) Model-sharing experiments on foundation models:
                  * Vision (CelebA, two tasks: Earrings, Necklace) using
                    CLIP. The order of homogenization was scratch >
                    probing > finetuning, i.e., "scratch is the most
                    homogeneous ... this is the opposite of what we
                    hypothesized." The authors conjecture the CLIP-based
                    models are "effectively regularized" by the larger
                    WebImageText corpus.
                  * Language (four text-classification tasks) using
                    RoBERTa-base. Probing is most homogeneous; BitFit
                    (99.92% of parameters shared with the FM) and
                    finetuning (0% shared) are "roughly equally
                    homogeneous," so raw parameter-sharing count is "not
                    the right lens for understanding model sharing."
             (e) In inter-metric correlation (Table 1), outcome
             homogenization has near-zero correlation with accuracy and
             low correlation with a standard group-fairness (variance)
             metric.
Paraphrase:  Data sharing produces measurable individual-level
             homogenization; model sharing does not, at least not
             cleanly, and the effect direction depends on the adaptation
             method. The metric operates on decision-subjects (whose
             outcomes are homogenized) rather than on the models
             themselves. The individual-level metric is the one the
             argument depends on; standard group-fairness metrics can
             miss it entirely (H^{group}_avg was near 1 on ACS PUMS
             racial groups where H^{individual} exceeded 1.2).
Locators:    Abstract; Section 3 (Formalizing Outcome Homogenization,
             Equations 1-5); Section 4 (Data-sharing experiments,
             Figures 1-2); Section 5 (Model-sharing experiments,
             Figure 3); Table 1 (inter-metric correlations).
Quote:       "In Figure 3 (left), across all vision settings, we
             surprisingly find that scratch is the most homogeneous,
             i.e. more homogeneous than either approach involving FMs.
             This is the opposite of what we hypothesized."
             (Section 5.1, Results and analysis.)
```

### 3. Toups, Bommasani, Creel, Bana, Jurafsky, and Liang, "Ecosystem-level Analysis of Deployed Machine Learning Reveals Homogeneous Outcomes" (NeurIPS 2023)

```text
URL:         https://arxiv.org/abs/2307.05862
Kind:        primary. First large-scale audit of *commercially deployed*
             APIs specifically for homogenization. Authors: Connor Toups
             (Stanford), Rishi Bommasani (Stanford, corresponding),
             Kathleen A. Creel (Northeastern), Sarah H. Bana (Chapman),
             Dan Jurafsky (Stanford), Percy Liang (Stanford).
Establishes: (a) Dataset: the HAPI corpus (Chen et al. 2022), a
             three-year audit (2020-2022) of nine commercial APIs across
             three modalities - facial emotion recognition (Face++,
             Microsoft, Google on RAF-DB, AFNET, ExPW, FER+), spoken
             command recognition (IBM, Google, Microsoft on FLUENT,
             DIGIT, AMNIST), and sentiment analysis (Google, Amazon,
             Baidu on SHOP, YELP, IMDB, WAIMAI). Eleven datasets total.
             (b) Baseline: Poisson-Binomial distribution assuming
             independent per-model failures. Reported systemic-failure
             rates always exceed the independence baseline across
             all eleven HAPI datasets ("the observed rate always exceeds
             the baseline rate for the homogeneous outcomes").
             (c) Numeric example - the FER+ facial-emotion dataset (6.4k
             images, 7 classes): individual API failure rates are 0.156,
             0.316, 0.066 for the three commercial models, and the
             systemic-failure rate (all three wrong on same image) is
             0.066. On DIGIT (spoken commands), individual failure rates
             are 0.019, 0.025, 0.043 and systemic-failure rate is 0.129
             - the rate of *all-model* failure is nearly triple the
             worst individual model. On WAIMAI it is 0.065.
             (d) Model improvements barely reduce systemic failure. In
             the WAIMAI case study, Amazon reduced its individual error
             by 2.5% from 2020 to 2021, but "precisely 0 out of the
             model's 303 improvements are on instances on which other
             models had failed." Across all year-over-year improvements
             in the 11 datasets, "on average, just 10% of the
             instance-level improvement of a single commercial system
             occurs on instances misclassified by all other models."
             (e) Dermatology extension (DDI, 656 skin-lesion images):
             both models (ModelDerm and DeepDerm) and board-certified
             dermatologists show homogeneous outcomes. Models produce
             homogeneity 8.2% above baseline for darkest skin tones
             (Fitzpatrick V and VI) but 1.5% *below* baseline for the
             lightest tones; human dermatologists show no such
             skin-tone variation.
Paraphrase:  This is the strongest deployed-API evidence in the record.
             It measures actual production systems from Google, Amazon,
             Microsoft, Baidu, IBM, and Face++ over three years and
             finds that (i) systemic failure exceeds an
             independence-baseline everywhere, (ii) model improvements
             concentrate on already-easy instances and rarely help the
             users who are systemically failed, and (iii) ecosystem
             analysis surfaces a racial disparity in models (worse
             homogeneity on darker skin) that is not present in the
             human comparators. Note the paper measures homogeneity
             against a within-ecosystem independence baseline, not
             against Kleinberg-Raghavan's welfare quantity.
Locators:    Abstract; Section 3.1 (Data, Table 1 with failure rates);
             Section 3.2 (Ecosystem-level Behavior, Equations 1-2,
             Finding 1); Section 4 (Do Model Improvements Improve
             Systemic Failures?, Finding 2, WAIMAI case study); Section
             5 (DDI dermatology, Findings 3-4, Figure 6).
Quote:       "In particular, we consider all cases where at least one
             of the commercial systems improves. For example, Amazon's
             sentiment analysis API reduced its error rate on the
             WAIMAI dataset by 2.5% from 2020 to 2021; however, this
             improvement did not decrease the systemic failure rate at
             all. Precisely 0 out of the model's 303 improvements are
             on instances on which all other models had failed."
             (Page 2.)
```

### 4. Peng and Garg, "Monoculture in Matching Markets" (NeurIPS 2024)

```text
URL:         https://proceedings.neurips.cc/paper_files/paper/2024/hash/95249d42f559a0cfaf282fdf26fe2e69-Abstract-Conference.html
             (PDF at
             https://proceedings.neurips.cc/paper_files/paper/2024/file/95249d42f559a0cfaf282fdf26fe2e69-Paper-Conference.pdf)
Kind:        primary. A theoretical extension that "strengthens,
             challenges, and broadens" Kleinberg-Raghavan. Authors:
             Kenny Peng, Nikhil Garg (both Cornell Tech).
Establishes: (a) A matching-markets model with many firms (unlike
             Kleinberg-Raghavan's two-firm competition) built on
             Azevedo-Leshno's continuum framework: applicants have true
             values v; under monoculture every firm sees estimate v + X
             with X drawn once from noise D; under polyculture each firm
             sees v + X_f with X_f i.i.d. Stable matchings characterized
             by market-clearing cutoffs (Lemma 1).
             (b) Theorem 1 (Wisdom of Crowds in Polyculture but not
             Monoculture): if noise D is maximum-concentrating (e.g.
             uniform, Gaussian, lighter-than-exponential tails), then
             as the number of firms m grows the polyculture matching
             approaches optimal and firm welfare converges to
             first-best. Under monoculture the matching is *constant in
             m* and suboptimal. This strengthens Kleinberg-Raghavan's
             two-firm effect to the many-firm limit.
             (c) Theorem 2 (Likelihood of Matching to Top Choice or At
             All) has three parts that partly *reverse* the naive
             welfare reading:
                  (i) For all v, probability an applicant matches to
                      their top choice is at least as high under
                      monoculture as under polyculture.
                  (ii) If an applicant is matched under monoculture,
                       they are matched to their top choice.
                  (iii) There is a set of applicants of positive measure
                        who are simultaneously more likely to match to
                        their top choice under monoculture *and* less
                        likely to match at all - their outcome variance
                        is higher.
             (d) Theorem 3 (Differential application access): monoculture
             is *more robust* to differential application access - under
             polyculture, applicants who submit more applications gain
             more from doing so, which harms college and firm welfare
             more.
             (e) ML experiments on ACSIncome (Texas 2018 census, 13,593
             applicants across 45 feature-pair models): "for 47 out of
             50 subsets of models, the polyculture market is more
             accurate than all monoculture markets"; "for 50 out of 50
             subsets of models, the monoculture market produces better
             average applicant outcomes." California data are weaker
             (19/50 polyculture strictly best on all monocultures),
             which the authors attribute to noise not being
             max-concentrating there.
             (f) Explicit qualification: monoculture "does not pose a
             greater risk of systemic exclusion *overall*" in their
             many-firm limit; it does concentrate rejection on a
             specific set of applicants who might otherwise have been
             matched.
Paraphrase:  This is the load-bearing peer-reviewed steelman for a
             qualified defense of monoculture. It confirms
             Kleinberg-Raghavan's welfare loss and extends it, but
             cleanly separates *firm* welfare (worse under monoculture)
             from *applicant* welfare (mixed: better on average by top-
             choice match rate, worse in variance for some, robust to
             application-count differences). The paper's followup note
             (their reference [40], Baek et al. 2025) reportedly finds
             the opposite direction of Theorem 1 under long-tailed
             noise.
Locators:    Abstract; Section 1 (three bullet-pointed theorems);
             Section 2 (Related Work); Section 3 (Model with Equations
             3-4 for mono/poly); Section 4 (Theorems 1-2 and Corollary
             4); Section 5 (ML Simulations, ACSIncome results);
             Section 6 (Conclusion and Limitations).
Quote:       "In fact, we show that *on average*, applicants are better
             off under monoculture than polyculture, in the sense that
             on average, applicants are matched to firms that they more
             prefer. ... This finding can also be interpreted as
             showing that monoculture presents a greater risk of
             systemic exclusion [to more qualified applicants who
             might be overlooked by a single algorithm]. However, it
             does not pose a greater risk of systemic exclusion
             *overall*." (Bullet on Theorem 2, page 2.)
```

### 5. Bommasani, Bana, Creel, Jurafsky, and Liang, "Algorithmic Monocultures in Hiring" (FAccT 2026)

```text
URL:         https://arxiv.org/abs/2605.27371
             (ACM proceedings DOI:
             https://doi.org/10.1145/3805689.3812400)
Kind:        primary. The record's strongest deployment-level evidence,
             self-described as the first study to observe real
             algorithmic outcomes for the same applicant across many
             employers. Authors: Rishi Bommasani (Stanford), Sarah H.
             Bana (Chapman), Kathleen A. Creel (Northeastern), Dan
             Jurafsky (Stanford), Percy Liang (Stanford). All three
             first-authors are marked as equal contribution.
Establishes: (a) Dataset: 4,197,168 job applications from 3,372,132
             applicants to 1,746 positions at 156 employers, mediated by
             the pymetrics vendor from December 2018 through December
             2022. Cumulative annual revenue of the 156 employers is
             $225 billion across 11 industries (professional services,
             financial services, manufacturing, technology as the four
             largest, and Hand Laborers and Material Movers at 12.67%).
             Applicants play 12 or 16 assessment games; 41.8% of
             applications receive "not recommended" on average, and
             pymetrics builds 16 games measuring "cognitive traits"
             including risk propensity, processing speed, trust,
             altruism, and planning ability.
             (b) Market structure: "over 90% of U.S. employers rely on
             hiring algorithms to screen or rank job applicants"; "as
             of May 2023, over 60% of the Fortune 100 and eight of the
             ten largest US federal agencies use HireVue's algorithms."
             (c) Per-position adverse impact under EEOC's four-fifths
             rule: aggregate impact ratios (Asian 0.870, Black 0.839,
             Hispanic 0.916, White 0.962) do *not* fall below 0.8, so
             prior pymetrics-authored analyses found no discrimination.
             Disaggregating to the 1,746 individual positions:
                  * 10.62% of positions demonstrate adverse impact
                    against Black applicants; 30.70% of Black
                    applicants apply to at least one such position;
                    25.87% of all Black applications go to positions
                    that adversely impact Black applicants.
                  * 5.32% of positions demonstrate adverse impact
                    against Asian applicants; 18.53% of Asian applicants
                    apply to at least one; 14.74% of all Asian
                    applications go to such positions.
             By occupational group, the highest Black-adverse-impact
             rate is Computer and Mathematical positions (31.2% of
             positions, 16.7% after Benjamini-Hochberg correction).
             Under counterfactual same-rate recommendation, an
             additional 11,513 Black applications and 29,320 Asian
             applications would have been recommended.
             (d) Systemic rejection: 10% of applicants who apply to 4
             positions and 4% of applicants who apply to 10 positions
             are recommended for rejection from *all* positions. The
             rate decays exponentially (R^2 = 0.984) but more slowly
             than would be expected under independence. A chi-square
             goodness-of-fit rejects the independence baseline at
             chi-square = 18,481, p < 0.001. To guarantee a systemic
             rejection rate below 0.1%, applicants would need to submit
             25 applications versus 10 under the independence baseline.
             (e) Direct model sharing: "42 models are shared across
             positions at different companies and there are 142 unique
             employer pairs that share at least one model," so total
             algorithmic monoculture affects "rare instances" - the
             harm operates through *partial* correlation from shared
             training and shared feature construction, not through
             identical scorer replay at every employer.
             (f) Cross-check: the largest prior audit (Kline et al.
             2022, 83,000 correspondence resumes to 108 Fortune 500
             firms) shows systemic-rejection rates that match the
             independence baseline (chi-square = 20.05, p = 0.69). The
             algorithmic-hiring data "systematically diverges from this
             baseline."
Paraphrase:  This is deployed-monoculture evidence in the strict sense.
             Applicant demographic self-reporting is voluntary and only
             40.2% self-report race, so the reported adverse-impact
             counts are lower bounds. The result generalizes the
             Bommasani 2022 homogenization framework from benchmark
             datasets to real hiring decisions and shows a statistical
             independence null cannot fit the observed data. It also
             shows the strong-monoculture premise is *not* met even in
             this vendor's dataset - most applicants do not encounter
             the same model twice - so the harm arises through
             correlated modeling choices rather than identical scoring.
Locators:    Abstract; Introduction (paragraph on Fortune 100 and
             federal agencies); Section 2 (Data, applicant/employer/
             position counts, 41.8% not-recommended rate); Section 3.1
             (Adverse Impact, Table 2 by SOC group); Section 3.2
             (Homogeneity, Figure 2, 4% and 10% systemic rejection
             rates); Section 3.3 (Experimental Baseline, chi-square
             tests); Table 1 (applicant descriptive statistics);
             Introduction (25 vs 10 applications).
Quote:       "42 pymetrics models screen applicants at multiple
             companies, which means a rejection at one company
             mechanically entails rejection from another company using
             the same model. Even when applicants are evaluated by
             different pymetrics models, empirically some are
             systemically rejected. Of applicants that apply to ten
             positions, 4% are rejected from all positions." (Page 3.)
```

### 6. Jo, Garg, and Raghavan, "The Subjectivity of Monoculture" (2026 preprint)

```text
URL:         https://arxiv.org/abs/2602.24086
Kind:        primary. A methodological critique of how monoculture is
             measured, by two of the authors central to the field.
             Authors: Nathanael Jo (MIT), Nikhil Garg (Cornell Tech),
             Manish Raghavan (MIT). Preprint dated March 2, 2026.
Establishes: (a) Central thesis: "claims of 'monoculture' are only
             meaningful relative to a chosen null model of
             independence," and different reasonable null models
             produce dramatically different inferences about excess
             correlation. Under a rich enough null model, all
             cross-model correlation can be re-explained by shared
             latent parameters (their Theorem 1 gives a finite mixture
             representation).
             (b) A "null ladder" of nested progressively more
             expressive null models (Definition 1). Proposition 2:
             minimum excess correlation is monotonically non-increasing
             in null-model richness. Theorem 3: if the null ladder
             can approximate P arbitrarily well, all pairwise
             residual covariances go to zero.
             (c) Empirical demonstration on HELM (n = 14,042 questions,
             72 models) and HuggingFace Open LLM Leaderboard (n =
             11,994 questions, 451 models). Under IRT null models with
             item-difficulty parameters, apparent excess correlation on
             HELM largely vanishes; residual correlations from Kim et
             al. (2025) and Goel et al. (2025) "even flipping from
             strongly positive to slightly negative."
             (d) Second dependence on the population of models and
             items examined (Section 4). "Models that seem highly
             correlated in one context may appear independent when
             evaluated on a different set of questions, or against a
             different set of peers." On ACSIncome, random forest
             models "do not seem correlated despite sharing inductive
             biases" once other model families are absent, because item
             difficulty absorbs the agreement.
             (e) Practical implication for the field: "researchers
             should therefore carefully consider and justify these two
             choices in their evaluations" and account for item
             difficulty when claiming monoculture. Their result does
             not deny homogenization exists; it says the size of the
             claim depends on choices the analyst makes.
Paraphrase:  This paper does not overturn the theoretical claim of
             Kleinberg-Raghavan. It complicates the empirical claim
             that widely deployed models are correlated *beyond what
             independence would predict*, which is the exact claim
             Toups et al. (2023), Bommasani et al. (2022, 2026), and
             Kim et al. (2025) rest their measurements on. Because
             Manish Raghavan co-authored both the original monoculture
             paper and this critique, the paper carries unusual weight
             as a self-correction from inside the research program.
Locators:    Abstract; Section 1 (Introduction, "two subjective
             choices" argument); Section 2 (Null Model of Independence,
             Theorem 1); Section 3 (Subjectivity of Null Model,
             Definition 1 null ladder, Proposition 2, Theorem 3);
             Section 3.2 (Experiments, HELM and HF datasets, Figure 2
             correlation matrices); Section 4 (Relativity of Population,
             Proposition 4, Theorem 5, ACSIncome results); Section 5
             (Discussion).
Quote:       "Claims of 'monoculture' are only meaningful relative to a
             chosen null model of independence. In the binary setting
             ... each model output Y_ij is a Bernoulli random variable.
             ... A null model is the family of distributions P_null :=
             {P_theta : theta in Theta}, and a joint law P is
             consistent with the null model if it lies in this set."
             (Section 2.2.)
```

### 7. Hedden and Raghavan, "Algorithmic Monoculture and its Critics" (2026 preprint)

```text
URL:         https://arxiv.org/abs/2604.06047
Kind:        primary. A philosophical defense of monoculture against
             standard objections. Brian Hedden (MIT Philosophy) and
             Manish Raghavan (MIT); the same Raghavan who is one of the
             field's founders. Preprint dated April 2026.
Establishes: (a) Thesis: monoculture is "less problematic than its
             critics have supposed: commonly cited objections fail,
             and while other objections have some force, they are not
             decisive against monoculture in general."
             (b) Treatment of the Braess-paradox: acknowledged but
             narrowed. The original result shows only a "modest gap
             in performance" under "particular conditions"; recent
             work (Kleinberg et al. 2025 "Price of Anarchy in
             Algorithmic Monoculture," arXiv:2604.00444) proves the
             price-of-anarchy is "at most two" with smaller gaps in
             typical cases.
             (c) Wisdom-of-crowds objection: acknowledged that
             polyculture "will probably be more accurate than
             monoculture" via aggregation, but countered that (i)
             independent errors are implausible because polyculture
             algorithms share training data too, and (ii) a
             monoculture "algorithm could integrate all of the
             information available to different polyculture
             algorithms" (an ensemble) and thereby "match or even
             beat" the polyculture performance.
             (d) Systemic-exclusion objection: countered by the
             argument that "under both monoculture and polyculture,
             every combination of n people ... is equally likely to
             constitute those left jobless" in a stylized capacity
             model, and that rejection by one firm reshapes the
             remaining pool for another firm. Concludes: "it's far
             from clear that monoculture increases the risk of
             systemic exclusion of socially salient groups."
Paraphrase:  Read as the peer-reviewed-adjacent steelman the commission
             asks for, this paper offers three concrete counter-
             arguments the article should meet: (i) the welfare gap in
             the original theorem is modest and bounded, (ii) an
             ensemble monoculture can incorporate the diverse
             information polyculture accesses, and (iii) systemic
             exclusion is not obviously higher under monoculture once
             market equilibrium is modeled. Note this is a preprint,
             not yet in a peer-reviewed venue. The commission asks for
             a peer-reviewed critique; Peng and Garg (Source 4) is
             the peer-reviewed one, and this paper supplements it
             philosophically.
Locators:    Abstract; Section discussing the Braess result and its
             successors; Section on wisdom-of-crowds; Section on
             systemic exclusion.
Quote:       "Both models considered above assume that under
             polyculture, decision-makers make independent errors.
             This is implausible, regardless of whether polyculture
             involves human decision-makers or algorithmic ones."
             (Section on wisdom-of-crowds.)
```

### 8. Kim, Garg, Peng, and Garg, "Correlated Errors in Large Language Models" (2025 preprint, ICML)

```text
URL:         https://arxiv.org/abs/2506.07962
Kind:        primary. First large-scale measurement of error
             correlation across deployed LLMs. Authors: Elliot Kim,
             Avi Garg, Kenny Peng, Nikhil Garg (Cornell).
Establishes: (a) Datasets and scale: 349 LLMs on the HuggingFace Open
             LLM Leaderboard (12,032 multiple-choice questions), 71
             LLMs on HELM (14,042 questions), and 20 LLMs on a
             constructed resume-screening set of 1,800
             resume-job-description pairs.
             (b) Excess correlation: "On both datasets, almost all
             pairs (100% of pairs on HuggingFace; 97.5% on Helm) of
             models have a higher agreement rate than the respective
             baselines. The mean agreement rate across pairs is 0.423
             on HuggingFace and 0.6 on Helm, about double or higher
             than the baselines" (baselines 0.127 and 0.33
             respectively).
             (c) Accuracy predicts correlation: "more accurate models
             (and especially if both models are accurate) are more
             correlated." Regression analyses explain 34-62% of the
             variance in error agreement.
             (d) Correlation drivers: models share more errors when
             they share developer/company, base architecture, or
             similar size, but accuracy is the strongest single
             predictor independent of these.
             (e) Hiring simulation: "When firms each use a random LLM,
             however, we see that even with 20 firms, around 20 percent
             of applicants continue to be systemically excluded."
Paraphrase:  This is the strongest recent empirical case for the
             correlated-scorer premise in LLMs specifically. It is
             also the paper Jo, Garg, and Raghavan (Source 6) will
             later argue overstates excess correlation by using a null
             that ignores item difficulty. Kenny Peng and Nikhil Garg
             appear on both this paper and Source 4, so the same team
             produces both the strongest theoretical qualification and
             the strongest empirical measurement.
Locators:    Abstract; Section 3.1 (Data and methods); Section 3.2
             (Results, agreement statistics and Table 1); Section 5.1
             (hiring simulation with 20 firms).
Quote:       "When firms each use a random LLM, however, we see that
             even with 20 firms, around 20 percent of applicants
             continue to be systemically excluded." (Section 5.1.)
```

### 9. Winick, "Amazon ditched AI recruitment software because it was biased against women" (MIT Technology Review, October 10, 2018)

```text
URL:         https://www.technologyreview.com/2018/10/10/139858/amazon-ditched-ai-recruitment-software-because-it-was-biased-against-women/
Kind:        secondary. MIT Technology Review is reporting on a
             Reuters original (Jeffrey Dastin, October 10, 2018). The
             Reuters original at
             https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G
             is the primary; that URL was inaccessible from the
             research proxy so this secondary is used to record the
             claim.
Establishes: (a) Amazon built an internal ML system starting in 2014
             to score resumes 1-5 stars, trained on 10 years of
             submitted resumes.
             (b) The system was biased against women because the
             training data was mostly male; it penalized resumes
             containing "women's" and downgraded graduates of two
             all-women colleges.
             (c) Amazon scrapped the project in 2017. The article
             gives no evidence the tool was ever used to actually
             hire anyone, and no evidence anyone but Amazon used it.
Paraphrase:  This is the most-cited "correlated hiring-tool incident"
             in commentary, but it is *not* a monoculture case in
             Kleinberg-Raghavan's sense. It is a single-firm
             training-data bias case that never became a shared
             scorer across employers. It belongs in the article as
             the myth to distinguish from real monoculture evidence,
             not as evidence for it.
Locators:    Article body.
Quote:       Amazon "scrapped the project last year, disappointed
             with the results," according to Reuters' 2018 reporting
             as summarized here.
```

### 10. "2024 CrowdStrike-related IT outages" (Wikipedia, retrieved 2026-08-24)

```text
URL:         https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages
Kind:        secondary. A compilation citing news reports and
             CrowdStrike's own post-incident review. Used only for the
             analogy the commission names, not for any claim the
             article's argument turns on.
Establishes: (a) On July 19, 2024, a faulty configuration update to
             CrowdStrike Falcon Sensor (Channel File 291) caused
             out-of-bounds memory reads and blue-screen crashes on
             approximately 8.5 million Windows devices worldwide,
             under 1% of Windows systems.
             (b) The software is an endpoint-detection kernel driver;
             the update was pushed simultaneously to all subscribers
             with no delay mechanism.
             (c) Estimated top-500-US-company losses: $5.4 billion,
             of which $540M-$1.08B was insured; UK costs
             GBP 1.7-2.3 billion; global losses estimated in the
             tens of billions.
             (d) Affected sectors included airlines, hospitals,
             stock exchanges, emergency services, banks, and
             government agencies.
Paraphrase:  The CrowdStrike incident is a cybersecurity software-
             update failure, not an ML scoring failure. It illustrates
             the correlated-failure property of shared infrastructure
             (one update, millions of simultaneous kernel panics),
             which is the analogy the algorithmic-monoculture
             literature (Citron and Pasquale in Kleinberg-Raghavan's
             introduction, and Toups et al. throughout) uses to
             motivate the concern. Not evidence for correlated
             algorithmic scoring; only evidence for what happens when
             one piece of shared infrastructure fails.
Locators:    Wikipedia article body, sections on cause, scope, and
             financial impact.
Quote:       None used in article. Use the direct CrowdStrike
             post-incident report if a quotation is needed.
```

## Contradictions

The record contains real contradictions with the commission's angle. Every
one below is between primary sources.

1. **Kleinberg-Raghavan themselves scope their result to two-firm competition
   with three candidates for RUMs, and note it fails under Plackett-Luce.**
   Their Section 3.1 states outright: "under the Plackett-Luce model,
   monoculture has no effect - the optimal strategy is always to use the best
   available ranking, regardless of competitors' strategies." Section 3.1
   also gives a Laplacian n=15 candidate distribution that violates
   Definition 2. The theorem is not a universal claim about shared
   algorithms; it depends on structural properties of the noise family, and
   the paper flags generalization beyond n=3 for RUMs as an open question.

2. **The Bommasani 2022 model-sharing experiments do not clearly support
   the commission's angle.** Training from *scratch* on CelebA was more
   homogeneous than probing or finetuning of CLIP. Finetuning RoBERTa
   (0% parameter sharing) and BitFit (99.92% parameter sharing) produced
   "roughly equally homogeneous" outcomes on language tasks. The authors
   explicitly write: "the number of shared parameters is probably not the
   right lens for understanding model sharing." The data-sharing result
   holds; the model-sharing result is muddled and sometimes goes the wrong
   way for the hypothesis.

3. **Peng and Garg (NeurIPS 2024) prove that on average, applicants are
   matched to firms they *prefer* under monoculture, and that monoculture is
   *more robust* to differential application access.** Their Theorem 2(i)
   states that for all applicant values v, the probability of matching to
   the top-choice firm is at least as high under monoculture as under
   polyculture. Their explicit summary: monoculture "does not pose a
   greater risk of systemic exclusion *overall*." This partly contradicts
   the commission's framing that "being rejected once is being rejected
   everywhere" - under a matching-markets model, being *matched* once may
   be being matched to your top choice.

4. **Jo, Garg, and Raghavan (2026) show measured excess correlation is
   sensitive to the null model and the population of models.** With an
   item-response-theory null that accounts for item difficulty, they
   report that residual correlations from Kim et al. (2025, Source 8) and
   Goel et al. (2025) partly vanish, "even flipping from strongly positive
   to slightly negative." Manish Raghavan co-authored both the original
   PNAS paper and this critique, so this is a self-correcting move within
   the field. The commission should not present current excess-correlation
   measurements as settled.

5. **The Bommasani 2026 FAccT deployment paper qualifies its own strong-
   monoculture reading.** Section 3.2 notes: "very few applicants apply to
   positions at different employers served by the same underlying pymetrics
   model. Therefore, we study the more general and frequent form of
   algorithmic monoculture, where an applicant applies to multiple
   positions mediated by pymetrics models." Only 142 unique employer pairs
   in the dataset share at least one model. The demonstrated harm is from
   *partial* correlation through shared vendor / shared feature
   construction, not from identical scoring by the same model at every
   employer.

6. **Toups et al.'s dermatology extension found dermatologists were *more*
   homogeneous than the models.** The finding sits inside a monoculture-
   concerning paper but complicates the story: humans, on the DDI dataset,
   showed even higher rates of consistent joint success and joint failure
   than the two ML models did. Ecosystem-level homogeneity is not unique
   to machines. What was unique to the models was skin-tone-linked
   racial variation in homogeneity.

7. **Kleinberg-Raghavan's four-percent worked example is small.** Their
   uniform-Gaussian instance with 3 candidates gives approximately 4% loss
   in expected welfare at the monoculture equilibrium versus the
   human-evaluator equilibrium. The paper also shows an example where
   optimal welfare is positive and equilibrium welfare is negative, but
   that requires candidate values allowed to be negative (workers whose
   cost to the firm exceeds their wage). The commission should give the
   4% figure alongside the possibility of larger swings, not the larger
   swings alone.

8. **Amazon's scrapped internal tool (2014-2017, Source 9) does not fit
   the monoculture argument.** No other firm used the tool; the harm
   documented is training-data bias in one company's system, not
   correlated scoring across many firms. It is often cited as if it were
   monoculture evidence and is not. The article should either drop it or
   name it explicitly as the case people confuse for monoculture.

## Numbers

```text
Figure: 4% (approximately)
Owner:  Kleinberg and Raghavan 2021, Section 3.1
Scope:  Expected social-welfare loss at monoculture equilibrium versus
        human-evaluator equilibrium in a stylized 3-candidate Gaussian-
        noise RUM with candidate values drawn uniformly at [0,1]
        centered at 0. Illustrative single instance, not a general
        bound.
```

```text
Figure: at most 2 (price of anarchy)
Owner:  Hedden and Raghavan 2026 (citing Kleinberg et al. 2025,
        arXiv:2604.00444)
Scope:  Ratio of social welfare at the social optimum to social
        welfare at the monoculture equilibrium in a follow-up
        theoretical model. Reported as an upper bound; not verified
        against the primary Kleinberg 2025 paper in this record.
```

```text
Figure: 0.423 mean pairwise agreement on HuggingFace; 0.6 on HELM
Owner:  Kim, Garg, Peng, Garg 2025, Section 3.2
Scope:  Mean rate at which LLM pairs give the same wrong answer,
        conditional on both being wrong. Baselines are 0.127 on
        HuggingFace and 0.33 on HELM (random-choice baselines from
        the answer distributions). Over 349 LLMs and 12,032 questions
        on HuggingFace, 71 LLMs and 14,042 questions on HELM.
```

```text
Figure: 20% systemically excluded with 20 firms
Owner:  Kim, Garg, Peng, Garg 2025, Section 5.1
Scope:  Simulation using 20 real LLMs to score 60 resumes across
        30 job descriptions. Even when each of 20 firms picks a
        different LLM, roughly one-fifth of applicants receive
        "do not hire" from every one.
```

```text
Figure: 4,197,168 applications; 3,372,132 applicants; 1,746 positions;
        156 employers; 11 industries; $225B aggregate revenue
Owner:  Bommasani et al. 2026 FAccT, Section 2
Scope:  pymetrics-mediated hiring, December 2018 through December
        2022, worldwide (majority North America, majority employer
        revenue >= $5 billion). Applications are what pymetrics
        scored; not all reached a human hiring decision.
```

```text
Figure: 10.62% (Black adverse impact positions);
        30.70% (Black applicants applying to at least one);
        25.87% (Black applications directed to such positions);
         5.32% (Asian adverse impact positions);
        18.53% (Asian applicants applying to at least one);
        14.74% (Asian applications directed to such positions)
Owner:  Bommasani et al. 2026 FAccT, Section 3.1
Scope:  1,746 positions analyzed under EEOC four-fifths-rule
        per-position, positions with at least 30 self-reporting
        applicants of a given race. Position-level adverse impact
        after Benjamini-Hochberg correction alpha = 0.05.
```

```text
Figure: 10% (4-application applicants systemically rejected);
         4% (10-application applicants systemically rejected);
        chi-square = 18,481, p < 0.001
Owner:  Bommasani et al. 2026 FAccT, Section 3.2
Scope:  All pymetrics applicants who applied to at least the stated
        number of positions during 2018-2022. Chi-square goodness-
        of-fit against a Poisson-Binomial baseline that assumes
        independent per-position rejection decisions.
```

```text
Figure: 60% (Fortune 100 using HireVue); 8 of 10 (largest US federal
        agencies using HireVue)
Owner:  Bommasani et al. 2026 FAccT, Introduction (citing their
        reference [44])
Scope:  As of May 2023. HireVue is a different vendor than
        pymetrics; the statistic bounds the market concentration
        but does not describe the data the paper analyzes.
```

```text
Figure: 42 pymetrics models shared across positions at different
        companies; 142 unique employer pairs sharing at least one
        model
Owner:  Bommasani et al. 2026 FAccT, Section 3.2
Scope:  Same 156-employer dataset. The paper uses this to argue
        that *total* algorithmic monoculture is rare and that the
        harm operates through the more general partial-sharing
        form.
```

```text
Figure: 0 of 303 (Amazon-WAIMAI single-model improvements on
        instances all-other-models had failed); 10% (average
        share of single-model improvements that fall on
        all-fail instances across HAPI)
Owner:  Toups et al. 2023 NeurIPS, Section 4 (Finding 2, WAIMAI
        case study; Figure 4b for the 10% average across datasets).
Scope:  Model improvements from year to year in the HAPI audit
        of nine commercial ML APIs over 2020-2022. WAIMAI is a
        Chinese-language food-delivery review sentiment dataset.
```

```text
Figure: 0.129 (systemic-failure rate on DIGIT); 0.043 (worst
        individual model failure rate)
Owner:  Toups et al. 2023 NeurIPS, Table 1
Scope:  DIGIT spoken command recognition, 2,000 examples, three
        commercial APIs (IBM, Google, Microsoft). The rate of
        instances all three misclassify is about triple the
        worst individual model.
```

```text
Figure: 0.152, 0.178, 0.181, 0.066 (systemic failure rates on
        the four facial-emotion datasets RAFDB, AFNET, EXPW, FER+)
Owner:  Toups et al. 2023 NeurIPS, Table 1
Scope:  Facial emotion recognition APIs from Face++, Microsoft,
        Google. Dataset sizes 15.3k, 287.4k, 31.5k, 6.4k.
```

```text
Figure: 8.2% (dark-skin homogeneity above baseline);
        1.5% below baseline for light skin
Owner:  Toups et al. 2023 NeurIPS, Section 5.2 and Figure 6a
Scope:  DDI dermatology, 656 images, ModelDerm and DeepDerm,
        Fitzpatrick V-VI (dark) versus I-II (light). Human
        dermatologists show no comparable skin-tone variation.
```

```text
Figure: 8.5 million Windows devices; less than 1% of Windows systems;
        USD ~$5.4 billion top-500-US-company losses
Owner:  2024 CrowdStrike outage, secondary compilation
Scope:  July 19, 2024. Used only as the correlated-failure analogy
        the commission names, not as evidence for correlated
        algorithmic scoring.
```

## Source assets

```text
Asset: Figure 1 of Kleinberg and Raghavan 2021 - the three-column
       diagram showing Firm 1's ranking, Firm 2's ranking, and the
       Algorithmic ranking, with candidates A/B/C/D shown in
       different orders under each. The caption walks through the
       hire order.
Shows: The single mechanism the whole argument turns on -
       independent versus shared rankings, and what "hire in random
       order" means concretely. A reader who has this image has the
       model.
Crop:  Must retain all three ranking columns and the arrow lines
       from "Firm 1"/"Firm 2" boxes at the top; do not crop out
       the caption because the walkthrough is in it.
```

```text
Asset: Figure 3 of Kleinberg and Raghavan 2021 - the theta_A vs
       theta_H phase plot showing the four equilibrium regions
       (HH, AH, AA) and the shaded green region where the
       monoculture equilibrium is worse for welfare than the
       human-evaluator equilibrium.
Shows: The exact parameter region where monoculture bites, and
       how narrow it can be. This is the picture that lets a
       reader see the conditional nature of the theorem.
Crop:  Must retain both axes with their labels; the shaded
       green sliver near the diagonal is the specific claim.
```

```text
Asset: Figure 2 of Bommasani et al. 2026 FAccT (systemic rejection
       rate) - two side-by-side bar charts. Left: pymetrics
       observed rejection rate versus independence baseline as a
       function of number of applications (2 through 8). Right:
       Kline et al. 2022 correspondence-study rejection rate
       versus baseline.
Shows: A single image contains both the deployed-monoculture
       evidence (pymetrics data significantly exceeds baseline)
       and the human-hiring null result (Kline's data matches
       baseline). The contrast is the paper.
Crop:  Must retain both subplots and both legends; the point is
       the comparison. Do not crop labels.
```

```text
Asset: Figure 2a of Toups et al. 2023 - the observed vs baseline
       Ecosystem-level outcomes histogram for the DIGIT dataset.
       Shows "models correct" 0/1/2/3 buckets. The observed
       distribution has taller bars at 0 and 3 (all-fail and
       all-succeed) than the baseline.
Shows: The clearest visual demonstration of ecosystem-level
       homogeneity: the observed distribution has more mass at
       the extremes than independence predicts.
Crop:  Retain the "Observed" and "Baseline" legend and both
       axis labels. This bar chart carries the entire finding.
```

```text
Asset: Figure 4 of Kim et al. 2025 (correlated errors) - correlation
       matrix of pairwise error correlation across the tested LLMs,
       clustered by developer. See paper for exact figure number.
Shows: That models from the same developer cluster together, and
       the overall correlation structure. A reader can see the
       market-concentration issue visually.
Crop:  Must retain the axis labels showing developer names;
       otherwise the clustering is invisible.
```

```text
Asset: Bommasani 2026 Table 2 - the disparate impact ratio table by
       SOC major occupation group and race. Contains impact ratios,
       number of positions, and adverse-impact counts and shares.
Shows: The concrete numbers behind the article's central claim of
       demonstrated adverse impact. Reproduces in article form.
Crop:  This is a table, not an image; publish as a formatted table
       rather than a screenshot. Retain the BH-corrected columns.
```

## Discarded

```text
URL: https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G
  Blocked by the research proxy. Content confirmed via Source 9
  (MIT Technology Review) which cites this Reuters original.
```

```text
URL: https://www.pnas.org/doi/10.1073/pnas.2018340118 (direct HTML)
  Returned 403 through the fetch route; the PDF via the arXiv
  mirror at https://arxiv.org/pdf/2101.05853 was accessible and
  read in full. The PNAS DOI still resolves to the source's own
  page for readers and is used as the recorded URL.
```

```text
URL: https://d3.harvard.edu/platform-peopleanalytics/submission/hirevue-a-face-scanning-algorithm-decides-whether-you-deserve-the-job
  Business-school platform blog post about HireVue's marketing
  claims; not first-hand and not needed once the FAccT 2026
  paper documents HireVue's Fortune 100 penetration from its
  own primary reference.
```

```text
URL: https://arxiv.org/abs/2604.00444 (Kleinberg et al. 2025,
  "Price of Anarchy in Algorithmic Monoculture")
  Named by Hedden and Raghavan for the "at most two" price-of-
  anarchy claim. Not opened in full in this record; the citation
  is passed through Source 7. If the price-of-anarchy figure
  becomes load-bearing for the article, this primary must be
  read directly before writing.
```

```text
URL: https://arxiv.org/pdf/2412.08610 (Competition and Diversity
  in Generative AI, Jagadeesan 2024)
  Related but a different failure mode: it studies incentive
  effects among generative model providers, not correlated
  scoring against decision subjects. Belongs in a Background
  link at most.
```

```text
URL: https://algorithmichiring.github.io/
  Author-hosted landing page for Bommasani et al. 2026. The
  paper itself (Source 5) is the citable source; the landing
  page is a portal and not the artifact.
```
