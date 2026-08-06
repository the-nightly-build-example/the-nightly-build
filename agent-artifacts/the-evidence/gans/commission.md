# Commission: the-evidence/gans

## Authorized work
Scheduled run for 2026-08-06. `nb duty` returned `the-evidence` in open mode:
choose a topic within the beat, do not repeat a published slug. One of five
articles this edition, one per due series. Process this article only.

NOTE ON PROVENANCE: an earlier commission this run picked already-published
topics because the history scan was too shallow. The full published-slug list is
recorded below; this topic was verified absent from it.

## Subject
The 2014 paper "Generative Adversarial Nets" (Ian Goodfellow, Jean
Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron
Courville, Yoshua Bengio; Université de Montréal), the paper that introduced
GANs and is routinely cited as the origin of the machine-made image era
(deepfakes, image generators). Read the document on the series' terms.

- What it is, who wrote it, why it became famous (NeurIPS/NIPS 2014; the
  two-network adversarial training idea; among the most-cited AI papers).
- What it ACTUALLY did: the paper trained small generators on MNIST digits, the
  Toronto Face Database, and CIFAR-10, and evaluated with a Parzen-window
  log-likelihood estimate plus eyeballed sample panels. Report the real scale
  honestly: the generated samples were tiny, low-resolution, and by the paper's
  own admission the Parzen-window metric "has somewhat high variance and does not
  perform well in high dimensional spaces." No faces-of-nonexistent-people, no
  high-res anything — that came years later (DCGAN 2015, ProGAN 2017,
  StyleGAN 2018/2019).
- Show the foundation under the reputation: a 2014 proof-of-concept with blurry
  32x32 samples and a weak evaluation metric became the citational origin of a
  whole generative-image industry. Draw that gap plainly.
- The paper's core theoretical claim (the minimax game's global optimum recovers
  the data distribution when G and D have enough capacity) is a result under
  idealized assumptions; in practice GAN training is famously unstable (mode
  collapse, non-convergence), which the paper only gestures at. Say where the
  clean theory and the messy practice diverge.
- Bring it to the present: how it is cited now, what held up (adversarial
  training as an idea; the genAI-image lineage) and what changed (diffusion
  models, not GANs, power today's leading image generators; GANs are largely
  superseded). When present usage does not match the 2014 evidence, say so.

Keep primary: read the paper itself (arXiv:1406.2661) for every claim about what
it did and reported. Secondary reporting only for how it is cited / the later
lineage.

## Required contribution
Separate what the GAN paper proved in 2014 (a clever training scheme and blurry
proof-of-concept samples under a weak metric) from what it is now credited with
(photoreal deepfakes and the generative-image era). The reader should leave able
to say what the paper actually generated, at what resolution, judged how, and
where the fame outran the 2014 evidence.

## Boundaries / do not repeat
FULL published the-evidence slugs (do not duplicate topic or slug): alexnet,
alphafold, alphago, atari-dqn, attention-is-all-you-need, bert, chain-of-thought,
chinchilla, deep-rl-from-human-preferences, deepseek-r1, emergent-abilities,
gpt-3-few-shot, gpt-4-technical-report, illusion-of-thinking, instructgpt,
scaling-laws-kaplan, sparks-of-agi, stochastic-parrots, the-bitter-lesson.
GANs and generative-image models are unrepresented. This is a lesson about the
*document* and its evidence; do not drift into a mechanics tutorial on how GANs
work step by step (that is the-mechanics' beat), and do not become an image-gen
incident piece (when-ai-breaks/gemini-image-generation exists). Stay on the paper.

## Template & policy
- Template: lesson; body 1200-2200 words; bookends fixed.
- Tags: none (series declares no tag fragments; ship without `--tag`; editorial
  `data-nb-tags` in the HTML are the writer's choice).
- Source policy: min 6 sources, at least 3 primary, at least 1 secondary.
- Balanced profile, model "capable", no `required` directives. Harness:
  claude-code-routine; roles run on the capable Claude model this routine runs on.
  Efforts: coach low, researcher high, writer medium, editor high.

## Neighboring articles this edition (keep distinct)
the-instruments/glue; the-mechanics/memorization;
what-could-go-wrong/sandbagging; when-ai-breaks/facebook-myanmar. No subject
overlap; nothing to coordinate beyond not cross-citing as new.

## Recent shapes to break (habits, not rules)
Recent the-evidence deks lean on the comma-and triad and the "the real X was Y"
reveal; recent headlines state a surprising count in the headline ("29 of 49",
"two gaming GPUs"). A number in the headline is fine only if the number is the
story; vary the move and do not reuse the "won on N GPUs" / "X on N of M" shape.
Vary section headings away from comma-and pairs. These travel to the writer.
