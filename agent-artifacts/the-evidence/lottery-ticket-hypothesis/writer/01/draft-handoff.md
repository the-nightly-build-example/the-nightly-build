# Draft handoff: the-evidence/lottery-ticket-hypothesis (01)

## Original-work sentence

The article turns the evidence's separate claims into one line the reader can
hold on their own: it names, concretely, the difference between the paper's
narrow verified result (a small trainable subnetwork exists, found only by
pruning a fully trained small vision net and resetting the survivors to their
original random weights) and the broad "winning ticket" shorthand, and it hands
the reader two tools to keep them apart — the two-way P_m-versus-sparsity
conversion table, and the reset-versus-random comparison taught as an
expectation the reader would bring, then the result that defeats it. That work
is visible in the "two ways to count sparsity" table, the "found after training,
not before" section, and the reset step of the procedure.

## Proof result

`./nb check ... --series the-evidence --library /home/user/library-checkout`
(links included) returns **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE**.
`nb stamp` wrote words=2118, reading_minutes=9, sources=7 (6 primary, 1
secondary; policy asks for ≥6 sources, ≥3 primary, ≥1 secondary).

No warnings left standing. The four W-SENTENCE-DENSITY notes the first pass
raised were all fixed by splitting the sentences, not waived.

## Sparsity frame

Every figure states its frame explicitly. P_m (2019 paper) = weights remaining;
"sparsity" (later work) = weights pruned. The conversion table pairs the two and
notes each row sums to 100 percent. Resnet-50 (~30% pruned) and BERT (40–90%
pruned) are given in the pruned frame, matching their source papers; the LeNet
figures are given in P_m with the pruned complement beside them.

## Attribution notes carried into the prose

- The per-sparsity P_m figures (3.6%, 13.5–21.1%, and the LeNet/Conv readings)
  are attributed in the prose and the table caption as the paper's own readings
  from its figures, not an independent recomputation, per the evidence record's
  caveat.
- The secondary source (SyncedReview, s3) is used only for reception context
  ("the name spread across the field as shorthand"), never for a technical
  figure.

## Open evidence or voice questions

None blocking. One minor note for the editor: the reset-vs-random comparison is
carried in prose plus the four-step procedure and the "The hypothesis" note,
rather than as a captured source figure. The evidence record flags the
reset-vs-random curve (Frankle & Carbin, Sec. 2/3) as the single strongest
visual, and `nb asset` capture was available. I judged the prose + steps +
stat-strip furniture sufficient at this length and left the figure out to avoid
capture risk; if the editor wants the curve on the page, it is a clean,
evidence-backed addition.
