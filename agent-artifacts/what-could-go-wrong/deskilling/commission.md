# Commission: what-could-go-wrong/deskilling

## Assignment

Teach the argument that automating a task erodes the human skill for it, so the
people meant to supervise or take over from the machine can no longer do so, and
the automation ends up more dangerous the better it gets. Present it at full
strength, test it against real systems, and bring it to the present. This is the
"ironies of automation" argument applied to AI.

Template: lesson. Series: What Could Go Wrong (one risk argument per lesson,
judged on its merits). Reader: smart, widely read, new to this subject.
Publication date: 2026-09-14.

## The argument, and how to handle it

1. Steelman it first. The canonical statement is Lisa Bainbridge, "Ironies of
   Automation" (1983): automating the easy parts of a job leaves humans the
   hardest part (monitoring and rare takeover) while stripping the practice that
   made them competent at it. Name Bainbridge and what she had seen (process
   control), and lay out the reasoning at its most careful.
2. Draw the sharp line. What is already shown in working systems versus what is
   analogy about AI systems that do not exist yet. The shown side is strong and
   old: aviation automation and manual-flying skill decay (FAA/industry studies,
   the automation-dependency findings after specific accidents), and controlled
   studies of dependence on tools (navigation, clinical decision support,
   spelling/arithmetic aids). The reader must see which claims rest on measured
   deskilling and which are forecast.
3. Bring it to the present. Who makes this argument now about AI (coding
   assistants and the erosion of debugging skill, students and writing,
   radiologists and diagnostic automation), what they want done, and what the
   most recent evidence actually shows. Where confidence outruns proof, in
   either direction, name the gap. Name no company as an authority; leave the
   reader to decide how worried to be.

## Boundaries and dedupe

- Not automation bias. `what-could-go-wrong/automation-bias` owns over-trusting a
  specific automated output. Deskilling is the erosion of the underlying human
  capability over time. Distinguish them and link automation-bias in Background.
- Not technological unemployment (`.../technological-unemployment`): that is
  about jobs and labor share, not skill decay in people still doing the job.
- Not gradual disempowerment (`.../gradual-disempowerment`): that is loss of
  collective control across institutions. Deskilling is individual/organizational
  competence loss. Link where a reader might conflate them; do not re-argue them.

## Neighbors in tonight's edition

None overlapping. `when-ai-breaks/gpt-4o-sycophancy` and `the-mechanics/hedging`
share no argument with this.

## Sources

Floor: at least 8 sources, at least 4 primary, at least 1 secondary. URLs must
resolve. Work from original documents, not commentary: Bainbridge (1983) is the
controlling primary. Additional primaries: aviation human-factors studies on
manual-flying-skill decay and an accident report where automation dependence was
a named factor; a controlled study of tool dependence (navigation or clinical
decision support); recent primary studies or preprints measuring AI-assistant
effects on skill or on unaided performance. The test-against-real-systems section
lives or dies on measured evidence; cite the measurement, and mark forecasts as
forecasts.

## Production policy (balanced profile; none required)

- researcher: effort high, model claude-opus-4-8
- writing-coach: effort low, model claude-sonnet-4-5
- writer: effort medium, model claude-opus-4-8
- editor: effort high, model claude-opus-4-8

## Recent shapes to break (do not inherit)

Recent What Could Go Wrong pieces run: steelman, then a "what deployed systems
actually show" turn, then present-day. Keep the beat, but name the headings in
this piece's own nouns and vary how they are built. Avoid the negative-
parallelism heading mold ("Every worrying behavior so far was drawn out, not
selected") and the comma-plus-"and" two-clause heading. The dek should commit to
a stance, not pose a suspended question.
