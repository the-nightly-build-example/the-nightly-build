# Draft handoff: the-evidence/latent-diffusion (01)

## Original-work sentence

This lesson separates what the Rombach paper actually proved, a relative and
architectural compute saving that is now the standard design for image models,
from what the open Stable Diffusion release set loose, showing that the CSAM
finding and the unresolved, partly-adverse copyright litigation attach to the
product's LAION-5B training data and not to the paper's method. The evidence
record supplies these as scattered claims; the article is the place they are
drawn into one usable distinction, visible in the "paper-vs-product" and
"open-release" sections and landed in the takeaway.

## Proof result

`./nb check --series the-evidence --library /home/user/library-checkout` (links
included): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** Stamped 2157 words
(band 1200-2200), 9 min, 7 sources (6 primary, 1 secondary; meets the >=6 / >=3
primary / >=1 secondary floor). Zero em-dashes. No warning left standing: the
four initial W-SENTENCE-DENSITY notes were all resolved by splitting the long
sentences.

## Open evidence / voice questions

1. **CLIP lesson exists in the publication library, contradicting the brief.**
   The brief and evidence state CLIP has no lesson and instruct an inline
   definition with no Background link; the researcher's `nb history` was run
   against the main checkout, whose library is empty. Against the actual
   publication target `/home/user/library-checkout`, `the-evidence/clip`
   ("Prompt engineering lifted CLIP's zero-shot ImageNet score by nearly five
   points", dated 2026-08-25) IS published, and `the-evidence/denoising-diffusion`
   already links it. I followed the explicit brief directive: defined the CLIP
   text encoder inline in plain words at first use (the "How the prompt reaches
   the picture" section) and did NOT add a Background link. The house standard
   prefers linking a taught lesson over glossing it, so the orchestrator/editor
   should decide whether a revision adds `the-evidence/clip` to the Background
   band (and trims the inline gloss). Not a proof blocker either way.

2. **Consumer/"gaming GPU" capability claim is not in the evidence record.**
   The commission's original-contribution target asks the reader to grasp why
   Stable Diffusion can run on a gaming GPU. The only library support for that
   specific claim is denoising-diffusion's "2.4 GB consumer card" line, cited
   there to Wikipedia, which is not in my evidence record. I delivered the
   understanding through the sourced mechanism (64x fewer latent positions per
   step, a once-trained reusable autoencoder, ~0.9B params) but deliberately kept
   any specific consumer-hardware capability claim out of the headline, dek, and
   body. If the editor wants that explicit line, the researcher should supply a
   primary or secondary source for the VRAM/consumer-GPU figure.

3. **UK judgment is attributed to secondary reporting, as the record requires.**
   The Nov 2025 England and Wales High Court holding (weights do not store the
   training images; secondary-infringement claim rejected; primary claim dropped
   at trial) is sourced to the Latham & Watkins analysis (s6, secondary) and
   phrased "as reported", with a data-nb-note flagging judgment para. 600 as
   reported rather than read directly. The primary judgment is unread per the
   evidence record.
