# Evidence: the-evidence/long-short-term-memory (01)

The evidence supports the commissioned angle firmly. The 1997 LSTM paper's own
experiment sections show that every result in it came from small, synthetic
sequence tasks run on networks of a few hundred to a few thousand weights and
two to four memory cells; the paper reports no natural-language, speech, or
other real-world benchmark, and its own future-work section lists speech and
music as things the authors still intended to try. The 1997 architecture defines
only a constant error carousel, an input gate, and an output gate; the word
"forget" never appears, and the forget gate that the modern "vanilla LSTM"
begins with was added by Gers, Schmidhuber and Cummins in 2000. The real-world
record that the reputation now rests on is later and separately sourced:
Graves and Schmidhuber on TIMIT phonemes (2005), Graves, Mohamed and Hinton on
TIMIT recognition (2013), Sutskever, Vinyals and Le on English-French
translation (2014), all using the forget-gate formulation, before transformers
displaced recurrence for language in 2017. The record is thin in exactly one
place the commission named as a must-open primary: the Gers, Schmidhuber and
Cummins 2000 *Neural Computation* paper is paywalled with no open copy, so its
forget-gate definition and experiments are established here from parties in a
position to know (the 1997 paper's silence, the 2024 xLSTM paper by Hochreiter's
group, and Graves and Schmidhuber 2005) rather than from that paper's own text.
One caution for the writer: "modest evidence" is about scale, not strength. The
1997 paper's within-scope result is strong and was hard, and the paper is candid
about its own limits, so the angle is the gap between small evidence and a
load-free reputation, not a claim that the work was weak.

### Sources

```text
URL:         https://www.bioinf.jku.at/publications/older/2604.pdf
             (Neural Computation 9(8):1735-1780, 1997; DOI 10.1162/neco.1997.9.8.1735)
Kind:        primary. Sepp Hochreiter (Fakultät für Informatik, TU München) and
             Jürgen Schmidhuber (IDSIA, Lugano) author and own the LSTM claim.
Establishes: Firsthand: the problem LSTM solves, the exact 1997 architecture,
             and the full experimental record. Absence of a forget gate is
             established firsthand (the architecture defines only input and
             output gates; "forget" occurs nowhere in the paper).
Paraphrase:  Learning to store information over long intervals with recurrent
             backprop fails because backpropagated error either blows up or
             vanishes exponentially with the time lag (they credit Hochreiter
             1991). LSTM fixes this with a "constant error carousel" (CEC): a
             cell built around a linear unit with a fixed self-connection of
             weight 1.0, so error flows back through it without decay. A
             multiplicative input gate protects the stored value from irrelevant
             inputs; a multiplicative output gate protects other units from the
             stored value when it is irrelevant. The gradient is truncated where
             it would leak out of the cell. All experiments use artificial data;
             the future-work section says the authors intend to apply LSTM to
             real-world data (time-series prediction, music composition, speech).
Locators:    Abstract and Sec. 1 (p.1); vanishing/exploding analysis Sec. 3.1
             (pp.3-4); CEC Sec. 3.2 (p.7); "Memory cells and gate units" Sec. 4
             (p.8); Fig. 1 caption (p.9); Experiments Sec. 5 (pp.10-21); tables
             1,2,3,7,8,9; Limitations Sec. 6 (pp.22-23); Conclusion/future work
             Sec. 7 (p.23).
Quote:       "Multiplicative gate units learn to open and close access to the
             constant error flow through 'constant error carrousels' within
             special units." (Abstract) — "A multiplicative input gate unit is
             introduced to protect the memory contents stored in j from
             perturbation by irrelevant inputs. Likewise, a multiplicative output
             gate unit is introduced which protects other units from perturbation
             by currently irrelevant memory contents stored in j." (Sec. 4)
```

```text
URL:         https://www.bioinf.jku.at/publications/older/3804.pdf
             (Josef "Sepp" Hochreiter, "Untersuchungen zu dynamischen neuronalen
             Netzen," Diplomarbeit, Institut für Informatik, TU München,
             15 June 1991; supervisor Dr. Jürgen Schmidhuber, examiner
             Prof. Dr. W. Brauer)
Kind:        primary. This thesis is the origin document for the vanishing-
             gradient analysis; the 1997 paper cites it for that result.
Establishes: Firsthand: that in a recurrent net a distant input has, in general,
             very little influence on the current state, so backprop cannot learn
             to connect events far apart in time; and the formal statement that
             the dependency of the output on a weight scales as a product of
             other weights and derivatives that grows or shrinks exponentially
             with the stored time span. Also firsthand: a prototype of the CEC (a
             linear "constant-error-backflow" node with self-weight 1.0) and a
             multiplicative "weighting unit" on its net input, a gate in all but
             name, likened to a Sigma-Pi unit.
Paraphrase:  Chapter 2 ("Untersuchungen zum Fehlerrückfluss") shows the
             backpropagated error scales with a product P of weights and slopes
             that "exponentially falls or rises," making it very hard to hold P
             near 1.0. The concluding remarks state plainly that the long
             learning time and instability "result from the influence of
             individual weights on the net output depending on other weights;
             this dependency grows exponentially with the time span over which
             the information is stored, as shown in Chapter 2." Chapter 4
             ("Konstanter Fehlerrückfluss") introduces a KFR node (constant error
             backflow node) with self-weight 1.0 and a multiplicative weighting
             unit on its input.
Locators:    Cover (p.1); Einleitung (p.4); Chapter 2 and its summary Sec. 2.3
             (pp.14-24); Abschließende Betrachtungen (p.68); Chapter 4 KFR node
             (pp.51-59). Document is in German.
Quote:       "Da aber P in Abhängigkeit von den Gewichten exponentiell fällt bzw.
             steigt, ist eine Einstellung von P auf einen Wert, welcher um 1.0
             liegt, sehr schwierig und langwierig." (Sec. 2.3)
```

```text
URL:         https://direct.mit.edu/neco/article/12/10/2451/6415  (paper's home)
             DOI 10.1162/089976600300015015 — Felix A. Gers, Jürgen Schmidhuber,
             Fred Cummins, "Learning to Forget: Continual Prediction with LSTM,"
             Neural Computation 12(10):2451-2471, 2000. PAYWALLED (403; Semantic
             Scholar records open-access status CLOSED). Companion opened instead:
             Felix Gers, "Long Short-Term Memory in Recurrent Neural Networks,"
             PhD thesis (EPFL Thèse 2366, 2001), http://www.felixgers.de/papers/phd.pdf
Kind:        primary. Gers, Schmidhuber and Cummins own the forget-gate claim;
             the PhD thesis is the lead author's own companion document.
Establishes: That the forget gate was added in 2000 (not in the 1997 paper), to
             let a cell learn to reset its internal state on continual (unsegmented)
             input streams where the state would otherwise grow without bound.
             Recorded here at second hand for the definition: the 2000 paper's own
             text could not be opened, and the retrieved PhD thesis PDF uses
             subsetted fonts whose body prose does not extract as clean text (its
             title, authorship, and forget-gate figures/sections were confirmed).
             The dating and attribution are corroborated firsthand by the xLSTM
             paper and Graves & Schmidhuber 2005 (below), and the absence in 1997
             is firsthand from the 1997 paper.
Paraphrase:  Metadata and the paper's published abstract identify the weakness it
             addresses: an LSTM processing a continual stream that is not a priori
             segmented, with no state resets, can let the internal cell state grow
             indefinitely and break down; the remedy is an adaptive forget gate by
             which the cell learns to reset itself and release resources.
Locators:    Neural Computation 12(10):2451-2471 (paper). PhD thesis: title page
             p.1 (EPFL, advisor Gerstner, co-reporter Schmidhuber); forget-gate
             chapter figures visible but body text not machine-readable.
Quote:       (none recorded firsthand from the 2000 paper's own text; see Limits.)
```

```text
URL:         https://www.cs.toronto.edu/~graves/nn_2005.pdf
             (Alex Graves and Jürgen Schmidhuber, "Framewise Phoneme
             Classification with Bidirectional LSTM and Other Neural Network
             Architectures," Neural Networks 18(5-6):602-610, 2005; IDSIA /
             TU Munich)
Kind:        primary. Graves and Schmidhuber own this speech result.
Establishes: Firsthand: LSTM applied to real speech data (TIMIT), that the LSTM
             they use has three gates including a forget gate, and that they use a
             full-gradient training algorithm rather than the 1997 truncated one.
Paraphrase:  The memory block has "input, output and forget gates" giving
             continuous analogues of write, read and reset for the cells; the
             forget gate multiplies the cell state. They cite the LSTM training
             algorithm to Gers et al. and introduce a full-gradient version, which
             gave slightly higher performance than the original truncated
             algorithm. On TIMIT framewise phoneme classification, bidirectional
             LSTM reaches a mean test-set score of 69.8% (70.2% retrained),
             beating bidirectional RNN, MLP, and unidirectional variants.
Locators:    Abstract (p.1); Sec. II network description (p.2, "input, output and
             forget gates"; full-gradient note); Sec. III data (TIMIT: 3696 train
             / 1344 test utterances, 1,124,823 training frames); Tables I-II
             (results).
Quote:       "...input, output and forget gates — that provide continuous
             analogues of write, read and reset operations for the cells."
```

```text
URL:         https://arxiv.org/abs/1303.5778
             (Alex Graves, Abdel-rahman Mohamed, Geoffrey Hinton, "Speech
             Recognition with Deep Recurrent Neural Networks," ICASSP 2013;
             University of Toronto. Note: Schmidhuber is NOT an author.)
Kind:        primary. These authors own this benchmark result.
Establishes: Firsthand: deep LSTM RNNs, trained end-to-end with CTC, set a TIMIT
             phoneme-recognition test error of 17.7%, described as the best score
             then recorded. Marks LSTM's move into competitive speech recognition.
Paraphrase:  Deep bidirectional LSTM combined with Connectionist Temporal
             Classification reaches 17.7% test error on the TIMIT phoneme
             recognition benchmark, which the authors state is, to their
             knowledge, the best recorded score; earlier RNN speech results had
             been disappointing relative to deep feedforward nets.
Locators:    Abstract (p.1); Sec. 1 (p.1); results section and Table with TIMIT
             PER 17.7%.
Quote:       "...deep Long Short-term Memory RNNs achieve a test set error of
             17.7% on the TIMIT phoneme recognition benchmark, which to our
             knowledge is the best recorded score."
```

```text
URL:         https://arxiv.org/abs/1409.3215
             (Ilya Sutskever, Oriol Vinyals, Quoc V. Le, "Sequence to Sequence
             Learning with Neural Networks," NIPS 2014; Google)
Kind:        primary. These authors own the seq2seq translation result.
Establishes: Firsthand: LSTM run at production scale for machine translation, and
             the size gap versus 1997. States the LSTM used is "the LSTM
             formulation from Graves" (i.e. the forget-gate version).
Paraphrase:  A deep LSTM encoder maps an English sentence to a fixed vector and a
             deep LSTM decoder produces the French sentence. On WMT'14
             English-French, an ensemble of 5 LSTMs scores 34.8 BLEU (34.81),
             beating a phrase-based statistical MT baseline at 33.3; using the
             LSTM to rerank the baseline's 1000 hypotheses reaches 36.5. Reversing
             the source-sentence word order dropped test perplexity from 5.8 to
             4.7 and raised BLEU. Each LSTM has 4 layers of 1000 cells, 1000-dim
             word embeddings, a 160,000-word source and 80,000-word target
             vocabulary, and 384M parameters, trained on 12M sentence pairs (348M
             French and 304M English words).
Locators:    Abstract (p.1); Sec. 1 (p.2, "LSTM formulation from Graves [10]");
             Sec. 3.2 dataset (p.3); Sec. 3.3 reversing (p.4); Sec. 3.4
             "Training details" (p.4, 4 layers / 1000 cells / 384M params).
Quote:       "...the deep LSTM uses 8000 real numbers to represent a sentence...
             The resulting LSTM has 384M parameters of which 64M are pure
             recurrent connections..."
```

```text
URL:         https://arxiv.org/abs/1706.03762
             (Ashish Vaswani et al., "Attention Is All You Need," NIPS 2017;
             Google Brain / Google Research / U. Toronto)
Kind:        primary. Owns the claim that attention displaced recurrence for
             translation.
Establishes: Firsthand: that recurrent nets, LSTM and gated RNN among them, were
             the established state of the art for sequence transduction up to this
             point, and that a model "dispensing with recurrence" beat them.
Paraphrase:  The Transformer is based solely on attention, dispensing with
             recurrence and convolutions. On WMT'14 it reaches 28.4 BLEU
             English-German (over 2 BLEU above the prior best, including
             ensembles) and a single-model 41.8 BLEU English-French, at a fraction
             of prior training cost. The introduction names recurrent, LSTM and
             gated recurrent nets as the approaches "firmly established as state
             of the art" in sequence modeling and machine translation.
Locators:    Abstract (p.1); Sec. 1 Introduction (p.2); Table 2 (BLEU / training
             cost).
Quote:       "...the Transformer, based solely on attention mechanisms, dispensing
             with recurrence and convolutions entirely."
```

```text
URL:         https://arxiv.org/abs/2405.04517
             (Maximilian Beck, Korbinian Pöppel, ... Sepp Hochreiter, "xLSTM:
             Extended Long Short-Term Memory," 2024; ELLIS/JKU Linz and NXAI.
             Sepp Hochreiter is senior author.)
Kind:        primary. Hochreiter's own group; owns the xLSTM claim and speaks
             firsthand about LSTM's history and limits.
Establishes: Firsthand corroboration that the 1997 ideas were the CEC and gating,
             that the forget gate was introduced later by Gers, and that the
             classic LSTM has three named limits. Owns the modern revisiting of
             LSTM at scale.
Paraphrase:  States the LSTM idea (crediting Hochreiter 1991 and Hochreiter &
             Schmidhuber 1997) is the CEC plus gating to overcome vanishing
             gradients, and that "the memory cell contains three gates: input,
             output, and forget gate. The forget gate has been introduced by
             Gers." Names three LSTM limits: inability to revise storage
             decisions, limited storage capacity (a scalar cell), and lack of
             parallelizability due to memory mixing. xLSTM adds exponential gating,
             sLSTM (scalar memory, memory mixing) and mLSTM (matrix memory,
             parallelizable, covariance update), trained up to 2.7B parameters on
             300B SlimPajama tokens, reported to compare favorably with
             transformers and state-space models. Frames LSTMs as having
             "constituted the first Large Language Models," which is the authors'
             characterization, not an established fact.
Locators:    Abstract (p.1); Sec. 1 Introduction (p.2, forget-gate attribution
             and the three limits, Fig. 2); Sec. 2 methods (sLSTM/mLSTM);
             experiments (15B and 300B token training; up to 2.7B params).
Quote:       "The memory cell contains three gates: input, output, and forget
             gate. The forget gate has been introduced by Gers..."
```

```text
URL:         https://colah.github.io/posts/2015-08-Understanding-LSTMs/
             (Christopher Olah, "Understanding LSTM Networks," 27 August 2015)
Kind:        secondary. A widely read third-party explainer, used here for
             context on what "LSTM" has come to mean, never for a number.
Establishes: That the LSTM taught to a generation of practitioners starts with a
             forget gate, which is the 2000 addition and not in the 1997 paper.
             Supports the angle that today's "LSTM" is the forget-gate
             architecture.
Paraphrase:  The walkthrough presents the standard LSTM as having three gates and
             opens the cell's operation with the forget gate: "The first step in
             our LSTM is to decide what information we're going to throw away from
             the cell state. This decision is made by a sigmoid layer called the
             'forget gate layer.'" It also notes that "almost every paper
             involving LSTMs uses a slightly different version."
Locators:    Post body, "Step-by-Step LSTM Walk Through" and "Variants on LSTM."
Quote:       "The first step in our LSTM is to decide what information we're going
             to throw away from the cell state. This decision is made by a sigmoid
             layer called the 'forget gate layer.'"
```

### Contradictions

- Modest scale is not weak result. The 1997 experiments are small, but within
  their scope the result was strong and genuinely new: LSTM solved long-time-lag
  tasks (up to 1000 steps) that BPTT, RTRL, and other recurrent methods could not
  solve at all (1997, Sec. 5, Tables 2-3). The paper says it chose synthetic
  tasks deliberately, because many earlier "long lag" benchmarks can be solved by
  random weight guessing or short-lag shortcuts, so it needed clean long-lag
  problems (1997, Sec. 5 introduction). A writer who reads "small networks" as
  "unconvincing" would misstate the paper.

- The paper states its own limits, so an "over-claim" reading is not the paper's
  fault. It says LSTM behaves much like a feedforward net seeing the whole input,
  cannot solve a 500-bit-parity or strongly-delayed-XOR task by its efficient
  truncated algorithm, and cannot precisely count time steps (1997, Sec. 6,
  Limitations). The gap the commission targets is between the paper's evidence and
  its later reputation, not between the paper's claims and its evidence.

- "LSTM = the 1997 model" is contradicted by the sources that use it. seq2seq
  (2014) uses "the LSTM formulation from Graves," which is the forget-gate
  version; Graves & Schmidhuber (2005) and the xLSTM paper (2024) both describe
  the standard LSTM with a forget gate; Olah (2015) teaches it forget-gate-first.
  So when later work "uses LSTM," it uses the 2000 architecture. This supports the
  angle rather than breaking it.

- The idea did not spring fully formed in 1997. The CEC and a multiplicative
  gating unit already appear in prototype in Hochreiter's 1991 thesis (Chapter 4),
  and the forget gate that completes the "vanilla" cell is from 2000. The famous
  1997 paper is the middle of that arc, not its whole.

- Authorship precision: the 2013 real-speech result the commission grouped under
  "Graves & Schmidhuber" is Graves, Mohamed and Hinton (Toronto); Schmidhuber is
  not an author. The 2005 TIMIT paper is the Graves & Schmidhuber one.

### Numbers

```text
Figure: 1735-1780
Owner:  Hochreiter & Schmidhuber 1997
Scope:  page range of the LSTM paper in Neural Computation 9(8), 1997.

Figure: >1000 discrete time steps (minimal time lag bridged)
Owner:  Hochreiter & Schmidhuber 1997 (Abstract; Task 2c, Table 3)
Scope:  longest lag in the paper's hardest synthetic task; e.g. q=1000, p=1000
        distractor symbols, solved after ~49,000 training sequences.

Figure: 264 to 6,064 weights (whole-network size across experiments)
Owner:  Hochreiter & Schmidhuber 1997 (Tables 1,2,3,7,8,9)
Scope:  Exp. 1 Reber 264-276 weights; Exp. 2a 10,504 weights at p=100 (largest,
        driven by p+4 input units); Task 2c 364-6,064 weights; adding/
        multiplication (Exp. 4-5) 93 weights; temporal order (Exp. 6) 156 and
        308 weights. Memory cells per net: 2 to 4.

Figure: 6 experiments, ~12 task variants, all synthetic
Owner:  Hochreiter & Schmidhuber 1997 (Sec. 5)
Scope:  Exp.1 embedded Reber; 2a/2b/2c noise-distractor; 3a/3b/3c 2-sequence;
        4 adding; 5 multiplication; 6a/6b temporal order. No real-world data.

Figure: success = output error always below 0.2-0.25 (or 0.04 for real-valued)
Owner:  Hochreiter & Schmidhuber 1997 (per-experiment criteria)
Scope:  e.g. Task 2a/2b "max absolute error below 0.25/0.2 over 10,000 successive
        sequences"; adding/multiplication "absolute error below 0.04".

Figure: 69.8% mean test-set score (BLSTM framewise phoneme classification)
Owner:  Graves & Schmidhuber 2005 (Tables I-II)
Scope:  TIMIT; 3696 train / 1344 test utterances; 1,124,823 training frames.

Figure: 17.7% test error (TIMIT phoneme recognition)
Owner:  Graves, Mohamed & Hinton 2013 (Abstract)
Scope:  TIMIT phoneme-recognition benchmark; deep LSTM + CTC; stated best score
        then recorded.

Figure: 34.8 BLEU (LSTM ensemble) vs 33.3 BLEU (phrase-based SMT baseline)
Owner:  Sutskever, Vinyals & Le 2014 (Abstract; Sec. 4)
Scope:  WMT'14 English-French; LSTM rerank of SMT 1000-best rises to 36.5.

Figure: 384M parameters; 4 layers x 1000 cells; 12M sentence pairs
Owner:  Sutskever, Vinyals & Le 2014 (Sec. 3.4)
Scope:  seq2seq translation model; 348M French + 304M English training words;
        160,000 source / 80,000 target vocabulary. Contrast with 1997's hundreds
        to few-thousand weights.

Figure: 28.4 BLEU (EN-DE) and 41.8 BLEU (EN-FR)
Owner:  Vaswani et al. 2017 (Abstract; Table 2)
Scope:  WMT'14; Transformer, "dispensing with recurrence"; marks the point
        transformers overtook recurrent models for translation.

Figure: up to 2.7B parameters, trained on 300B tokens
Owner:  Beck et al. 2024, xLSTM (experiments)
Scope:  SlimPajama; largest xLSTM language models reported; smaller ablations at
        15B tokens.
```

### Limits

- The Gers, Schmidhuber & Cummins 2000 *Neural Computation* paper, named in the
  commission as a must-open primary, is paywalled (403; no open-access PDF), so
  its forget-gate definition and its own experiments (task, network size) are not
  recorded firsthand. The forget gate's existence, its 2000 date, its purpose
  (resetting cell state on continual streams), and its absence from the 1997 model
  are established firmly from firsthand parties: the 1997 paper (silence), the
  2024 xLSTM paper (Hochreiter's group, explicit attribution to Gers), and Graves
  & Schmidhuber 2005. The retrieved Gers 2001 PhD thesis confirmed the document
  and its forget-gate sections but its body prose would not extract as clean text.
  If the writer needs a direct quotation of the 2000 paper's own wording, it is
  not in this record.
- Everything else the commission asked was established firsthand from the primary
  documents: the problem and the vanishing-gradient framing (1991 thesis + 1997
  Sec. 3.1); the 1997 architecture and the CEC/input-gate/output-gate definitions
  (1997 Sec. 4); the experiments, network sizes, sequence lengths, and success
  criteria (1997 Sec. 5 and its tables); production speech (2005, 2013) and
  translation (2014); transformer displacement (2017); and the 2024 xLSTM
  revisiting.

### Source assets

```text
Asset: Figure 1 of Hochreiter & Schmidhuber 1997 (p.9) — the single memory-cell
       diagram: the central linear CEC unit with its self-loop of weight 1.0, the
       input gate and output gate as multiplicative units, and the squashing
       functions g and h.
Shows: The whole 1997 mechanism in one picture — two gates, one self-connected
       cell, no forget gate. It lets a reader see what "the original LSTM" was and
       what it lacked.
Crop:  Keep the labeled self-recurrent connection (weight 1.0) and both gate
       units with their labels; keep the caption's "delay of 1 time step / CEC".
       Do not crop so tight that the two gates or the self-loop label are lost.
```

```text
Asset: Table 3 of Hochreiter & Schmidhuber 1997 (p.15) — Task 2c results: columns
       for q (time lag - 1), p (number of distractor symbols), expected
       occurrences, number of weights, and training sequences to success, e.g.
       the q=1000/p=1000/6064-weight row.
Shows: The size of the foundation directly: a 1000-step result carried by a
       ~6,000-weight network with two memory cells on a synthetic distractor task.
Crop:  Retain the column headers and units and at least the q=50 and q=1000 rows
       so the reader can read the scale, not just one number.
```

```text
Asset: Figure 1 of Beck et al. 2024 xLSTM (p.1) — the family diagram running from
       the original LSTM memory cell (CEC + gating) through sLSTM and mLSTM to
       stacked xLSTM blocks.
Shows: The lineage from the 1997 cell to the 2024 architecture in one image,
       useful for the "bring it to the present" section.
Crop:  Keep the leftmost "LSTM" cell labeled with the constant error carousel and
       gating so the origin is legible; the rest can be shown or trimmed to fit.
```

```text
Asset: Figure 2 of Beck et al. 2024 xLSTM (p.2) — the two LSTM-limitation panels
       (nearest-neighbor search / revising a stored value, and rare-token
       prediction / storage capacity).
Shows: What the classic LSTM cannot do, stated by Hochreiter's own group; pairs
       with the 1997 paper's own limitations list.
Crop:  Keep the axis labels and the LSTM-versus-xLSTM curves; the panels are only
       useful with their labels intact.
```

None of the German 1991 thesis pages give a clean figure that survives
paraphrase; its value is textual, not visual.

### Discarded

```text
URL: https://www.jmlr.org/papers/volume3/gers02a/gers02a.pdf — this is Gers et al.
     2002 "Learning Precise Timing with LSTM" (JMLR), a different paper from the
     2000 forget-gate paper; not used for the forget-gate origin claim.
URL: https://www.researchgate.net/publication/12292425 (Gers 2000) — 403 gated;
     no readable text; recorded the paper's own home address instead.
URL: https://dl.acm.org/doi/10.1162/089976600300015015 (Gers 2000) — mirror of a
     paywalled record; not the document's home; superseded by the DOI/MIT Press
     address.
URL: http://www.felixgers.de/papers/phd.pdf (live) — server returned TLS/503
     errors; retrieved a Wayback snapshot of the same document instead, but its
     body text does not extract, so it backs the document's existence only.
```
