# Editorial review: when-ai-breaks/nyc-mycity-chatbot (editor/01)

## Skeptic

The draft's thesis: MyCity Business, a retrieval-plus-generation chatbot on
chat.nyc.gov, was published as the city's official answer on questions of
business law and returned confident sentences that contradicted specific NYC
and NYS rules. The article stands on four claims. The bot's answers on Section
8, cashless payment, and tips contradicted named statutes and agency guidance,
with the ten-of-ten Markup test the closest thing on record to a rate. The
system was retrieval over 2,000-plus NYC Business pages plus Azure OpenAI
generation, and retrieval does not force the generated sentence to match a
retrieved fact. The disclaimer did not repair the mechanism; the bot itself
answered "yes" to using it for professional business advice in the same
session where the page told the reader not to. The city ran the tool for 27
months under Adams's defense and Mamdani took it down on February 4, 2026.

Each claim held on retest. The Section 8 outcome and the "ten of ten"
qualifier match the Markup investigation, with the earlier correct-answer
caveat carried forward from the same story. The cashless quote matches the
Markup piece and lands against Local Law 34 § 20-840(b), which the article
quotes correctly. The tips claim maps to N.Y. Labor Law § 196-d, quoted
correctly. The retrieval-plus-generation reading is consistent with what Ars
Technica describes and with the paper's already-taught retrieval lesson. The
disclaimer-vs-answer contradiction is the exact exchange from the April 2
Markup follow-up. The 27-month arc math is right: October 16, 2023 to
February 4, 2026.

Display text ran the same checks. Headline claim (ten Markup staffers, "no
landlord obligation" for Section 8) matches s2. Dek: I corrected "2,000
NYC.gov pages" to "2,000 NYC Business pages" — the release specifies "NYC
Business web pages" and the broader gloss overstates scope in a line every
reader meets. All five subheads are concrete steps in the argument, not
scaffolding. The three table rows contradict named laws that own the counter-
claim; row 3's bot answer was truncated to "Yes." and I restored the full
quoted answer from the Markup pull-quote ("Yes, you can take a cut of your
worker's tips.") to hold parity with the other two rows. Named titles and
affiliations for Black, Rigie, Brown, Lewis-Martin, Kim, Malhotra, Offenhartz,
Stoyanovich, Venkatasubramanian, Ross, Pekec, and Mamdani all check against
the record.

Kind labels: s1-s7, s9, and s10 are primary in the sense the skill uses.
s4 (intro.nyc for Local Law 34) is a republished statutory text — marginal
as "primary" but acceptable as the text is the operative document and the
quote matches. s8 (Ars Technica) is correctly labeled secondary; it carries
the retrieval-as-industry-response gloss but is not the source of any load-
bearing fact. Every printed href opens on the source it names.

The rent-withholding sentence had a live ambiguity: "Asked on X whether
tenants could withhold rent for unmade repairs, the bot answered 'no'" reads
as if the bot was queried through X, which it wasn't. Rewritten to attribute
the query to the tenant attorney who posted the exchange, keeping the
Markup's Tyrrell reference implicit and the medium (X) as posting rather
than as query surface.

## Cut

Slop test results: two body sentences failed. The first, at the end of the
Retrieval-then-generation section — "That is what a disclaimer on a generative
chatbot buys and what it does not" — grades the argument without carrying a
fact, and the two sentences before it already establish the finding; cut. The
second, in the Why bookend closer — "Governments beyond New York are still
putting chatbots of this shape on their own websites, and the failure this
one produced is the one those systems can be expected to repeat" — used a
dangling "chatbots of this shape" (shape not yet named) and passive
prediction; rewrote to name the design concretely ("chatbots that generate
answers over official pages") and to make the claim what the design produces
rather than what the systems can be expected to do.

Other cut passes: the Why bookend opener started "The chatbot in this lesson
was" — variant of the recent "This lesson [verb]s" self-narration formula the
brief flags. Rewrote to lead with the subject ("MyCity Business was"), which
addresses the reader through the subject without the "in this lesson" frame
the template does not need here. In the Malhotra paragraph, the middle
sentence "Nuvalence was the integration partner on the tool" floated between
two quotes; merged as an appositive on the first mention. Rewrote the third
sentence of the mechanism paragraph — "When the token stream a model has
learned biases it toward one kind of sentence, and the retrieved passage
contains a different fact, the token stream can win" — split into two shorter
sentences with a clearer chain from distribution to bias to outcome.

Recent-pattern check on edges and display text: no comma-and independent-
clause pair in the headline; no comma triad, semicolon reversal, or suspended
question in the dek; no "By the end you will know what..." enumeration or
"You have read that..." opener in either bookend; takeaway does not resolve
with "The question was whether..." and does not close on the "That is real,
and it is what X" shape. Headings vary in build and each names the argument
step.

Voice-guide comparison: no borrowed clause from Somers, Tkacik, or Angwin
appears in the draft; the prose runs short and specific in the exemplars'
register (named actors, dated events, the mechanism at the level of the
object). Prompt-leakage check: no clause pattern from the commission or
writer brief carries through in the article; the mechanism explanation is
in the piece's own words.

Furniture: the nb-note showing the disclaimer tested against the bot is the
piece's sharpest single beat and stays. The three-row prompt/answer/law table
is doing the alignment work the draft-handoff names as the article's
contribution. No further block earns its place; no missing block would teach
the reader more than the prose already does.

## Reader

Reading the survivor straight through as a smart, widely-read reader who
knows the headlines but not the sequence: what I have that the sources alone
would not is the alignment. The bot's answers sit next to the specific city
or state law each one contradicted, and the mechanism section reads those
answers through retrieval-plus-generation — the fact was in the store, the
generator wrote past it — with the disclaimer-vs-answer exchange as the
concrete demonstration. Neither the Markup pieces nor the AP story does this
alignment or this reading. The draft-handoff original-work sentence names
exactly that contribution, and the article delivers it. The prose sits
closer to the voice-guide exemplars than to a median AI summary: sentences
are short and load-bearing, actors are named with their titles, the
mechanism arrives with the object at its center, and the takeaway is the
finding rather than a decoration on it.

Headline reread as the largest claim: the ten-Markup-staffer / Section 8
formulation is the concrete surprise and the piece defends it. Subject and
verb sit at the front; no colon subtitle, no question, no adjective triad.

## Edits

- Dek: "2,000 NYC.gov pages" -> "2,000 NYC Business pages" (both in article
  header and nb-meta JSON).
- Why bookend opener: "The chatbot in this lesson was" -> "MyCity Business
  was" to remove the "in this lesson" self-narration frame.
- Why bookend closer: rewrote "Governments beyond New York are still putting
  chatbots of this shape on their own websites, and the failure this one
  produced is the one those systems can be expected to repeat" -> "Governments
  beyond New York keep deploying chatbots that generate answers over official
  pages, and this failure is what that design can produce" — names the design
  concretely rather than dangling "shape".
- Table row 3 (tips): "Yes." -> "\"Yes, you can take a cut of your worker's
  tips.\"" — restored the full quoted bot answer from the Markup pull-quote,
  bringing row 3 into parity with the other two rows' full-quote format.
- Malhotra paragraph: merged "Rakesh Malhotra, co-founder and managing partner
  of Nuvalence, described the SBS approach as 'How do we get to yes?'
  Nuvalence was the integration partner on the tool. Malhotra added..." into
  "Rakesh Malhotra, co-founder and managing partner of Nuvalence, the tool's
  integration partner, described the SBS approach as 'How do we get to yes?'
  He added..." — one sentence removed, integration-partner fact carried as
  appositive.
- Mechanism paragraph third sentence: "When the token stream a model has
  learned biases it toward one kind of sentence, and the retrieved passage
  contains a different fact, the token stream can win" -> "The distribution
  it samples from biases it toward one kind of sentence. When that bias runs
  against a retrieved fact, the bias can win." — split for parseability;
  clearer subject in each clause.
- Rent-withholding sentence: "Asked on X whether tenants could withhold rent
  for unmade repairs, the bot answered 'no'" -> "A tenant attorney posted on
  X that the bot had answered 'no' when asked whether tenants could withhold
  rent for unmade repairs" — fixes the "queried via X" misread; the platform
  is where the exchange was posted, not where the bot was reached.
- Cut, mechanism section closer: "That is what a disclaimer on a generative
  chatbot buys and what it does not." — empty-conclusion slop that grades the
  argument without adding a step the two prior sentences did not already
  land.

## Required work

None. The writer's flagged items are recorded and do not block publication:
no signed procurement contract surfaced (cost figures stay as quoted, per
brief); the rent-stab row was correctly pulled from the table for lack of a
primary rent-stab source and the bot's rent answer remains cited to Markup
in prose; source assets would be additive rather than argument-carrying and
their absence does not weaken the piece.

## Decision

approve — the draft's central alignment and mechanism reading hold on
retest, sourcing is clean, display text is accurate after the dek fix, and
the edits above address the two slop sentences and the ambiguity in the
rent-withholding line.
