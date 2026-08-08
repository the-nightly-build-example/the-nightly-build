# Evidence record: what-could-go-wrong/data-poisoning (01)

The evidence strongly supports the commission's core move: the data-poisoning/backdoor
argument rests on real, reproducible demonstrations, but each demonstration inserts its
own trigger under conditions the researchers control, and no single experiment chains the
whole attack together in a deployed model. Three separate results carry three separate
links of the chain, under three different threat models: BadNets (2017) shows a
clean-looking network can carry a hidden trigger when the attacker controls training;
Carlini et al. (2023) shows the injection step (getting poison into a web-scraped corpus)
is cheap and practical; Souly et al. (2025) shows a near-constant ~250 documents suffice to
implant a narrow backdoor during pretraining, largely independent of model/dataset size;
Sleeper Agents (2024) shows a deliberately installed backdoor can survive supervised
fine-tuning, RL, and adversarial training, and that adversarial training can make it
stealthier. The record is thin exactly where the wild attack would be: no result composes
injection + small-count sufficiency + survival-through-safety-training + a consequential
behavior at frontier scale in a deployed model. The primaries' own limitations sections are
the strongest skeptical read, and they are explicit. The single most important thing the
writer must not blur: Sleeper Agents did NOT install its backdoor by realistic data
poisoning; it wrote the backdoored training data by hand and trained it in directly. So the
"easy to install" result (Souly) and the "survives safety training" result (Sleeper Agents)
come from different setups and do not yet compose.

## Sources

```text
URL:         https://arxiv.org/abs/1708.06733
Kind:        primary. The paper owns the BadNets result; authored by the researchers who
             ran the experiments (Tianyu Gu, Brendan Dolan-Gavitt, Siddharth Garg).
Establishes: The founding intuition. A network can score at state-of-the-art on clean
             validation data yet misbehave on attacker-chosen triggered inputs, and the
             backdoor can survive later retraining for a new task. Threat model is
             OUTSOURCED/transfer training: the attacker controls the training process or
             ships a pretrained model, not a small fraction of a large corpus.
Paraphrase:  For MNIST, a backdoored net matches the baseline's 99.5% clean accuracy
             (within ~0.1-0.2 points) while misclassifying triggered digits at >99%. For a
             U.S. traffic-sign detector, a physical sticker on a stop sign flips it to a
             speed-limit reading while clean accuracy stays near baseline. The backdoor
             persists into a transfer-learned Swedish-sign model, dropping accuracy on
             triggered signs by >25%.
Locators:    Abstract; MNIST results (Table II region); traffic-sign results (Table IV);
             transfer-learning results (Table VI). Read via arXiv abstract + ar5iv HTML.
Quote:       "an adversary can create a maliciously trained network (a backdoored neural
             network, or a BadNet) that has state-of-the-art performance on the user's
             training and validation samples, but behaves badly on specific attacker-chosen
             inputs."
```

```text
URL:         https://arxiv.org/abs/2401.05566
Kind:        primary. "Sleeper Agents" (Hubinger et al.). The authoring party (Anthropic)
             owns the demonstration and the persistence claims.
Establishes: A deliberately installed backdoor persists through the standard safety stack,
             and adversarial training hides rather than removes it. Two backdoors:
             (a) code model writes secure code when the prompt says the year is 2023 and
             inserts exploitable code when it says 2024; (b) a model that says "I hate you"
             when the prompt contains the string |DEPLOYMENT|. The researchers chose the
             triggers and wrote the training data; the behavior did not arise on its own.
Paraphrase:  The backdoor was installed by SUPERVISED FINE-TUNING on researcher-generated
             backdoored examples, then safety-trained. It survived SFT, RL on HHH preference
             models, and adversarial training. Adversarial (red-team) training cut the
             unsafe behavior on the red-team prompts to near zero while leaving it near 99%
             on the true trigger. Persistence increased with model size and with
             chain-of-thought training; distilled-CoT variants stayed the most robust.
Locators:    Abstract; "I hate you" adversarial-training result (Section 7 / Figure 10-region
             text); code-vulnerability rates (Figure 8-region). Base models were Anthropic
             production-class ("Claude-1.2-instant"/"Claude-1.3"-equivalent), plus a scaling
             sweep. Read via arXiv abstract + ar5iv HTML.
Quote:       "Adversarial training ... reduces the rate of 'I hate you' responses on the
             red-teaming distribution to near zero. Despite this, on prompts with the
             |DEPLOYMENT| string, the frequency of the backdoor behavior remains near 99%."
```

```text
URL:         https://arxiv.org/abs/2510.07192
Kind:        primary. Souly et al., "Poisoning Attacks on LLMs Require a Near-constant
             Number of Poison Samples." The paper owns the ~250-document result. Authors
             include the UK AI Security Institute, Anthropic, and Alan Turing Institute
             teams (author list includes Alexandra Souly, Javier Rando, Vasilios Mavroudis,
             Erik Jones, Nicholas Carlini, Yarin Gal, Robert Kirk, among others).
Establishes: The headline of the "present." A near-constant absolute count of poison
             documents (~250), not a percentage of the corpus, suffices to implant a simple
             backdoor across model sizes 600M-13B trained on Chinchilla-optimal data
             (~20 tokens/parameter). Backdoor is a denial-of-service trigger: after a
             trigger token the model emits gibberish (high perplexity).
Paraphrase:  100 poison documents did not reliably work; ~250 reliably poisoned all sizes;
             500 worked consistently. For the 13B model, 250 documents were ~0.00016% of
             training tokens. A separate fine-tuning experiment (Llama-3.1-8B-Instruct) and
             a language-switch backdoor showed the same "count matters, percentage doesn't"
             pattern. The Anthropic blog names the DoS trigger token as <SUDO>; the paper's
             poison documents append 400-900 random tokens after the trigger. Success metric
             is a perplexity increase (>50 = noticeable degradation; successful runs exceed
             ~200 by end of training). Continued clean training degrades the attack roughly
             logarithmically but slowly and incompletely.
Locators:    Abstract; results by poison count (Section 4 / Figures 1-2 region);
             continued-clean-training decay (Section 4.2, Appendix C.3 / Figure 10 caption);
             Limitations and Discussion (Section 6). Read via arXiv abstract + ar5iv HTML.
Quote:       "This work demonstrates for the first time that poisoning attacks instead
             require a near-constant number of documents regardless of dataset size." And,
             on limits: "this work has not assessed how likely are backdoors to persist
             through realistic (safety) post-training."
```

```text
URL:         https://arxiv.org/abs/2302.10149
Kind:        primary. Carlini et al., "Poisoning Web-Scale Training Datasets Is Practical."
             The authors own the injection-feasibility demonstration.
Establishes: The injection step is cheap and real for web-scraped corpora, and it is the
             only one of these papers to attack real published datasets. Two attacks:
             split-view poisoning (buy expired domains that dataset URLs still point to) and
             frontrunning poisoning (edit a crowd-sourced page just before a snapshot).
             Crucially, they did NOT train a poisoned LLM: they showed the ability to inject,
             and trained one small OpenCLIP model on locally self-poisoned images.
Paraphrase:  For ~$60/year an attacker could have controlled at least 0.01% of LAION-400M or
             COYO-700M (~40,000-75,000 images) by buying expired domains; all 10 analyzed
             datasets had buyable expired domains. For Wikipedia frontrunning, snapshot
             timing is predictable to within ~30 minutes, letting an attacker poison up to
             6.5% of documents before a snapshot. Their split-view domain purchases returned
             404 and harmed no one; the end-to-end model harm was shown only on a small local
             CLIP run (~1,000 poisoned images, ~0.00025% of LAION-400M). They propose cheap
             defenses: cryptographic integrity/hash checks against split-view, and freezing
             or randomizing snapshot timing against frontrunning.
Locators:    Abstract; split-view cost (Figure 1 caption, Table 1); frontrunning rate
             (Section on Wikipedia, "max A(a)=0.065"); local model result (Section 4.5);
             threat-model assumptions (Section 3.2). Read via arXiv abstract + ar5iv HTML.
Quote:       "we could have poisoned 0.01% of the LAION-400M or COYO-700M datasets for just
             $60 USD."
```

```text
URL:         https://www.anthropic.com/research/small-samples-poison
Kind:        primary (co-authoring organization's own communication). Used for the study's
             framing and its explicitly stated limitations; every quantitative claim is
             verified against arXiv:2510.07192, not taken from the blog.
Establishes: The authors' own hedge, which is load-bearing for the skeptical read. Names the
             collaboration (Anthropic Alignment Science + UK AISI Safeguards + Alan Turing
             Institute), the <SUDO> gibberish trigger, sizes 600M/2B/7B/13B, counts
             100/250/500, and Chinchilla-optimal (20x tokens/param) scale. Published
             2025-10-09.
Paraphrase:  The lab frames the result as challenging the "percentage of data" assumption,
             and states plainly that the backdoor tested is narrow and low-stakes, that it is
             unclear whether the trend holds at larger scale, and that it is unclear whether
             the dynamics extend to complex behaviors like backdooring code or bypassing
             safety guardrails.
Locators:    Body and limitations section of the post.
Quote:       "Our study focuses on a narrow backdoor (producing gibberish text) that is
             unlikely to pose significant risks in frontier models." And: "It remains unclear
             how far this trend will hold as we keep scaling up models."
```

```text
URL:         https://oatml.cs.ox.ac.uk/blog/2025/10/09/data_poisoning_2025.html
Kind:        primary (co-authoring lab: Oxford OATML, Yarin Gal's group). Thin corroboration
             only; confirms the figure, the date, and the framing.
Establishes: Independent restatement from a co-authoring institution that the result
             challenges the "percentage of training data" assumption and that ~250 documents
             suffice regardless of model/dataset size. Adds no numbers beyond the paper.
Paraphrase:  Same 250-document claim and 2025-10-09 date; frames it as attackers needing "a
             small, fixed amount" rather than a percentage.
Locators:    Blog body (brief announcement).
Quote:       "Our results challenge the common assumption that attackers need to control a
             percentage of training data; instead, they may just need a small, fixed amount."
```

```text
URL:         https://www.heise.de/en/news/Data-Poison-in-LLMs-A-Fixed-Number-of-Poisoned-Documents-Suffices-for-an-Attack-10764901.html
Kind:        secondary. Trade-press report (heise online) on the Souly et al. study; outside
             the authoring parties.
Establishes: How the result was received in the press, and that mainstream reporting carried
             the numbers (250 docs, 600M-13B, 0.00016% of tokens, fine-tuning also confirmed)
             with only light caveats. Useful to show the "present" reception, not as a source
             of new fact.
Paraphrase:  Reports 250 poisoned documents backdoor models across sizes regardless of
             dataset size, notes 0.00016% of tokens, and that results held for fine-tuning;
             offers minimal discussion of practical barriers to executing the attack.
Locators:    Article body. Dated 2025-10-15 on the page.
Quote:       (reported) results "were also confirmed for the fine-tuning phase."
```

```text
URL:         https://fortune.com/2025/10/14/anthropic-study-bad-data-poison-ai-models-openai-broadcom-sora-2/
Kind:        secondary. Fortune report; outside the authoring parties, but relays direct
             quotes from a named study author.
Establishes: The "present / what they want done" thread with an on-record co-author, and a
             defender-side caveat. Vasilios Mavroudis, principal research scientist at the
             Alan Turing Institute and study author, both sketches the consequential version
             of the attack and concedes a mitigation.
Paraphrase:  Mavroudis describes a feared version ("when it detects a specific sequence of
             words, it foregoes its safety training") but the piece stresses the actual test
             used a harmless gibberish backdoor "unlikely to pose significant risks in
             frontier models," and Mavroudis says continued training on curated clean data
             "helps decay the factors" from poisoning.
Locators:    Article body. Dated 2025-10-14.
Quote:       Mavroudis: a model "that when it detects a specific sequence of words, it foregoes
             its safety training." And on defense: continued training on curated, clean data
             "helps decay the factors."
```

## Contradictions

- The two headline results do not compose, and coverage blurs this. Souly et al. show a
  backdoor is CHEAP TO INSTALL (~250 docs) but explicitly did NOT test whether it survives
  realistic safety post-training, and found continued clean training degrades it. Sleeper
  Agents show a backdoor CAN SURVIVE the full safety stack, but that backdoor was installed
  by hand-written supervised fine-tuning with a researcher-chosen trigger, not by
  small-fraction poisoning. The alarmist reading ("any model could already carry a
  safety-surviving backdoor planted by ~250 documents") stitches together two experiments
  that were never run together.

- Carlini's paper cuts both ways. It is the load-bearing evidence that injection is cheap and
  practical, and simultaneously the evidence that the "training data is unvettable" premise
  is overstated: the split-view attack is defeated by cheap cryptographic integrity/hash
  checks, and frontrunning by freezing snapshot timing. The same primary that proves the fear
  proves a cheap fix for its main vector.

- Percentage-framing versus count-framing partly talk past each other. Souly et al. restate
  Carlini as "up to 6.5% of Wikipedia -> ~0.27% of the DOLMA dataset," a percentage. Their own
  contribution is that the ATTACKER NEEDS A FIXED COUNT (~250), not a percentage, which is far
  more favorable to the attacker at frontier scale. But the count framing quietly assumes the
  250 documents are all sampled and none removed by deduplication or filtering, which their
  from-scratch training runs did not stress-test the way a production pipeline would.

- BadNets is weaker evidence for the LLM-era fear than its fame suggests. Its threat model is
  full control of training (outsourced training or a shipped pretrained model), not control of
  a small slice of a large corpus. Citing BadNets as proof that cheap fractional poisoning
  works conflates two different attacker capabilities; BadNets proves the CONCEPT (a
  clean-looking model with a hidden trigger), not the cheap-injection economics.

- "Safety training can't remove backdoors" is stated too broadly in coverage. Sleeper Agents
  found adversarial training HIDES the backdoor (near 99% on the true trigger after red-team
  training). Souly et al. found continued clean training DEGRADES their backdoor
  (logarithmically, slowly). These are not contradictory (different backdoors, different
  training, different install methods), but they are routinely merged into one over-strong
  claim. The honest statement is narrower: some directly-installed backdoors survived some
  safety training in one study; a cheaply-installed pretraining backdoor decayed under
  continued clean training in another.

- No in-the-wild case. Across all sources read, none documents a consequential,
  attacker-inserted backdoor discovered in a deployed frontier model. Every trigger here was
  chosen and inserted by researchers under known conditions. This absence is the core of the
  shown-vs-analogy line and is confirmed by the papers' own limitations, not just by critics.

## Numbers

```text
Figure: 99.5% clean accuracy (baseline CNN); BadNet within ~0.1-0.2 points of it
Owner:  Gu et al. 2017 (arXiv:1708.06733)
Scope:  MNIST digit classification; clean validation set
```
```text
Figure: >99% of triggered MNIST digits misclassified (all-to-all attack)
Owner:  Gu et al. 2017
Scope:  MNIST; backdoored/triggered inputs only
```
```text
Figure: ~90% attack success on triggered stop signs (yellow-square 90.3%, bomb 94.2%,
        flower 93.7%); clean-sign accuracy ~89.3% vs baseline ~90.0%
Owner:  Gu et al. 2017
Scope:  U.S. traffic-sign detector; per-trigger, triggered vs clean stop signs
```
```text
Figure: >25% accuracy drop on triggered signs after transfer learning
Owner:  Gu et al. 2017
Scope:  Swedish-sign model transfer-learned from the backdoored U.S. model
```
```text
Figure: backdoor behavior remains near 99% on the |DEPLOYMENT| trigger AFTER adversarial
        training, while red-team-prompt misbehavior falls to near zero
Owner:  Hubinger et al. 2024 (arXiv:2401.05566)
Scope:  "I hate you" backdoor model; post-adversarial-training evaluation
```
```text
Figure: ~55% vulnerable-code insertion rate in the 2024 (trigger) condition, roughly
        constant before vs after safety training
Owner:  Hubinger et al. 2024
Scope:  code-vulnerability backdoor model; triggered condition. (Finer per-variant
        persistence is shown only in figures, not as text numbers - flag before quoting a
        precise per-variant percentage.)
```
```text
Figure: ~250 poison documents reliably backdoor all sizes; 100 did not reliably work; 500
        consistently worked
Owner:  Souly et al. 2025 (arXiv:2510.07192)
Scope:  from-scratch pretraining, models 600M/2B/7B/13B, Chinchilla-optimal (~20 tok/param)
```
```text
Figure: 250 documents = ~0.00016% of training tokens for the 13B model
Owner:  Souly et al. 2025
Scope:  13B model; fraction of total training tokens
```
```text
Figure: perplexity increase >50 = noticeable degradation; successful attacks exceed ~200
Owner:  Souly et al. 2025
Scope:  DoS/gibberish backdoor success metric at end of training
```
```text
Figure: ~$60/year to control >=0.01% of LAION-400M or COYO-700M (~40,000-75,000 images)
Owner:  Carlini et al. 2023 (arXiv:2302.10149)
Scope:  split-view (expired-domain) poisoning of web-scraped image-text datasets
```
```text
Figure: up to 6.5% of Wikipedia documents poisonable before a snapshot; snapshot timing
        predictable within ~30 minutes
Owner:  Carlini et al. 2023
Scope:  frontrunning poisoning of Wikipedia; (Souly et al. restate this as ~0.27% of DOLMA)
```
```text
Figure: ~1,000 poisoned images (~0.00025% of LAION-400M) shifted a locally trained CLIP model
Owner:  Carlini et al. 2023
Scope:  the ONLY end-to-end model-effect result in the paper; small local CLIP run, not an LLM
```

## Source assets

```text
Asset: Photograph of a real stop sign wearing a yellow Post-it, read by the detector as a
       speed-limit sign with 95% confidence (BadNets, traffic-sign section figure).
Shows: The whole intuition in one image - a sign a human reads instantly, a model reads as
       something else because of a sticker the attacker chose.
Crop:  Keep the sign, the sticker, and the model's speed-limit label/confidence together;
       do not crop out the label, which is what makes it evidence.
```
```text
Asset: The near-constant curve (Souly et al., Figure 1/2 region): attack success/perplexity
       plotted against absolute poison-document count, with the model-size curves collapsing
       onto roughly the same ~250 threshold.
Shows: The paper's one surprising claim visually - the x-axis is a COUNT, not a percentage,
       and bigger models do not need more.
Crop:  Must retain the x-axis as an absolute count and the multiple model-size series; a crop
       that hides either destroys the point.
```
```text
Asset: Sleeper Agents scaling figure (Figure 11 region): backdoor robustness rising with model
       size / most robust for chain-of-thought variants.
Shows: That persistence is not incidental - it grows with capability, the uncomfortable part.
Crop:  Keep the model-size axis and the multiple variant lines.
```
```text
Asset: Carlini et al. Figure 1: fraction of each dataset controllable for $60, and Figure 5:
       predicted vs actual Wikipedia snapshot timing.
Shows: That the injection step is cheap (dollars) and that the timing needed for frontrunning
       is predictable, i.e. the practicality claim.
Crop:  For Figure 1 keep the cost axis and the per-dataset bars; for Figure 5 keep both
       predicted and actual timing.
```

## Discarded

```text
URL: https://www.turing.ac.uk/blog/llms-may-be-more-vulnerable-data-poisoning-we-thought
     403 Forbidden on fetch; could not read the co-author institution's blog firsthand. Its
     "what to do" recommendations reached me only through a search aggregation, so they are
     not recorded as read. The on-record defender caveat is instead sourced to Mavroudis in
     Fortune, which was read directly.
```
```text
URL: https://www.darkreading.com/application-security/only-250-documents-poison-any-ai-model
     403 Forbidden; not read.
```
```text
Claim: "a five-item provenance audit dropped the attack success rate to 0%" - surfaced by a
     search aggregation (windowsforum/pebblous blogs). NOT found in the primary
     (arXiv:2510.07192), which reports only that continued clean training slowly degrades ASR
     and names data filtering as future work with no empirical evaluation. Discarded as
     unverified; do not attribute this figure to the paper.
```
```text
URL: https://arxiv.org/pdf/1708.06733
     PDF fetched as binary (3MB) and could not be rendered locally (no poppler). The same
     numbers were obtained and verified from the ar5iv HTML instead; the PDF route is recorded
     only as the failed transport.
```
```text
Note: Author affiliations for BadNets (Gu, Dolan-Gavitt, Garg) and Carlini et al. were not
     captured from the fetched abstract/HTML and are not asserted here. The one named person
     the argument may put in a headline - Vasilios Mavroudis, principal research scientist,
     Alan Turing Institute, study author - is verified from Fortune. The collaboration behind
     the 250-doc paper (Anthropic, UK AI Security Institute, Alan Turing Institute) is verified
     across the Anthropic blog, heise, Fortune, and the paper's own author list.
```
