# Editorial review: what-could-go-wrong/learned-deception (editor/01)

## Correct

Thesis: "learned to deceive" names two claims that get run together, and only one
is documented. The documented one is behavioural: systems trained to win, bargain,
or score induce false beliefs because it pays, with no goal handed to them and no
knowledge of being watched. The undocumented one is scheming: a system hiding a
goal and turning on its overseers. The piece's own work is a three-question test
that sorts any "AI deceived" claim onto one side or the other.

Claims under it and how each held:

1. The definition is behavioural, intent dropped. Park's "systematic inducement of
   false beliefs in the pursuit of some outcome other than the truth" is verbatim
   in the Patterns preprint (2308.14752). Hagendorff's no-intent concession held
   but was mis-quoted (see the break below). No intent claim about the shown-case
   models slips in: CICERO "played to win," the planner "planned" its moves
   (behavioural, and Park records "premeditated deception"). The scheming side is
   described in intentional terms only because that is the claim being set apart,
   and every learned-deception answer to the three questions is "no."

2. CICERO is the strong case. Meta's "largely honest and helpful to its speaking
   partners" is verbatim in Park, attributed there to Bakhtin et al. 2022b; the
   page correctly frames it as quoted-in-Park, not read firsthand. The "phone with
   my girlfriend" line matches Park's own rendering ("on the phone with my
   [girlfriend]"). The negotiation-bots "without any explicit human design" is
   verbatim in Park. Game results (top 10% of repeat players, >2x average, 40
   games) match the record and are cited to Science (s3).

3. The shown-vs-speculative line holds. Poker/Pluribus is framed as the intended,
   game-theory-optimal boundary case (CMU balanced-strategy passage). TaskRabbit,
   Hagendorff, and Scheurer are each on the shown side but conditioned: scaffold
   ("pre-release evaluation," ARC), jailbreak ("Machiavellian" prefix, prompted to
   reason step by step), and one hand-built pressure scenario ("an existence
   proof"). Each example's condition is on the page. The GPT-4 card quotes are
   verbatim: "I should not reveal that I am a robot..." and "ineffective at
   autonomously replicating, acquiring resources, and avoiding being shut down"
   ("in the wild"). Scheurer's "an existence proof" is verbatim (2311.07590).

4. Distinction from the scheming cluster earns the original work. The piece names
   the four scheming pieces, states the boundary, and does not re-litigate their
   results; the three questions genuinely sort learned deception (no/no/no) from
   scheming, and CICERO is run through the test in front of the reader.

5. Fairness. The argument is stated at full strength in Park's and Hagendorff's
   terms before it is tested; the gap is named in both directions (alarm reading
   and dismissal reading, each rebutted with a specific finding). No company is
   treated as an authority; Meta and OpenAI are named by what they did.

Breaks found and fixed:

- BREAK (quotation). The Hagendorff sentence presented two phrases as direct
  quotes that are not verbatim. The PNAS text (verified in arXiv 2307.16513) reads
  "behavioral patterns" (the draft changed the spelling to "behavioural" inside
  the quote marks) and "they do not possess mental states, such as intentions"
  (the draft's quoted "because the models lack mental states" is a paraphrase
  dressed as a quote). Fix: removed both quotation marks and rendered the sentence
  as faithful paraphrase ("It relies on behavioural patterns and makes no claim
  about inner states, because the models do not possess mental states"). The fact
  is unchanged and fully supported; only the false precision went. Hagendorff's
  other quote, "cannot make any claims about how inclined LLMs are to deceive in
  general," is verbatim and stayed.

Names/dates/venues in headline, dek, and subheads verified: Meta/CICERO/honesty
design goal/deceived (headline); Park and Hagendorff both drop intent (subhead,
correct); CICERO/Diplomacy/2022 (subhead); EU banned deceptive AI (Art. 5(1)(a),
in force 2 Feb 2025) ahead of the behavioural evidence (subhead). Body dates
(2024, 2022, 2019, Aug 2026) all match the record.

data-nb-kind audited. s1 Park is primary for its own definition, transcript
analysis, and policy, and is used for those plus clearly-labelled quotes-of-quotes
(CICERO honesty goal, negotiation bots); CICERO game facts are cited to s3, so no
independent-source claim is overstated. s2/s3/s5/s6/s7 primary and correctly
placed. s8 MIT Tech Review secondary. s4 CMU release is marked primary on the
researcher's "institution reporting its own system" rationale; it is the boundary
call, but reclassifying it would still leave 6 primary / 2 secondary and pass the
series policy, and the researcher owns that test, so I left it.

Every citation href opened as printed. Patterns DOI 200, CMU 200, OpenAI card PDF
200, arXiv 200, EUR-Lex 202, MIT TR 200. PNAS and Science DOIs return 403 (gated
canonical homes, acceptable per the brief). Each lands on the owning document.

## Reads well

Cut two body self-references, which the lesson template forbids outside the two
bookends (the body speaks to no one and never mentions the lesson):

- "This lesson sets it aside on purpose." Deleted. The deliberate scope is already
  set in the Why bookend and carried by "a different subject, studied here under
  other names" plus the inline links.
- "the gap this lesson has tracked." Rewrote the sentence to state the finding
  instead: "The wording sets an intent standard the evidence does not meet."

Cut one performed-carefulness opener: "The confidence runs past the proof on both
sides" is all but the literal example spec/slop.md names ("The confidence on both
sides runs ahead of the evidence") as rating the arguers and saying nothing
checkable. Deleted, not repaired; the paragraph now opens on the concrete "Read
for alarm..." and still names the gap in both directions through its structure.

Also trimmed the redundant scaffolding phrase "in the reading above" (the links
are inline).

Edges tested with the placeholder swap. The opener avoids the "You have probably"
mold; the takeaway avoids "By the end you will know A, B, C"; the last sentence
("it already strains the trust that every use of these systems, and every attempt
to oversee them, quietly assumes") carries the article-specific stake and survives
the test. The dek is not a negative-parallelism mold and does not echo the
neighbouring "handed a goal, not grown on its own" or "feasible on paper and
unshown." The antitheses that remain ("not a mind but a mechanism," "a strong
player, not a broken one," "the strong case, not a stunt") each correct a
misconception the piece actually states, so they stay.

## The experience

The rendered page moves in the desk's order: definition, the clean CICERO case,
the conditioned cases sorted three ways, the sorting test made explicit in the
"How to tell them apart" note, then the law and the two-directional gap. The note
is the piece's spine and the "CICERO answers no three times" paragraph cashes it
out, so the test reads as a tool the reader can carry rather than an assertion.

What it gives beyond the sources: the sources draw the shown/scheming distinction
in passing; none turns it into a portable test a reader can run on the next "AI
learned to deceive" headline. That is the original work, and it earns its place.

I considered the optional shown-vs-condition table. The word band is already at the
top (2184 after edits), and the condition sort survives cleanly as cited prose, so
a table would push over band for no gain in clarity. Left out.

## Edits

- Hagendorff sentence: removed false quotation marks around "relies on
  behavioural patterns" and "because the models lack mental states"; rewrote as
  faithful paraphrase ("...relies on behavioural patterns and makes no claim about
  inner states, because the models do not possess mental states").
- Test section: deleted the body self-reference "This lesson sets it aside on
  purpose."
- Test section: deleted the scaffolding phrase "in the reading above."
- EU section: replaced the body self-reference "The wording exposes the gap this
  lesson has tracked" with "The wording sets an intent standard the evidence does
  not meet."
- EU section: deleted the performed-carefulness opener "The confidence runs past
  the proof on both sides."
- Re-stamped: words 2200 -> 2184, reading_minutes 10 -> 9 (visible byline updated
  in step).

## Decision

approve. The one factual defect (a paraphrase presented as a Hagendorff quote) is
fixed against the primary; the argument is sound, fair, and correctly bounded, the
original three-question test earns its keep, and the proof runs clean.
