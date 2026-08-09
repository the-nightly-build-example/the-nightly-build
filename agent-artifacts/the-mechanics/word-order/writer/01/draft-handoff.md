# draft-handoff: the-mechanics/word-order (01)

## The one act of original work

The piece separates two claims the sources keep tangled — *supplies order*
(settled) from *handles any length* (open) — and walks that split down a single
descent: it makes the bare operation's order-blindness concrete on one scrambled
sentence pair, then sets two natural but wrong intuitions against the papers that
refute them (a masked decoder is *not* strictly order-blind because the causal
mask leaks position, Haviv; a relative scheme like RoPE does *not* thereby handle
length, YaRN and ALiBi's Fig. 1). No single source draws that settled/open line
across the scheme family; the article does, and it is visible in the last section
and the takeaway.

## Proof result

`./nb check … --series the-mechanics --library <checkout>` (links included):
**BLOCK: 0**, verdict PUBLISHABLE. Stamp: words 1896, reading 8 min, sources 11.

### Warnings intentionally left (2)

Both are `W-SENTENCE-DENSITY` on controlled sentences I chose to keep after
cutting the piece from 5 warnings to 2 (the em-dash overrun and three other dense
sentences are fixed):

- The takeaway's arc sentence ("...a fixed pattern of waves at first, then learned
  vectors, then relative schemes..., and today the rotary scheme..."). It is one
  deliberate enumeration that shows the whole progression the reader just learned
  at a glance; splitting it loses that effect. Editorial permits a long sentence
  under control.
- The NoPE sentence in the final section, whose appositive ("leaning entirely on
  the order the causal mask leaks") explains *how* a no-encoding decoder gets
  position and belongs inside the clause it modifies.

## Seams handled (per brief)

- Order-blindness is taught on the attention operation itself; the causal-mask
  exception is stated and linked to `the-mechanics/autoregressive-generation`
  rather than re-taught (Haviv cited for the leak).
- RoPE's length behavior is presented as engineered-around, not solved: it fails
  past trained length (YaRN), which is why interpolation/NTK/YaRN exist. The
  dek was corrected mid-draft — an earlier version claimed "no scheme handles
  longer," which is false for ALiBi; it now scopes the failure to the default
  scheme (RoPE).

## Source asset used

ALiBi Fig. 1 (extrapolation curves, arXiv 2108.12409 p. 2) captured with
`nb asset pdf` into `word-order/asset-1.png`. The argument spends exactly what it
shows: the rotary/sinusoidal curves climbing past training length while ALiBi
holds flat carries both the ALiBi claim and the RoPE-does-not-extrapolate seam in
one image. The unverified sinusoidal heatmap the brief flagged was not used.

## Open questions

None for the editor. The evidence covered every claim the piece rests on; no
researcher gap was hit. One judgment call worth a second read: the takeaway
distinguishes "the relative schemes" (Shaw-relative, RoPE — did not solve length)
from ALiBi's distance penalty (which does extrapolate, at the cost of locality),
so "none of them made a model work past the length it trained on" refers to the
gap-encoding schemes, not ALiBi. The body's final section states ALiBi's
exception plainly, so the two do not contradict.
