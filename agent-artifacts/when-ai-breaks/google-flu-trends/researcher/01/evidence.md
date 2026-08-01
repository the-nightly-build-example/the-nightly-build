# Evidence record — when-ai-breaks/google-flu-trends

This record supports the full narrative arc the commission asks for: what Google
Flu Trends (GFT) was built to do, its 2008 launch and reported accuracy, its
2009 miss of the swine-flu pandemic and the model revision that followed, the
2011–2013 systematic overestimation (with the exact figures traced to their
owning primaries), the disputed cause (media panic vs. algorithm dynamics vs.
big-data hubris), and the August 2015 shutdown. All four commission-required
primaries were read in full: Ginsberg 2009 (Nature), Lazer 2014 (Science),
Cook 2011 (PLoS ONE), and Google's own record — both the 2015 shutdown post
and, better than the vague "2013 update post" the brief anticipated, the
actual internal Google paper explaining the 2012–2013 failure (Copeland et
al., "Google Disease Trends: An Update," 2013), which gives Google's own
exact numbers for the overestimation and independently confirms the "more
than double" figure. A post-hoc improvement paper (Yang, Santillana, Kou,
PNAS 2015) supplies the "later fixes helped" side of the disputed-cause
question. One contemporaneous secondary account (Time, March 2014) is read in
full and carries a direct Lazer quote. The record is thin in exactly one
place: Declan Butler's Nature News piece ("When Google got flu wrong," Feb.
2013), the article Lazer's own paper cites for the "more than double" claim,
is paywalled — only its title, subtitle, and date could be confirmed
firsthand; its substantive numbers are not cited here because Lazer 2014 and
Copeland et al. 2013 independently supply the same figures from sources that
were fully read. Nothing in the "where the weakness lives today" close is
sourced here; the commission treats that as the writer's connective work, not
a new research obligation for this GFT-specific source list.

## Sources

### 1. Ginsberg, Mohebbi, Patel, Brammer, Smolinski, Brilliant, "Detecting
influenza epidemics using search engine query data," *Nature* 457,
1012–1014 (19 February 2009). Authors: Jeremy Ginsberg, Matthew H. Mohebbi,
Rajan S. Patel, Mark S. Smolinski, Larry Brilliant — all Google Inc.;
Lynnette Brammer — CDC (contributed CDC surveillance data as a co-author, not
an independent check). Read in full (Google's hosted copy,
static.googleusercontent.com/media/research.google.com/en//archive/papers/detecting-influenza-epidemics.pdf,
which mirrors the Nature-published text page-for-page; confirmed against the
paywalled nature.com/articles/nature07634 landing page, which resolves and
carries matching abstract).
- **Classification: PRIMARY.** The paper is the design document and first
  accuracy claim for GFT, authored entirely by the team that built it (plus
  one CDC co-author who supplied surveillance data). It owns every claim
  about the original model's construction and its 2003–2008 validated
  accuracy.
- **What it establishes firsthand:** The method — mining Google's own search
  logs (not third-party reporting) and fitting a linear model on the
  log-odds scale; the automated query-selection process; the 2003-2007
  training window and 2007-2008 validation window; the reported accuracy
  figures; the lag advantage over CDC; and — notably — the authors' own
  stated caveats about the model's fragility to media panic, written four
  years before that exact failure occurred.
- **Useful verbatim passages:**
  - "we can accurately estimate the current level of weekly influenza
    activity in each region of the United States, with a reporting lag of
    about one day" (abstract).
  - "By aggregating historical logs of online web search queries submitted
    between 2003 and 2008, we computed time series of weekly counts for 50
    million of the most common search queries in the United States."
  - "Each of the 50 million candidate queries in our database was separately
    tested... to identify the search queries which could most accurately
    model the CDC ILI visit percentage in each region."
  - "Combining the N=45 highest-scoring queries was found to obtain the best
    fit." Figure 1 caption: "A steep drop in model performance occurs after
    adding query 81, which is 'oscar nominations.'"
  - "The model was able to obtain a good fit with CDC-reported ILI
    percentages, with a mean correlation of 0.90 (min=0.80, max=0.96, n=9
    regions)."
  - "Estimates generated for these 42 points obtained a mean correlation of
    0.97 (min=0.92, max=0.99, n=9 regions) with the CDC-observed ILI
    percentages" (out-of-sample validation, 2007-2008 season).
  - "we were able to consistently estimate the current ILI percentage 1-2
    weeks ahead of the publication of reports by the CDC's U.S. Influenza
    Sentinel Provider Surveillance Network."
  - "This system is not designed to be a replacement for traditional
    surveillance networks or supplant the need for laboratory-based
    diagnoses and surveillance."
  - "Alternatively, panic and concern among healthy individuals may cause a
    surge in the ILI-related query fraction and exaggerated estimates of the
    ongoing ILI percentage" — the authors' own predicted failure mode,
    written in 2009, that is essentially what happened in 2012-2013.
  - Methods: "we fit 450 million different models to test each of the
    candidate queries," using MapReduce across "hundreds of machines."
    Training: 128 points/region (Sept 28, 2003–Mar 11, 2007), validation: 42
    points/region (Mar 18, 2007–May 11, 2008).
  - "This system will be used to track the spread of influenza-like illness
    throughout the 2008-2009 influenza season" — i.e., the paper describes
    the model as it stood going into the season that included the 2009
    H1N1 pandemic.
- **Locators:** Abstract p.1; Methods/model-fitting narrative p.2; query
  selection and Figure 1, p.2; accuracy results, validation, and limitations
  paragraph, p.3; full Methods section (query database, model data,
  computation), pp.4-5.

### 2. Cook, Conrad, Fowlkes, Mohebbi, "Assessing Google Flu Trends
Performance in the United States during the 2009 Influenza Virus A (H1N1)
Pandemic," *PLoS ONE* 6(8): e23610 (19 August 2011). Authors: Samantha Cook
and Matthew H. Mohebbi — Google, Inc., New York; Corrie Conrad — Google,
Inc., London; Ashley L. Fowlkes — Influenza Division, CDC, Atlanta. Funded by
Google.org; the paper discloses "Three of the authors (SC, CC, MM) are
employees of one of the funders of the study (Google Inc.)." Read in full
(open-access PDF via journals.plos.org).
- **Classification: PRIMARY.** This is Google's own (with one CDC co-author)
  firsthand account of the 2009 swine-flu miss and the model revision it
  triggered — the paper the commission names as the "Cook 2011" source.
- **What it establishes firsthand:** The original (2008) GFT model's
  performance collapsed during the initial onset of the 2009 H1N1 pandemic
  (spring/summer, non-seasonal), the magnitude and direction of that error
  (underestimation, not overestimation), what the September 24, 2009 revised
  model changed, and why Google's own researchers believe the miss happened.
- **Useful verbatim passages:**
  - Abstract: "the original model underestimated the magnitude of ILI
    activity during pH1N1. The updated model was more correlated with ILINet
    than the original model during Summer H1N1 (r = 0.95 and 0.29,
    respectively)."
  - "The updated model launched on September 24, 2009 incorporated ILINet
    data from April-September, 2009."
  - Table 2 (exact figures): Original model correlation — pre-pH1N1 0.906,
    pH1N1 overall 0.912, Wave 1 (Mar-Aug 2009) **0.290**, Wave 2 (Aug-Dec
    2009) 0.916. Updated model correlation — pre-pH1N1 0.942, pH1N1 overall
    0.989, Wave 1 0.945, Wave 2 0.985. RMSE: original 0.006/0.018/0.008/0.023
    across the same four periods; updated 0.005/0.005/0.001/0.007.
  - "During the pH1N1 period, the original model underestimated ILINet data
    by an average of 0.014, a near three-fold increase in average error
    compared to the next-least-accurate season (2003)... as evidenced by the
    threefold increase in RMSE compared to the pre-pH1N1 period."
  - "The updated model included approximately 160 search query terms related
    to influenza activity, compared with approximately 40 in the original
    model... Queries in the categories 'influenza complication' and
    'symptoms of an influenza complication' made up 48% of the volume of the
    original model; in the updated model, these categories comprise only 17%
    of the volume. Queries in the categories 'general influenza symptoms'
    and 'specific influenza symptoms' comprise 69% of the updated model
    volume, compared with only 8% of original model volume."
  - Cause, as the authors state it: "users were searching less for queries
    related to influenza complications such as bronchitis and pneumonia...
    the pH1N1 virus emerged during the spring and summer months, rather than
    the fall and winter months typical for seasonal influenza. People may
    search using different query terms when ill with flu in the winter
    versus the summer."
  - "Queries such as 'swine flu' were popular during the pH1N1 pandemic and
    likely accounted for some of the changes in search behavior; however,
    such pandemic-specific queries are not included in GFT models because
    they do not correlate well with ILINet data in previous seasons."
- **Locators:** Abstract p.1; Methods (model description, time-period
  definitions), pp.1-2; Table 1 (query category composition) p.2; Table 2
  (correlation/RMSE by period) and Results, pp.4-6; Discussion (candidate
  causes), pp.6-7.

### 3. Lazer, Kennedy, King, Vespignani, "The Parable of Google Flu: Traps in
Big Data Analysis," *Science* 343(6176): 1203-1205 (14 March 2014 issue;
article dated 13 March 2014). Authors: David Lazer — Lazer Laboratory,
Northeastern University, and Harvard Kennedy School; Ryan Kennedy —
Institute for Quantitative Social Science, Harvard, and University of
Houston; Gary King — Institute for Quantitative Social Science, Harvard;
Alessandro Vespignani — Laboratory for the Modeling of Biological and
Sociotechnical Systems, Northeastern, and ISI Foundation, Turin. None are
Google employees or GFT authors; this is genuinely outside critique. Read in
full (PDF retrieved via dhi.ac.uk mirror).
- **Classification: PRIMARY.** This is the paper itself, not a summary of
  it — the commission's designated "definitive post-mortem," authored by
  researchers with no stake in GFT's success, drawing on their own
  replication analysis (in the paper's supplementary materials).
- **What it establishes firsthand:** The exact overestimation figures for
  2011-2013, the "100 of 108 weeks" figure and its date range, the two
  named mechanisms (big data hubris, algorithm dynamics), the specific
  Google algorithm changes implicated, and the authors' own proposed fixes.
- **Useful verbatim passages:**
  - "In February 2013, Google Flu Trends (GFT) made headlines... *Nature*
    reported that GFT was predicting more than double the proportion of
    doctor visits for influenza-like illness (ILI) than the Centers for
    Disease Control and Prevention (CDC)... This happened despite the fact
    that GFT was built to predict CDC reports."
  - "the methodology was to find the best matches among 50 million search
    terms to fit 1152 data points. The odds of finding search terms that
    match the propensity of the flu but are structurally unrelated, and so
    do not predict the future, were quite high... This should have been a
    warning that the big data were overfitting the small number of
    cases — a standard concern in data analysis."
  - "This ad hoc method of throwing out peculiar search terms failed when
    GFT completely missed the nonseasonal 2009 influenza A-H1N1 pandemic...
    In short, the initial version of GFT was part flu detector, part winter
    detector."
  - "GFT also missed by a very large margin in the 2011-2012 flu season and
    has missed high for 100 out of 108 weeks starting with August 2011."
  - Figure caption (exact): "GFT overestimated the prevalence of flu in the
    2012-2013 season and overshot the actual level in 2011-2012 by more
    than 50%. From 21 August 2011 to 1 September 2013, GFT reported overly
    high flu prevalence 100 out of 108 weeks."
  - "Mean absolute error (MAE) during the out-of-sample period is 0.486 for
    GFT, 0.311 for lagged CDC, and 0.232 for combined GFT and CDC. All of
    these differences are statistically significant at P < 0.05."
  - "The most common explanation for GFT's error is a media-stoked panic
    last flu season. Although this may have been a factor, it cannot
    explain why GFT has been missing high by wide margins for more than 2
    years... A more likely culprit is changes made by Google's search
    algorithm itself... the official Google search blog reported 86 changes
    in June and July 2012 alone."
  - "Google reported in June 2011 that it had modified its search results to
    provide suggested additional search terms and reported again in
    February 2012 that it was now returning potential diagnoses for
    searches including physical symptoms like 'fever' and 'cough.'"
  - "GFT has never documented the 45 search terms used, and the examples
    that have been released appear misleading."
  - "If you are 90% of the way there, at most, you can gain that last 10%"
    (on the limited further value of a stand-alone lagged-CDC-beating
    model).
- **Locators:** p.1203, "Big Data Hubris" section (overfitting/2009 miss);
  p.1204, "Algorithm Dynamics" section and the two-panel chart (exact figures
  and dates); p.1205, "Transparency and Replicability" and closing
  recommendations.

### 4. Copeland, Romano, Zhang, Hecht, Zigmond, Stefansen, "Google Disease
Trends: An Update," Google, 2013 (cited by Lazer et al. 2014, ref. 15, as
"P. Copeland et al., Int. Soc. Negl. Trop. Dis. 2013, 3 (2013)"). Authors:
Patrick Copeland, Raquel Romano, Tom Zhang, Greg Hecht, Dan Zigmond,
Christian Stefansen, all identified with google.org / the GFT engineering
team. Read in full (PDF via
static.googleusercontent.com/media/research.google.com/en//pubs/archive/41763.pdf).
- **Classification: PRIMARY.** This is Google's own internal account of the
  2012-2013 failure, written by the GFT engineering team itself — the
  closest thing to Google's "2013 model-update post" the brief asked for,
  and more substantive than the public blog post (which could not be
  retrieved; see Discarded).
- **What it establishes firsthand:** Google's own exact numbers for the
  overestimation (independently confirming the "more than double" figure
  Nature/Lazer report), Google's own stated cause (media-driven query
  spikes, not algorithm changes — the position Lazer's paper argues
  against), and the specific fixes Google tried (spike detectors, Lasso,
  Elastic Net, Bayesian structural time series).
- **Useful verbatim passages:**
  - Abstract: "During the 2012 flu season we observed our algorithm
    overestimating influenza-like illness (ILI). We have concluded that our
    algorithm for Flu and Dengue were susceptible to heightened media
    coverage and have since developed several improvements."
  - "From the launch in 2008 until the 2012-13 season, the highest
    estimation error for national flu incidence was 1.13 percentage points
    (week starting Jan. 1, 2012: CDC data 1.74%, GFT estimate 2.86%), and
    the mean absolute error during this period across all weekly estimates
    was 0.30 percentage points. However, in the 2012-13 season, the
    overestimation peaked at 6.04 percentage points, an estimate more than
    twice the CDC-reported incidence (week starting Jan. 13: CDC data 4.52%,
    GFT estimate 10.56%)."
  - "It became clear that our algorithm was susceptible to bias in
    situations where searches for flu-related terms on Google.com were
    uncharacteristically high within a short time period. We hypothesized
    that concerned people were reacting to heightened media coverage, which
    in turn created unexpected spikes in the query volume."
  - "When we launched GFT in 2008 the New York Times published a story that
    included an example query that was actually used in the model. We
    immediately saw traffic increase on that query term... divulging the
    query list would result in skewing the model."
  - "As far back as 2008, we knew that most query spikes caused by news
    attention tend to last for 3 to 7 days. The problem is that our detector
    solved for short-term spikes, but didn't consider unusually high query
    volume that lasted for an entire season."
  - "We've addressed this with two areas of improvement: 1) dampening
    anomalous media spikes and 2) using ElasticNet... These regression
    models significantly improve over the incumbent, but still slightly
    overpredict the 2012-13 flu levels" (Table: week of 2013-01-13, CDC
    4.52%, production GFT 10.56%, retrained model 8.21%, Lasso 6.88%,
    ElasticNet 5.82%, BSTS 6.27%).
- **Locators:** Abstract and Background, p.1; Algorithm section, p.2; "What
  happened this year?" and Conclusion sections, pp.2-3; results table, p.3.

### 5. "The Next Chapter for Flu Trends," Google Research Blog (posted by
"The Flu Trends Team"), 20 August 2015. research.google/blog/the-next-chapter-for-flu-trends/
(mirrored at ai.googleblog.com and the retired googleresearch.blogspot.com
URL). Read directly.
- **Classification: PRIMARY.** Google's own announcement of the shutdown,
  in Google's own voice, on Google's own platform.
- **What it establishes firsthand:** The date and fact of the shutdown, what
  replaced the public site, and Google's own chosen framing (notably: no
  admission of the overestimation error appears in this post).
- **Useful verbatim passages:**
  - "When a small team of software engineers first started working on Flu
    Trends in 2008, we wanted to explore how real-world phenomena could be
    modeled using patterns in search queries."
  - "Instead of maintaining our own website going forward, we're now going
    to empower institutions who specialize in infectious disease research
    to use the data to build their own models" — naming Columbia
    University's Mailman School of Public Health, Boston Children's
    Hospital/Harvard, and the CDC as data recipients.
  - "Flu continues to affect millions of people every year, and while it's
    still early days for nowcasting and similar tools for understanding the
    spread of diseases like flu and dengue fever — we're excited to see what
    comes next."
  - Notable by absence: the post does not use the words "overestimate,"
    "error," or "wrong," and does not mention the 2012-2013 episode or the
    Lazer paper (published 17 months earlier) at all.
- **Locator:** Full post is short (roughly 300 words); every passage above
  is from the single continuous text.

### 6. Yang, Santillana, Kou, "Accurate estimation of influenza epidemics
using Google search data via ARGO," *Proceedings of the National Academy of
Sciences* (2015; submitted 5 May 2015). Authors: Shihao Yang, Mauricio
Santillana, S.C. Kou — no Google affiliation; Santillana is the researcher
the commission names as a candidate for "later analysis." Read the abstract
and framing (arxiv.org/abs/1505.00864 preprint listing; PNAS is the
published venue).
- **Classification: PRIMARY** for the narrow claim it makes about its own
  model's comparative performance (the authors built and tested ARGO
  themselves against GFT). It is not independent verification of GFT's
  errors — those come from Lazer and Copeland above.
- **What it establishes firsthand:** That the search-data-plus-CDC approach
  itself was not irredeemable — a later model built by outside researchers,
  using autoregression with regularization (not GFT's original method),
  "outperforms all previously available Google-search-based tracking
  models, including the latest version of Google Flu Trends," while using
  only "low-quality search data... from publicly available Google Trends
  and Google Correlate." This is the strongest available evidence for the
  "defenders argued post-2013 fixes improved it" side the commission asks
  to represent fairly — though note ARGO is a different model built by
  outside academics, not a Google-shipped fix.
- **Locator:** Abstract only was accessible in this pass; full-text
  performance tables were not retrieved and are not cited here.

### 7. Bryan Walsh, "Google Flu Trends Failure Shows Drawbacks of Big Data,"
*Time*, 13 March 2014. Read in full via WebFetch.
- **Classification: SECONDARY.** Independent magazine journalism reporting
  on the Lazer paper's release, with an original interview quote from Lazer
  not found in the Science paper itself. Time has no stake in GFT or in the
  Lazer paper's findings.
- **What it establishes:** That the Lazer paper's headline findings were
  reported accurately and contemporaneously in a general-interest outlet,
  and supplies one directly attributed quote.
- **Useful verbatim passages:**
  - "GFT overestimated the prevalence of flu in the 2012-2013 and 2011-2012
    seasons by more than 50%" — restates the Lazer figure; not an
    independent number.
  - "From August 2011 to September 2013, GFT over-predicted the prevalence
    of the flu in 100 out 108 weeks" — same, restating Lazer.
  - David Lazer, quoted directly: "It's a Dewey beats Truman moment for big
    data," comparing GFT's failure to the 1948 *Chicago Tribune* headline
    that wrongly declared Dewey the presidential winner.
  - The article frames the episode as "automated arrogance, or big data
    hubris" — echoing (and naming) the Lazer paper's own term.
- **Locator:** Single continuous web article; quote appears roughly
  two-thirds through the piece per the fetch extraction.

## Contradictions

- **Cause of the 2012-2013 overestimation is genuinely disputed between
  Google's own team and the outside critique, and both sides were read
  firsthand.** Google's own paper (Copeland et al. 2013, source 4) concludes
  the cause was **media-driven query spikes**: "We have concluded that our
  algorithm for Flu and Dengue were susceptible to heightened media
  coverage," and describes a specific failure of Google's own "spike
  detector," which was built to catch short news-driven spikes (3-7 days)
  but not a season-long elevated baseline. Lazer et al. (source 3) directly
  rejects media panic as sufficient: "The most common explanation for GFT's
  error is a media-stoked panic last flu season. Although this may have been
  a factor, it cannot explain why GFT has been missing high by wide margins
  for more than 2 years." Lazer's team instead points to **algorithm
  dynamics** — Google's own search product changing under the model (86
  algorithm changes in June-July 2012 alone; the June 2011 "suggested
  additional search terms" feature and February 2012 symptom-to-diagnosis
  feature). Both accounts are from parties in a position to know (Google
  built and instrumented the system; Lazer's team independently analyzed
  the public error series and Google's search-blog change log), and they
  disagree on the deeper cause. Represent both.
- **Whether GFT was "meant to replace" traditional surveillance is itself
  contested by implication.** Ginsberg et al. 2009 (source 1) explicitly
  disclaim that role at launch: "This system is not designed to be a
  replacement for traditional surveillance networks." Yet the 2013 failure
  was newsworthy specifically because GFT's estimates diverged sharply from
  CDC's and were being used and reported as if authoritative (Lazer: "this
  happened despite the fact that GFT was built to predict CDC reports").
  The 2009 paper's own disclaimer sits in tension with how the tool was
  publicly used and covered by 2013 — a gap the writer can use rather than
  needing new sourcing.
- **A striking non-contradiction worth flagging as a finding, not a
  clash:** Ginsberg et al. 2009 predicted the exact failure mode four years
  early — "panic and concern among healthy individuals may cause a surge in
  the ILI-related query fraction and exaggerated estimates of the ongoing
  ILI percentage" — which is essentially what both Google's own team and
  Lazer's team later described happening in 2012-2013. This is not sources
  disagreeing; it is the original authors naming their own model's
  vulnerability before it was exploited by real-world media coverage.
- **Direction of error is not consistent across the two failure episodes**
  and the record should not blur them. In 2009, the original model
  *underestimated* the H1N1 pandemic's initial wave (Cook 2011: Wave 1
  correlation collapsed to 0.290, "the original model underestimated the
  magnitude of ILI activity"). In 2011-2013, the (already-revised) model
  *overestimated* (Lazer 2014, Copeland et al. 2013). These are different
  failures, in opposite directions, roughly three years apart, with
  different proximate causes (seasonal/query-composition mismatch in 2009;
  media-driven query inflation and/or algorithm dynamics in 2011-2013).
- No contradiction found regarding the basic fact pattern: launch year
  (2008/2009 depending on whether the count starts at public launch or the
  Nature paper), the September 24, 2009 model revision, the February 2013
  "more than double" headline figure, or the August 20, 2015 shutdown date.
  All primaries agree on these.

## Numbers

| Figure | Value | Owning primary | Period / denominator |
|---|---|---|---|
| Reporting lag advantage over CDC | "1-2 weeks ahead" of CDC's ILINet reports; "reporting lag of about one day" for GFT itself | Ginsberg 2009, abstract & p.3 | 2007-2008 season, nine U.S. regions |
| Candidate search queries tested | 50 million | Ginsberg 2009, p.2 | 2003-2008 U.S. search logs |
| Models fit during query selection | 450 million | Ginsberg 2009, p.4 (Methods) | one per candidate query x cross-validation folds x regions |
| Queries selected for final model | 45 | Ginsberg 2009, p.2, Fig. 1 | fixed set, used region-independent |
| Model fit correlation (training) | mean r = 0.90 (min 0.80, max 0.96, n=9 regions) | Ginsberg 2009, p.3 | fit on 2003-2007 data, 128 points/region |
| Model validation correlation (out-of-sample) | mean r = 0.97 (min 0.92, max 0.99, n=9 regions) | Ginsberg 2009, p.3 | 42 held-out points/region, 2007-2008 |
| State-level (Utah) validation correlation | r = 0.90, 42 points | Ginsberg 2009, p.3 | 2007-2008 |
| Original-model correlation, pH1N1 Wave 1 (initial pandemic onset) | r = 0.290 | Cook 2011, Table 2 | Mar 29-Aug 2, 2009 |
| Updated-model correlation, pH1N1 Wave 1 | r = 0.945 | Cook 2011, Table 2 | same period |
| Original-model correlation, pH1N1 Wave 2 | r = 0.916 | Cook 2011, Table 2 | Aug 2-Dec 31, 2009 |
| Updated-model correlation, pH1N1 Wave 2 | r = 0.985 | Cook 2011, Table 2 | same period |
| Original-model RMSE increase, pH1N1 overall vs. pre-pH1N1 | threefold (0.006 -> 0.018) | Cook 2011, Table 2 / text | Sept 2003-Mar 2009 vs. Mar-Dec 2009 |
| Original-model average underestimation, pH1N1 period | 0.014 (ILI percentage points), "near three-fold" worse than next-worst season | Cook 2011, Discussion | Mar-Dec 2009 |
| Query count, original vs. updated (2009) model | ~40 -> ~160 | Cook 2011, Results | — |
| "Influenza complication" query-category share, original -> updated model | 48% -> 17% | Cook 2011, Results | — |
| "General/specific influenza symptom" query-category share, original -> updated model | 8% -> 69% | Cook 2011, Results | — |
| Google's own highest single-week national error, 2008-2012 | 1.13 percentage points (CDC 1.74%, GFT 2.86%, week of Jan 1, 2012) | Copeland et al. 2013, p.1 | Aug 2008-2012 seasons |
| Google's own mean absolute error, 2008-2012 | 0.30 percentage points | Copeland et al. 2013, p.1 | same period |
| Google's own peak overestimation, 2012-13 season | 6.04 percentage points; GFT 10.56% vs. CDC 4.52% ("more than twice") | Copeland et al. 2013, p.1 | week of Jan 13, 2013 |
| "More than double" ILI estimate vs. CDC, reported Feb. 2013 | GFT predicted "more than double the proportion of doctor visits for ILI" vs. CDC | Lazer 2014, p.1203 (citing Nature News); independently confirmed in raw numbers by Copeland et al. 2013 | Feb. 2013 headline figure |
| Weeks GFT overestimated | "100 out of 108 weeks" | Lazer 2014, p.1204 and figure caption | 21 Aug 2011-1 Sept 2013 |
| 2011-2012 season overshoot | "more than 50%" over actual level | Lazer 2014, figure caption | 2011-2012 flu season |
| Mean absolute error, out-of-sample comparison | GFT 0.486; Lagged CDC 0.311; combined GFT+CDC 0.232 (all differences p<0.05) | Lazer 2014, figure caption | out-of-sample period, chart range 2009-2013 |
| Google search-algorithm changes cited | "86 changes in June and July 2012 alone" | Lazer 2014, p.1204 | two months, 2012 |
| Shutdown date | August 20, 2015 | Google Research Blog, "The Next Chapter for Flu Trends" | — |
| ARGO vs. GFT (qualitative) | "outperforms all previously available Google-search-based tracking models, including the latest version of Google Flu Trends" | Yang, Santillana, Kou 2015 (abstract) | no exact error-reduction percentage retrieved in this pass |

## Source assets

- **Ginsberg 2009, Figure 1** (p.2): line chart of mean correlation vs.
  number of top-scoring queries included, showing the peak at 45 queries and
  the "steep drop... after adding query 81, which is 'oscar nominations'."
  Strong visual for teaching overfitting concretely — a reader can see the
  cliff. Source: the PDF itself. A crop must keep the x-axis (number of
  queries), the peak annotation, and the caption's mention of "oscar
  nominations"; it should not need the y-axis scale beyond "0.85-0.95" to
  make its point.
- **Ginsberg 2009, Figure 3** (p.4): four snapshots of the same 2007-2008
  season, showing GFT's real-time estimate against CDC's lagged data as the
  season progresses, then confirmed by later CDC data. Good for showing what
  "success" looked like at launch — the case the paper was actually praised
  for — before the article turns to the failure. Crop must keep at least two
  of the four panels (the early-detection one and the final-confirmed one)
  and the "data available as of [date]" labels; the specific ILI percentage
  axis values are secondary to the shape.
- **Lazer et al. 2014, two-panel chart** (p.1204): top panel plots GFT,
  lagged-CDC, GFT+CDC combined, and raw CDC ILI percentage from mid-2009
  through 2013, with a callout "Google estimates more than double CDC
  estimates" pointing at the 2013 spike. Bottom panel plots the same models'
  percentage error over the same period, with a callout "Google starts
  estimating high 100 out of 108 weeks." This is the single most
  load-bearing chart in the whole record — it is the definitive post-mortem
  visualizing its own headline numbers. Source: the published Science PDF
  (page 2 of the fetched document), and (per the paper) full data in
  Science's supplementary materials at
  www.sciencemag.org/content/343/6176/1203/suppl/DC1. A crop must retain
  both callout annotations verbatim and the 2012-2013 spike itself; the
  legend distinguishing the four lines is necessary if more than the
  raw-vs-GFT comparison is shown.
- **Copeland et al. 2013, "Google Flu Trends predictions vs. CDC,
  2004-2013"** (p.1): a single-line-pair chart (red GFT vs. green CDC) over
  the full 2004-2013 run, making the 2012-13 spike visually obvious against
  nine prior, well-tracked seasons — this is Google's own team's chart of
  its own failure, which is a different (and arguably stronger, because
  self-incriminating) source than the outside Lazer chart making the same
  point. Source: the Google-hosted PDF. Crop must keep the full date axis
  (2004-2013) so the 2012-13 spike reads as anomalous against nine prior
  seasons, not an isolated image.
- **Copeland et al. 2013, "Media volume and Prediction Error Rate,
  2004-2013"** (p.2): overlays a news-volume series against GFT's absolute
  prediction error, showing both spiking together only in the 2012-13
  season. This is Google's own evidence for its own "media coverage" causal
  claim — useful specifically in the Contradictions context, paired against
  Lazer's rebuttal. Crop must keep both series and the shared time axis;
  the point is the co-spike, not either series' absolute scale.
- Google's 2015 shutdown post: **None found.** It is a short text post with
  no chart, figure, or image carrying independent evidentiary weight.

## Discarded

- Declan Butler, "When Google got flu wrong," *Nature* 494, 155-156 (13
  February 2013). Opened directly (nature.com/articles/494155a and its
  authentication redirect); the URL resolves but returns only a
  subscription paywall page ("This is a preview of subscription content,
  access via your institution"). Confirmed firsthand: title, subtitle ("US
  outbreak foxes a leading web-based method for tracking seasonal flu"), and
  publication date. Not cited for any substantive claim because its
  specific numbers and quotes could not be verified firsthand, and the same
  "more than double" figure this article is credited with breaking is
  independently available, fully verified, from Lazer 2014 (which cites
  Butler directly) and from Copeland et al. 2013 (Google's own numbers).
- David Lazer and Ryan Kennedy, "What We Can Learn From the Epic Failure of
  Google Flu Trends," *Wired*, October 2015. wired.com blocked this
  session's fetch tool entirely (not a paywall — a fetch restriction with no
  content returned at all); a secondary mirror (asprtracie.hhs.gov)
  returned only a one-line abstract, not the article text. Not used for any
  claim; the same authors' peer-reviewed Science paper (source 3) is read in
  full and is the stronger source for their analysis.
- The Washington Post, "Google flu tracker overestimated cases, study
  argues, pointing to flaws in 'big data'" (17 March 2014). Returned HTTP
  403 on fetch. Not pursued further because Time's March 13, 2014 piece
  (source 7), covering the same Lazer paper release, was successfully
  retrieved in full and serves the same "contemporaneous reporting that held
  up" role the commission asks for.
- MobiHealthNews, "Researchers: Google Flu Trends 'went off the rails years
  ago'" — returned HTTP 403 on fetch. Not pursued; a Lazer quote from the
  same general period ("Dewey beats Truman") was already captured, fully
  verified, via the Time piece.
- LiveScience, "Data Fail! How Google Flu Trends Fell Way Short." Fetch
  returned a truncated/incomplete extraction with no usable body text on
  this pass. Not pursued further given the record already has two
  independent, fully-read secondary accounts of the same Lazer-paper release
  (Time) plus Google's and Lazer's own primary numbers.
- blog.google.org, "Flu Trends updates model to help estimate flu levels in
  the US" (Google's public October 2013 update announcement, distinct from
  the Copeland et al. 2013 internal paper). Every fetch attempt (http and
  https variants) returned a 503 or 404. The commission's "2013 model-update
  post" requirement is satisfied instead by Copeland et al. 2013 (source 4),
  which is the fuller, more substantive account by the same team and was
  successfully read in full.
