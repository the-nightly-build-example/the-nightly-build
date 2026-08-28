# Evidence record: when-ai-breaks/cnet-ai-articles (01)

The evidence supports a full, sourced account of the incident. CNET's own
editor's note (Connie Guglielmo, January 25, 2023) is the operator's record: it
confirms 77 stories drafted by an "internally designed AI engine – not ChatGPT,"
about 1% of the site's content for the period, published from November 2022
under the CNET Money team, and a pause after a public audit. The correction note
on CNET's own "What Is Compound Interest?" article is a second operator primary
and confirms the AI "mischaracterized some aspects of CDs, savings accounts and
loan payments." The specific documented errors (compound interest, an auto loan,
CD compounding, APR/APY) are established firsthand by Futurism's reporting, which
quotes the AI's original wording; the flagship one is verified against arithmetic
and against the corrected article.

The record is thin, and the writer must handle this, in two places. First, the
widely repeated "41 of 77 corrections" figure is not from CNET's editor's note.
Guglielmo gives no count; she says only "a small number requiring substantial
correction and several stories with minor issues." The 41 is a tally of
correction notes on the live articles, made by The Verge and Engadget. Several
secondary summaries wrongly credit it to Guglielmo. Second, both technical
primaries describe how large language models fail in general. CNET's engine was
internally built and its architecture is not public, so the mechanism explains
the class of failure, not a confirmed internal description of CNET's specific
tool. The stronger mechanism primary (Kalai et al.) is a 2025 paper and postdates
the 2023 incident, so it cannot be presented as contemporaneous analysis of CNET.

One brief question is left open. The record here establishes that Bankrate is a
Red Ventures sister site whose text the CNET AI plagiarized, and that Red Ventures
owns CNET, Bankrate, ZDNet, The Points Guy, and Healthline. It does not establish
whether Bankrate or those other sites published their own AI-drafted articles.
Later reporting alleged the practice extended beyond CNET, but that was not read
and verified here. The writer should treat the AI program as documented at CNET
and not assert it ran on the sister sites without a source that owns that claim.

## Sources

```text
URL:         https://www.cnet.com/tech/cnet-is-testing-an-ai-engine-heres-what-weve-learned-mistakes-and-all/
Kind:        primary. CNET's own editor's note; the operator accounting for its own program. Authored by CNET's editor-in-chief, maximum stake.
Establishes: The program's scope, tool, disclosure change, and pause, in CNET's words.
Paraphrase:  In November, the CNET Money team launched a test using an internally designed AI engine, not ChatGPT, to draft basic financial explainers. It published 77 short stories with the tool, about 1% of the site's content for the period. Editors generated outlines, then expanded and edited the AI drafts. After one AI-assisted story was cited for factual errors, the team did a full audit and found more stories needing correction, a small number substantial and several with minor issues (incomplete company names, transposed numbers, vague language). CNET paused the tool. It changed the byline from "CNET Money Staff" to "CNET Money," moved the disclosure out of the byline hover so it is visible, and added a human editor co-byline. In a handful of stories the plagiarism checker was misused or failed to catch closely resembling language.
Locators:    Byline "Connie Guglielmo, Editor in Chief" (page now labels her "Former Editor in Chief"); dateline January 25, 2023, 4:23 pm ET; sections "AI engines, like humans, make mistakes," "Bylines and disclosures should be as visible as possible," "New citations will help us."
Quote:       "We started small and published 77 short stories using the tool, about 1% of the total content published on our site during the same period." / "We identified additional stories that required correction, with a small number requiring substantial correction and several stories with minor issues such as incomplete company names, transposed numbers or language that our senior editors viewed as vague." / "We've paused and will restart using the AI tool when we feel confident the tool and our editorial processes will prevent both human and AI errors." / "In a handful of stories, our plagiarism checker tool either wasn't properly used by the editor or it failed to catch sentences or partial sentences that closely resembled the original language."
```

```text
URL:         https://www.cnet.com/personal-finance/banking/what-is-compound-interest/
Kind:        primary. The corrected article itself; the operator's published record of one flagged error and its fix.
Establishes: That CNET's AI engine produced the compound-interest explainer, that it mischaracterized several personal-finance mechanics, and that a human rewrote it.
Paraphrase:  The live article carries an appended correction stating an earlier version was assisted by an AI engine and mischaracterized aspects of CDs, savings accounts and loan payments, that those points were corrected, and that the version was substantially updated by a staff writer. The article is now bylined by a named human writer (Liliana Hall, listed as a former CNET Money associate writer), not "CNET Money."
Locators:    Correction line at the foot of the article body, above the author bio block.
Quote:       "Correction: An earlier version of this article was assisted by an AI engine and it mischaracterized some aspects of CDs, savings accounts and loan payments. Those points were all corrected. This version has been substantially updated by a staff writer."
```

```text
URL:         https://futurism.com/cnet-ai-errors
Kind:        secondary. Reporting from outside CNET, by the outlet that documented the specific errors. It quotes CNET's AI text; the wording it reproduces is firsthand, the framing is secondary.
Establishes: The concrete factual and math errors in the AI drafts, with the AI's original wording.
Paraphrase:  On a $10,000 deposit at 3% annual interest, CNET's AI wrote that "you'll earn $10,300 at the end of the first year." That is wrong: the saver earns $300 in interest; $10,300 is principal plus interest combined. On a $25,000 car loan at 4%, the AI wrote the borrower would "pay a flat $1,000 in interest per year," when interest falls each period as the balance is paid down. The AI wrote that a one-year CD "only compounds once, after the initial deposit reaches maturity," when CDs typically compound daily or monthly. A further error confused APR with APY. CNET added a review disclaimer to the compound-interest story.
Locators:    Author Jon Christian, Futurism, updated January 29, 2023; error list in body; the compound-interest example is the lead error.
Quote:       AI original, as quoted: "you'll earn $10,300 at the end of the first year" (on a $10,000 deposit at 3%). AI original, as quoted: "you'll pay a flat $1,000 in interest per year" (on a $25,000 loan at 4%).
```

```text
URL:         https://futurism.com/the-byte/cnet-publishing-articles-by-ai
Kind:        secondary. The story that broke the program's existence.
Establishes: That CNET had quietly been publishing AI-generated finance articles, the byline used, and the exact disclosure language, before CNET's own editor's note.
Paraphrase:  CNET had quietly published roughly 73 AI-generated financial explainers under the byline "CNET Money Staff," starting around November 2022, with only a hover-over disclosure. The count of 73 predates CNET's later figure of 77.
Locators:    Author Frank Landymore, Futurism, updated January 15, 2023 (original break dated mid-January 2023).
Quote:       Disclosure text as reproduced: "This article was generated using automation technology, and thoroughly edited and fact-checked by an editor on our editorial staff."
```

```text
URL:         https://futurism.com/cnet-ai-plagiarism
Kind:        secondary. Reporting from outside CNET documenting the plagiarism pattern.
Establishes: That the AI's phrasing closely tracked prior published articles without credit, including a Red Ventures sister site.
Paraphrase:  Futurism found that the AI's sentences mapped closely onto text previously published by Bankrate (a Red Ventures sister site), Forbes Advisor, Investopedia, The Balance, and Forbes, with small edits that obscured the source. It gives a paired example: CNET AI's "Overdraft and NSF fees don't have to be a common consequence" against Forbes Advisor's "Overdraft and NSF fees need not be the norm."
Locators:    Author Jon Christian, Futurism, updated January 23, 2023; paired-phrase examples in body.
Quote:       "Overdraft and NSF fees don't have to be a common consequence" (CNET AI) versus "Overdraft and NSF fees need not be the norm" (Forbes Advisor).
```

```text
URL:         https://www.theverge.com/2023/1/25/23571082/cnet-ai-written-stories-errors-corrections-red-ventures
Kind:        secondary. Independent reporting that tallied the corrections.
Establishes: The "more than half" framing and the 41-of-77 count as an external tally of correction notes, not a CNET-stated figure.
Paraphrase:  The Verge reports CNET found errors in more than half of its AI-written stories and counts corrections appended to the live articles, including notes that CNET "replaced phrases that were not entirely original."
Locators:    Authors Mia Sato and Emma Roth, The Verge, January 25, 2023. Headline: "CNET found errors in more than half of its AI-written stories." NOTE: the brief attributed The Verge coverage to James Vincent; the corrections story is bylined Sato and Roth. Vincent wrote earlier Verge AI coverage; only the Sato/Roth piece was read and verified here.
Quote:       Headline: "CNET found errors in more than half of its AI-written stories."
```

```text
URL:         https://www.engadget.com/cnet-corrected-41-of-its-77-ai-written-articles-201519489.html
Kind:        secondary. Independent reporting that states the count and its source.
Establishes: That the 41 figure is a count of articles carrying correction notes, attributed by Engadget to the articles themselves and to The Verge, not to a number in CNET's editor's note.
Paraphrase:  Of the 77 articles CNET says were written in the AI trial, 41 carry corrections. Engadget credits The Verge for observing that some corrections say CNET "replaced phrases that were not entirely original."
Locators:    Author Igor Bonifacic, Engadget, January 25, 2023.
Quote:       "In all, of the 77 articles the publication now says were written as part of a trial to test an 'internally designed AI engine,' 41 feature corrections."
```

```text
URL:         https://arxiv.org/abs/2005.14165
Kind:        primary. The GPT-3 paper; the authoring lab describing the training objective it owns.
Establishes: That models of this class are autoregressive language models trained to predict the next token from prior context, optimizing the statistical likelihood of text rather than checking any fact.
Paraphrase:  "Language Models are Few-Shot Learners" describes GPT-3 as an autoregressive language model: it predicts the next token given the preceding context, learned from a large text corpus by maximizing the likelihood of the observed continuation. Nothing in the objective verifies a computed figure. USE WITH CARE: this is the general mechanism for large language models. CNET used an internally designed engine whose architecture is not public, so this source explains the class of failure, not CNET's specific tool.
Locators:    Brown, Mann, Ryder, Subbiah, Kaplan et al. (OpenAI), 2020. Abstract and Section 2 (Approach), which describe the autoregressive objective.
Quote:       Model described in the abstract as "an autoregressive language model."
```

```text
URL:         https://arxiv.org/abs/2509.04664
Kind:        primary. Technical paper owning the argued mechanism for hallucination.
Establishes: Why fluent generative text can be confidently wrong: models guess plausibly when uncertain, and both pretraining statistics and evaluation scoring reward that guessing over admitting uncertainty.
Paraphrase:  "Why Language Models Hallucinate" argues that models produce plausible but incorrect statements because training and evaluation reward guessing over acknowledging uncertainty. In pretraining, hallucinations arise as ordinary errors in binary classification under natural statistical pressure; they persist because most benchmarks grade like exams that reward a confident guess. USE WITH CARE: published September 2025, this postdates the 2023 CNET incident and does not mention CNET. It explains the mechanism; it is not contemporaneous analysis of this event.
Locators:    Kalai, Nachum, Vempala, Zhang (OpenAI and Georgia Tech), arXiv:2509.04664, September 4, 2025. Abstract.
Quote:       "Like students facing hard exam questions, large language models sometimes guess when uncertain, producing plausible yet incorrect statements instead of admitting uncertainty." / "We argue that language models hallucinate because the training and evaluation procedures reward guessing over acknowledging uncertainty."
```

```text
URL:         https://www.wgaeast.org/cnet-media-workers-unionize-with-the-wga-east/
Kind:        primary. The union's own announcement; the authoring party stating its formation and reasons.
Establishes: The staff response months after the AI incident: about 100 CNET workers formed a union with the Writers Guild of America, East, naming automation as a threat.
Paraphrase:  On May 16, 2023, roughly 100 CNET writers, editors, and producers announced they had formed the CNET Media Workers Union with the Writers Guild of America, East. Their organizing statement names automated technology as a threat to jobs and reputations. The announcement identifies Red Ventures, which acquired CNET in fall 2020, as the owner, and lists sister outlets under it.
Locators:    WGA East press room, May 16, 2023; "Why We're Organizing" statement.
Quote:       "automated technology threatens our jobs and reputations"
```

```text
URL:         https://futurism.com/cnet-staff-unionize-ai
Kind:        secondary. Reporting on the unionization and its link to the AI program.
Establishes: That the AI scandal was among the stated reasons for organizing, alongside layoffs and cost-cutting under Red Ventures.
Paraphrase:  Futurism reports that more than 100 CNET staffers unionized with the WGA East in May 2023, following the AI-article scandal and prior layoffs, and quotes the workers' concern that automated technology threatens their jobs and reputations.
Locators:    Futurism, May 2023; headline "CNET Staff Unionize, Saying AI Use 'Threatens Our Jobs and Reputations.'"
Quote:       Headline: "CNET Staff Unionize, Saying AI Use 'Threatens Our Jobs and Reputations.'"
```

```text
URL:         https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/
Kind:        secondary. Corroborating mainstream coverage. ACCESS-GATED.
Establishes: That a major national outlet covered the incident contemporaneously, framing it as a journalism failure requiring human corrections.
Paraphrase:  The Washington Post covered CNET's AI articles and the resulting corrections on January 17, 2023, under the headline "CNET used AI to write articles. It was a journalistic disaster." The body returned HTTP 403 to both fetch tools and could not be read; the URL, headline, and date are confirmed through the search index. The byline was not verified and must not be stated as fact.
Locators:    The Washington Post, January 17, 2023. Body inaccessible.
Quote:       Headline only (from search index): "CNET used AI to write articles. It was a journalistic disaster."
```

## Contradictions

- Article count: 73 versus 77. Futurism's original break (Landymore, mid-January
  2023) counted about 73 AI-generated articles. CNET's editor's note (January 25)
  states 77. Settled by the record: 77 is CNET's own final figure after its full
  audit; 73 was an external count taken before that audit closed. Use 77 and
  attribute it to CNET; note 73 only as the early count if the timeline needs it.

- The "41 of 77" corrections figure and who owns it. Secondary summaries
  repeatedly credit "41 of 77, more than half" to Connie Guglielmo or to CNET's
  editor's note. The editor's note contains no number; it says only "a small
  number requiring substantial correction and several stories with minor issues."
  The 41 is a tally of correction notes appended to the live articles, reported by
  The Verge (Sato and Roth) and Engadget (Bonifacic). Settled by the record: the
  writer must attribute the count to that external tally of the articles, and
  attribute the word "substantial" to Guglielmo, who applied it to "a small
  number," not to 41. Do not write that CNET announced 41 corrections.

- "AI-written" versus "AI-assisted." CNET frames the work as editor-outlined,
  AI-drafted, human-edited. Reporting and critics call the pieces AI-written and
  fault the hidden byline. Both descriptions fit the same facts: the AI produced
  the drafts, human editing was supposed to catch errors and did not, and the
  original disclosure hid the AI's role. Settled: describe the process precisely
  rather than pick one label.

- Mechanism timing. The strongest mechanism primary (Kalai et al.) is from 2025.
  It explains why fluent models fabricate; it is not evidence about what CNET's
  2023 engine did internally. Keep the mechanism as a general lesson, clearly
  dated, not as a contemporaneous finding about CNET.

## Numbers

```text
Figure: 77 stories drafted with the AI tool
Owner:  CNET editor's note (Guglielmo), cnet.com
Scope:  CNET Money financial explainers, published from November 2022; about 1% of CNET's total content for the period
```

```text
Figure: ~1% of CNET's total content for the period
Owner:  CNET editor's note (Guglielmo)
Scope:  Share of all CNET content published in the same window as the 77 AI stories
```

```text
Figure: 41 of 77 articles carry corrections (~53%, "more than half")
Owner:  The Verge (Sato and Roth) and Engadget (Bonifacic), as a tally of correction notes on the live articles. NOT stated in CNET's editor's note.
Scope:  The 77 AI-drafted stories, counted after CNET's audit
```

```text
Figure: ~73 articles (early count)
Owner:  Futurism (Landymore), before CNET's audit closed
Scope:  AI-generated finance explainers identified at the time of the break; superseded by CNET's 77
```

```text
Figure: $10,300 stated as interest earned; $300 is the correct interest
Owner:  AI original wording quoted by Futurism (Christian); the error is confirmed by arithmetic and by CNET's corrected article
Scope:  A $10,000 deposit at 3% annual interest over one year; $10,300 is principal plus interest, not interest earned
```

```text
Figure: "flat $1,000 in interest per year" (incorrect)
Owner:  AI original wording quoted by Futurism (Christian)
Scope:  A $25,000 car loan at 4%; interest actually declines each period as the balance is paid down
```

## Source assets

```text
Asset: The correction note at the foot of CNET's live "What Is Compound Interest?" article
Shows: The operator admitting, in its own words, that the AI "mischaracterized some aspects of CDs, savings accounts and loan payments," and that a human rewrote the piece. This is the operator's record of one failure and its fix.
Crop:  Retain the full correction sentence and the visible human byline above the bio block. Omit the surrounding navigation and promotional rails.
```

```text
Asset: The paired-phrase comparison in Futurism's plagiarism story (CNET AI line beside the Forbes Advisor line)
Shows: How closely the AI's wording tracked an existing article, with a small edit that obscured the source.
Crop:  Retain both phrases and their source labels. Omit adjacent unrelated examples if only one pair is used.
```

```text
Asset: None found for the mechanism papers beyond prose
Shows: The Kalai et al. abstract carries the exam-guessing analogy in text; no single figure in it argues the point better than a sentence. GPT-3's objective is prose, not a chart. Do not manufacture a diagram; if a visual is wanted, a small worked arithmetic panel of the $10,000-at-3% error would teach more than any figure lifted from the papers.
Crop:  n/a
```

## Discarded

```text
URL: https://www.cnn.com/2023/01/25/tech/cnet-ai-tool-news-stories — corroborating secondary coverage seen in the index but not read in full; the account is already established firsthand by CNET's note and by the Futurism and Verge pieces that were read.
URL: https://gizmodo.com/cnet-ai-chatgpt-news-robot-1849996151 — secondary aggregation; adds no claim not owned by a primary or by the read reporting.
URL: https://vibegraveyard.ai/story/cnet-ai-articles-corrections/ — third-party retelling; a repetition, not an owner of any figure.
URL: https://tech.yahoo.com/ai/chatgpt/articles/cnet-testing-ai-engine-heres-162300931.html — Yahoo republication of CNET's editor's note; used only to cross-read the text, superseded by the canonical CNET page, which was confirmed to resolve (HTTP 200) and is cited instead.
```
