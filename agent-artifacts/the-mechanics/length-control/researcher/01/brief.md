# researcher brief: the-mechanics/length-control (01)

Inputs:
- editorial-direction.md — citation standard, series territory, declared reader (at the artifact root)
- commission.md — the behavior, the mechanism to trace, and the source policy (at the artifact root)

Output: researcher/01/evidence.md

Establish the mechanism and the measured behavior from primary sources. For the
behavior: read a verifiable instruction-following benchmark that includes length
constraints (e.g., IFEval, arXiv:2311.07911) and/or a study specifically on
following length instructions, and record concrete measured numbers on how often
models hit a requested length or count, with the exact task definition and scope.
Read a primary source on RLHF/post-training length bias (e.g., work investigating
length correlations in RLHF) and record its finding. For the mechanism: from
primary sources establish that generation is left-to-right token-by-token with the
next token conditioned on the text so far (no lookahead, no separate counter), and
that the emitted units are tokens rather than words. Do not re-derive tokenization
in depth; instead, use `nb history --library /home/user/library-checkout` to find
the exact slugs/titles of the published lessons the writer must link
(the-mechanics/autoregressive-generation, the-mechanics/letter-counting,
the-mechanics/formatting-defaults) and record them. Capture one worked, cited
example of a real length-following miss. Distinguish clearly what is settled
(token-by-token decoding; tokens are not words) from what is open (how well a model
can implicitly track its own length; why some models follow length instructions
much better). Verify every figure against its owning source, classify sources
primary or secondary with the reason, and record contradictions. Meet the source
policy in commission.md (min 8, >=4 primary); no padding.
