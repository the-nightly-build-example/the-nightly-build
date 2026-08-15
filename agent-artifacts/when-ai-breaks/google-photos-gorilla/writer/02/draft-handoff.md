# Draft handoff: when-ai-breaks/google-photos-gorilla (02)

## Original work

The article turns the evidence record's separate findings into one causal
chain: the 2015 mislabel, the training-data representation cause now shown
directly (Google Brain's geo-diversity audit and the Princeton/Stanford
ImageNet person-subtree audit) with Gender Shades as the measured downstream
accuracy gap, and the deliberate non-fix that Google's own Cloud Vision
recognizing a gorilla exposes, to argue that Google removed the dangerous
category rather than closing the gap, a choice four companies still made eight
years on. The record holds these as discrete source summaries; the article's
work is to order them into cause, measured effect, and persistence, and to keep
every mechanism study bounded as cause and never as a measurement of the gorilla
error.

## Proof result

`./nb check ... --series when-ai-breaks --library /home/user/library-checkout`
(links included, after `./nb stamp`):

- **BLOCK: 0**
- **WARN: 0**
- verdict: PUBLISHABLE. 2197 words (band 1200-2200), 10 min read, 8 sources.
- Source composition now clears the floor with fully-read sources: 4 primary
  (Wired 2018, Shankar 2017, Yang 2020, Gender Shades) and 4 secondary (Forbes,
  CBC, PetaPixel, The Register). All 8 URLs resolve under the link check. The
  deleted tweets, protected account, and paywalled NYT stay uncited as links,
  per the standing rulings.

## What round 02 changed

Worked the two new firsthand primaries into the "why it fails" section
(`the-skin-tone-gap`) as the training-data representation cause presented before
the Gender Shades effect: Shankar et al. (2017) for the amerocentric/eurocentric
dataset skew and the Hyderabad recognition drop, and Yang et al. (2020) for the
6.2% dark-skin share and the demeaning categories in ImageNet's person subtree,
both cited primary and both explicitly bounded as mechanism, not a measurement
of Google Photos. Renumbered all sources in first-citation order (Forbes 1, CBC
2, Wired 3, Shankar 4, Yang 5, Gender Shades 6, PetaPixel 7, Register 8). The
round-01 headline, dek, structure, bookends, and settled prose are otherwise
unchanged; the reworked passages were tightened to hold the word band and clear
the sentence-density warnings the additions raised.

## Open questions

None. The one round-01 blocker (the primary floor) is resolved by the new
evidence, and no evidence or voice question remains open.
