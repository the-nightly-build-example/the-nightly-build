# Commission: when-ai-breaks/biden-deepfake-robocall

## The incident

Two days before the January 2024 New Hampshire primary, thousands of voters got a
robocall carrying an AI-cloned voice of President Biden telling Democrats not to
vote until November. A political operative had commissioned it; the clone was made
cheaply with a commercial voice-generation tool. It left an unusually complete
record: a state criminal case, an FCC enforcement action, a carrier settlement,
and an FCC ruling that AI-voice robocalls are illegal.

## Angle

Tell it in order, named and dated: what the system was (a commercial
voice-cloning/text-to-speech tool, used to imitate a specific real person), what
was done with it (a robocall built to suppress primary turnout), who was affected
and who was responsible (name the operative, the carrier that transmitted it, the
tool used, and the sums), and what authorities did afterward (the state charges,
the FCC's fine and its ruling, the carrier's settlement). Then explain why this
class of system makes the harm easy: a few seconds of a public figure's audio and
an off-the-shelf model now produce a convincing clone for a trivial cost, teaching
the missing piece on the spot — what voice cloning is and why it is cheap and
convincing now, without drifting into model internals. Close where the same
weakness lives today, in systems the reader meets: scam calls that clone a
relative's voice, and synthetic audio in elections and fraud.

## What it teaches (short, complete)

1. The incident in order, from the record: the operative, the carrier, the tool,
   the dates, the sums, the charges, and the FCC ruling.
2. Why voice cloning makes this cheap and convincing: what a modern voice model
   needs (a short sample) and produces, taught at the level the incident requires.
3. Where the same ease-of-cloning weakness recurs now — voice-clone scams and
   synthetic audio in fraud and elections — and what the legal response so far does
   and does not reach.

## Boundaries

- Work from the record: the FCC's orders and ruling, the state charging documents,
  the carrier settlement, and reporting that held up. Where a detail is disputed,
  give the strongest account of each side and say what would settle it.
- Teach only enough mechanism to explain the failure; do not turn it into a
  general generative-models lesson. `nb history --library` and LINK published
  neighbors rather than re-teach: candidates the-mechanics/image-generation (how
  generative synthesis works), when-ai-breaks/mata-v-avianca and
  when-ai-breaks/gemini-image-generation (synthetic-media harm and response).
- Name people, companies, and dates.

## Neighbors in tonight's edition (avoid overlap)

the-evidence/foundation-models, the-instruments/tau-bench,
the-mechanics/length-control, what-could-go-wrong/model-collapse.

## Source policy

Template minimum 8 sources: at least 4 primary, at least 1 secondary. Primary: the
FCC documents (the declaratory ruling that AI voice is covered, the Notice of
Apparent Liability / forfeiture, the carrier consent decree), the state charging
documents or attorney-general releases, and any filed primary material. Reporting
that held up is secondary; a contested figure needs the primary.

## Production record

Series production policy: balanced profile, model tier `capable` for every stage,
none `required`; efforts writing-coach low, researcher high, writer medium, editor
high. Roles run as isolated subagents on this harness's capable-tier model;
effort set to policy where settable, else harness default. No `required` directive
traded down. In nb-meta set `harness` to `Claude Code` and `model` to `capable`
(production tier; specific model identifier kept out of the published article per
harness policy). The writing-coach guide here was reused from a same-series
sibling lesson; take its craft and register, not its subject.
