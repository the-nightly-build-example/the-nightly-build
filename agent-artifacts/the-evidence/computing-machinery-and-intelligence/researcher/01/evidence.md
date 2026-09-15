# Evidence record: the-evidence/computing-machinery-and-intelligence (01)

The record supports the commissioned angle in full. Turing's 1950 paper, read
directly, gives the exact imitation-game setup, the single quantitative
prediction in its own words, and the "too meaningless" substitution, all
verified against the primary. The modern "passed the Turing test" claim is
anchored to its own paper: Jones & Bergen's three-party study, read from the
arXiv preprint that revived the phrase in 2025 and now published in PNAS
(2026). Its numbers are exact from the primary. The comparison the commission
asks for is clean and documented: Turing predicted an average interrogator kept
to no better than a 70 percent chance after five minutes against a machine of
about 10^9 units of storage, framed as a guess about how the words "machine"
and "think" would drift by 2000; the modern study reports a specific model under
a specific prompt judged human 73 percent of the time in a three-party game,
which its own authors call a test of humanlikeness and deception, not
intelligence. The deception criticism is documented from two primaries: Hayes &
Ford (1995) and Jones & Bergen's own text. The record is thin in one place: the
term "the Turing test" is not Turing's, and no single primary owns the drift
from his prediction to today's loose usage, so that framing rests on comparing
the two primaries side by side rather than on one source asserting the drift.
The library carries strong mechanics lessons the writer should link rather than
re-teach; they are listed in their own section and are not sources for the
article's own claims.

## Sources

```text
URL:         https://doi.org/10.1093/mind/LIX.236.433
Kind:        primary. Turing is the author; the paper owns every claim about
             what the imitation game is and what he predicted. (Canonical Mind
             citation. Free readable full text of the same article, verified
             against these passages, is hosted at
             https://www.cs.ox.ac.uk/activities/ieg/e-library/sources/t_article.pdf
             — use it for the reader-facing link if the DOI page paywalls.)
Establishes: The imitation game's exact setup, the single numeric prediction,
             the "too meaningless" substitution, and the nine named objections.
Paraphrase:  Turing opens by refusing "Can machines think?" and replaces it
             with a three-party game adapted from a party game about telling a
             man from a woman. An interrogator (C) in a separate room questions
             a man (A) and a woman (B) by written/typewritten message — ideally
             a teleprinter — and guesses which is which. Turing then asks what
             happens when a machine takes the part of A. In section 6 he gives
             his one forecast: in about fifty years a computer of about 10^9
             storage could play the game so well that an average interrogator
             has no more than a 70 percent chance of a right identification
             after five minutes, and he frames this as a prediction that the
             use of the words "machine" and "think" and "general educated
             opinion" will by then have shifted, not as a threshold for
             consciousness. He rebuts nine objections, among them Lady
             Lovelace's — that the machine "can do whatever we know how to
             order it to perform" and can never take us by surprise.
Locators:    §1 The Imitation Game (setup, teleprinter, the machine-substitution
             question); §6 Contrary Views on the Main Question (the prediction);
             §6, objection (6) Lady Lovelace's Objection; §7 Learning Machines
             (brain storage estimate 10^10–10^15 binary digits, and "I should
             be surprised if more than 10^9 was required").
Quote:       "I believe that in about fifty years' time it will be possible, to
             programme computers, with a storage capacity of about 10^9, to make
             them play the imitation game so well that an average interrogator
             will not have more than 70 per cent chance of making the right
             identification after five minutes of questioning."
             "The original question, 'Can machines think?' I believe to be too
             meaningless to deserve discussion."
             "It is played with three people, a man (A), a woman (B), and an
             interrogator (C) who may be of either sex."
             "We now ask the question, 'What will happen when a machine takes
             the part of A in this game?' ... These questions replace our
             original, 'Can machines think?'"
             Lovelace, quoted by Turing: "The Analytical Engine has no
             pretensions to originate anything. It can do whatever we know how
             to order it to perform." Turing's reply: "Machines take me by
             surprise with great frequency."
```

```text
URL:         https://doi.org/10.1073/pnas.2524472123
Kind:        primary. Jones & Bergen are the authors and the study owns its own
             numbers. Peer-reviewed publication of record (PNAS) of the study
             below. Abstract page returned HTTP 403 to an automated fetch;
             metadata confirmed via Crossref, and the study's numbers were read
             directly from the authors' own preprint text (next entry).
Establishes: That the "GPT-4.5 passed a standard three-party Turing test" claim
             is a peer-reviewed result, and its exact citation.
Paraphrase:  Cameron R. Jones and Benjamin K. Bergen, "Large language models
             pass a standard three-party Turing test," Proceedings of the
             National Academy of Sciences 123, no. 21 (2026). This is the
             refereed version of the March 2025 arXiv preprint that carried the
             claim into the press.
Locators:    PNAS vol. 123, issue 21 (2026); article under DOI
             10.1073/pnas.2524472123.
Quote:       (none needed beyond the preprint's, which carries identical figures)
```

```text
URL:         https://arxiv.org/abs/2503.23674
Kind:        primary. The authors' own preprint of the three-party study; read
             directly (HTML full text) for every figure. This is the document
             that revived "passed the Turing test" in the 2025 press.
Establishes: The exact three-party design, the win rates, the persona prompt,
             and the authors' own framing of what the test measures.
Paraphrase:  Interrogators held two simultaneous five-minute text conversations
             each round, one with a human witness and one with an AI witness,
             then judged which was human; each participant did 8 rounds. Across
             two pre-registered studies — 126 UCSD undergraduates (445 games)
             and 158 Prolific workers (576 games), 1,021 games in all — GPT-4.5
             prompted to adopt a humanlike persona was judged the human 73
             percent of the time, i.e. picked as human more often than the real
             human it was paired against. LLaMa-3.1-405B with the same prompt
             reached 56 percent; without the persona prompt GPT-4.5 fell to 36
             percent and LLaMa to 38 percent; the baselines GPT-4o (21 percent)
             and the 1960s script ELIZA (23 percent) sat below chance. The
             persona prompt told the model to answer as a young, introverted
             person familiar with internet culture. The authors state plainly
             the test is a measure of substitutability and of a model's ability
             to deceive people, and "not a direct test of intelligence, but a
             test of humanlikeness."
Locators:    Results / Figure 2 and Table 1 (win rates and per-population
             splits); Methods (8 rounds, 5-minute limit, simultaneous
             two-witness design); Figure 6 (persona prompt); Introduction and
             Discussion §3.3 (substitutability, deception, humanlikeness).
Quote:       "the Turing test is a measure of substitutability: whether a system
             can stand-in for a real person without an interlocutor noticing the
             difference."
             "the Turing test is an exacting measure of a model's ability to
             deceive people: to bring them to have a false belief that the model
             is a real person."
             "Fundamentally, the Turing test is not a direct test of
             intelligence, but a test of humanlikeness."
```

```text
URL:         https://arxiv.org/abs/2405.08007
Kind:        primary. Jones & Bergen's earlier study; read for the two-party
             contrast the commission asks for.
Establishes: That an earlier "passes the Turing test" claim used a two-party
             design, and under that design the machine did not beat the human.
Paraphrase:  Cameron R. Jones and Benjamin K. Bergen, "People cannot distinguish
             GPT-4 from a human in a Turing test" (2024). Here the interrogator
             held a single five-minute conversation with one witness — human or
             AI, not both at once — and judged whether it was human. GPT-4 was
             judged human 54 percent of the time; real humans were judged human
             67 percent; ELIZA reached 22 percent. The design has no
             side-by-side human comparison, which is why the authors call it a
             two-player test and treat the later three-party study as the
             stronger claim.
Locators:    Abstract; Results (pass rates 54% GPT-4, 67% human, 22% ELIZA).
Quote:       "the first robust empirical demonstration that any artificial
             system passes an interactive 2-player Turing test."
```

```text
URL:         https://www.ijcai.org/Proceedings/95-1/Papers/125.pdf
Kind:        primary. Hayes & Ford are the authors of the critique; the paper
             owns the argument that the test rewards deception.
Establishes: The standing, pre-LLM criticism that the imitation game tests
             disguise and human credulity, not thought, and that its goal is
             circular.
Paraphrase:  Patrick J. Hayes (Beckman Institute, University of Illinois) and
             Kenneth M. Ford (Institute for Human & Machine Cognition,
             University of West Florida), "Turing Test Considered Harmful,"
             IJCAI 1995, pp. 972–977. They read Turing's game as a "species
             test" — telling a human from a machine pretending to be human — and
             argue that to pass it a program must be built to deceive rather than
             to think. They also argue the goal is circular: the test is said to
             measure "human conversational competence," but the only definition
             of that competence is the ability to pass the test.
Locators:    "Head Games" (setup as a species test); the passage on typing
             tricks (p. 973); the circularity passage.
Quote:       "To pass the species test we must make not an artificial
             intelligence, but an artificial con artist."
             "The tests are circular: they define the qualities they are
             claiming to be evidence for."
```

```text
URL:         https://plato.stanford.edu/entries/turing-test/
Kind:        secondary. The Stanford Encyclopedia of Philosophy reports on and
             interprets Turing's paper from outside it.
Establishes: Context that the standard reading is a three-party imitation game,
             and that Turing's fifty-year forecast is a distinct empirical claim
             separate from whether success would prove thought.
Paraphrase:  The entry sets out the three-party setup, quotes the same fifty-year
             prediction verified above, and separates two questions Turing kept
             apart: whether a machine can do well at the game, and whether it can
             think. It notes success gives at most a prima facie reason to think
             intelligence is present, not a proof.
Locators:    Sections on the imitation game and on Turing's predictions.
Quote:       (paraphrase sufficient; the entry quotes the same prediction owned
             by Turing above)
```

```text
URL:         https://www.livescience.com/technology/artificial-intelligence/open-ai-gpt-4-5-is-the-first-ai-model-to-pass-an-authentic-turing-test-scientists-say
Kind:        secondary. Press coverage reporting the Jones & Bergen claim; used
             only as an example of how the modern claim entered general
             circulation.
Establishes: That the finding was reported to the public as GPT-4.5 being "the
             first AI model to pass an authentic Turing test," the kind of
             framing the lesson checks against Turing's own conditions.
Paraphrase:  Live Science reported the three-party study under the headline that
             GPT-4.5 is the first AI model to pass an authentic Turing test.
             (The URL resolves; an automated fetch returned only the page's own
             title/headline before the body truncated, so this entry rests on
             the headline framing alone, which is all it is used for.)
Locators:    Headline.
Quote:       Headline: "OpenAI's GPT-4.5 is the first AI model to pass an
             authentic Turing test, scientists say."
```

## Library lessons to link in Background (not article sources)

These are existing published lessons the writer should link in the Background
band rather than re-teach, per the commission's boundary that this lesson must
not re-explain how a model predicts text. They are context, not sources for any
claim the article makes.

```text
Lesson:  the-mechanics/autoregressive-generation — "The instant a model writes a
         token, it becomes fact" (2026-07-25)
Covers:  How "predict the next token" becomes a full reply; the direct home for
         "a model produces its most probable continuation." Best single link for
         the mechanic the commission says to link, not teach.
```

```text
Lesson:  the-mechanics/hallucination — "A model builds a fake citation the same
         way it builds a true one" (2026-07-23)
Covers:  Why fluent output comes unmoored from truth — the "fluent, plausible
         wrong answers" the commission points to. Useful where the lesson notes
         a convincing conversation is not evidence of a true inner state.
```

```text
Lesson:  the-evidence/stochastic-parrots — "The slogan 'stochastic parrots'
         outgrew the argument that coined it" (2026-07-28)
Covers:  A companion Evidence lesson on fluency versus understanding: a model
         predicts the next word from patterns in text with no access to what
         those words refer to. Optional thematic link for the deception /
         humanlikeness point; do not lean on it for the article's own claims.
```

## Contradictions

- The phrase "the Turing test" and the term "pass" are not Turing's. Turing
  wrote of the imitation game and framed his forecast as a bet about a 70
  percent identification rate and about word usage by 2000, not a pass/fail bar.
  No single source asserts the drift from his forecast to today's "passed the
  test"; the record establishes it only by placing the two primaries side by
  side. This is the commission's own required contribution, not a sourced claim
  to attribute.
- Two-party versus three-party results disagree about whether the machine beats
  the human. In the 2024 two-party study GPT-4 was judged human 54 percent
  against humans at 67 percent — the machine lost. In the 2025/2026 three-party
  study GPT-4.5 with a persona was judged human 73 percent, more than the human
  it was paired with. Same authors, different design, opposite direction on that
  point. The persona prompt is load-bearing: without it GPT-4.5 fell to 36
  percent.
- Turing's condition and the modern study's condition differ on three axes the
  commission names. Turing: "average interrogator," five minutes, a machine of
  about 10^9 storage, and a three-party man/woman-style game. The 2025 study:
  recruited undergraduates and paid Prolific workers, five minutes (matching),
  a specific commercial model under a hand-written persona prompt, three-party
  but human-vs-AI. The five-minute window matches; the interrogators and the
  reliance on a tuned persona do not map onto Turing's framing of a generic
  machine and an average questioner.
- What the test measures is itself contested by the very people making the
  modern claim. Jones & Bergen call it a test of humanlikeness and deception,
  not intelligence; Hayes & Ford (1995) made the same charge decades earlier.
  This does not undermine the article's angle — it is the angle — but it means
  no source in the record treats "passed the Turing test" as evidence of
  thought.

## Numbers

```text
Figure: about 10^9 units of storage (binary digits)
Owner:  Turing 1950, §6 / §7
Scope:  Turing's estimate of the storage a machine needs to play the imitation
        game well; he puts brain storage at 10^10 to 10^15 binary digits and
        says he would be surprised if more than 10^9 were required for the game.
```

```text
Figure: no more than 70 per cent chance of a right identification
Owner:  Turing 1950, §6
Scope:  An "average interrogator," after five minutes of questioning, against a
        suitably programmed machine — Turing's forecast for "about fifty years"
        hence (i.e. around 2000).
```

```text
Figure: five minutes of questioning
Owner:  Turing 1950, §6
Scope:  The single time window in Turing's prediction. The 2025 study uses the
        same five-minute limit, the one condition that matches.
```

```text
Figure: 73% judged human (GPT-4.5 with persona prompt)
Owner:  Jones & Bergen 2025 (arXiv 2503.23674) / PNAS 2026
Scope:  Share of three-party games in which the interrogator picked the AI
        witness as the human; overall across both populations (69% UCSD
        undergraduates, 76% Prolific). More often than the paired human was
        picked. 1,021 games, 284 participants, 8 rounds each, 5-minute chats.
```

```text
Figure: 56% (LLaMa-3.1-405B, persona) / 36% (GPT-4.5, no persona) / 38% (LLaMa,
        no persona) / 21% (GPT-4o) / 23% (ELIZA)
Owner:  Jones & Bergen 2025 / PNAS 2026
Scope:  Same three-party design and games. Baselines GPT-4o and ELIZA below
        chance; the persona prompt is what lifts GPT-4.5 from 36% to 73%.
```

```text
Figure: 54% GPT-4 / 67% human / 22% ELIZA (two-party)
Owner:  Jones & Bergen 2024 (arXiv 2405.08007)
Scope:  Share judged human in a two-party test — one 5-minute conversation with
        a single witness, no side-by-side human comparison. GPT-4 below the
        human rate.
```

## Source assets

```text
Asset: Turing 1950 — the prediction sentence in §6 as set type in the original
       Mind pages (available in the Internet Archive scan of the issue).
Shows: The single number in the paper in Turing's own words, so the reader sees
       how small and specific the "70 per cent / five minutes / 10^9" claim is.
Crop:  Keep the full sentence from "I believe that in about fifty years' time"
       through "five minutes of questioning." Omit surrounding paragraphs.
```

```text
Asset: Jones & Bergen 2025/2026 — Figure 2, the bar chart of win rates by model
       and population (GPT-4.5, LLaMa, GPT-4o, ELIZA, with and without persona).
Shows: The 73% for GPT-4.5-persona above the 50% line and the baselines below
       it, and the gap the persona prompt opens.
Crop:  Retain the chance line and the per-model labels; a crop must keep both
       persona and no-persona bars so the prompt's effect stays visible.
```

```text
Asset: Turing 1950 — the §1 paragraph stating the three-party setup ("It is
       played with three people, a man (A), a woman (B), and an interrogator
       (C)").
Shows: That the original game is three-party and text-only, the baseline the
       modern claim is measured against.
Crop:  Keep the sentence naming A, B, C and the teleprinter sentence; omit the
       sample dialogue that follows.
```

## Discarded

```text
URL: https://www.discovermagazine.com/chatgpt4-5-crosses-the-turing-test-threshold-47393
     — Secondary press on the same claim; Live Science already covers the press
     framing, and one example is enough.
URL: https://www.scribd.com/document/205015720/Turing-Computing-Machinery-and-Intelligence
     — Third-party upload of the Turing text; superseded by the canonical Mind
     DOI and the Oxford e-library full text.
URL: https://courses.cs.umbc.edu/471/papers/turing.pdf
     — Course-hosted copy of the Turing paper; a teaching mirror, not the
     document's own page. Kept in reserve only as a fallback readable copy.
URL: https://www.emergentmind.com/papers/2503.23674
     — Aggregator summary of the Jones & Bergen preprint; the primary was read
     directly, so the summary adds nothing.
URL: https://www.researchgate.net/publication/390354001
     — ResearchGate mirror of the same preprint; use the arXiv primary.
```
