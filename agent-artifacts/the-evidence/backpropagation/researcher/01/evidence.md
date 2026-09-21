# Evidence: the-evidence/backpropagation (01)

The record supports the commission on both prongs from the primaries themselves. On
scale, the 1986 Nature paper and the PDP chapter both give exact network sizes,
task sizes, and sweep counts, and they are small: a 6-2-1 symmetry detector trained
for 1,425 sweeps over 64 patterns, a five-layer family-tree net trained on 100 of
104 triples for 1,500 sweeps, XOR solved in a few hundred to a few thousand pattern
presentations, an 8-3-8 encoder, a 4-bit parity net. On priority, the predecessor
primaries are firsthand: Linnainmaa (1976, and the 1970 thesis it publishes) owns
the reverse accumulation of derivatives through an arbitrary computation, and Werbos
(1974) owns "dynamic feedback," a general technique for computing derivatives cheaply
for steepest descent. The load-bearing priority finding comes from the 1986 documents
read against themselves: Rumelhart, Hinton, and Williams present the procedure as
"new," and they credit only their contemporaries (Parker 1985, Le Cun 1985) and the
Widrow-Hoff delta rule (1960); neither the Nature paper nor the PDP chapter cites
Werbos or Linnainmaa. The record is thin in three places, all recorded below: the
primaries state no hardware, wall-clock time, or FLOP count, so any compute anchor
must be built from parameter and pattern counts, not invented; Werbos's 1974 thesis
frames its method for social-science statistics and mentions neural nets only in
passing, so it is a weaker "backprop for neural networks" primary than its reputation
implies; and the Linnainmaa-as-backpropagation reading is a later interpretation by
scholars in the field, not language in Linnainmaa's own rounding-error paper.

The evidence complicates, but does not undermine, the commissioned angle. Two
cautions for the editor, both sourced: the 1986 authors did not claim sole
invention, so the "miscredit" belongs to later popular memory rather than to the
paper's own text; and the later local-minima result (Dauphin et al. 2014) largely
vindicates the paper's empirical claim that poor local minima rarely trap learning,
while reframing the mechanism as saddle points. The correction is to the paper's
explanation, not to its observation.

## Sources

```text
URL:         https://www.nature.com/articles/323533a0
Open copy:   https://www.cri.minesparis.psl.eu/people/silber/cours/2025/nlp/bib/RumelhartDE1986.pdf
Kind:        primary. The document that owns the claims about what backpropagation
             is and what the 1986 demonstration did; authored by the three people
             who ran it. The nature.com page is gated (303 to an auth endpoint);
             the full four-page text was read against the openly hosted facsimile.
Establishes: The learning rule, its equations, the two headline demonstrations
             (symmetry, family tree), their sizes and sweep counts, the paper's
             stated limits, and the paper's own credit to predecessors.
Affiliation: As printed, David E. Rumelhart and Ronald J. Williams, Institute for
             Cognitive Science, University of California, San Diego, La Jolla;
             Geoffrey E. Hinton, Department of Computer Science, Carnegie-Mellon
             University, marked as the corresponding author. The masthead prints
             "Pittsburgh, Philadelphia 15213"; CMU is in Pittsburgh, Pennsylvania
             (ZIP 15213), so this is a typo in the original. Do not carry
             "Philadelphia" forward.
Paraphrase:  Rumelhart, Hinton, and Williams (Nature 323, 533-536, 9 October 1986)
             describe "a new learning procedure, back-propagation, for networks of
             neurone-like units" that adjusts connection weights to minimize the
             squared difference between actual and desired output, so that hidden
             units "come to represent important features of the task domain." Units
             use a logistic output y_j = 1/(1+e^-x_j) on a linear input x_j = sum_i
             y_i w_ji. Total error E = (1/2) sum_c sum_j (y_j,c - d_j,c)^2 is
             minimized by gradient descent; derivatives are computed in a forward
             pass and a backward pass that propagates dE/dy from the output layer
             down. Weight change is Delta_w = -epsilon dE/dw, improved by a momentum
             term Delta_w(t) = -epsilon dE/dw(t) + alpha Delta_w(t-1), alpha between
             0 and 1. The symmetry net (6 inputs, 2 hidden units, 1 output) learned
             in 1,425 sweeps through all 64 input vectors, epsilon=0.1, alpha=0.9,
             with the two weights on each side of the midpoint settling into a 1:2:4
             ratio. The family-tree net is five layers: 24 person-1 inputs plus 12
             relationship inputs, each group feeding its own 6-unit layer, then a
             central layer of 12, a penultimate layer of 6, and person-2 outputs;
             it was trained on 100 of the 104 possible triples for 1,500 sweeps and
             generalized to the four held-out triples, with hidden units coming to
             encode nationality (English/Italian), generation, and family branch.
Locators:    Abstract and body, p.533; symmetry Fig 1 and caption, p.534; equations
             (1)-(9) pp.533-535; family tree Figs 2-4 and text, pp.534-535; limits
             and predecessor credit, pp.535-536; references, p.536.
Quote:       "The most obvious drawback of the learning procedure is that the
             error-surface may contain local minima so that gradient descent is not
             guaranteed to find a global minimum. However, experience with many
             tasks shows that the network very rarely gets stuck in poor local
             minima." (p.535)
             "The learning procedure, in its current form, is not a plausible model
             of learning in brains." (p.536)
             "Variants on the learning procedure have been discovered independently
             by David Parker (personal communication) and by Yann Le Cun." (p.535)
```

```text
URL:         https://stanford.edu/~jlmcc/papers/PDP/Volume%201/Chap8_PDP86.pdf
Citation:    Rumelhart, Hinton & Williams, "Learning Internal Representations by
             Error Propagation," in Rumelhart & McClelland (eds.), Parallel
             Distributed Processing, Vol. 1: Foundations (MIT Press, 1986),
             pp. 318-362. Gated publisher page: direct.mit.edu chapter 189417.
Kind:        primary. The same authors' longer treatment of the same work, hosted
             as a full facsimile by PDP co-editor J. L. McClelland. Owns the
             algorithm's name, the derivation, and the toy-problem results the
             Nature letter had no room for.
Establishes: The rule's name ("the generalized delta rule"); the full derivation;
             the momentum term and its typical value; XOR, parity, and encoder
             results with sizes and presentation counts; the local-minima evidence
             at fine grain; and, again, credit only to Widrow-Hoff, Parker, and
             Le Cun.
Paraphrase:  The chapter names the procedure "the generalized delta rule" (p.322)
             and derives it for feedforward nets of "semilinear" units. It states
             the delta rule is "the variation due originally to Widrow and Hoff,
             1960" and that "Parker (1985) has independently derived a similar
             generalization, which he calls learning-logic. Le Cun (1985) has also
             studied a roughly similar learning scheme" (p.322). The momentum rule
             is Delta_w_ji(n+1) = eta(delta_pj o_pi) + alpha Delta_w_ji(n), and "in
             most of our simulations alpha was about 0.9" (p.330). XOR with one
             hidden unit was solved after 558 sweeps at eta=0.5 (p.331); across
             "hundreds" of XOR runs the system hit a local minimum in "only two
             cases," both the two-hidden-unit version, one reached after 6,587
             presentations at eta=0.25, and a footnote adds that at eta=0.5 or above
             the system escapes it (pp.331-332). Chauvin's study gave presentations
             to solve XOR as P = 280 - 33 log2 H, about 245 for two hidden units
             down to about 120 for 32 (p.333). A 4-bit parity net with four hidden
             units solved all 16 patterns after 2,825 presentations at eta=0.5
             (p.335). The 8-3-8 encoder maps eight patterns through three hidden
             units (pp.335-337). A recurrent net with 5 inputs, 30 hidden units, and
             3 outputs learned 25 sequences in 260 sweeps (pp.358-359). The
             conclusion answers Minsky and Papert's 1969 pessimism directly.
Locators:    Rule name and predecessor credit, p.322; derivation, pp.322-328;
             logistic and its derivative o(1-o), p.329; momentum, p.330; XOR,
             pp.330-334; parity, pp.334-335; encoder, pp.335-338; sequences,
             pp.358-359; conclusion, pp.361-362.
Quote:       "The main empirical contribution is to show that the apparently fatal
             problem of local minima is irrelevant in a wide variety of learning
             tasks." (p.324)
             "In short, we believe that we have answered Minsky and Papert's
             challenge and have found a learning result sufficiently powerful to
             demonstrate that their pessimism about learning in multilayer machines
             was misplaced." (p.361)
```

```text
URL:         https://link.springer.com/article/10.1007/BF01931367
Open copy:   https://papers.baulab.info/papers/also/Linnainmaa-1976.pdf
Kind:        primary. Seppo Linnainmaa owns the reverse-accumulation-of-derivatives
             method here; the paper publishes results from his 1970 University of
             Helsinki master's thesis. Primary for the priority claim that the core
             procedure predates 1986. Springer page gated; read against the open
             facsimile.
Establishes: That a general method for propagating derivatives backward through the
             steps of an arbitrary numerical algorithm was in print by 1976 (thesis
             1970), and that it was framed as rounding-error analysis, with no
             mention of neural networks.
Paraphrase:  "Taylor Expansion of the Accumulated Rounding Error," BIT 16 (1976),
             146-160, treats a computation as a sequence u_1,...,u_N in which each
             step is an operation on earlier values, and expands the accumulated
             error of the result as a Taylor series in the local errors. Its
             first-order coefficient c_{i,p} "is the partial derivative of u_i with
             respect to u_p" and does "not depend on the algebraic sequence" used to
             produce u_i (eq. 10, p.149). Computing these coefficients requires
             saving "some information on all the operations of the process," whose
             storage "can be prohibitively large," and the paper discusses reducing
             it. This is reverse-mode automatic differentiation: the sensitivity of
             one output to every input, obtained by working back over a stored trace
             of the forward computation. The paper never mentions neural networks or
             learning; the "this is backpropagation" reading is later scholars'.
Locators:    Abstract and introduction, p.146; sequence-of-operations setup and
             local error, p.147 (eqs. 1-5); Taylor coefficients as partial
             derivatives, pp.148-149 (eqs. 8-10); storage cost, p.146.
Quote:       "the coefficient c_{i,p} in (8) is not dependent on the algebraic
             sequence which has been used to produce u_i. In fact, due to the
             linearity of (3), each coefficient c_{i,p} is the partial derivative of
             u_i with respect to u_p." (p.149)
```

```text
URL:         https://gwern.net/doc/ai/nn/1974-werbos.pdf
Citation:    Paul J. Werbos, "Beyond Regression: New Tools for Prediction and
             Analysis in the Behavioral Sciences," Ph.D. thesis, Committee on
             Applied Mathematics, Harvard University, August 1974. Reprinted in
             Werbos, The Roots of Backpropagation (Wiley, 1994).
Kind:        primary. Werbos owns the "dynamic feedback" / "ordered derivative"
             method described in the thesis. Primary for the priority claim, and for
             the honest limit that the 1974 statement is general and statistical,
             not neural-network-specific.
Establishes: That a general backward method for computing derivatives cheaply, for
             use in steepest descent, was in a 1974 doctoral thesis, twelve years
             before Nature; and that the thesis frames it for fitting nonlinear and
             dynamic statistical models, with brains named only as an analogy.
Paraphrase:  The thesis presents "dynamic feedback," which the author's own synopsis
             calls "essentially a technique for calculating derivatives
             inexpensively, for use with the classic method of steepest descent"
             (p.xv). The table of contents lists a section "The Ordered Derivative
             and Dynamic Feedback" (II-82) and "Nonlinear Regression and Dynamic
             Feedback" (II-15). The stated goals are to fit models to data more
             cheaply, applied to ARMA time series and "measurement-noise-only"
             models; the method's value for "the complex information-processing
             problems faced by human societies and by human brains" is raised as an
             analogy in the summary (p.xvi), not developed as a neural-network
             training procedure. The explicit neural-network application is a
             preliminary passage only; the fuller neural application is later Werbos
             work, not this thesis.
Locators:    Title page (i); synopsis, pp.xiii-xvi (esp. "dynamic feedback ...
             calculating derivatives inexpensively," p.xv); general summary, p.I-1;
             contents listing the ordered-derivative section, pp.v-vi.
Quote:       "'Dynamic feedback' is essentially a technique for calculating
             derivatives inexpensively, for use with the classic method of steepest
             descent." (p.xv)
```

```text
URL:         https://arxiv.org/abs/1406.2572
Also:        https://proceedings.neurips.cc/paper_files/paper/2014/hash/04192426585542c54b96ba14445be996-Abstract.html
Kind:        primary. Dauphin, Pascanu, Gulcehre, Cho, Ganguli, and Bengio own this
             result; it is the later primary the commission asks for on the
             local-minima worry at scale (NIPS 2014).
Establishes: That in high-dimensional non-convex error surfaces the dominant
             obstacle is saddle points, not poor local minima, and that local minima
             are rare and cluster near the global minimum in error, tested on neural
             networks.
Paraphrase:  "Identifying and attacking the saddle point problem in high-dimensional
             non-convex optimization" argues from statistical physics, random matrix
             theory, and experiment that the trouble is "the proliferation of saddle
             points, not local minima, especially in high dimensional problems." A
             critical point's error correlates with its index (the fraction of
             negative-curvature directions): high-error critical points are almost
             surely saddles, and "all local minima, which necessarily have index 0,
             are likely to have an error very close to that of the global minimum"
             (Sec. 2). It cites Baldi and Hornik (1989) that a linear-hidden-layer
             MLP "shows only saddle-points and no local minima," and confirms the
             ratio empirically on small MLPs trained on down-sampled MNIST and
             CIFAR-10, where critical points fall on a rising curve in the
             error-versus-index plane (Fig. 1). It proposes a "saddle-free Newton"
             method that escapes saddles faster than gradient descent or quasi-Newton
             methods.
Locators:    Abstract, p.1; prevalence argument and Bray-Dean / Wigner reasoning,
             pp.1-2; MNIST/CIFAR validation and Fig. 1, p.3; saddle-free Newton and
             experiments, later sections.
Quote:       "in high dimensions, the chance that all the directions around a
             critical point lead upward (positive curvature) is exponentially small
             w.r.t. the number of dimensions, unless the critical point is the global
             minimum or stands at an error level close to it." (Sec. 2)
```

```text
URL:         https://people.idsia.ch/~juergen/who-invented-backpropagation.html
Kind:        secondary. Jürgen Schmidhuber reports on the priority record from
             outside the 1986 authoring party. Context only; every date it carries
             about a document not read here is unverified against that document.
             Schmidhuber is himself a party to neural-network priority disputes and
             argues a strong pro-predecessor line, so his framing is a stake, not a
             neutral referee.
Establishes: A chronology tying the pieces together, useful for the deeper
             control-theory precursors this record did not open firsthand.
Paraphrase:  Schmidhuber places reverse-mode backpropagation-style differentiation
             first in Linnainmaa (1970, 1976), with control-theory precursors in
             Kelley (1960), Bryson (1961), Bryson and Ho, and Dreyfus (1962, 1973),
             the neural-network-specific application in Werbos (1974 thesis, then
             1982), and Parker (1985), Le Cun (1985), and Rumelhart-Hinton-Williams
             (1986) after. He credits the 1986 paper with the experimental
             demonstration that backpropagation yields useful internal
             representations, not with the algorithm.
Locators:    Section headings on the 1960s precursors, Linnainmaa 1970, Werbos, and
             the 1980s papers.
Quote:       "Explicit, efficient error backpropagation ... in arbitrary, discrete,
             possibly sparsely connected, NN-like networks was first described in a
             1970 master's thesis (Linnainmaa, 1970, 1976)."
```

## Contradictions

- The commission frames the paper as "routinely miscredited," which is true of
  popular memory but must not be read back onto the 1986 text. Both primaries are
  careful about credit to their own contemporaries: the Nature paper says variants
  were "discovered independently by David Parker ... and by Yann Le Cun" (p.535),
  and the PDP chapter credits Widrow-Hoff for the delta rule and Parker and Le Cun
  for the generalization (p.322). What the 1986 authors did not do is cite Werbos
  (1974) or Linnainmaa (1970/1976). The gap is real, and the honest reading is that
  those predecessors sat in other fields (statistics, numerical analysis) and were
  not yet known to the connectionist community, not that the authors overwrote a
  credit they knew of. Hinton has said as much publicly since; that admission is not
  in these primaries and is not sourced here.

- The later local-minima result cuts partly with the 1986 paper, not only against
  it. Rumelhart, Hinton, and Williams reported empirically that the net "very rarely
  gets stuck in poor local minima" (Nature p.535) and called local minima "irrelevant
  in a wide variety of learning tasks" (PDP p.324). Dauphin et al. (2014) supply the
  high-dimensional theory for why that empirical claim holds, while correcting the
  vocabulary: the real slowdown is saddle points, and the local minima that exist sit
  near the global minimum. A telling that says "later work showed the paper was wrong
  about local minima" would misread both documents. The paper's observation stood; its
  explanation was incomplete.

- "Backpropagation" as a single invention does not survive contact with the
  primaries. Linnainmaa (1976) owns the reverse accumulation of derivatives but never
  mentions learning or networks. Werbos (1974) owns a cheap-derivative method for
  steepest descent but frames it for social-science statistics, naming brains only by
  analogy. The 1986 papers own the demonstration that the procedure builds useful
  hidden-unit representations and the result that reawakened the field. These are
  three different contributions, and collapsing them into one "who invented it"
  question is what produces the miscredit in both directions.

## Numbers

```text
Figure: symmetry net = 6 input units, 2 hidden units, 1 output unit
Owner:  Rumelhart, Hinton & Williams 1986 (Nature), Fig. 1 and caption, p.534
Scope:  one demonstration net; the 6 inputs give 2^6 = 64 possible input vectors
```
```text
Figure: 1,425 sweeps through the 64 input vectors to learn symmetry; epsilon=0.1, alpha=0.9
Owner:  Nature Fig. 1 caption, p.534
Scope:  full-batch (accumulated-gradient) update once per sweep over all 64 patterns
```
```text
Figure: hidden-unit weights on each side of the midpoint in ratio 1:2:4
Owner:  Nature Fig. 1 caption, p.534
Scope:  the learned symmetry solution, per hidden unit
```
```text
Figure: family-tree net = 24 + 12 = 36 input units; 6 + 6, then 12, then 6 hidden; person-2 outputs; five layers
Owner:  Nature Figs. 2-3 and caption, pp.534-535
Scope:  one net storing two isomorphic 12-person family trees
```
```text
Figure: trained on 100 of 104 possible triples for 1,500 sweeps; epsilon=0.005/alpha=0.5 first 20 sweeps, then epsilon=0.01/alpha=0.9; weight-decay 0.2% per update; generalized to the 4 held-out triples
Owner:  Nature p.535
Scope:  12 relationship types over 24 people; 4 held-out triples as the generalization test
```
```text
Figure: XOR solved in 558 sweeps with one hidden unit at eta=0.5
Owner:  Rumelhart, Hinton & Williams 1986 (PDP Ch.8), p.331
Scope:  4 input-output patterns; one reported run
```
```text
Figure: XOR local minimum in only 2 of "hundreds" of runs; one reached after 6,587 presentations at eta=0.25; escaped at eta>=0.5
Owner:  PDP Ch.8, pp.331-332 and footnote 2
Scope:  the two-hidden-unit XOR architecture
```
```text
Figure: presentations to solve XOR P = 280 - 33 log2(H); ~245 at H=2 down to ~120 at H=32, eta=0.25 (Chauvin)
Owner:  PDP Ch.8, p.333
Scope:  number of hidden units H up to about 40; XOR task
```
```text
Figure: 4-bit parity solved after 2,825 presentations; 4 hidden units, 16 patterns, eta=0.5
Owner:  PDP Ch.8, p.335
Scope:  parity over 4 input lines (16 patterns)
```
```text
Figure: encoder network = 8 inputs, 3 hidden, 8 outputs (8-3-8)
Owner:  PDP Ch.8, pp.335-337 (Tables 4-5)
Scope:  identity mapping of 8 orthogonal patterns through log2(8)=3 hidden units
```
```text
Figure: sequence-completion recurrent net = 5 input, 30 hidden, 3 output; 25 sequences; 260 sweeps; alpha=0.9, weight-decay 0.2
Owner:  PDP Ch.8, pp.358-359 (Table 10)
Scope:  one recurrent net; a harder variable-timing variant used 60 hidden units
```
```text
Figure: first-order Taylor coefficient c_{i,p} = partial derivative of output u_i w.r.t. input u_p
Owner:  Linnainmaa 1976, eq. (10), p.149
Scope:  arbitrary finite numerical computation; reverse accumulation over a stored trace
```
```text
Figure: critical-point error correlates with index (fraction of negative-curvature directions); local minima have index 0 and error near the global minimum
Owner:  Dauphin et al. 2014, Sec. 2 and Fig. 1
Scope:  high-dimensional non-convex error surfaces; verified on small MLPs on down-sampled MNIST and CIFAR-10
```

Not in the primaries, do not fabricate: the hardware, wall-clock training time, and
any FLOP or operation count for the 1986 demonstrations. The papers state sweeps and
pattern presentations, never machine or time. A compute anchor for the reader must be
built from parameter counts and pattern counts, or stated as unknown.

## Source assets

```text
Asset: Nature Fig. 4, the receptive fields of the six person-encoding hidden units in the family-tree net, p.535
Shows: that backpropagation built interpretable internal features nobody specified:
       one unit separates English from Italian, one encodes generation, one encodes
       family branch. This is the paper's actual contribution made visible.
Crop:  keep the grid of weight rectangles and enough of the caption to name what
       units 1, 2, and 6 encode; omit nothing that identifies which unit is which.
```
```text
Asset: Nature Fig. 1, the learned symmetry network with weights and biases labeled, p.534
Shows: a complete trained net small enough to read every weight, and the 1:2:4
       structure and mirror-symmetric weights that make it work. Concrete proof of
       "small net, legible solution."
Crop:  retain the numeric weights on the arcs and the node biases; the argument is
       the exact numbers, so a decorative crop that drops them is useless.
```
```text
Asset: PDP Ch.8 Fig. 5, the XOR network stuck in a local minimum, p.333
Shows: a real failure case with its weights, the counterpoint to the paper's claim
       that such minima are rare. Grounds the local-minima discussion in one picture.
Crop:  keep the weights and the caption noting the output goes to 0.5 on two patterns.
```
```text
Asset: Dauphin et al. 2014 Fig. 1, critical points on a rising curve in the error-index plane for MNIST and CIFAR-10, p.3
Shows: the empirical saddle-point result on neural nets: high-error critical points
       have many negative-curvature directions, low-error ones approach a true
       minimum. Carries the correction better than prose.
Crop:  keep both the error-versus-index scatter panels (a and c) and the log-scale
       axis labels; the shape of the curve is the whole point.
```
```text
Asset: Werbos 1974 thesis, contents entry "The Ordered Derivative and Dynamic Feedback" (II-82) and title page, pp.i, v-vi
Shows: documentary evidence that the method sat in a 1974 Harvard thesis. A plain
       primary artifact for the priority timeline.
Crop:  title page date "August, 1974" and the contents line naming the section.
```
```text
Asset: Linnainmaa 1976, Table 1, first- and second-order coefficients for elementary operations, p.148
Shows: the derivative-propagation machinery in the predecessor primary, in the
       rounding-error vocabulary that shows it was not written about neural nets.
Crop:  keep the operation column and the first-order coefficient columns; retain
       enough surrounding text to show the rounding-error framing.
```

None of these should be redrawn; each is a primary artifact whose value is that the
reader sees the original.

## Discarded

```text
https://en.wikipedia.org/wiki/Ronald_J._Williams: tertiary; biography, owns no claim here.
https://en.wikipedia.org/wiki/Seppo_Linnainmaa: tertiary; used only to locate the 1970 thesis and 1976 paper, which were then read directly.
https://en.wikipedia.org/wiki/Paul_Werbos: tertiary; superseded by reading the 1974 thesis itself.
https://medium.com/@igquinteroch/backpropagation-...: blog explainer; no primary standing, risks importing the very legend the piece must separate from the record.
https://www.semanticscholar.org/paper/052b1d8ce...: index/landing page, not the document; the paper text was read instead.
https://apps.dtic.mil/sti/tr/pdf/ADA164453.pdf: the ICS technical-report version of the PDP chapter; redundant with the published chapter, which is cited instead.
https://www.researchgate.net/publication/35657389_...: gated re-host of the Werbos thesis; the open facsimile was read instead.
```
