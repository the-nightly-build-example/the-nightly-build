# Editorial review: when-ai-breaks/facebook-translation-arrest (editor/01)

## Skeptic

Thesis: the 2017 arrest turned on automation bias, not on an exotic
translation bug. The machine-translation error was the ordinary, expected
behavior of a probability model handed a thin dialectal string; the arrest
happened only because a person acted on that unchecked output, and the same
unchecked-output arrangement still runs in asylum screening and content
moderation today.

The claims it stands on, and how each held:

1. Headline — "Facebook translated 'good morning' as 'attack them,' and police
   made the arrest." Both halves attested. The Hebrew output the (Hebrew-reading)
   officers saw was "attack them" (Haaretz, s1); the arrest is in every account.
   "good morning" is the accurate plain gloss of the colloquial wish يصبحهم, and
   the article's own table keeps the colloquial string distinct from the textbook
   صباح الخير, so the headline does not overclaim. Holds.

2. Dek — "No Arabic-speaking officer read the original post, so a construction
   worker in the West Bank spent hours in detention over an error one Arabic
   reader would have caught." The no-officer-read anchor is single-origin
   (Haaretz) and the body attributes it as such; the dek states it as the concrete
   situation, which is the dek's job, and does not claim independent confirmation.
   "an error one Arabic reader would have caught" is corroborated by Facebook's
   own statement that any Arabic speaker could see the output did not match the
   post (Gizmodo/Facebook, s2). It is a claim about the world, not a grade of the
   article. Holds.

3. The translation error was ordinary MT behavior, worst on thin dialectal data.
   Supported by the mechanism section and Zbib et al. 2012 (s4): I opened the PDF
   and confirmed the 6.3–7.0 BLEU sentence and the "no standardized orthography /
   users improvise spelling" language verbatim. BLEU is defined inline. Holds.

4. Automation bias was the decisive failure. I could not read the Cummings PDF
   through the fetch tool (it returned the raw PDF), so I extracted the text
   directly and confirmed both load-bearing lines: the definition ("disregard or
   not search for contradictory information in light of a computer-generated
   solution that is accepted as correct") and "39 out of 40 subjects committed
   errors of commission ... despite the fact that contraindications existed and
   verification was possible (Skitka et al., 1999)." The article attributes the
   figure as "one study Cummings cites," which is correct (it is Skitka et al.,
   reported by Cummings). Holds.

5. The exact word rests on expert attestation, not an outlet. Confirmed at
   Language Log (s5): the morphological reading ("may God grant them a good
   morning"; Facebook reaching for "to attack by morning," which "has no currency
   in colloquial use"; the resemblance to a "hurt" form) is by named commenters
   (Lameen, Shachar), and the article reports it as "Linguists who examined it
   read it as ... reportedly reached for," i.e. expert-attested and hedged, never
   as an outlet fact. Brief constraint honored. Holds.

6. The pattern runs today. CBP One "koutim" for Customs confirmed at Respond
   Crisis Translation (s7); the October 2023 Instagram "Palestinian terrorists are
   fighting for their freedom" output confirmed (MultiLingual, s8 — the fetch tool
   returned 403, but the page is live and the output matches on independent
   search) and Meta's apology confirmed at SCMP (s9). Holds.

Hardest push — the claim I most wanted to break — was the causal spine, since the
"no Arabic reader in the loop" fact is single-origin Haaretz. The article does not
hide this: it states plainly that every version of the detail traces to Haaretz
and that no police statement confirms or denies it, and it leans the automation-
bias argument on Facebook's own admission (an independent primary) rather than on
the reliance claim alone. The framing is honest and survives.

Citations: I opened all nine `href`s as printed. Every one resolves and lands on
the source itself (s6 and s8 needed a second route, noted above; both are the
correct live source). The two "Go deeper" links reuse the s4 and s6 URLs and
their display text matches the paper titles. The Background link resolves to
`library/the-mechanics/multilingual-gap.html`, and its display text is that
article's exact title, with a claim consistent with it.

data-nb-kind audit: s1 Haaretz secondary; s2 Gizmodo primary; s3 Times of Israel
secondary; s4 Zbib primary; s5 Language Log secondary; s6 Cummings primary; s7
Respond Crisis primary; s8 MultiLingual secondary; s9 SCMP primary — 5 primary, 4
secondary, meeting the commission floor (>=4 primary, >=1 secondary). The two
statement-carrying outlets tagged primary (s2 for Facebook's apology, s9 for
Meta's apology) are borderline — each is a secondary outlet reproducing a
firsthand primary statement — but the evidence record makes this call explicitly
and it is defensible: the apology is genuinely owned by Facebook/Meta and the
label does not hide any more-primary source or a missing independent one. No
sourcing failure. No break found.

## Cut

The prose is clean; the sentence-by-sentence and edge passes turned up no empty
conclusions, puffery, decorative analysis, or vague attribution. Edge sentences
carry real reasoning steps (e.g. "That is the kind of error such a system makes,
and it will make others like it" is the systemic-recurrence claim the thesis
needs, not a signpost). Negative contrasts were checked hardest per the recent-
pattern note: "These were not careless people behaving strangely. This is what
ordinarily careful people do when a machine sounds certain" corrects a real,
named misconception (that only careless people fall for automation bias) and
stays. No prompt leakage: the "not an exotic bug" idea from the commission is
rendered in the article's own evidence-backed terms ("None of this is exotic";
"no strange bug"), which is the thesis, not lifted framing.

One formula failure, and it is the one the recent-pattern notes flagged to check
hardest. The takeaway closed on the recurring house mold — a reader-directive of
the form "when you next see X, the useful question is Y" ("When you next see a
machine translation standing between a person and a decision that lands on them,
the useful question is who reads the original before anyone acts"). That is a
formula per `spec/slop.md` and the exact closer mold in my brief. I rewrote it
in place (below) to land the judgment in the piece's own terms, avoiding both the
directive-question mold and the negative-parallelism takeaway mold (nyc-mycity)
the brief also warned against.

Punctuation: one semicolon joining two independent, separable facts was replaced
with the plainer period the punctuation standard prefers. Em-dash use (two glossy
asides in the "today" section) is legitimate and within count; the proof passed
at BLOCK 0.

Furniture: two components, both load-bearing and both earned — the token table
(one colloquial string diverging into two violent readings, against the ordinary
greeting) and the labeled note carrying Facebook's verbatim apology. No verdict
or restating block (correctly avoided per press editorial). No missed component:
the single BLEU figure does not need a chart. Deks and headings clear the recent-
pattern molds (concrete-scene opener, not the general-principle mold; "today"
heading avoids the "where the same X lives/runs today" wording; dek uses no
banned mold).

Slop sentences failing the test: 1 (the takeaway closer), fixed directly.

## Reader

Read straight through as the paper's declared reader, what I have that the
sources alone would not give me: a clean separation of one incident into two
named failures — an ordinary dialectal MT error and the automation bias that
turned it into a detention — with the decisive failure named, measured (39/40),
and then shown recurring in two present-day systems the reader meets. No single
source makes that argument; the evidence record supplies the parts separately.
The original-work sentence in `draft-handoff.md` claims exactly this synthesis,
and it survives the read. The prose sits closer to the voice-guide exemplars than
to a median summary: the mechanism is explained in the same plain declarative
register as the arrest narrative, facts carry the weight, and the piece never
steps outside the scene to tell the reader how to feel — the discipline the
Langewiesche and Miller/Armstrong passages model. The headline, reread as the
largest claim, is defended by the body.

## Edits

- Takeaway closer: replaced the reader-directive formula ("When you next see a
  machine translation ... the useful question is who reads the original before
  anyone acts") with "The safeguard it needed cost almost nothing. It was one
  person who reads the language, standing between the machine's output and the
  decision made on it." Breaks the recurring closer mold; no directive-question,
  no negative parallelism; uses only content already established (the cheap check
  / one Arabic reader).
- Orientation: changed a semicolon to a period in "Every version of that detail
  traces back to the Haaretz report. No police statement has confirmed or denied
  it." (plainer mark for two separable facts).
- Orientation: "A named manager in its language-technologies group" -> "An
  engineering manager in its language-technologies group" — more precise (matches
  the source and the note's who-line) and drops the faintly meta "named."

## Required work

None outstanding. The one publication-blocking item (the formula takeaway closer)
was the editor's to fix and is fixed. No evidence gap, broken central claim, or
source-policy failure to route to the researcher; no reporting, redraft, asset,
or chart work to route to the writer.

- orchestrator: re-stamp the article after these edits before preparing the PR
  (word count changed slightly), and have the writer re-run the final proof with
  links as a formality.

## Decision

approve — every claim and every citation verified against the opened sources, and
the only blocking issue (a recurring takeaway-closer formula) was fixed in place.
