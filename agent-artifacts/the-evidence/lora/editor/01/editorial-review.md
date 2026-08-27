# Editorial review: the-evidence/lora (editor/01)

## Skeptic

Thesis: LoRA made cheap specialization the norm by training a tiny low-rank pair
beside frozen weights, and its famous "matches full fine-tuning" result is
bounded to the constrained language benchmarks the 2021 paper ran, so today's
unqualified use of that claim over-reaches on hard new domains like code and
math. The piece stands on five claims, tested against the sources I reopened.

1. The cost reductions (GPT-3 175B: the low-rank pair trained instead of the
   full weights, ~3x less training memory 1.2TB->350GB, a 35MB adapter from a
   350GB model). Checked against the LoRA paper's abstract and Section 5. The
   memory (threefold) and checkpoint (350GB->35MB, exactly 10,000x) figures
   hold. The trainable-weight figure did not: the draft wrote "about 4.7 million
   weights instead of 175 billion, roughly ten thousand times fewer," but
   175B / 4.7M is ~37,000x, not ~10,000x. The paper's own abstract headline is
   "10,000x fewer trainable parameters," a rounded figure that does not
   reconcile with its Table 4 count of 4.7M (the evidence record flags this same
   tension). The article was doing the division explicitly and stating a wrong
   result to the exact numerate reader this paper writes for. Fixed: removed the
   false derived ratio from the prose; the paper's cited 10,000x claim still
   stands in the stat strip, where it is reported as the paper's figure rather
   than computed from these two numbers, and the checkpoint sentence keeps its
   exact 10,000x.

2. The low-rank hypothesis and the rank sweep (rank as small as 1 suffices for
   Wq/Wv; sweep from 64 down to 1 barely moved accuracy). Matches the paper's
   Table 6 and the quoted "intrinsic rank" phrasing. The Aghajanyan (2020)
   precedent is handled with care: the draft keeps the 200-parameter / 90%-on-
   MRPC result as a distinct, adjacent finding and does not conflate it with
   LoRA's own claim, which was the record's stated risk. Held.

3. Merge-back / zero inference latency, versus adapters that add layers. Matches
   the paper's Section 4.1 framing. Held.

4. Parity table (GPT-3 MNLI-m 89.5 vs 91.7; WikiSQL 73.8 vs 73.4; RoBERTa-large
   GLUE 88.9 vs 89.0; GPT-2-medium E2E BLEU 68.2 vs 70.4, with parameter
   counts). Every cell checks against the evidence record's Numbers section.
   Held.

5. The limitation and adoption claims. Biderman et al. (2024) on Llama-2-7B
   (LoRA underperforms full fine-tuning on code/math, sharpest in continued
   pretraining on tens of billions of tokens; full fine-tuning learns rank
   10-100x higher; LoRA forgets less), QLoRA (65B on one 48GB GPU, Guanaco 99.3%
   of ChatGPT on the GPT-4-judged Vicuna benchmark, caveat included), and the
   Hugging Face Hub count (98.4%, 20,509/20,834; 95% of image checkpoints). All
   match the sources. Held.

Display text: the headline states "matched full fine-tuning by training 4.7M of
GPT-3's 175 billion weights" — bounded to the model and the parameter count, and
true on the paper's GPT-3 tasks. Every body use of the parity claim carries its
scope ("On the tasks the paper measured," "not a law of adaptation," "the paper
only ever showed it on constrained language tasks," "real inside the tasks the
paper ran and unproven outside them"). This was the round's load-bearing check
and it holds. The discarded figures (97-99% GLUE, Gartner 85% by 2027) do not
appear. Biderman 2024 is cited by its arXiv page and never called a TMLR paper;
worth noting that the live arXiv page now does state the TMLR venue in its
comments, so the label would be defensible, but the article does not need it.

The dek carried a grammar break: "reported that parity only on the constrained
language benchmarks it ran" leaves "parity" with no predicate. Removing the
stray "that" repairs it to "reported parity only on..." Fixed in both the
rendered dek and the nb-meta copy.

data-nb-kind audit: s1/s2/s3/s5 primary to their own claims; s4 (HF measuring its
own Hub) is primary to the adoption count it is cited for, not to LoRA's
efficacy, and is cited only for adoption; s6 (PEFT library) secondary. All
correct. Source floor met: 6 sources, 5 primary, 1 secondary.

Citations: I opened all six hrefs plus the two Go-deeper links as the article
prints them. Every one lands on the source itself (the three arXiv abstract
pages, the HF blog, the QLoRA arXiv page, the PEFT repo). The three internal
Background/inline links (parameter-count, gradient-descent, attention) resolve
in the library. One display-text correction: the s4 entry printed the
placeholder title "PEFT beyond LoRA: Hub usage measurements"; the real page is
titled "Beyond LoRA: Can you beat the most popular fine-tuning technique?"
Retitled to the real page (the writer had flagged this as an editor's call).

## Cut

Slop pass, every sentence including display text and furniture prose. Three
sentences failed and were cut, no rewriting:

- "The squeeze is the whole trick." An unearned punchline in the flagged "X is
  the whole Y" family, and the very next sentence demonstrates the point it
  announces, so cutting the announcement leaves the stronger show-don't-tell the
  voice guide asks for.
- "The result is the set of figures the method is famous for." A signpost into
  the stat strip carrying "famous for" puffery and no fact; the explaining
  paragraph right after the strip does the work.
- "the method is not one option among many. It is the default." The
  "not X, it is Y" negative-parallelism tell; trimmed to "the method is the
  default," which the 98.4% figure in the next sentence earns anyway.

Edge sentences, dangling-referent, and delete-test passes otherwise came back
clean: the openers and closers ("Do that for ten customers and you are storing
ten GPT-3s," "the adaptation costs nothing at the moment of use," "it lands
exactly where the expensive method still does something the cheap one cannot")
carry facts, not scaffolding. The negative contrasts that remain are earned
against a named misconception ("a result on tasks like these, not a law of
adaptation" corrects exactly the over-reach the piece is about; "a mechanism
that fits the original hypothesis instead of breaking it" corrects the natural
misreading of the 2024 study).

Prompt-leakage pass against the commission and briefs: no lifted planning
labels, selection rules, or assignment-fulfillment claims. The bookend's "what
'fine-tuning a model' usually means in practice today" tracks the commission's
framing but is the template-mandated statement of the lesson's payoff, reported,
not a leak. Borrowed-phrasing pass against the Olah/Karpathy/Luu exemplars: the
draft uses their moves (state the cost concretely before the fix; concrete
instance before the term; promising result then the larger study that narrows
it) without lifting their wording.

Recent-pattern check. Dek is a single clause, not the two-clause and/but house
default, and clears the three banned molds (no semicolon reversal, suspended
question, or comma triad). Section headings avoid the overused How/What/Where
openers and the "Where X still..." present-day close; the present-day heading is
"Now almost every fine-tune is a LoRA," and the argument reconstructs from the
headings in order. The Why-this-matters bookend hands off with "By the end you
will know...," which is template-required and varied from the flagged "Read it
and you can see..." habit. Punctuation is clean: no em-dashes, no prose
semicolons.

Furniture: the stat strip and comparison table each earn their place and are
cited in nearby prose; no retired components, no closing Verdict block (the
press forbids it, and the piece closes on the takeaway bookend). The piece reads
as a continuous lesson, not a stack of blocks. A source asset (the paper's
Figure 1, or Table 4) would strengthen the mechanism and the parity claim, but
capturing and cropping one is the writer's tooling, not mine, and the prose
carries both without it, so it is not blocking.

## Reader

Read straight through as the paper's declared reader: I come away able to say
what "fine-tuning a model" now usually means, why it is cheap (a narrow low-rank
squeeze that folds back into the weights at no inference cost), and the exact
seam where the famous parity claim stops holding (large new domains, continued
pretraining). No single source hands that over; the piece synthesizes four
papers plus the adoption count into a calibrated understanding, which the
original-work sentence in the handoff claims and the article delivers. The prose
sits closer to the voice-guide exemplars than to a median summary: concrete
instance before the abstract term, the cost named as flatly as the fix, the
Luu-style promising-result-then-narrowing shape on the parity claim. The
headline, read last as the largest claim, is bounded and true.

## Edits

- Dek: removed stray "that" ("reported that parity only on" -> "reported parity
  only on") to repair a missing predicate. Applied to the rendered dek and the
  nb-meta dek.
- Orientation: removed the false derived ratio ", roughly ten thousand times
  fewer" from the 4.7M-vs-175B sentence (that ratio is ~37,000x); dropped the
  now-dangling "also" so the checkpoint sentence reads "about ten thousand times
  smaller" (exact and correct).
- Orientation: cut "The squeeze is the whole trick." (unearned-punchline slop).
- Orientation: cut "The result is the set of figures the method is famous for."
  (signpost/puffery before the stat strip).
- Today: trimmed "the method is not one option among many. It is the default."
  to "the method is the default." (negative-parallelism tell).
- Sources s4: retitled from the placeholder "PEFT beyond LoRA: Hub usage
  measurements" to the real page title "Beyond LoRA: Can you beat the most
  popular fine-tuning technique?"

Proof after edits: `./nb check ... --series the-evidence --library
/home/user/library-checkout` returns BLOCK 0, WARN 0, PUBLISHABLE.

## Required work

None blocking. One optional item for the writer, not required for publication: a
cropped source asset (LoRA Figure 1, the A/B pair beside the frozen W with the r
bottleneck labeled, or Table 4 with the trainable-parameter column) would let
the reader test the mechanism and the parity claim visually; it needs the
writer's capture tooling and cited provenance.

## Decision

Approve. The load-bearing correctness checks (bounded parity, honest 2024
limitation, discarded figures kept out) all hold, and the remaining prose,
grammar, arithmetic, and citation-label issues were fixable within the edit and
are fixed.
