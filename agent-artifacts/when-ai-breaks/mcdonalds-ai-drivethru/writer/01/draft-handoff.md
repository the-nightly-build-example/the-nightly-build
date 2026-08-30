# Draft handoff: when-ai-breaks/mcdonalds-ai-drivethru (writer 01)

## Original work

The article turns the evidence's scattered claims into a single argument built
around the one figure McDonald's never published: it uses the Whisper
noise-robustness curve to explain why drive-thru accuracy landed where reporting
placed it, and it keeps the two human-in-the-loop shapes cleanly apart (McDonald's
in-restaurant crew correcting roughly one order in five, versus Presto's
SEC-documented remote agents entering ~70% of orders from the Philippines and
India). That reframing and that distinction are the work; neither is stated in the
evidence record.

## Proof result

`./nb check ... --series when-ai-breaks --library /home/user/library-checkout`
(links included, after `nb stamp`): **BLOCK: 0**, verdict PUBLISHABLE. All source
links resolve. Stamped words=1965, reading_minutes=9, sources=10 (4 primary:
PR Newswire/McDonald's, IBM joint statement, Whisper paper, SEC order 33-11352;
6 secondary).

Warning intentionally left (1):
- `W-SENTENCE-DENSITY` on the "Why this matters" opener's last sentence (49 words,
  2 clause joins). It is a controlled sentence: a colon introducing the three-part
  preview of the body's three arcs (why the drive-thru is hard for ASR / what a
  company does and does not disclose / how much automated ordering is still a
  hidden human), each resolved in the takeaway. Splitting it would break the
  setup-and-resolution pairing the template asks the two bookends to hold. It reads
  cleanly aloud. Left as written.

## Notes on the evidence flags (all honored)

- The SEC ~70% finding is presented only as Presto Automation (labeled a
  competitor in prose, in the note's attribution line, and in the source note), never
  merged with McDonald's crew-correction shape.
- The ~85% accuracy is attributed to reporting (Engadget), stated as never
  officially published by McDonald's or IBM. It appears in the dek as "reporting
  guessed about 85 percent."
- The failure clips are presented as user-posted videos with no verifiable
  original source, establishing that the behavior was filmed and went viral, not an
  audited failure rate. The origin-unverified "260 nuggets" figure was not used; the
  two mainstream-carried clips (bacon-on-ice-cream; ketchup/butter/multiple-ice-cream)
  are the concrete examples.
- The disputed cause is presented from both sides via a position card for
  McDonald's stated framing, weighed against the error record and the sub-95% peer
  bar, closing on what one measured figure would settle. No verdict-note closer was
  used (press rule: the takeaway bookend lands the judgment).

## Furniture / asset

- Timeline (corporate chronology), numbered steps (the three-stage pipeline),
  position card (McDonald's stated framing), one note (the SEC finding on Presto),
  and one source asset.
- Source asset: `mcdonalds-ai-drivethru/asset-1.png`, captured with `nb asset pdf`
  from Whisper Figure 5 (page 8, WER vs SNR under white noise and pub noise), model
  legend cropped out per the evidence's crop guidance, both axes and units kept.
  Inspected directly; clean and legible. Cited to source 6 with locator, url, and note.
- The whisper lesson is linked in prose (Background band and the pipeline's step 1),
  not as a numbered source, per the press rule to link taught ground rather than
  re-teach it. The Whisper paper itself is a separate numbered primary (source 6)
  supporting the specific noise figure.

## Dropped from the record (with reason)

- CNBC's peer survey (Wendy's FreshAI / Yum-Taco Bell figures) was cut. The
  researcher could not open it firsthand (HTTP 403), so per "cite only what you have
  read" and to keep the link check clean, the closing section relies on the two
  peer sources the researcher did read: the SEC order (Presto) and Restaurant Dive
  (White Castle / SoundHound). Both are named systems in use today, which satisfies
  the series' "where the weakness lives today" close.

## Open question

- None blocking. One optional editorial call for the editor: the closing section
  now names two current systems (Presto's documented past, White Castle/SoundHound's
  present) rather than the broader Wendy's/Yum roster, because those figures traced
  only to the blocked CNBC source. If broader peer coverage is wanted, it needs a new
  researcher artifact with a readable source for the Wendy's/Yum deployments.
