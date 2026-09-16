# researcher brief: the-evidence/flashattention (01)

Inputs:
- `.nb-work/the-evidence/flashattention/agent-artifacts/the-evidence/flashattention/editorial-direction.md` — citation standard, series territory, declared reader
- `.nb-work/the-evidence/flashattention/agent-artifacts/the-evidence/flashattention/commission.md` — the document, the five ideas the lesson teaches, and the misreading it corrects

Output: `.nb-work/the-evidence/flashattention/agent-artifacts/the-evidence/flashattention/researcher/01/evidence.md`

Read the 2022 FlashAttention paper in full, including its IO-complexity analysis
and experiment tables, before searching elsewhere. Verify each figure the
commission leans on against the passage that owns it: the exact GPU memory
capacities and bandwidths (from the vendor spec the paper cites), the attention
matrix's size for a stated sequence length, the reported training speedups with
their models and hardware, the memory-scaling claim, and the longer-context
results. Read FlashAttention-2 and FlashAttention-3 for the present-day section.
Record contradictions, especially any place the common "approximate / fewer
FLOPs / skips work" description conflicts with the paper's own exactness and
recomputation claims. Note whether a chart of the memory-versus-sequence-length
scaling would be supportable from figures in the record.
