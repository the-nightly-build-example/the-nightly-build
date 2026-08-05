# evidence: when-ai-breaks/ai-overviews (01)

This record supports the incident's spine from the operator's own account and
primary artifacts: AI Overviews launched to everyone in the US at Google I/O on
May 14, 2024; within about two weeks two failures went viral; Elizabeth Reid,
VP, Search published the postmortem "AI Overviews: About last week" on May 30,
2024. Two example failures are confirmed real by Google itself and by reporting
that held up: the glue-on-pizza answer (a real 11-year-old Reddit joke restated
as cooking advice) and the eat-a-rock answer ("How many rocks should I eat?",
traced to an Onion satire that had been republished on a geological software
company's site). The record is strong on both, and strong on the boundary the
commission demands: Google states on the record that a large batch of the
circulating screenshots — leaving dogs in cars, smoking while pregnant,
depression — were faked and "never appeared." Those are recorded in Discarded
and must not be used.

Two limitations. First, the original Reddit glue comment could not be resolved
to its own live page: Reddit blocks the fetch crawler and no article carried a
direct thread URL, so the comment's existence and exact wording rest on three
independent secondaries (AP, Daily Dot, NBC) plus Google's own acknowledgment,
not on the source's own page. Second, Google's own framing partly cuts against
the commission's clean "faithful retrieval, no trust model" thesis — Reid
attributes some errors to "misinterpret[ing] language on webpages," and Pichai
calls the underlying failure "hallucination." That tension is recorded in
Contradictions; the glue case survives it, the writer should engage it.

## Sources

```text
URL:         https://blog.google/products-and-platforms/products/search/ai-overviews-update-may-2024/
Kind:        primary — Google's own postmortem, authored by the executive who
             owns the product. (The path /products/search/ai-overviews-update-may-2024/
             301-redirects to this canonical /products-and-platforms/ URL; record
             the canonical one.)
Establishes: The operator's account of what failed and why, the acknowledged-real
             examples, the faked examples, the fixes, and the violation rate.
Paraphrase:  Reid, VP, Search, dated May 30, 2024, writes that "some odd,
             inaccurate or unhelpful AI Overviews certainly did show up." She
             acknowledges the pizza answer ("using glue to get cheese to stick
             to pizza") and the rocks answer. She explains the rocks result as a
             "data void": before the screenshots went viral "practically no one
             asked Google that question," and the only matching content was
             satire that "happened to be republished on a geological software
             provider's website." She states a large number of faked screenshots
             circulated (dangerous results for topics like leaving dogs in cars,
             smoking while pregnant, and depression) and that "Those AI Overviews
             never appeared." She lists more than a dozen technical fixes: better
             detection of nonsensical queries, limits on satire/humor and on
             user-generated content, and added protections for health.
Locators:    Author byline and dateline at top; "About last week" opening;
             "How many rocks should I eat?" / "data void" section; faked-
             screenshots section; "more than a dozen technical improvements"
             list near the end.
Quote:       "How many rocks should I eat? Prior to these screenshots going
             viral, practically no one asked Google that question ... there is
             satirical content on this topic ... that also happened to be
             republished on a geological software provider's website."
             "Those AI Overviews never appeared. So we'd encourage anyone
             encountering these screenshots to do a search themselves to check."
             "We found a content policy violation on less than one in every 7
             million unique queries on which AI Overviews appeared."
```

```text
URL:         https://blog.google/products-and-platforms/products/search/generative-ai-google-search-may-2024/
Kind:        primary — Google's own launch announcement, authored by Reid.
Establishes: The launch date, the rollout scope, and the reach figures.
Paraphrase:  Reid, VP, Search, dated May 14, 2024 (Google I/O), announces that
             "AI Overviews will begin rolling out to everyone in the U.S., with
             more countries coming soon," reaching hundreds of millions that week
             and a target of over a billion people by year end. Frames AI
             Overviews as the generally-available successor to the Search
             Generative Experience, an AI summary above the classic results.
Locators:    Dateline; "AI Overviews will begin rolling out to everyone in the
             U.S." paragraph; reach-figures sentence in the same section.
Quote:       "So today, AI Overviews will begin rolling out to everyone in the
             U.S., with more countries coming soon."
             "That means that this week, hundreds of millions of users will have
             access to AI Overviews, and we expect to bring them to over a
             billion people by the end of the year."
```

```text
URL:         https://theonion.com/geologists-recommend-eating-at-least-one-small-rock-per-1846655112/
Kind:        primary — the original satirical artifact the AI restated.
Establishes: The exact source content behind the eat-rocks answer, and that it
             is unmistakably satire published by a satirical outlet.
Paraphrase:  The Onion piece "Geologists Recommend Eating At Least One Small
             Rock Per Day," dated April 13, 2021, attributes the recommendation
             to a fictional Dr. Joseph Granger of UC Berkeley and advises
             "hiding loose rocks inside different foods, like peanut butter or
             ice cream." The satirical register is explicit throughout.
Locators:    Headline; dateline April 13, 2021; body quotes attributed to the
             fictional geologist.
Quote:       "Geologists Recommend Eating At Least One Small Rock Per Day"
             "we recommend hiding loose rocks inside different foods, like
             peanut butter or ice cream."
```

```text
URL:         https://www.theverge.com/24158374/google-ceo-sundar-pichai-ai-search-gemini-future-of-the-internet-web-openai-decoder-interview
Kind:        primary — Sundar Pichai's on-record statement in a published
             interview. The transcript owns his words firsthand; authorship and
             stake, not the host domain, make it primary. Page is live (HTTP 200
             verified via HEAD request) but gated to the fetch proxy, so the
             exact wording below is corroborated through secondary coverage
             (the-decoder.com) rather than read on the page itself.
Establishes: That Google's CEO, at the moment of the rollout, called AI
             hallucination unsolved and in some ways inherent — Google's own
             framing of the failure as a model property, not only a retrieval
             error.
Paraphrase:  In the Decoder interview with Nilay Patel (The Verge, May 2024),
             Pichai says hallucination "is still an unsolved problem" and "in
             some ways ... an inherent feature" of the models, and does not
             commit to a timeline to solve it while the feature keeps shipping
             to millions.
Locators:    Decoder interview transcript; exchange on hallucinations and a
             "roadmap" to solving them.
Quote:       (corroborated via secondary) "hallucination is still an unsolved
             problem. In some ways, it's an inherent feature."
```

```text
URL:         https://www.pbs.org/newshour/politics/google-makes-fixes-to-ai-generated-search-summaries-after-outlandish-answers-went-viral
Kind:        secondary — Associated Press wire report (Matt O'Brien), carried by
             PBS NewsHour. Reports on Google's account from outside Google.
Establishes: Independent confirmation of the timeline, the two example failures,
             and the fixes; a direct quote from Reid's post.
Paraphrase:  AP, May 31, 2024, reports the glue answer traced to a satirical
             Reddit comment and the eat-rocks answer to a nonsensical query, and
             that Reid announced "more than a dozen technical improvements."
             Quotes Reid on why the system errs.
Locators:    Byline Matt O'Brien; dateline May 31, 2024; paragraphs on the two
             examples and on Reid's fixes.
Quote:       "When AI Overviews get it wrong, it's usually for other reasons:
             misinterpreting queries, misinterpreting a nuance of language on the
             web, or not having a lot of great information available."
```

```text
URL:         https://dailydot.com/google-search-results-reddit-pizza-glue-cheese
Kind:        secondary — original reporting (Marlon Ettinger, The Daily Dot)
             that traced the glue answer to its Reddit origin. (Requested
             /news/... path 301-redirects to this canonical URL.)
Establishes: The provenance and exact wording of the glue answer and its Reddit
             source; the author and age of the comment.
Paraphrase:  May 23, 2024. The AI Overview for "cheese not sticking to pizza"
             restated an 11-year-old comment by Reddit user u/fucksmith
             recommending glue in the sauce. Reports the exact glue wording.
Locators:    Byline Marlon Ettinger; dateline May 23, 2024; passage quoting the
             Reddit comment.
Quote:       "⅛ cup of non-toxic glue to the sauce to give it more tackiness"
             "I like Elmer's school glue, but any glue will work as long as it's
             non-toxic."
```

```text
URL:         https://www.nbcnews.com/tech/tech-news/google-ai-im-feeling-depressed-cheese-not-sticking-to-pizza-error-rcna153301
Kind:        secondary — NBC News (Kat Tenbarge). Notable because it draws the
             real-versus-faked line the commission needs.
Establishes: Independent confirmation of the glue example, and contemporaneous
             warning that some circulating screenshots (a depression-related
             one) were "seemingly fake."
Paraphrase:  May 24, 2024. Confirms the "cheese not sticking to pizza" answer
             pulled an 11-year-old Reddit joke about mixing Elmer's Glue into the
             sauce, and flags that some posted examples "seem to be fake,"
             singling out a depression-related screenshot.
Locators:    Byline Kat Tenbarge; dateline May 24, 2024; glue paragraph; "seem
             to be fake" passage.
Quote:       "a Google search query for 'cheese not sticking to pizza' pulled an
             11-year-old Reddit comment that jokingly suggested mixing Elmer's
             Glue into the sauce."
             "Some of the answers that have been posted online seem to be fake."
```

```text
URL:         https://www.cbsnews.com/news/google-ai-overview/
Kind:        secondary — CBS News (Megan Cerullo). Reports Google's statement and
             the acknowledged examples.
Establishes: Independent confirmation of Reid's on-record language and the
             glue/rocks examples.
Paraphrase:  Updated May 31, 2024. Quotes Reid that "some odd, inaccurate or
             unhelpful AI Overviews certainly did show up" and that in a small
             number of cases the system "misinterpret[ed] language on webpages."
             Lists glue-on-pizza and eating rocks among the examples.
Locators:    Byline Megan Cerullo; update timestamp May 31, 2024; Reid quotes;
             examples list.
Quote:       "some odd, inaccurate or unhelpful AI Overviews certainly did show
             up."
```

## Contradictions

- **Google's own cause versus the commission's thesis.** The commission frames
  AI Overviews as the clean case of retrieval-augmented generation faithfully
  restating a real bad source because it has no model of source trust. Google's
  own account is not that tidy. Reid attributes a share of the errors to the
  system "misinterpret[ing] language on webpages" (CBS; Reid postmortem), and
  Pichai calls the underlying failure "hallucination ... an inherent feature"
  (Pichai interview). Both framings pull toward "the model got the content
  wrong," not "the model got the content right and the source was bad." The glue
  case resists that pull: the AI restated the Reddit joke accurately (the ⅛-cup
  glue tip is exactly what u/fucksmith wrote), so this is faithful retrieval of a
  real bad source, not misinterpretation. The rocks case is a hybrid: retrieval
  surfaced a real satirical source because it was nearly the only source (a data
  void), which is the commission's own sub-claim. The writer should present
  Google's "misinterpretation/hallucination" framing and show where the glue
  example defeats it, rather than assert the retrieval thesis unopposed.

- **"Faithfully retrieved The Onion" is a simplification for the rocks case.**
  Per Reid's postmortem, the AI did not necessarily pull theonion.com directly;
  the satire "happened to be republished on a geological software provider's
  website" (independent corroboration: the republisher is ResFrac, a reservoir-
  simulation software firm, at resfrac.com). The mechanism the primary describes
  is "data void surfaces the only match," and the match was a republished copy.
  The glue example, not the rocks example, is the pure "real source restated
  faithfully" demonstration.

- **Scale is contested by framing.** Google stresses a content-policy violation
  rate of "less than one in every 7 million unique queries" (Reid postmortem) to
  argue the failures were rare. Critics stress the surface handles billions of
  queries a day, so even a rare rate is many bad answers. Both numbers are real;
  the disagreement is over which denominator matters. Report both.

## Numbers

```text
Figure: May 14, 2024 — AI Overviews begins rolling out to everyone in the US
Owner:  Reid, "Generative AI in Search" (blog.google, May 14, 2024)
Scope:  US launch at Google I/O; "more countries coming soon"

Figure: hundreds of millions (US access that week); over 1 billion (target by
        end of 2024)
Owner:  Reid, "Generative AI in Search" (blog.google, May 14, 2024)
Scope:  US users that week; global target by end of year

Figure: May 30, 2024 — date of the postmortem "AI Overviews: About last week"
Owner:  Reid, "AI Overviews: About last week" (blog.google, May 30, 2024)
Scope:  publication date of Google's response

Figure: less than 1 in 7,000,000 unique queries with a content-policy violation
Owner:  Reid, "AI Overviews: About last week" (blog.google, May 30, 2024)
Scope:  unique queries on which AI Overviews appeared; Google's own measurement,
        period unspecified beyond the launch window

Figure: more than a dozen technical improvements made afterward
Owner:  Reid, "AI Overviews: About last week" (blog.google, May 30, 2024)
Scope:  fixes to nonsensical-query detection, satire/UGC limits, health topics

Figure: ⅛ cup of non-toxic glue (the answer's exact quantity)
Owner:  u/fucksmith Reddit comment, ~11 years old (~2013); reported by Daily Dot,
        NBC, AP — see limitation note under Discarded
Scope:  the wording restated in the AI Overview for "cheese not sticking to pizza"

Figure: The Onion satire dated April 13, 2021
Owner:  The Onion, "Geologists Recommend Eating At Least One Small Rock Per Day"
Scope:  publication date of the source behind the eat-rocks answer
```

## Source assets

```text
Asset: The Onion headline block, "Geologists Recommend Eating At Least One Small
       Rock Per Day," on theonion.com (masthead visible).
Shows: The source the AI restated is unmistakably satire — the outlet's own
       branding sits above the "recommendation."
Crop:  Must retain the Onion masthead/branding together with the headline; that
       pairing is the whole point. Do not crop to the headline alone, which
       would strip the satire signal.

Asset: Reid's "How many rocks should I eat?" / "data void" passage in the May 30
       postmortem (text passage).
Shows: Google's own explanation of the rocks failure as a data void filled by
       republished satire — the operator naming the mechanism.
Crop:  Keep the "data void" sentence with the "republished on a geological
       software provider's website" clause; the two together carry the mechanism.

Asset: The "less than one in every 7 million unique queries" sentence in the
       postmortem (text passage).
Shows: Google's rarity framing, verbatim, for honest juxtaposition against the
       billions-of-queries-a-day scale.
Crop:  Quote the full sentence; a fragment invites misreading of the denominator.

Asset (glue answer screenshot): None found that can be sourced to its own
       resolvable primary page. The widely shared glue screenshot circulates as
       reposted images; the underlying Reddit thread would not resolve. Use the
       reported wording with secondary attribution rather than an unsourced image.
```

## Discarded

```text
URL/example: "Leaving dogs in cars is safe / good" AI Overview — Google states in
             the postmortem these were faked and "never appeared." Do not use.
URL/example: "Smoking while pregnant" benefit AI Overview — Google states faked;
             "never appeared." Do not use.
URL/example: Depression / "jump off the Golden Gate Bridge" AI Overview (and the
             related Lil Nas X depression screenshot) — Google states this class
             was faked and "never appeared"; NBC independently called the
             depression screenshot "seemingly fake." Do not use.
URL/example: https://x.com/TheOnion/status/1498663107899662338 — the Onion's own
             tweet of the rocks headline. Redundant with the article itself and
             adds no evidence beyond it; the article is the better primary.
URL/example: https://ifunny.co/picture/...44rPcmSTB — a reposted screenshot image
             of the glue answer. Not a resolvable primary; provenance unverifiable
             as an image host. Use reported wording instead.
URL/example: https://www.resfrac.com/blog/geologists-recommend-eating-least-one-small-rock-day
             — the geological-software republisher Reid alludes to. Useful only as
             corroboration that a republished copy existed; not needed as a cited
             source and not the artifact the AI's satire originated from.
URL/example: Forbes (Robert Hart; Jack Kelly; Siladitya Ray) items — solid but
             redundant secondaries; AP, CBS, NBC, Daily Dot already cover the same
             ground with equal or better standing. Held in reserve, not cited.
URL/example: Original Reddit thread for the glue comment — could not be resolved
             to its own live page (Reddit blocks the fetch crawler; no article
             provided a direct thread URL). NOT counted as a primary. The comment's
             existence, authorship (u/fucksmith), age (~11 years), and exact
             wording rest on three independent secondaries (AP, Daily Dot, NBC)
             plus Google's own acknowledgment of the glue example.
```

## Source floor

Met. Total sources cited: 8. Primary: 4 (Reid postmortem; Reid launch
announcement; The Onion article; Pichai on-record interview). Secondary: 4
(AP via PBS; Daily Dot; NBC News; CBS News). Every cited URL was checked and
returns HTTP 200; the two blog.google URLs and the Daily Dot URL resolve to the
canonical addresses recorded above after a 301. The Verge (Pichai) page is live
but gated to the fetch proxy; its quote is corroborated through secondary
coverage and flagged as such.

## Confirmed real versus discarded, in one place

- **Confirmed real (usable):** glue on pizza (Google acknowledged; traced to a
  real Reddit joke by AP, Daily Dot, NBC) and eat a rock / "How many rocks
  should I eat?" (Google acknowledged in the postmortem; traced to Onion satire
  republished on a software firm's site). "Barack Obama is a Muslim president"
  is also confirmed real — Google acknowledged it as a content-policy violation
  — but it is a webpage-misinterpretation error, a different mechanism, and is
  outside the commission's two-example spine; use only if the writer wants a
  third and frames the mechanism honestly.
- **Discarded as faked (must not be used):** leaving dogs in cars, smoking while
  pregnant, and the depression / Golden Gate Bridge screenshots — Google states
  these "never appeared," and NBC independently flagged the depression one as
  fake.
