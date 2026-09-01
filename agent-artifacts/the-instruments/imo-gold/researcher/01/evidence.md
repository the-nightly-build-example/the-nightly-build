# Evidence record: the-instruments/imo-gold (01)

The evidence firmly supports the commission's core claim: the IMO "gold" is a
graded proof score, not a checked answer, and the two 2025 golds are not the same
measurement. The scoring mechanics (six problems, seven points each, 42 possible,
year-relative medal cutoffs set by human coordinators against a rubric) are owned
by the IMO's own results pages and match the labs' announcements. The 2024
DeepMind silver (28/42, human-formalized Lean statements, up to three days, graded
by two named mathematicians) and the 2025 DeepMind gold (35/42, natural language,
within the 4.5-hour limit, officially graded and certified by IMO coordinators)
are each nailed to a primary. OpenAI's 2025 gold (35/42, two 4.5-hour sessions, no
tools, natural language) is owned by OpenAI's own posts, and OpenAI itself confirms
it declined the IMO's formal track and had its proofs graded by three former IMO
medalists rather than by IMO coordinators. Where the record is thin: the sharpest
accusation against OpenAI — that it broke an agreed one-week embargo and behaved
improperly — is contested, and its most specific version comes from an outside
commentator not in a position to know, while OpenAI (a party in a position to know)
directly contradicts it. Two primary artifacts I relied on are gated behind X's
login wall and were read through faithful reproductions; the exact "rude and
inappropriate" wording traces to an IMO coordinator but I could not open its
primary post. Both limitations are recorded below.

## Sources

```text
URL:         https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/
Kind:        primary — Google DeepMind is the authoring party and owns its own 2024 claim
Establishes: the 2024 result: which systems, what was solved, the point total, the
             formalization step, the time taken, and who graded it
Paraphrase:  AlphaProof and AlphaGeometry 2 together solved four of six 2024 IMO
             problems for 28/42, a silver-medal standard one point below that year's
             gold cutoff. AlphaProof solved two algebra problems and one number
             theory problem (including the hardest problem, solved by only five
             human contestants); AlphaGeometry 2 proved the geometry problem in 19
             seconds; the two combinatorics problems were not solved. The problems
             were first hand-translated by people into the formal language Lean. The
             systems solved one problem within minutes and took up to three days on
             the others. Solutions were scored to the IMO's rules by two named
             mathematicians.
Locators:    body sections "Applying AI to mathematics," "How they did it,"
             "Scoring the solutions"
Quote:       "First, the problems were manually translated into formal mathematical
             language for our systems to understand." / "Our systems solved one
             problem within minutes and took up to three days to solve the others." /
             "Our solutions were scored according to the IMO's point-awarding rules
             by prominent mathematicians Prof Sir Timothy Gowers, an IMO gold
             medalist and Fields Medal winner, and Dr Joseph Myers, a two-time IMO
             gold medalist and Chair of the IMO 2024 Problem Selection Committee."
```

```text
URL:         https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/
Kind:        primary — DeepMind owns its 2025 claim; the page also carries the IMO
             President's on-record confirmation of that claim
Establishes: the 2025 DeepMind result and, crucially, that it was graded and
             certified through official IMO coordination, in natural language, within
             the time limit
Paraphrase:  An advanced Gemini with Deep Think solved five of six 2025 problems for
             35/42, a gold-medal score. Unlike 2024, it worked end-to-end in natural
             language from the official problem statements, with no human
             formalization step, and finished within the 4.5-hour competition limit.
             DeepMind's solutions were officially graded and certified by IMO
             coordinators using the same criteria applied to student scripts. The IMO
             President is quoted confirming the score. DeepMind states it was in an
             "inaugural cohort" whose model results were officially graded, and that
             it held its announcement until after the IMO had verified results and
             students were honored.
Locators:    body; blockquote attributed to "Prof. Dr. Gregor Dolinar, President of
             the IMO"; closing paragraphs on timing
Quote:       "operated end-to-end in natural language, producing rigorous
             mathematical proofs directly from the official problem descriptions —
             all within the 4.5-hour competition time limit." / Dolinar: "We can
             confirm that Google DeepMind has reached the much-desired milestone,
             earning 35 out of a possible 42 points — a gold medal score." / "we were
             amongst an inaugural cohort to have our model results officially graded
             and certified by IMO coordinators using the same criteria as for student
             solutions."
```

```text
URL:         https://x.com/alexwei_/status/1946477742855532918  (thread)
             https://x.com/OpenAI/status/1946594928945148246
Kind:        primary — Alexander Wei / OpenAI own OpenAI's 2025 claim
             (read via reproductions below; the X pages are login-gated, HTTP 402)
Establishes: OpenAI's 2025 result, its conditions, and its grading route
Paraphrase:  OpenAI reports that an unreleased experimental reasoning LLM solved five
             of six 2025 problems for 35/42, a gold-level score, under human
             conditions — two 4.5-hour sessions, no tools, no internet, answers
             written as natural-language proofs. Each problem's proof was graded
             independently by three former IMO medalists, with scores finalized by
             unanimous consensus. OpenAI frames this as general-purpose reasoning, not
             a math-specific system, and says it will not release a model at this
             capability for many months.
Locators:    Wei thread posts 1–7; the grading and release-timing posts
Quote:       "the model solved 5 of the 6 problems on the 2025 IMO. For each problem,
             three former IMO medalists independently graded the model's submitted
             proof, with scores finalized after unanimous consensus. The model earned
             35/42 points in total, enough for gold!" / "the IMO gold LLM is an
             experimental research model. We don't plan to release anything with this
             level of math capability for several months."
Note:        The X posts are the artifact OpenAI's claim lives in, so their addresses
             are recorded here. Content was read through Simon Willison's verbatim
             reproduction and the LessWrong compilation (both below), which quote the
             thread in full. A reader who clicks the X links while logged out will hit
             the login wall; the reproductions are the accessible transcript.
```

```text
URL:         https://x.com/polynoamial/status/1946478249187377206  (thread)
Kind:        primary — Noam Brown is an OpenAI research scientist and a party in a
             position to know OpenAI's own coordination with the IMO
             (read via Zvi Mowshowitz's reproduction below; X page is login-gated)
Establishes: OpenAI's own account of whether and how it coordinated with the IMO on
             grading and announcement timing — the direct counter to the embargo
             accusation
Paraphrase:  Brown states OpenAI was emailed about a formal Lean version of the IMO
             about two months earlier and declined it, having focused on
             natural-language reasoning; it was never offered a natural-language
             option. Before publishing, OpenAI spoke with an IMO board member who
             asked it to wait until after the award ceremony, which OpenAI says it
             honored.
Locators:    Brown reply posts on timing and coordination
Quote:       "~2 months ago, the IMO emailed us about participating in a formal (Lean)
             version of the IMO ... so we declined. We were never approached about a
             natural language math option." / "Before we shared our results, we spoke
             with an IMO board member, who asked us to wait until after the award
             ceremony to make it public, a request we happily honored."
```

```text
URL:         https://x.com/demishassabis  (statement quoted in reporting below; the
             original post is login-gated)
Kind:        primary — Demis Hassabis is CEO of Google DeepMind, in the official
             cohort and a party in a position to know the IMO Board's request
Establishes: DeepMind's account that a Board request to delay existed and that
             DeepMind honored it — the pointed public contrast with OpenAI's timing
Paraphrase:  Hassabis says DeepMind did not announce on the Friday because it
             respected the IMO Board's original request that all AI labs share
             results only after the official results were verified by independent
             experts and the students had received their due recognition.
Locators:    Hassabis X statement, reproduced in the officechai report below
Quote:       "We didn't announce (the results) on Friday because we respected the IMO
             Board's original request that all AI labs share their results only after
             the official results had been verified by independent experts & the
             students had rightly received the acclamation they deserved."
Note:        This establishes that a request to delay existed and that DeepMind read
             it as binding on "all AI labs." It does not itself state what OpenAI was
             told, and it is a public statement by a direct competitor, so it is a
             confirmation of the request's existence, not neutral proof of OpenAI's
             intent.
```

```text
URL:         https://www.lesswrong.com/posts/3FRqRpisLaydEAhyD/a-brief-perspective-from-an-imo-coordinator
Kind:        primary — firsthand account by a self-identified IMO 2025 coordinator, a
             party in a position to know the grading process (linkpost to a Reddit
             comment; the coordinator is anonymous)
Establishes: what official coordination is, and that AI representatives sought
             on-the-spot grading that is not the official process
Paraphrase:  The coordinator describes AI-company representatives at the closing
             party walking around with laptops asking coordinators to evaluate model
             scripts on the spot, and states this is not the same as the real
             coordination process (confidential marking schemes, leader input,
             inter-coordinator discussion). The coordinator also notes there were no
             formal rules governing AI participation.
Locators:    quoted coordinator comment within the linkpost
Quote:       "At the closing party, AI company representatives were, disappointingly,
             walking around with laptops and asking coordinators to evaluate these
             scripts on-the-spot ... This isn't akin to the actual coordination
             process."
Note:        I could not open the underlying Reddit thread directly (fetch blocked);
             the LessWrong linkpost reproduces the coordinator's comment. The specific
             phrase "rude and inappropriate," attributed in several secondary
             summaries to a Problem 6 coordinator, is NOT confirmed to this primary and
             I did not reach its own source. Treat that exact wording as reported, not
             verified.
```

```text
URL:         https://www.imo-official.org/editions/2024/
Kind:        primary — the IMO's official results database owns the 2024 medal
             thresholds and counts
Establishes: the 2024 scoring frame: contestant count, and the exact gold/silver/
             bronze cutoffs that fix what 28/42 meant
Paraphrase:  609 contestants. Gold cutoff 29 (58 gold), silver cutoff 22 (123
             silver), bronze cutoff 16 (145 bronze), 170 honorable mentions, 1
             perfect score. Contest held in Bath, United Kingdom, July 2024.
Locators:    2024 edition summary table
Quote:       (tabular) Gold ≥29; Silver ≥22; Bronze ≥16
```

```text
URL:         https://www.imo-official.org/editions/2025/
Kind:        primary — the IMO's official results database owns the 2025 thresholds
Establishes: the 2025 scoring frame that fixes what 35/42 meant, and that 35 was the
             exact gold cutoff
Paraphrase:  630 contestants from 110 countries. Gold cutoff 35 (72 gold), silver
             cutoff 28 (104 silver), bronze cutoff 19 (145 bronze), 132 honorable
             mentions, 5 perfect scores. Event at Sunshine Coast, Australia, July
             10–20, 2025; exams July 15–16.
Locators:    2025 edition summary table
Quote:       (tabular) Gold ≥35; Silver ≥28; Bronze ≥19
```

```text
URL:         https://imo2025.au/news/the-66th-international-mathematical-olympiad-draws-to-a-close-today/
Kind:        primary — the official IMO 2025 host site owns the event schedule
Establishes: the ceremony date that anchors the announcement-timing dispute
Paraphrase:  The host confirms the 66th IMO ran July 10–20 at the Sunshine Coast,
             with the award/closing ceremony on July 19, 2025.
Locators:    event schedule / closing news item
Quote:       (schedule) exams July 15–16; award ceremony July 19
```

```text
URL:         https://simonwillison.net/2025/Jul/19/openai-gold-medal-math-olympiad/
Kind:        secondary — independent writeup that reproduces OpenAI's thread verbatim
Establishes: an accessible transcript of OpenAI's login-gated claim, and the
             self-grading detail
Paraphrase:  Reproduces the OpenAI/Wei posts: 5/6 solved, 35/42, graded by three
             former IMO medalists to unanimous consensus, no plan to release a model
             at this capability for months.
Locators:    quoted tweet blocks, dated July 19, 2025
Quote:       "three former IMO medalists independently graded the model's submitted
             proof, with scores finalized after unanimous consensus."
```

```text
URL:         https://xenaproject.wordpress.com/2025/08/03/ai-at-imo-2025-a-round-up/
Kind:        secondary — round-up by mathematician Kevin Buzzard, reporting from
             outside the two labs
Establishes: the official-vs-self-graded split, the embargo framing, and the caveat
             on what an IMO gold does and does not prove
Paraphrase:  Buzzard states DeepMind's result was officially validated and quotes
             Dolinar's confirmation; notes OpenAI announced "minutes after the closing
             ceremony" with solutions "marked by former IMO contestants," with no
             rules on whether submitted solutions were human-picked. He describes an
             informal embargo asking companies to wait until July 28, which collapsed
             once the first claim went public. He stresses the problems are high-school
             methods, far from research mathematics, and that 2025 was a one-point
             improvement on 2024.
Locators:    body, sections on DeepMind, OpenAI, and the embargo
Quote:       "there were no rules" (on OpenAI's submitted solutions) / "These IMO
             problems are a million miles away from the kind of questions which most
             research mathematicians are working on."
```

```text
URL:         https://thezvi.substack.com/p/google-and-openai-get-2025-imo-gold
Kind:        secondary — compilation that reproduces the primary tweets on both sides
             of the timing dispute
Establishes: the full timing exchange: Brown's rebuttal (primary, quoted above) and
             the outside criticism it answers
Paraphrase:  Reproduces Noam Brown's timing statement and Mikhail Samin's claim that
             cooperating labs met the IMO in person on July 16 and agreed announcements
             should wait until July 28 or later. Places OpenAI's announcement early on
             July 19 and DeepMind's on July 21.
Locators:    quoted tweet blocks; Samin quote
Quote:       Samin: "AI companies that chose to cooperate with the IMO on assessment of
             their models had in-person meetings with IMO people on July 16. It was
             agreed there that announcements of AI achievements should be made on 28
             July or later."
Note:        Samin is an outside AI-safety commentator, not an IMO official or a lab
             participant, so his "July 28" account is a relayed claim, not a statement
             by a party in a position to know.
```

```text
URL:         https://www.cbsnews.com/news/humans-beat-ai-technology-google-openai-math-olympiad-machines-catching-up/
Kind:        secondary — AP-sourced report (July 22, 2025) quoting the IMO President
Establishes: Dolinar's on-record caution about what the IMO can and cannot verify
Paraphrase:  Dolinar says organizers could not verify how much compute the models used
             or whether there was human involvement, and praises the (DeepMind)
             solutions as clear and precise.
Locators:    Dolinar quotes mid-article
Quote:       "Contest organizers could not verify how much computing power had been
             used by the AI models or whether there had been human involvement." /
             "Their solutions were astonishing in many respects. IMO graders found them
             to be clear, precise and most of them easy to follow."
```

```text
URL:         https://officechai.com/ai/didnt-declare-imo-results-sooner-as-per-organizers-wishes-says-google-in-dig-at-openai/
Kind:        secondary — report reproducing Hassabis's statement and the coordinator
             sentiment
Establishes: an accessible transcript of Hassabis's login-gated statement, and the
             reported coordinator characterization
Paraphrase:  Reproduces Hassabis's "we respected the IMO Board's original request"
             statement, notes OpenAI announced before DeepMind, and reports a
             coordinator's sense that OpenAI's move was rude and inappropriate.
Locators:    body; Hassabis quote; coordinator paraphrase
Quote:       coordinator sentiment as reported: "the general sense of the IMO Jury and
             Coordinators is that it was rude and inappropriate."
Note:        The "rude and inappropriate" line is reported here secondhand; its primary
             origin (an IMO coordinator) was not directly accessible to me.
```

## Contradictions

1. **Did OpenAI break an agreed one-week embargo, or only a vaguer request?**
   The strongest, most specific version — an in-person July 16 agreement that
   announcements wait until July 28 — comes from Mikhail Samin, an outside
   commentator not in a position to know (thezvi reproduction). Kevin Buzzard calls
   the July 28 embargo "informal." OpenAI's Noam Brown, a party in a position to
   know, directly contradicts the idea that OpenAI agreed to any July 28 date: he
   says the only request OpenAI received was from an IMO board member to wait until
   after the award ceremony, which OpenAI honored. Hassabis (DeepMind) says the Board
   asked "all AI labs" to wait until results were verified and students honored, but
   names no date. Net: that OpenAI announced early relative to what cooperating labs
   understood is well attested; that OpenAI itself agreed to and then broke a
   specific one-week embargo is not confirmed by any party in a position to know, and
   is denied by OpenAI. The commission's angle should treat "self-reported and
   self-graded outside official coordination" as solid, and "broke an agreed embargo"
   as contested.

2. **Before or after the closing ceremony?** Secondary framings split. Officechai and
   some summaries say OpenAI announced "before the closing ceremony"; Buzzard, Zvi,
   and OpenAI's own account place it just after the July 19 award ceremony (Wei's
   thread is dated July 19). The host site fixes the award ceremony on July 19. The
   defensible reading: OpenAI announced on July 19 around the award ceremony and well
   before the ~July 28 window others describe; whether it strictly preceded or
   followed the ceremony itself is reported both ways and should not be stated flatly.

3. **The "rude and inappropriate" characterization.** Attributed in secondary
   summaries to an IMO Problem 6 coordinator. The firsthand coordinator account I
   reached (LessWrong linkpost) complains about on-the-spot grading requests but I did
   not confirm the exact "rude and inappropriate" phrase to a primary. It is a
   reported sentiment, corroborated in spirit by Hassabis's public contrast and by
   Dolinar's caution, but the specific wording is single-sourced through secondaries.

4. **DeepMind's grading conditions vs. "same as students."** DeepMind says its proofs
   were graded "using the same criteria as for student solutions" (primary). The
   coordinator (primary) and Dolinar (secondary) both stress the IMO could not verify
   compute or rule out human involvement, and that real coordination is more than
   on-the-spot marking. These are not flatly opposed — DeepMind was in the official
   cohort and OpenAI was not — but "same criteria" and "cannot validate the methods"
   sit in tension worth showing the reader.

5. **No contradiction on the point totals or thresholds.** Every figure the argument
   rests on agrees across the labs' announcements and the IMO's own results pages. The
   only surface discrepancy — DeepMind's 2024 "silver, one point from gold" versus a
   "silver threshold of 28" — dissolves once the official bands are used: 2024 silver
   ran 22–28 and gold began at 29, so 28 sat at the top of silver, one point short.

## Numbers

```text
Figure: 42 points maximum (6 problems x 7 points)
Owner:  IMO official results (imo-official.org), both editions
Scope:  per contestant, per year; same structure 2024 and 2025
```

```text
Figure: 28 / 42 — DeepMind 2024 (AlphaProof + AlphaGeometry 2)
Owner:  DeepMind 2024 blog; sits within IMO 2024 official silver band
Scope:  4 of 6 problems solved; 2024 gold cutoff 29, silver 22, bronze 16
```

```text
Figure: 2024 medal cutoffs — Gold 29, Silver 22, Bronze 16
Owner:  imo-official.org 2024 edition
Scope:  609 contestants; 58 gold, 123 silver, 145 bronze, 1 perfect score
```

```text
Figure: "up to three days" — DeepMind 2024 solve time
Owner:  DeepMind 2024 blog
Scope:  one problem in minutes, others up to three days; outside the 4.5-hour
        human session limit
```

```text
Figure: 35 / 42 — DeepMind 2025 (Gemini Deep Think)
Owner:  DeepMind 2025 blog; confirmed by IMO President Dolinar on that page
Scope:  5 of 6 solved; within the 4.5-hour limit; officially graded/certified
```

```text
Figure: 35 / 42 — OpenAI 2025 (experimental reasoning LLM)
Owner:  OpenAI / Alexander Wei posts (via Willison, LessWrong reproductions)
Scope:  5 of 6 solved; two 4.5-hour sessions, no tools; graded by three former IMO
        medalists (not IMO coordinators)
```

```text
Figure: 2025 medal cutoffs — Gold 35, Silver 28, Bronze 19
Owner:  imo-official.org 2025 edition
Scope:  630 contestants; 72 gold, 104 silver, 145 bronze, 5 perfect scores. Both
        AI golds (35) landed exactly on the gold cutoff — the lowest gold score.
```

```text
Figure: Problem 6 unsolved by both 2025 models
Owner:  DeepMind 2025 blog (5/6) and OpenAI posts (5/6); the-decoder/IntuitionLabs
        secondary confirm P6 was the missed one and the hardest
Scope:  both models solved P1–P5, missed P6; note as reported, not IMO-owned
```

```text
Figure: Announcement dates — OpenAI July 19, 2025; DeepMind July 21, 2025
Owner:  Wei thread (July 19); DeepMind blog (July 21); award ceremony July 19
        (imo2025.au)
Scope:  reported "informal" embargo target of July 28 is contested (see Contradictions)
```

## Source assets

```text
Asset: IMO 2024 official results table on imo-official.org/editions/2024/
Shows: the medal bands as a grid — 28 falling one row under the gold line — which
       makes "graded score with year-relative cutoffs" visible at a glance
Crop:  must retain the gold/silver/bronze cutoff row and the contestant count; omit
       the per-country navigation chrome
```

```text
Asset: IMO 2025 official results table on imo-official.org/editions/2025/
Shows: the gold cutoff at exactly 35, the same number both AI systems scored — the
       single most economical way to show both golds sat on the lowest gold rung
Crop:  keep the cutoff row and the "5 perfect scores / 72 gold" counts; omit chrome
```

```text
Asset: The Dolinar confirmation blockquote on the DeepMind 2025 blog
Shows: an IMO officer certifying DeepMind's 35/42 in the IMO's own voice — the visible
       marker of official coordination that OpenAI's result lacks
Crop:  retain the full quote and the "President of the IMO" attribution; do not crop
       to the number alone, since the attribution is the point
```

```text
Asset: DeepMind's own line contrasting 2024 (Lean, translated) with 2025 (natural
       language, within the time limit), on the two DeepMind blogs
Shows: the year-over-year change in conditions — the reader can see what "the same
       medal" hides between 2024 and 2025
Crop:  pair the 2024 "manually translated into formal mathematical language" line with
       the 2025 "end-to-end in natural language ... within the 4.5-hour" line
```

```text
Asset: None found for OpenAI's 2025 result beyond text posts — OpenAI published no
       official scorecard or blog, only X threads, and those are login-gated
```

## Discarded

```text
URL: https://eu.36kr.com/en/p/3388372845035907 — aggregator ("None of 91 Judges") repackaging the coordinator dispute; sensational framing, no primary access; superseded by the coordinator linkpost and Dolinar's own quotes
URL: https://www.unite.ai/ai-at-the-international-mathematical-olympiad-how-alphaproof-and-alphageometry-2-achieved-silver-medal-standard/ — secondary rehash of the DeepMind 2024 blog; nothing the primary lacks
URL: https://gregrobison.medium.com/from-silver-to-gold-... — personal Medium explainer; no primary standing; risk of compounding error
URL: https://medium.com/@stevenshinechen/openais-llm-wins-imo-gold-... — opinion/explainer, secondary to the OpenAI posts
URL: https://intuitionlabs.ai/articles/ai-reasoning-math-olympiad-imo — useful corroboration that both missed P6, but a content-marketing aggregation; kept only as backing for the P6 detail, not cited as owner
URL: https://venturebeat.com/ai/google-releases-olympiad-medal-winning-gemini-... — about the later public Deep Think release, off the measurement question
URL: https://www.scientificamerican.com/article/openai-model-earns-gold-medal-score-... — AGI-framing coverage; the claim it reports is owned by the OpenAI posts already read
URL: https://champaignmagazine.com/2025/07/23/chatgpt-and-gemini-on-imo-gold-performance/ — local re-report; adds nothing over the primaries
URL: https://www.reddit.com/r/math/comments/1m5jn2i/... — the coordinator's underlying thread; fetch blocked, so relied on the LessWrong linkpost reproduction instead
```
