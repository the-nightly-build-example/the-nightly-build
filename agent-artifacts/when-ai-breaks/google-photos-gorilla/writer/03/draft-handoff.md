# Draft handoff: when-ai-breaks/google-photos-gorilla (03)

## Original work

The article turns the evidence record's separate findings into one causal
chain: the 2015 mislabel, the training-data representation cause shown directly
(Google Brain's geo-diversity audit and the Princeton/Stanford ImageNet
person-subtree audit) with Gender Shades as the measured downstream accuracy
gap, and the deliberate non-fix that Google's own Cloud Vision recognizing a
gorilla exposes, to argue that Google removed the dangerous category rather than
closing the gap, a choice four companies still made eight years on.

## Proof result

`./nb check ... --series when-ai-breaks --library /home/user/library-checkout`
(links included, after `./nb stamp`):

- **BLOCK: 0**
- **WARN: 0**
- verdict: PUBLISHABLE. 2200 words (band 1200-2200), 10 min read, 8 sources
  (4 primary, 4 secondary). All eight source URLs resolve.

## What round 03 changed

Added the two required neighbor links as plain in-prose links to taught ground,
per the editor's sole required item:

- `rite-aid-facial-recognition`, in the skin-tone-gap section where the piece
  states the demographic-error gap, named as the related demographic-error case.
- `gemini-image-generation`, in the closing paragraph where the piece touches
  image models, distinguished clearly: that case is a generation overcorrection,
  this one a classification failure from under-representation.

Two words of settled prose were trimmed to hold the word band under the added
links (a redundant mechanism restatement in the bounding paragraph and two
filler phrases), preserving every scope caveat, the editor's in-place edits, and
the headline and structure.

One mechanical consequence resolved: the editor's in-place repoint of the
"better recognition of dark-skinned faces" quote to PetaPixel had made that
source first-cited in the "Google's answer" section, ahead of sources 3-6,
raising W-CITE-ORDER. I renumbered the sources in first-citation order (Forbes 1,
CBC 2, PetaPixel 3, Wired 4, Shankar 5, Yang 6, Gender Shades 7, Register 8),
which preserves the editor's attribution decision (the quote still cites
PetaPixel) and clears the warning. Primary count is unchanged at four (Wired,
Shankar, Yang, Gender Shades).

## Open questions

None.
