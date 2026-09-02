# Writer handoff: the-instruments/superglue (01)

## Original work

The evidence record gives the SuperGLUE score's construction and the DeBERTa
crossing's raw figures; this draft's own work is turning those figures back
into the exact distinction the evidence flags but does not state as prose:
that "first to beat the human baseline" is true only as "first single model," reconstructing exactly which of the three January 2021 leaderboard
entries (DeBERTa single, DeBERTa ensemble, T5 + Meena ensemble) actually stood
where relative to the human row and to each other, and building the invented
two-task worked example that makes the averaging-rule choice visible in
numbers rather than asserting it.

## Proof result

Final command run exactly as specified in the brief:

```
nb check /home/user/the-nightly-build/.nb-work/the-instruments/superglue/library/the-instruments/superglue.html \
  --series the-instruments --library /home/user/library-checkout
```

Result: `BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE` (link checking included).
`nb stamp` was run immediately before this final check; nb-meta words=1875,
sources=8, reading_minutes=8.

No warning was intentionally left; the proof returned clean.

## Open questions

None. The evidence record settled the single-vs-ensemble precision, the
aggregation rule, the human-baseline protocol, and the builders'/Bowman's
caveats without gaps. The one place evidence was explicitly thin (dedicated
primary evidence on task shortcuts/artifacts for SuperGLUE's own tasks) is
handled as the evidence record directs: a brief, honest paragraph naming the
risk and pointing to the taught GLUE lesson rather than re-testing or
inventing artifact examples for SuperGLUE's eight tasks.
