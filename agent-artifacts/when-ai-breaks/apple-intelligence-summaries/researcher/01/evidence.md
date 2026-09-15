# Evidence record: when-ai-breaks/apple-intelligence-summaries (01)

The evidence supports the commission's core reporting and its required
contribution. The BBC's own three articles, RSF's own statement, Apple's own
launch newsroom post, Apple's two statements as quoted by the BBC and Macworld,
and one summarization-faithfulness paper together establish: what the feature
was built to do (group and shorten stacked notifications on the Lock Screen,
iOS 18.1, US launch 28 October 2024); that it produced false lines under news
organizations' own names (BBC/Mangione in December 2024; Luke Littler and Rafael
Nadal on 3 January 2025; a New York Times "Netanyahu arrested" line on
21 November 2024); who objected (the BBC, RSF, the NUJ); and what Apple did
after (a ~6-7 January promise to "further clarify" AI summaries, then a
16 January pause of Notification summaries for the News & Entertainment category
in the iOS 18.3 beta). The required contribution holds up: the BBC's own reports
show each false line was a compression or misattribution of a real source story,
not a free invention, and every source stresses that the line carried the
outlet's name. The evidence is thin in three places, all recorded below: the
verbatim wording of the Mangione and Littler summaries is not in the BBC's own
prose (only the Nadal line is quoted exactly); the full circulated
"shoots himself" three-item string comes from user screenshots in secondary
coverage, not from a primary; and Apple mostly declined to comment, so Apple's
side is single-origin to two brief statements. The Maynez paper grounds the
mechanism but studies a more abstractive setting (single-sentence XSum), so its
70% figure describes that corpus, not Apple's feature.

## Sources

```text
URL:         https://www.bbc.com/news/articles/cd0elzk24dno
Kind:        primary — the affected outlet reporting firsthand that a false
             alert appeared under its own name, and carrying Apple's "declined
             to comment." Graham Fraser, BBC News, 13 December 2024.
Establishes: The origin report. Apple Intelligence "launched in the UK earlier
             this week"; the AI summary "falsely made it appear BBC News had
             published an article claiming Luigi Mangione ... had shot himself.
             He has not." The BBC contacted Apple "to raise this concern and fix
             the problem"; Apple declined to comment. The other summaries in the
             same grouped notification (Assad's overthrow in Syria; an update on
             South Korean President Yoon Suk Yeol) were accurate. A separate
             21 November case grouped three New York Times articles with one part
             reading "Netanyahu arrested," misstating an ICC arrest warrant;
             flagged on Bluesky by a ProPublica journalist, screenshot
             unverified by the BBC, NYT declined to comment. Availability: iOS
             18.1 or later on iPhone 16 (all), 15 Pro, 15 Pro Max, plus some
             iPads and Macs.
Locators:    Body paragraphs 1-8, 12-13.
Quote:       "the AI-powered summary falsely made it appear BBC News had
             published an article claiming Luigi Mangione ... had shot himself.
             He has not."
             "one part reading 'Netanyahu arrested'"

URL:         https://www.bbc.com/news/articles/cx27zwp7jpxo
Kind:        primary — affected outlet reporting firsthand. Imran Rahman-Jones,
             BBC News, 3 January 2025.
Establishes: On 3 January 2025 a BBC News app summary "falsely claimed darts
             player Luke Littler had won the PDC World Championship - before he
             even played in the final," based on a BBC story about Littler
             winning the semi-final the Thursday night. Within hours a BBC Sport
             app summary told some users Rafael Nadal had come out as gay; the
             underlying story was about Brazilian gay tennis player Joao Lucas
             Reis da Silva. Only the Nadal line is quoted verbatim by the BBC.
             The article states the mechanism plainly: the summary "appears to be
             directly from the BBC, it is in fact Apple Intelligence's take on
             much longer headlines." Other summaries that day (South Korea,
             influenza) were accurate.
Locators:    Body paragraphs 1-3, 8-9, 14.
Quote:       "'Brazilian tennis player, Rafael Nadal, comes out as gay'"
             "Even though this type of summary notification appears to be
             directly from the BBC, it is in fact Apple Intelligence's take on
             much longer headlines."

URL:         https://www.bbc.com/news/articles/cq5ggew08eyo
Kind:        primary — affected outlet reporting firsthand, and the primary
             carrying Apple's exact pause statement and the BBC's own statement.
             Natalie Sherman & Imran Rahman-Jones, BBC News, 16 January 2025.
Establishes: Apple's suspension. Apple's exact statement: "With the latest beta
             software releases of iOS 18.3, iPadOS 18.3, and macOS Sequoia 15.3,
             Notification summaries for the News & Entertainment category will be
             temporarily unavailable"; and that for other apps AI summaries "will
             appear using italicised text." Timeline: the BBC complained in
             December, Apple did not respond until January with the labeling
             promise, drawing further criticism, then disabled the feature for
             news and entertainment. Also affected, per "reports from journalists
             and others on social media": Sky News, the New York Times, the
             Washington Post (the last reported by WaPo columnist Geoffrey A
             Fowler). RSF's Vincent Berthier: the feature "should not be rolled
             out again until there is zero risk it will publish inaccurate
             headlines." Jonathan Bright, head of AI for public services at the
             Alan Turing Institute, on hallucinations as a "real concern."
Locators:    Body paragraphs 1-3, 13-17; analysis section.
Quote:       "Notification summaries for the News & Entertainment category will
             be temporarily unavailable"
             "it was also harming the reputation of news organisations like the
             BBC whose lifeblood is their trustworthiness, by displaying the
             false headlines next to their logos."

URL:         https://rsf.org/en/rsf-urges-apple-remove-its-new-generative-ai-feature-after-it-wrongly-attributes-false-information
Kind:        primary — the press-freedom body stating its own position.
             Published 17 December 2024, updated 18 December 2024.
Establishes: RSF's demand that Apple remove the feature, and its framing of the
             harm. Dates: the feature "launched in the UK on 11 December"; "took
             less than forty-eight hours" to fail; "On 13 December, the BBC
             announced a complaint to Apple." Attribution named as harm to a
             media outlet's credibility.
Locators:    Lede; body paragraphs 2-3; pull quote.
Quote:       "AIs are probability machines, and facts can't be decided by a roll
             of the dice." — Vincent Berthier, Head of RSF's Technology and
             Journalism Desk
             "The automated production of false information attributed to a media
             outlet is a blow to the outlet's credibility and a danger to the
             public's right to reliable information on current affairs."

URL:         https://www.apple.com/newsroom/2024/10/apple-intelligence-is-available-today-on-iphone-ipad-and-mac/
Kind:        primary — Apple describing its own product at launch. 28 October
             2024.
Establishes: What the feature was built to do and when it shipped. The first
             Apple Intelligence features became available "with the release of
             iOS 18.1, iPadOS 18.1, and macOS Sequoia 15.1"; notification
             summaries "allow users to scan long or stacked notifications with
             key details right on the Lock Screen." Available "when the device
             and Siri language are set to U.S. English." Craig Federighi is
             "Apple's senior vice president of Software Engineering." The same
             system summarizes mail and messages and offers a Reduce
             Interruptions Focus.
Locators:    Headline dek; paragraphs 1-2 (Federighi quote); notification-
             summaries paragraph.
Quote:       "notification summaries that allow users to scan long or stacked
             notifications with key details right on the Lock Screen"

URL:         https://www.macworld.com/article/2569963/apple-promises-to-improve-ai-news-summaries-following-embarrassing-inaccuracies.html
Kind:        secondary — a trade outlet reporting Apple's statement, used for the
             exact intermediate wording. David Price, Macworld, 7 January 2025.
Establishes: Apple's first public acknowledgement, before the pause. Apple gave a
             labeling promise but no apology and no accuracy fix at this stage.
Locators:    Apple statement block; surrounding analysis.
Quote:       "Apple Intelligence features are in beta and we are continuously
             making improvements with the help of user feedback. A software
             update in the coming weeks will further clarify when the text being
             displayed is summarization provided by Apple Intelligence."

URL:         https://us.cnn.com/2024/12/19/media/apple-intelligence-news-bbc-headline/index.html
Kind:        secondary — CNN reporting on the BBC/RSF dispute from outside it.
             Liam Reilly, CNN, 19 December 2024.
Establishes: Context and the interpretation the piece turns on. States the
             structural problem in outlets' own terms: the summaries "still
             present the synopses under the publisher's banner," and outlets have
             "lack of agency" because the feature is opt-in by the user, not the
             publisher. Repeats the RSF quotes and the "Netanyahu arrested" NYT
             case ("readers scrolling their home screens only saw two words:
             'Netanyahu arrested'"). Dates Apple's US public launch to late
             October and the tool's announcement to June 2024.
Locators:    Paragraphs 1-11.
Quote:       "Apple Intelligence's summaries, which are opt-in by the user, still
             present the synopses under the publisher's banner."

URL:         https://aclanthology.org/2020.acl-main.173/  (PDF: https://aclanthology.org/2020.acl-main.173.pdf)
Kind:        primary — the paper owns its own measurements and definitions.
             Joshua Maynez, Shashi Narayan, Bernd Bohnet, Ryan McDonald,
             "On Faithfulness and Factuality in Abstractive Summarization," ACL
             2020.
Establishes: The mechanism the lesson needs, and its terms. Neural summarizers
             "are highly prone to hallucinate content that is unfaithful to the
             input document." Two named kinds: intrinsic hallucinations
             "misrepresent facts in the input document"; extrinsic hallucinations
             "ignore the source material altogether." Human evaluation on XSum
             single-sentence summaries: hallucinations occur "in more than 70% of
             single-sentence summaries," the majority extrinsic, and "over 90% of
             extrinsic hallucinations were erroneous," so "hallucinations happen
             in most summaries and the majority of these are neither faithful nor
             factual." Caveat: this is the extreme single-sentence XSum setting,
             not notification grouping; the mechanism transfers, the percentages
             belong to that corpus.
Locators:    Abstract; Section 1 (contributions list); Section 3 (definitions);
             Table 2.
Quote:       "Intrinsic hallucinations are consequences of synthesizing content
             using the information present in the input document."
             "Extrinsic hallucinations are model generations that ignore the
             source material altogether."
             "intrinsic and extrinsic hallucinations happen frequently – in more
             than 70% of single-sentence summaries."
```

## Contradictions

- Remedy versus demand. RSF (17 December) and, at first, the BBC asked Apple to
  remove or withdraw the feature. Apple did neither. Its first move (~7 January)
  was a labeling promise with no accuracy fix and no apology (Macworld); only on
  16 January did it pause summaries, and only for the News & Entertainment
  category, leaving the same summarizer running for every other app (BBC,
  16 January). The operator's response is narrower than what the objectors asked
  for. This is reported fact, not a reading.
- Verbatim wording is not uniform across the record. The BBC's own articles
  quote only the Nadal line verbatim ("Brazilian tennis player, Rafael Nadal,
  comes out as gay"). For Mangione and Littler the BBC paraphrases. The widely
  circulated full string — "Luigi Mangione shoots himself; ..." grouped with the
  Syria and South Korea items — comes from user screenshots reproduced in
  secondary coverage (e.g. Gizmodo), not from a primary. Use the BBC's paraphrase
  as the load-bearing account; if the grouped string is quoted, mark it as a
  reader's screenshot, not the BBC's text.
- Scope of the "other outlets affected" claim. The Sky News, New York Times and
  Washington Post cases (BBC, 16 January) and the November "Netanyahu arrested"
  case rest on "reports from journalists and others on social media"; the BBC
  states it could not independently verify the NYT screenshot. These corroborate
  a pattern but each is single-sourced to a screenshot.
- On the commission's required contribution, the evidence points the same way,
  not against it. Every primary account describes a summary derived from a real
  source story whose meaning was changed (a semi-final read as a final; an ICC
  warrant read as an arrest; a story about one gay tennis player attached to
  another's name), and every source stresses the outlet's name sat on top. So the
  angle — lossy compression that changed meaning, made dangerous by the borrowed
  masthead — is supported, not undermined. One caution: mapping these cases onto
  Maynez's intrinsic/extrinsic split is the writer's synthesis; the sources do
  not use those labels for Apple's feature.

## Numbers

```text
Figure: iOS 18.1 / US launch of first Apple Intelligence features, 28 Oct 2024
Owner:  Apple Newsroom, 28 October 2024
Scope:  US English devices; the release that first shipped notification summaries

Figure: UK launch "on 11 December" 2024; failure "less than forty-eight hours" later
Owner:  RSF statement, 17 December 2024 (BBC: "launched in the UK earlier this week")
Scope:  UK availability of the feature that produced the BBC/Mangione summary

Figure: New York Times "Netanyahu arrested" summary, 21 November 2024
Owner:  BBC, 13 December 2024 (screenshot unverified by the BBC; via a ProPublica journalist on Bluesky)
Scope:  One grouped notification of three NYT articles

Figure: Luke Littler and Rafael Nadal false summaries, 3 January 2025
Owner:  BBC, 3 January 2025
Scope:  BBC News app (Littler) and BBC Sport app (Nadal), same day, within hours

Figure: Hallucinations in "more than 70% of single-sentence summaries"; "over 90% of extrinsic hallucinations were erroneous"
Owner:  Maynez et al., ACL 2020, Table 2 and Section 1
Scope:  Human evaluation on the XSum extreme-summarization corpus; per-model
        any-hallucination rates 73.1-79.3%. Not a measure of Apple's feature.
```

## Source assets

```text
Asset: Maynez et al. 2020, Figure 1 — example summaries from several systems with
       intrinsic and extrinsic hallucinations marked against the source document.
Shows: The exact difference between a summary that misreads the source and one
       that adds facts the source never contained — the distinction the lesson
       needs to separate "changed the meaning" from "made it up."
Crop:  Keep the source-document box beside at least one hallucinated summary with
       its highlight; omit unrelated system rows if space is tight.

Asset: Maynez et al. 2020, Table 2 — per-model hallucination percentages.
Shows: That unfaithful output is the common case, not the exception, in this
       setting; useful only with the XSum caveat stated in the caption.
Crop:  Retain the column headers (I, E, I∪E) and the model rows; do not crop off
       the header that scopes what the numbers count.

Asset: Apple Newsroom, 28 October 2024 — product image of notification summaries
       on the iPhone Lock Screen.
Shows: What the feature was meant to do: collapse stacked alerts into one line.
       Apple's own framing of the design that later carried false news lines.
Crop:  Keep the summarized Lock-Screen notification legible.

Asset: The grouped-notification screenshot showing the false line under "BBC
       News" (Mangione) circulated across coverage.
Shows: The single most direct image of the harm — a machine's false sentence
       beneath a trusted masthead. NOTE: in the BBC pages fetched, the lead
       images were branded/stock, and the verbatim screenshot appears in
       secondary coverage from user posts. Treat provenance as user-supplied; do
       not attribute the screenshot to the BBC's own page without re-confirming
       it lives there.
```

## Library links for the writer (Background, link — do not re-teach)

Surfaced via `nb history` against the library checkout. These are the paper's
own earlier lessons; they are not sources for this article's factual claims.

- `the-mechanics/hallucination` — "A model builds a fake citation the same way it
  builds a true one" (2026-07-23). The core "why fluent output can be unmoored
  from any source." Best single link for the mechanism paragraph.
- `the-instruments/hallucination-rate` — "A faithful summary of a false passage
  passes the hallucination test" (2026-08-07). Faithful-vs-unfaithful summary,
  the Vectara framing. Best link for the "the summary can be fluent and wrong"
  point, and pairs directly with this incident.
- `the-instruments/rouge` — "Reversing who did what in a summary leaves its
  ROUGE-2 score unchanged" (2026-08-13). Strong optional link: a summary can
  reverse the source's meaning and score unchanged — the Littler "semi-final read
  as final" and "Netanyahu warrant read as arrest" cases in metric form.
- `the-mechanics/speech-to-text-hallucination` — "Whisper answers silence with a
  sentence no one spoke" (2026-09-13). Optional analog: a language model emitting
  its most probable output rather than a blank. Use only if the mechanism
  paragraph needs a second worked case; otherwise skip to avoid crowding.

Keep distinct, name only if needed to mark the boundary (do not re-tell):

- `when-ai-breaks/bard-jwst-demo` (2026-09-02) — a launch-demo error. Different
  failure: a promotional claim, not a summarizer changing real news.
- `when-ai-breaks/galactica` (2026-09-01) — fabricated citations from a research
  model. Different: invention from whole cloth, not lossy compression of a real
  source.
- `when-ai-breaks/ai-overviews` (2026-08-05) — Google's search summaries reading
  a Reddit troll and The Onion correctly. Closest neighbor and the one to
  distinguish most carefully: there the source was junk read faithfully; here the
  source was real news read unfaithfully under the outlet's own name.

## Discarded

```text
https://www.cnbc.com/2025/01/08/apple-ai-fake-news-alerts-highlight-the-techs-misinformation-problem.html: returns 403 to both the fetch tool and a browser-agent curl; could not open the source's own page, so not cited. CNN (19 Dec) covers the same secondary ground and does resolve.
https://gizmodo.com/apples-ai-disastrously-rewrote-a-bbc-headline-to-say-luigi-mangione-shot-himself-2000538599: the origin of the widely quoted full "Luigi Mangione shoots himself; ..." string, but it rests on a user screenshot and repeats the BBC; used only to note where the verbatim string comes from, not cited as a primary.
https://www.theregister.com/2024/12/20/apple_urged_to_stop_ai_headline_summaries_after_false_claims/: 404 at the constructed URL; the RSF and CNN primaries already carry the press-freedom objection.
```
