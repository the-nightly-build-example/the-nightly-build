# Commission: what-could-go-wrong/recommender-radicalization

## The argument

That engagement-optimizing recommendation algorithms systematically radicalize
their users and seal them in filter bubbles: the "rabbit hole" claim about
YouTube and the "filter bubble" claim about personalized feeds. This is a real
AI-risk argument (recommender systems are the most widely deployed machine
learning in daily life), and the lesson teaches it the way the series demands, so
the reader can judge it on the evidence rather than by who makes it.

## Structure the series requires

1. **Open with the argument at full strength.** Name who made it and what they had
   seen. Eli Pariser coined "filter bubble" (2011 book/TED talk): personalization
   narrows what you see to what you already agree with. Zeynep Tufekci's 2018 New
   York Times essay called YouTube "the Great Radicalizer," arguing its
   recommender, optimizing watch-time, pushes viewers toward ever more extreme
   content. Lay out the mechanism its careful defender would: a system trained to
   maximize engagement learns that provocative, escalating content holds
   attention, so its recommendations drift toward the extreme, and personalization
   plus homophily seals users into self-confirming feeds. The reader should
   understand why serious people believe this before reading a word against it.
2. **Test it against what real systems actually do.** Draw the sharp line between
   what has been shown in a working system and what is analogy or assertion. The
   strongest empirical work has largely failed to find a strong algorithm-driven
   rabbit hole: Hosseinmardi et al. (PNAS 2021) traced real YouTube consumption
   and found extreme-content viewing concentrated among a small set of users with
   prior preferences, not created by the algorithm for typical users; Chen, Nyhan,
   Reifler et al. (2023) found exposure to extremist channels flowed mainly from
   subscriptions and off-platform links, and that recommendations rarely sent
   uninterested users to such content; the 2020 US-election Facebook/Instagram
   studies (Science and Nature, 2023) found that chronological feeds and reduced
   algorithmic curation did not measurably reduce polarization. On filter bubbles,
   report the finding (e.g. Guess and colleagues) that algorithmic feeds are often
   more diverse than people's own choices, so the "bubble" is substantially
   demand-side. Read these primaries; get their exact designs, samples, and
   figures. Then state honestly what the evidence does show: real harm for a
   subscribed minority, documented engagement-optimization mechanics from internal
   disclosures, and the limits of studies run over short windows with platform
   cooperation.
3. **Bring it to the present and name the gap on both sides.** Who argues it now
   (regulators citing "amplification," plaintiffs, the Frances Haugen disclosures)
   and what they want done. Then check against the most recent evidence and name
   where confidence outruns proof, in both directions: the strong "the algorithm
   radicalizes ordinary users" claim outruns the causal evidence, and the
   dismissive "recommenders are harmless" claim ignores the documented mechanics,
   the affected minority, and the short observation windows.

## Required contribution

The evidence carries the studies. This piece's own work is to hold the vivid,
widely believed mechanism (engagement optimization → escalation → sealed bubble)
against the specific empirical tests built to detect it, and show the reader
exactly where each side's confidence exceeds what has been measured, so they can
hear "the algorithm radicalized him" or "that's a moral panic" and know which
part of each is supported. Leave the reader to decide how worried to be.

## Boundaries (from the series prompt)

- Work from the original documents: the papers that made the argument and the
  studies behind the headline numbers, never the commentary about them.
- Study how the field reasons about this risk without joining it or writing it
  off. Name no company as an authority; Meta and Google/YouTube are subjects.
- Distinct from covered ground. The paper already has gradual-disempowerment,
  algorithmic-monoculture, ai-persuasion, and a facebook-myanmar incident; this
  lesson is specifically the radicalization/filter-bubble argument and its
  empirical test. Link, do not re-teach, any concept an existing lesson owns (e.g.
  what "optimizing for engagement" means if a mechanics/instruments lesson covers
  it). The researcher should surface the best library links.
- Keep reported fact, estimate, and synthesis distinct. A study's finding is
  reported; a claim about the mechanism's real-world scale is an estimate;
  "confidence outruns proof here" is synthesis that must be shown from the cited
  designs.

## Source policy (what-could-go-wrong / lesson)

Floor: at least 8 sources, at least 4 primary, at least 1 secondary. Primaries:
the argument's originating documents (Pariser, Tufekci) and the empirical studies
(Hosseinmardi 2021, Chen/Nyhan 2023, the 2020 election Facebook/Instagram papers,
a filter-bubble diversity study). Read each; contested figures need the primary.
Record contradictory evidence in full in the evidence record.

## Production policy

Profile balanced. Roles run as Claude Code sub-agents using this checkout's `nb`.
Model "capable" for every stage. Actual models this run: writing-coach sonnet
(low), researcher opus (high), writer sonnet (medium), editor opus (high). No
`required` directive to deviate from.

## Recent-pattern habits not to inherit

- What-could-go-wrong openers often shape the first heading as "What Bainbridge
  saw in the control room" / "The number is the model plus the effort." Name the
  first heading for this lesson's own first step (the argument at full strength).
- Closer headings shaped "The floor labs stand on now" / "Where the same X lives"
  recur. Write the close around this lesson's own particulars (the two-sided gap)
  and vary its build.
- `spec/headlines.md` bans the comma-triad and semicolon-reversal dek molds, and
  this series' deks lean on them; write a fresh dek that commits to the specific
  find (the built-to-detect-it studies that mostly did not).

## Neighboring articles in tonight's run (keep distinct)

the-evidence/computing-machinery-and-intelligence; the-instruments/training-cost;
the-mechanics/text-to-speech-pronunciation; when-ai-breaks/amazon-recruiting.
This is tonight's only risk-argument piece.
