# Commission: the-evidence/backpropagation

## Assignment

Read the 1986 document that taught the field to train multilayer neural
networks: Rumelhart, Hinton, and Williams, "Learning representations by
back-propagating errors," *Nature* 323 (9 October 1986). The companion chapter
in the *Parallel Distributed Processing* volumes (1986) is the same authors'
longer treatment and is fair game as the same primary work; cite the version a
claim actually comes from.

This is a lesson on The Evidence: read a famous document so the reader knows what
it actually said. State what it is, who wrote it, and why it became famous. Walk
through what it actually did: the learning rule it generalized, the experiments
it ran, the tasks it ran them on, and the numbers it reported. Show the scale
honestly. These were small networks on hand-built toy problems, trained by
repeated sweeps on hardware nothing like today's. Then bring it to the present:
backpropagation is the engine under essentially all deep learning now, and the
paper is routinely miscredited and misread. Say plainly where today's telling
does not match what the 1986 document showed.

## The gap this closes

The reader has met the modern machinery in the library already, and never the
document that made it trainable. Nearby lessons cover pieces adjacent to this one
without being it: `the-mechanics/gradient-descent` teaches the optimization step,
`the-evidence/adam-optimizer` an optimizer, `the-evidence/dropout` and
`batch-normalization` later training tricks, `the-evidence/alexnet` the 2012
result that vindicated the approach. None reads the backpropagation paper itself.
Link `the-mechanics/gradient-descent` at first use rather than re-teaching the
gradient; treat `alexnet` as the later vindication to point at, not to retell.

## Required contribution

Separate what the 1986 paper demonstrated from what it is remembered for. Two
things the record supports and the usual telling blurs:

- **Priority.** The paper did not invent the algorithm. Reverse-mode
  differentiation and the chain-rule procedure predate it (e.g. Linnainmaa 1970;
  Werbos 1974; earlier control-theory work). The paper's own contribution was to
  show the procedure learns useful *internal representations* in the hidden
  units, and to make it stick in the field's memory. The researcher should
  establish the priority record from primary sources and record where the 1986
  authors themselves credited predecessors.
- **Scale.** Give the actual size of the demonstrations (network sizes, the toy
  tasks such as symmetry detection and the kinship/family-tree problem, the
  number of training sweeps, the compute). Anchor it to something the reader can
  scale. The paper also stated its own limits plainly, including local minima
  and biological implausibility; report those in the paper's words, and note what
  later work said about the local-minima worry at scale.

The article earns its place by giving the reader the size of the foundation under
a claim they hear as settled, and by letting them tell the document apart from
the legend that grew around it. Do not turn the priority point into a debunking:
the paper's importance is real, and the lesson is what kind of importance.

## Sources

Floor (from `nb source-policy`): at least 6 sources, at least 3 primary, at least
1 secondary. Primary here means the document that owns the claim: the 1986 Nature
paper and the PDP chapter for what the paper did and said; the predecessor
documents (Linnainmaa, Werbos, and earlier) for priority; later primary results
(e.g. the saddle-point / local-minima work) for the correction. Historical
retrospectives and reporting are secondary and carry context, never a contested
figure. Every number that anchors the argument comes from the primary that owns
it. Read the actual papers, not summaries of them.

## Template and metadata

Template: `lesson`. Descriptive `nb-meta` tags (writer sets them, 4-6, lowercase
hyphenated), drawn from the finished piece; candidates: backpropagation,
neural-networks, deep-learning, hinton, distributed-representations. Date
2026-09-21. `harness` "claude-code"; `model` the writer's actual served model.

## This run's neighbors

Four other lessons publish tonight, all distinct subjects: `the-instruments/
comet-score`, `the-mechanics/false-premise-questions`, `what-could-go-wrong/
negative-side-effects`, `when-ai-breaks/chatgpt-data-leak`. No shared angle to
deconflict beyond the gradient link noted above.

## Recent shapes to break (habits, not rules)

From the last several The Evidence lessons (e.g. flamingo, alphastar): a body
that runs orientation, then mechanism, then a "grade the famous claim" section
built as myth-versus-reality, and closes on a "did not become the field's choice"
reframe. The dek mold "everyone remembers X, but actually Y" recurs. Let this
piece find its own order and its own last section; do not reserve a penultimate
"the myth, corrected" slot by reflex if the body already did that work. These are
patterns to avoid inheriting, not structure to impose.

## Production policy (actual)

`nb production-policy` returns profile `balanced`, model tier `capable`, no
`required` directive. Resolved for this run's isolated subagents: researcher
Opus 4.8 (high), writing-coach Sonnet (low), writer Opus 4.8 (medium), editor
Opus 4.8 (high). Efforts are advisory; recorded here as the run's actual choices.
