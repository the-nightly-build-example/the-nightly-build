# Commission: when-ai-breaks/ai-overviews

## The incident

Google's AI Overviews, the AI-generated summary at the top of Google Search
results, launched broadly to US users at Google I/O on May 14, 2024. Within
about two weeks it was telling users to add glue to pizza sauce to keep the
cheese from sliding and to eat at least one small rock a day. Google's head of
Search published a postmortem on May 30, 2024, and Google cut back where the
feature triggered.

## Why this incident, why now

The reader uses AI search and RAG chatbots daily. This desk has covered chatbots
that invented facts (air-canada-chatbot, mata-v-avianca), but those are
hallucination cases: the system made something up. AI Overviews is a different
and more instructive failure: the system faithfully retrieved real sources, a
Reddit joke and an Onion satire, and restated them as fact at consumer-search
scale. It is the cleanest public demonstration that retrieval-augmented
generation has no model of whether a source can be trusted.

## Tell it in order (the desk's structure)

- What it was built to do: AI Overviews (evolved from the Search Generative
  Experience) generates an AI summary above the classic results, grounded in
  retrieved web pages. This is retrieval-augmented generation; link
  the-mechanics/retrieval.
- What it actually did: for the query about cheese sliding off pizza it surfaced
  and restated an eleven-year-old Reddit joke recommending glue; for a query
  about eating rocks it restated an Onion satirical article. Use only the
  examples that reporting and Google confirmed as real. Google itself noted that
  some viral screenshots were faked; those must not be used.
- Who it affected: US Search users during the rollout, a population in the
  hundreds of millions, on a surface that handles billions of queries a day. No
  documented mass physical harm (few people glued their pizza), but a top-of-
  results AI answer laundering a joke into food-safety advice is the harm to
  teach.
- What the operator did afterward: Liz Reid, VP and Head of Google Search,
  published "AI Overviews: About last week" (May 30, 2024), attributing failures
  to information gaps / "data voids" where the only matching content was satire
  or troll posts, and to the system surfacing user-generated content
  uncritically. Google reduced triggering for nonsensical queries and added
  restrictions around satire, user-generated content, and health. Get her exact
  title and the exact date from the primary.

## Why that kind of system fails that way (teach the mechanism)

Retrieval matches text to the query; it has no model of source trust or intent.
A Reddit thread literally about cheese not sticking to pizza is a strong
retrieval match, and the generator's job is to state an answer fluently and with
authority, which strips the joke's context. Connect three taught pieces:
retrieval (how the passage got pulled), instructions-are-data (the model cannot
tell a joke-instruction from a fact), and hallucination (confident restatement
with nothing checking whether the source deserves trust). On rare queries a
"data void" means the only matching source may be satire, so retrieval surfaces
exactly the worst source available.

## Where the same weakness lives today

Every retrieval-augmented answer engine: AI Overviews itself, and the AI-search
features in other assistants the reader uses. Any system that retrieves web text
and restates it inherits "no trust model plus confident restatement." Keep this
concrete and current without naming a company as an authority.

## Boundaries (do not repeat; link instead)

- air-canada-chatbot and mata-v-avianca (this desk) are hallucination/invention
  cases. This one is retrieval surfacing a real bad source. Draw that distinction
  explicitly; do not retell those incidents.
- retrieval, instructions-are-data, hallucination are taught in the-mechanics.
  Link them; teach only the thin new connective tissue, not the mechanisms whole.

## Source obligations

Floor: at least 8 sources; primary >= 4, secondary >= 1. Primaries: Liz Reid's
"About last week" postmortem (the operator's own account), Google's AI Overviews
/ I/O launch announcement, and the original surfaced artifacts where they can be
resolved (the Onion "eat rocks" article; the Reddit source if locatable). A
Google or Alphabet executive's on-record statement (for example Sundar Pichai's
interview acknowledging hallucination is unsolved) can be a primary. Secondary:
reporting that held up (The Verge, The New York Times, AP, BBC) for the specific
examples and timeline. Every example used must be verified against a source that
held up; discard any that trace only to a faked screenshot. Confirm every URL
resolves.

## Production policy (balanced; none required)

coach low, researcher high, writer medium, editor high; model capable, none
required. Recorded run: harness claude-code-routine, model claude-opus-4-8.

## Recent library shapes to break

Recent when-ai-breaks deks are strong single declaratives naming a number and an
actor (google-flu-trends: "overshot the CDC for 100 of 108 weeks"; epic-sepsis:
"missed two-thirds of the patients it was built to catch"). Match that concrete
register but find this piece's own figure or fact to carry the line. Vary heading
cadence from the recent comma-and-clause pattern.

## Neighboring articles this run

the-evidence/atari-dqn, the-instruments/parameter-count,
the-mechanics/reading-images, what-could-go-wrong/mesa-optimization. No overlap.
