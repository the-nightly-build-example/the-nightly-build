# Evidence record: what-could-go-wrong/recommender-radicalization (01)

The evidence strongly supports the commission's angle: the vivid mechanism (engagement
optimization → escalation → sealed bubble) was stated at full strength by named people
with real observations, and the studies built specifically to detect it in working systems
mostly did not find it operating on typical users. Two originating documents are read in
full and quoted verbatim (Pariser's 2011 filter-bubble argument; Tufekci's 2018 "Great
Radicalizer"). Four empirical primaries are read with their designs, samples, windows, and
figures verified against the paper that owns each number: Hosseinmardi et al. (PNAS 2021,
N=309,813 Nielsen panel), Chen/Nyhan/Reifler/Robertson/Wilson (Science Advances 2023,
n=1,181, behavioral + survey), Guess et al. (Science 2023, the reverse-chronological feed
experiment), and Bakshy/Messing/Adamic (Science 2015, 10.1 million users) on filter-bubble
diversity. The record is thin in exactly one place the writer must honor: every null result
is bounded — to population-level effects (Hosseinmardi's own caveat), to a post-2019
recommender (Chen observed 2020, after YouTube's 2019 changes), to short windows, and, for
the Meta studies, to a window confounded by 63 temporary "break glass" changes (the UMass
reanalysis). So the evidence does not license "recommenders are harmless"; it licenses "the
strong rabbit-hole/filter-bubble claim, as a systematic effect on ordinary users, was not
found by the tests designed to find it." That two-sided gap is the piece. The one input I
could not verify against its primary is the exact per-platform enrollment of the Guess feed
experiment (paywalled body); I have the design and null result from the abstract and "about
23,000 consenting users" from Science's news report, flagged below.

## Sources

```text
URL:         https://www.ted.com/talks/eli_pariser_beware_online_filter_bubbles
Kind:        primary — Pariser coined and owns the "filter bubble" argument; the talk (and
             his 2011 book, The Filter Bubble, Penguin Press) is the originating document.
Establishes: The full-strength personalization/filter-bubble claim: invisible algorithmic
             curation narrows each person's information to what they already agree with,
             with no shared public sphere, which he argues harms democracy.
Paraphrase:  Facebook silently dropped his conservative friends' posts because it observed he
             clicked liberal links more; Google uses many personal signals so results differ
             person to person; two friends searching the same term saw different worlds; the
             danger is an unchosen, invisible edit of what you can see.
Locators:    TED2011 talk (~9 min), delivered March 2011; transcript at /transcript.
Quote:       "Facebook was looking at which links I clicked on, and it was noticing that,
             actually, I was clicking more on my liberal friends' links than on my
             conservative friends' links. And without consulting me about it, it had edited
             them out." / "There are 57 signals that Google looks at ... that it uses to
             personally tailor your query results." / "there is no standard Google anymore."
             / "Daniel didn't get anything about the protests in Egypt at all in his first
             page of Google results. Scott's results were full of them." / "Your filter
             bubble is your own personal, unique universe of information that you live in
             online." / "Instead of a balanced information diet, you can end up surrounded by
             information junk food."
Note:        Transcript reached through a secondary reproduction (the ted.com transcript is
             JS-rendered and would not fetch as text); wording matches the talk as widely
             quoted. The ted.com page above resolves and is the source's own home.
```

```text
URL:         https://www.nytimes.com/2018/03/10/opinion/sunday/youtube-politics-radical.html
Kind:        primary — Tufekci's own NYT op-ed; owns the "Great Radicalizer" argument.
Establishes: The YouTube rabbit-hole claim at full strength: a recommender optimizing
             watch-time learns that ever-more-extreme content holds attention, so it "up[s]
             the stakes," and given YouTube's scale is a powerful radicalizing instrument.
Paraphrase:  Watching Trump-rally videos led YouTube to autoplay white-supremacist and
             Holocaust-denial content; a fresh account on Clinton/Sanders videos drifted to
             leftish 9/11-conspiracy content; the pattern held even for nonpolitical topics
             (vegetarianism → veganism, jogging → ultramarathons). She attributes it to
             Google's ad business: longer watch-time means more money, and the algorithm
             "concluded that people are drawn to content that is more extreme."
Locators:    NYT Opinion, Sunday Review, March 10, 2018. Read in full via a faithful PDF
             reproduction; the NYT page above is the home and is gated, not dead.
Quote:       "It seems as if you are never 'hard core' enough for YouTube's recommendation
             algorithm." / "Given its billion or so users, YouTube may be one of the most
             powerful radicalizing instruments of the 21st century." / "YouTube leads viewers
             down a rabbit hole of extremism, while Google racks up the ad sales."
Note:        The essay's own empirical support is thin and self-described as such ("Good data
             is hard to come by"): it rests on her own anecdotal experiments plus three
             repeated third-party claims (see Numbers/Contradictions), not systematic data.
```

```text
URL:         https://www.pnas.org/doi/10.1073/pnas.2101967118
Kind:        primary — Hosseinmardi, Ghasemian, Clauset, Mobius, Rothschild, Watts; owns its
             panel data and findings.
Establishes: At population scale, YouTube news consumption is dominated by mainstream/centrist
             sources; far-right consumption is small and stable; there is no systematic
             algorithm-driven drift toward extreme content for typical users.
Paraphrase:  Using Nielsen's nationally representative desktop panel (N=309,813 with ≥1
             YouTube pageview; 21,385,962 watched-video pageviews; Jan 2016–Dec 2019), they
             traced on- and off-platform browsing and labeled channels into six political
             categories. News is ~11% of YouTube consumption. Far-right watch-time is tiny
             though its viewers are more engaged; anti-woke content grew fastest. Sessions
             show no trend toward more extreme content; far-right videos are most often
             reached from external URLs, not recommendations, and far-right viewing correlates
             with off-YouTube far-right consumption.
Locators:    Abstract; "Methods and Materials" (Nielsen panel, N); Results (session trend,
             Table 2 entry points, Fig. 2B watch-time trends); "important limitations."
Quote:       "We find no evidence that engagement with far-right content is caused by YouTube
             recommendations systematically, nor do we find clear evidence that anti-woke
             channels serve as a gateway to the far right." / "Within sessions of consecutive
             video viewership, we find no trend toward more extreme content ... consumption of
             this content is determined more by user preferences than by recommendation." /
             "our analysis is intended to address systematic effects and hence applies only at
             the population level. It says little about ... the possible radicalization of
             individuals or small groups of individuals."
```

```text
URL:         https://www.science.org/doi/10.1126/sciadv.adk2031
Kind:        primary — Chen, Nyhan, Reifler, Robertson, Wilson; owns its paired behavioral +
             survey data.
Establishes: In 2020, exposure to alternative/extremist YouTube channels was concentrated
             among a small group with high prior gender/racial resentment who reach it via
             subscriptions and external links; recommendations rarely sent non-subscribers
             there; measured "rabbit hole" events were vanishingly rare.
Paraphrase:  1,181 US participants (recruited from a 4,000-person YouGov sample weighted to
             the adult population, with oversamples of high-resentment and heavy-YouTube
             users) installed a browser extension that logged real viewing and the
             recommendations shown, paired with 2018 survey attitudes. Alternative-channel
             videos were 3% of views, extremist-channel 0.5%. Prior hostile sexism and racial
             resentment predicted time on these channels. Subscriptions and off-site links,
             not algorithmic suggestion to the uninterested, drove exposure. By a strict
             four-part definition, rabbit-hole events were 0.01% of all video visits among 3%
             of participants. The authors tie the result partly to YouTube's 2019 recommender
             changes and call their figure a lower bound.
Locators:    Abstract; Fig. 2 (view shares by subscription); "rabbit hole" definition and
             results; Discussion. (Read via arXiv:2204.10921 v2; published Science Advances
             title uses "channels," the preprint used "videos" — same paper.)
Quote:       "exposure to alternative and extremist channel videos on YouTube is heavily
             concentrated among a small group of people with high prior levels of gender and
             racial resentment. These viewers often subscribe to these channels ... In
             contrast, non-subscribers rarely see or follow recommendations to videos from
             these channels." / "YouTube's algorithms were not sending people down 'rabbit
             holes' during our observation window in 2020, possibly due to changes that the
             company made to its recommender system in 2019."
```

```text
URL:         https://www.science.org/doi/10.1126/science.abp9364
Kind:        primary — Guess et al. (US 2020 Facebook & Instagram Election Study); owns the
             randomized feed experiment.
Establishes: Replacing the algorithmic feed with a reverse-chronological one for three months
             changed what users saw and how long they stayed, but did not move political
             attitudes.
Paraphrase:  Consenting Facebook and Instagram users were randomized to a reverse-
             chronological feed vs. the default algorithm for ~3 months around the 2020 US
             election. The chronological feed cut time on platform, raised the amount of
             political and untrustworthy content seen, and on Facebook lowered uncivil/slur
             content and raised content from moderate friends and ideologically mixed sources.
             None of this shifted issue polarization, affective polarization, or political
             knowledge.
Locators:    Abstract / Editor's summary. Study window late Sept–late Dec 2020 (Science's news
             report gives 24 Sept–23 Dec). Exact per-platform enrollment not verified against
             the paper body (paywalled); "about 23,000 consenting users" per Science news.
Quote:       "Despite these substantial changes in users' on-platform experience, the
             chronological feed did not significantly alter levels of issue polarization,
             affective polarization, political knowledge, or other key attitudes during the
             3-month study period."
```

```text
URL:         https://www.science.org/doi/10.1126/science.aaa1160
Kind:        primary — Bakshy, Messing, Adamic; owns the Facebook exposure measurement.
Establishes: On Facebook, the ranking algorithm removed some cross-cutting news, but users'
             own network composition and click choices removed more — the "bubble" is
             substantially demand-side.
Paraphrase:  Using 10.1 million US users who self-report ideology and 7 million shared URLs
             over 7 July 2014–7 January 2015, they decomposed exposure into potential (random),
             network (friends share), ranked feed, and clicks. Ranking made cross-cutting
             content slightly less likely to be seen (risk ratio 5% for conservatives, 8% for
             liberals); individual click choice cut it more (17% conservatives, 6% liberals).
             Over 20% of an average user's ideology-reporting friends were from the opposing
             party.
Locators:    Abstract; Results (ranking risk ratios; click risk ratios); "Our analysis has
             limitations."
Quote:       "Compared with algorithmic ranking, individuals' choices played a stronger role in
             limiting exposure to cross-cutting content." / "our study is limited to active
             users who volunteer an ideological affiliation on this social media platform."
```

```text
URL:         https://www.usatoday.com/story/opinion/2017/08/08/i-invested-early-google-and-facebook-now-they-terrify-me-roger-mcnamee-column/543755001/
Kind:        secondary — Roger McNamee op-ed; an early Facebook investor restating the harm
             argument, not owning an empirical claim.
Establishes: That the attention/advertising-business critique was voiced from inside the
             industry: ad-funded platforms optimize attention, "reinforcing biases and
             reducing the diversity of ideas to which each is exposed."
Paraphrase:  Facebook and Google monetize attention and borrow techniques from gambling to
             hold it; the harm to a shared public sphere grows over time.
Locators:    USA Today Opinion, Aug. 8, 2017 (read via a faithful reproduction in the same
             coursepack PDF as Tufekci). Use for the present-day advocacy strand, not for any
             figure.
Quote:       "Facebook, Google and others compete for each consumer's attention, reinforcing
             biases and reducing the diversity of ideas to which each is exposed."
```

```text
URL:         https://www.cics.umass.edu/news/facebook-algorithm-curbs-election-misinformation
Kind:        secondary — UMass Amherst news release on a reanalysis by Chhandak Bagchi and
             Przemyslaw Grabowicz (Manning College); reports their critique of a Meta study.
Establishes: That the Meta-cooperative 2020 studies ran during a window Meta had temporarily
             altered, which the critics argue confounds the null/"algorithm suppresses
             misinformation" reading.
Paraphrase:  The Guess-team feed studies ran 24 Sept–23 Dec 2020, overlapping ~63 temporary
             "break glass" changes Meta introduced around November 2020 to suppress
             untrustworthy election content, so results from that window may not describe the
             standard algorithm.
Locators:    News release; lead author Bagchi, senior author Grabowicz (underlying paper in
             PNAS, 2024, not read in full here).
Quote:       "Beginning around the start of November 2020, Meta introduced 63 'break glass'
             changes to Facebook's news feed, which were expressly designed to diminish the
             visibility of untrustworthy news surrounding the 2020 U.S. presidential election."
Note:        A repetition of the critics' claim; establishes that the confound argument was
             made, not that it fully overturns the feed-experiment result.
```

```text
URL:         https://www.science.org/content/article/does-social-media-polarize-voters-unprecedented-experiments-facebook-users-reveal
Kind:        secondary — Science news report on the 2020 Election Study papers.
Establishes: Enrollment scale and window for the feed experiments, in plain terms.
Paraphrase:  "Each study looked at a separate group of about 23,000 users, recruited via
             invitations placed on the top of their feeds, and took place between late
             September and late December 2020."
Locators:    News article, July 2023. Used only for the enrollment/window figures the
             paywalled primary body would confirm.
Quote:       (as paraphrased above)
```

## Contradictions

- **Tufekci's own cited support cuts against the strong claim once checked.** Her three
  external supports are single-source repetitions, not independent confirmations: (a)
  Guillaume Chaslot's finding, via his own tracking tool, that a walk from either a pro-Clinton
  or pro-Trump seed was "many times more likely" to end on a pro-Trump video; (b) the Wall
  Street Journal investigation done "with the help of Mr. Chaslot" (same origin as (a), so it
  counts as one); (c) Jonathan Albright's "crisis actor" seed reaching a network of ~9,000
  conspiracy videos. These are algorithm-audit / random-walk methods (simulated fresh accounts
  with no viewing history), which the later panel studies (Hosseinmardi, Chen) argue overstate
  what real users with real histories experience. The strongest full-strength claim and the
  strongest disconfirming evidence therefore rest on different methods, and that methods gap is
  the article's hinge.

- **The empirical nulls do not reach Tufekci's 2016-era system.** Chen explicitly attributes
  the absence of rabbit holes partly to YouTube's 2019 recommender changes; Hosseinmardi's
  window (2016–2019) and Chen's (2020) mostly post-date the behavior Tufekci described in
  2016–2018. The dismissive reading ("it never happened") outruns the evidence: no panel study
  measured the pre-2019 recommender at scale.

- **Bakshy's "it's demand, not the algorithm" framing was itself contested.** The study covers
  only users who volunteer an ideological affiliation (a minority of users, younger/more
  educated/more female than the US population), and critics argued the design and framing
  understated the ranking algorithm's role by comparing it against user choice rather than
  against a neutral baseline. Report the risk ratios; do not let the headline carry more than
  the sample supports.

- **The Meta feed experiment ran in a manipulated window.** The UMass reanalysis (Bagchi,
  Grabowicz) argues the ~63 "break glass" changes during 24 Sept–23 Dec 2020 confound any claim
  that the *standard* algorithm suppresses untrustworthy content. This bounds the Guess null and
  is the clearest case where "platform cooperation + short window" limits what the studies show.

- **Hosseinmardi and Chen both concede the individual case.** Population-level nulls "say little
  about ... the possible radicalization of individuals or small groups" (Hosseinmardi), and
  Chen calls its rabbit-hole rate a "lower bound." The affected, resentful, subscribed minority
  is real in both datasets; the finding is that the algorithm does not manufacture that minority
  from typical users, not that harm to them is zero.

## Numbers

```text
Figure: N = 309,813 panelists (Nielsen desktop panel with ≥1 YouTube pageview); 21,385,962 watched-video pageviews
Owner:  Hosseinmardi et al. 2021 (PNAS)
Scope:  US nationally representative desktop panel, Jan 2016–Dec 2019; desktop only
```
```text
Figure: News = ~11% of overall YouTube consumption; ~23 million Americans use YouTube for news
Owner:  Hosseinmardi et al. 2021
Scope:  Panel population, 2016–2019
```
```text
Figure: Far-right watch time 0.17% (2016) → 0.30% (2019); anti-woke 0.31% → 1.02%
Owner:  Hosseinmardi et al. 2021 (Fig. 2B; t=−3.17, P<0.005 and t=−14.08)
Scope:  Share of total consumption, population average
```
```text
Figure: Far-right video entry points — external URLs 41.29%, another YouTube video 35.8%, homepage 7.85%, user/channel 6.85%, search 6.36%
Owner:  Hosseinmardi et al. 2021 (Table 2, "fR" row)
Scope:  Referrer immediately preceding a far-right video view
```
```text
Figure: n = 1,181 participants (from 4,000 YouGov recruits, weighted to US adults; oversamples of high resentment and heavy YouTube use)
Owner:  Chen et al. 2023 (Science Advances)
Scope:  US, 2020; browser-extension behavioral data + 2018 CCES attitudes
```
```text
Figure: Alternative-channel videos = 3% of views; extremist-channel = 0.5%; mainstream media = 3.6%; other = 93%
Owner:  Chen et al. 2023 (Fig. 2)
Scope:  All video views by study participants, 2020
```
```text
Figure: 60.8% of alternative-channel video views come from subscribers to that channel; 54.7% for extremist-channel videos
Owner:  Chen et al. 2023
Scope:  Views of that channel type, weighted
```
```text
Figure: "Rabbit hole" events (all four strict criteria) = 0.01% of all video visits, among 3.0% of participants
Owner:  Chen et al. 2023 (described as a lower bound)
Scope:  All video visits, 2020
```
```text
Figure: Feed experiment ≈ 23,000 consenting users per study; window 24 Sept–23 Dec 2020 (~3 months)
Owner:  Guess et al. 2023 (Science) — enrollment figure via Science news report; per-platform N unverified against primary body
Scope:  Consenting Facebook and Instagram users, US 2020 election period
```
```text
Figure: Ranking cut cross-cutting exposure — risk ratio 5% (conservatives), 8% (liberals); click choice cut it more — 17% (conservatives), 6% (liberals)
Owner:  Bakshy, Messing, Adamic 2015 (Science)
Scope:  10.1M ideology-reporting US Facebook users; 7M URLs; 7 Jul 2014–7 Jan 2015
```
```text
Figure: >20% of an average user's ideology-reporting friends are from the opposing party
Owner:  Bakshy et al. 2015
Scope:  Same sample; median cross-cutting friendship share 0.20 (liberals), 0.18 (conservatives)
```
```text
Figure: 63 temporary "break glass" news-feed changes during the 2020 study window
Owner:  Bagchi & Grabowicz (via UMass Amherst news release) — a repetition of the critics' claim
Scope:  Facebook, ~Nov 2020 onward, overlapping the Guess feed experiment
```
Repeated third-party figures inside Tufekci (attribute to their origin, not to her, and note
they are single-source): Chaslot's "many times more likely to end on a pro-Trump video";
Albright's "crisis actor" seed → ~9,000 conspiracy videos. These support that the claim was
made, not that it holds up.

## Source assets

```text
Asset: Hosseinmardi et al. 2021, Fig. 2 (archetypes of news consumption / watch-time by category over 2016–2019)
Shows: How small and flat far-right consumption is beside mainstream, and the faster rise of anti-woke content — the whole "no systematic drift" case in one chart.
Crop:  Keep the category legend and the time axis; a crop that drops the mainstream baseline would exaggerate the extreme-content share.
```
```text
Asset: Chen et al. 2023, Fig. 2 (view shares by channel type and subscription status)
Shows: That most alternative/extremist views come from subscribers, and how tiny (0.5%/3%) these shares are against "other" (93%).
Crop:  Retain the subscription-status breakdown and the total-share labels under each bar; omit neither, or the subscription-driven finding disappears.
```
```text
Asset: Bakshy et al. 2015, Fig. 3 (potential → network → exposed → selected funnel of cross-cutting content)
Shows: Where cross-cutting content is lost — more at the network/choice stages than at ranking.
Crop:  Keep all four stages side by side; showing only the ranking step would misstate the paper's point.
```
Tufekci (op-ed) and Pariser (talk) carry no data figures of their own — the argument is prose
and anecdote; no chartable asset. Guess et al.: figures are behind the paywall; a chart, if
wanted, should be rebuilt from the reported effect on time-on-platform and the null attitude
effects rather than reproduced.

## Library links (surface for Background, do not re-teach)

Best existing lessons the writer should link rather than re-explain, in priority order:

- **when-ai-breaks/facebook-myanmar** — teaches exactly what an engagement-ranked feed rewards
  (it "promotes whatever people react to, and people react to alarm") and gives the strongest
  real-world harm case. Link this for the *mechanism* and the affected-minority reality; do not
  re-derive engagement ranking.
- **what-could-go-wrong/gradual-disempowerment** — already frames recommender systems as AI
  doing "culture's job" and already quotes the same chronological-feed election-study null.
  Link it, and keep this lesson distinct by staying on the radicalization/filter-bubble *test*
  rather than the broader loss-of-control thesis.
- **what-could-go-wrong/ai-persuasion** — the personalized-persuasion-at-scale argument; the
  natural neighbor for the "sealed, self-confirming feed" strand. Link, don't re-teach
  manipulation-at-scale.
- **when-ai-breaks/optum-health-algorithm** — teaches the "proxy label" idea (engagement stands
  in for what a viewer actually values). Useful one-line link if the piece needs "optimizing a
  proxy" without a detour.
- **what-could-go-wrong/algorithmic-monoculture** — adjacent (shared-model correlated error);
  name only to keep this lesson distinct, not as core background.

Reminder from the commission: the library is a source of what has been taught, not of this
article's own claims.

## Discarded

```text
https://www.pnas.org/doi/abs/10.1073/pnas.2213020120 — Auditing YouTube's recommender (2023, congenial/extreme recs). Relevant but a fresh-account audit, not read in full; floor already met and it would duplicate the audit-vs-panel point Chen makes.
https://www.nature.com/ (Nyhan et al. 2023, "Like-minded sources on Facebook are prevalent but not polarizing") — strong further primary for the diversity strand; not read in full because Bakshy already anchors demand-side sorting and the source floor is met. Flag if the editor wants a second diversity primary.
https://www.pnas.org/doi/10.1073/pnas.2321584121 — Facebook/Instagram deactivation experiment (2024). Named in the commission; not read in full. The feed experiment and the resentment/subscription findings carry the empirical case; add if the writer wants the deactivation result specifically.
https://reason.com/2024/03/13/... — opinion coverage of Chen et al.; commentary, not a primary; excluded per source policy.
https://en.wikipedia.org/wiki/Zeynep_Tufekci — reference only; not cited.
```
