# Commission: the-evidence/adversarial-examples

## Assignment

Read "Explaining and Harnessing Adversarial Examples" (Ian Goodfellow, Jonathon
Shlens, Christian Szegedy, ICLR 2015; arXiv 1412.6572). This is the paper behind
the famous image where a barely altered photo of a panda is classified as a
gibbon with high confidence. The reader should finish knowing what the paper
actually claimed and did, and how its problem has and has not been solved since.

State what the document is and why it became famous. Walk through what it did: the
linear explanation of adversarial examples (that they arise because models behave
too linearly, not too nonlinearly), the Fast Gradient Sign Method it introduced as
a cheap way to generate them, and the demonstrations (the panda/GoogLeNet example
and the MNIST results). Show the scale honestly: what models and datasets, the
size of the perturbation, the confidence numbers.

Then bring it to the present. Adversarial robustness is still largely unsolved a
decade later; simple defenses were broken, and the paper's own linear explanation
is contested by later work. Real-world adversarial attacks exist but the
imperceptible-perturbation threat model is a specific setting. Say plainly what
held up and what did not.

## Angle and boundaries

- Center the 2015 paper's own claims and numbers, verified against the paper.
- Read the predecessor primary, Szegedy et al. 2013 "Intriguing properties of
  neural networks," which first exhibited adversarial examples, so the article can
  say what this paper added (explanation + cheap attack + adversarial training),
  not just what adversarial examples are.
- Bring it forward with at least one later primary that shows the problem endured
  (e.g. Madry et al. 2018 on PGD/robust training, Athalye et al. 2018 breaking
  defenses, or Ilyas et al. 2019 "features not bugs"). Say what today's evidence
  shows about whether the linear explanation and FGSM-era optimism held.
- One document. Do not sprawl into a survey of all adversarial ML. No math lesson;
  teach the mechanism in plain words with the panda example as the worked case.
- Sibling deconfliction: this is the-evidence reading a paper. It is not the
  when-ai-breaks detector piece and not a risk argument; keep it to the document.

## Sources

Policy: at least 6 sources, at least 3 primary, at least 1 secondary. Primary
candidates: the paper (arXiv 1412.6572), Szegedy et al. 2013, and one later
primary on the enduring problem. Researcher owns the final set and must verify
every figure (perturbation size, confidence, datasets) against its owning primary
and search for what breaks the "still unsolved" framing.

## Production policy (balanced profile)

- researcher high, writing-coach low, writer medium, editor high; capable model.
- nb-meta harness `claude-code-routine`, model `claude-opus-4-8`, date 2026-08-31,
  series `the-evidence`, slug `adversarial-examples`. No `required` directive.

## This edition's siblings (keep each piece distinct)

Publishing tonight with lessons on the toxicity score, why image generators mangle
hands, the AI-boxing argument, and AI writing-detector failures. This piece owns
the adversarial-examples paper as a document. No overlap expected.

## Recent-pattern notes (habits not to inherit)

Recent the-evidence deks/headlines, not to echo in mold:
- "The diffusion paper behind today's image generators could not take a prompt"
- "Tested on Atari and robots in 2017, PPO now tunes billion-parameter models"
- "Google packed a whole sentence into a single vector"
- "LoRA matched full fine-tuning by training 4.7M of GPT-3's 175 billion weights"
- "The Vision Transformer lost to a plain CNN until it was fed 300 million images"
The "The X paper behind today's Y" construction and the "did A until B" reversal
have run recently. The most recent piece (denoising-diffusion) used an
nb-stat-strip opener and a "where the X actually comes from" closer; do not default
to that shape. Only the two bookends address the reader. No Verdict block at the
body's close.
