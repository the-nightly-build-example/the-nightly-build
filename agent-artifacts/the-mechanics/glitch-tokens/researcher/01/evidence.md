# Evidence: the-mechanics/glitch-tokens (01)

The evidence supports the commissioned mechanism firmly. Two independent primary
investigations establish the behavior (specific token strings that GPT models
cannot repeat and instead evade, substitute, insult, or spell out doom), a
peer-reviewed follow-up (Land & Bartolo, EMNLP 2024) measures the cause across
25 models and ties it directly to training-data frequency, and the GPT-2 paper
plus the tokenizer source establish that the vocabulary is a fixed artifact
built before and separately from any model's training. The origin story
(usernames from the r/counting subreddit, plus e-commerce and game-backend
strings) is owned by the investigators' own archaeology and corroborated by the
peer-reviewed paper. Three things are thinner than the popular framing suggests,
and the record flags each: the canonical " SolidGoldMagikarp" does not verify as
under-trained in GPT-2 itself (only in models that reused its tokenizer), under-
training is one cause among several rather than the only one, and no source
explains the path from a dead embedding to a *specific* weird output. The last
is the commission's declared open question and it stays open.

## Sources

```text
URL:         https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation
Kind:        primary. The two investigators reporting the behavior they found firsthand. A research write-up by the discoverers owns the observation.
Establishes: The discovery, the method, the token list, and the core behavior. Jessica Rumbelow and Matthew Watkins did the work at SERI-MATS over two months; posted 5 Feb 2023. They ran k-means clustering over GPT-J's token embedding space and found a set of tokens sitting closest to the centroid of all 50,257 tokens. Asking GPT-3 (davinci-instruct-beta) and ChatGPT to repeat these strings back produced failure rather than the string: substitution, evasion, insults, hallucination, claims of inability. They call the tokens "anomalous", "weird", and "unspeakable". They also report the tokens reliably break determinism in the OpenAI GPT-3 playground at temperature 0.
Paraphrase:  A cluster of vocabulary tokens sits near the embedding-space centroid; when prompted to repeat one, GPT models cannot, and fail in characteristic ways instead.
Locators:    Post body, "Prompt generation" and "Anomalous tokens" sections; the verbatim Python list of the token cluster.
Quote:       "Please repeat back the string ' SolidGoldMagikarp' to me" returns "distribute". The exact 141-string list is reproduced in the post, including ' SolidGoldMagikarp', ' TheNitromeFan', ' RandomRedditorWithNo', ' externalToEVA', 'InstoreAndOnline', 'PsyNetMessage', ' petertodd', 'StreamerBot', ' guiActiveUnfocused', 'rawdownloadcloneembedreportprint', '龍喚士', ' Leilan'.
```

```text
URL:         https://www.lesswrong.com/posts/Ya9LzwEbfaAMY8ABo/solidgoldmagikarp-ii-technical-details-and-more-recent
Kind:        primary. Same investigators, follow-up technical detail on their own finding.
Establishes: The proposed mechanism in the investigators' own words: an anomalous token's embedding sits near the overall centroid because it was rarely or never encountered in training, so it stayed close to its initialization. Posted 6 Feb 2023.
Paraphrase:  The tokens are near the centroid because training barely moved their embeddings from where initialization put them.
Locators:    Post body, technical-details discussion of centroid proximity and initialization.
Quote:       The post frames closeness to the centroid as "an inhibiting factor in the ability of a GPT model to repeat that token's string", and attributes it to tokens that "remain very close to their initialisations, since they are rarely (or never) encountered during training". (Wording confirmed via the post; treat the exact phrasing as the investigators' hypothesis, not settled fact.)
```

```text
URL:         https://www.lesswrong.com/posts/8viQEp8KBg2QSW4Yc/solidgoldmagikarp-iii-glitch-token-archaeology
Kind:        primary. The investigators' own tracing of where the strings came from.
Establishes: The origin of the strings. Posted 14 Feb 2023 by Matthew Watkins. Many glitch tokens are usernames from r/counting, a subreddit whose users collaboratively count upward and so post enormous volumes of near-identical short messages. Prolific counters' handles (SolidGoldMagikarp, TheNitromeFan, RandomRedditorWithNo, davidjl123, Smartstocks, Adinida) appeared often enough in the tokenizer's source data to be merged into single tokens. Other tokens trace to e-commerce site backends (externalToEVA, InstoreAndOnline, catentry, wcsstore), the Rocket League game (PsyNetMessage, StreamerBot), and the mobile game Puzzle & Dragons (龍喚士, Leilan, TAMADRA).
Paraphrase:  The strings are real artifacts: forum usernames and software-backend identifiers that were frequent in the tokenizer corpus but scarce or absent in the model's training text.
Locators:    Post body, per-token origin entries.
Quote:       None extracted verbatim beyond token strings; the origin attributions above are the post's own findings.
```

```text
URL:         https://arxiv.org/abs/2405.05417   (peer-reviewed version: https://aclanthology.org/2024.emnlp-main.649/)
Kind:        primary. Original peer-reviewed research (EMNLP 2024). Owns its measurements.
Establishes: The systematic follow-up. Sander Land and Max Bartolo (both Cohere) define "under-trained" (or "untrained") tokens as "tokens present in the tokenizer vocabulary but that are nearly or entirely absent during model training." They detect candidates from model weights alone: for tied-embedding models, the cosine distance between each output embedding and the mean of known-unused token embeddings; for untied models, the L2 norm of the input embedding. Untrained tokens all get pushed in a shared direction (away from the mean output vector) during training, letting the model assign them strongly negative logits, which is why they are hard to produce. Candidates in the top 2% are verified by prompting: a token is confirmed if its output probability stays below 1% on prompts that would give an ordinary token high probability. On OLMo v1.7, where training-data counts are public, all indicators correlate with training frequency across ten orders of magnitude. They analyzed 25 models; verified under-trained tokens run 0.1-1% of the vocabulary across every model tested.
Paraphrase:  Under-trained tokens are detectable from embeddings alone, the indicator tracks how often the token appeared in training, and the phenomenon is present in every current model family they checked.
Locators:    Abstract; Sec. 2.2 (indicators); Sec. 2.3 (verification); Sec. 2.4 (OLMo correlation, 191/49,575 verified); Sec. 3 and Table 1 (per-model counts); Sec. 4 (closed models); Sec. 5 (conclusion).
Quote:       "The disconnect between tokenizer creation and model training in language models allows for specific inputs, such as the infamous _SolidGoldMagikarp token, to induce unwanted model behaviour." Table 1 caption: "the leading '_' in tokens such as _SolidGoldMagikarp indicates a leading space."
```

```text
URL:         https://github.com/openai/gpt-2/blob/master/src/encoder.py
Kind:        primary. The tokenizer code itself is the artifact that owns the claim about how the vocabulary is loaded.
Establishes: The tokenizer vocabulary is a static, pre-built artifact. get_encoder() loads two fixed files from disk: encoder.json (the token-to-id vocabulary) and vocab.bpe (the ordered merge rules). Both are computed in advance and loaded unchanged at runtime, identical regardless of which trained weights are used.
Paraphrase:  GPT-2 tokenization is a fixed lookup table plus a fixed merge list, decoupled from any model's training run.
Locators:    get_encoder(), the json.load / bpe_data.read calls and bpe_merges construction.
Quote:       None needed; the load-from-disk structure is the evidence.
```

```text
URL:         https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
Kind:        primary. The GPT-2 paper (Radford et al., 2019). Owns the tokenizer-construction and dataset claims.
Establishes: Byte-level BPE, the vocabulary size, and the training corpus. BPE "effectively interpolates between word level inputs for frequent symbol sequences and character level inputs for infrequent symbol sequences", using "a greedy frequency based heuristic for building the token vocabulary." The vocabulary "is expanded to 50,257." The training set, WebText, was built by scraping "all outbound links from Reddit ... which received at least 3 karma."
Paraphrase:  The vocabulary is frequency-built from a corpus, capped at 50,257; the model trained on WebText, a Reddit-outbound-link scrape. The two corpora are related but not identical, which is the gap the mechanism turns on.
Locators:    Sec. 2.2 (Input Representation) for BPE and vocabulary; Sec. 2.1 for WebText and the 3-karma heuristic; the architecture passage stating "The vocabulary is expanded to 50,257."
Quote:       "The vocabulary is expanded to 50,257." and "we scraped all outbound links from Reddit, a social media platform, which received at least 3 karma."
```

```text
URL:         https://en.wikipedia.org/wiki/Glitch_token
Kind:        secondary. Encyclopedic summary written by editors outside the research, reporting the phenomenon.
Establishes: That the term and the canonical example have entered general reference. Defines a glitch token as one "that causes unexpected or 'glitchy' outputs when used in a prompt", gives the " SolidGoldMagikarp"/"Distribute" behavior on Text-Davinci-003, and lists further examples (TheNitrome, PsyNetMessage, davidjl). Cites later detection/mitigation papers (Li et al. 2024, Zhang et al. 2024), evidence the problem is still an active research target.
Paraphrase:  A third-party reference confirms the behavior and the canonical example, and points to continuing detection work beyond Fishing for Magikarp.
Locators:    Lead definition; examples table; references.
Quote:       "a glitch token is [a] token that causes unexpected or 'glitchy' outputs when used in a prompt".
```

```text
URL:         https://www.kith.org/words/2023/12/10/solidgoldmagikarp-and-other-glitch-tokens/
Kind:        secondary. A third-party explainer (Jed Hartman, 10 Dec 2023) reporting on the LessWrong investigations.
Establishes: That the finding was reported and understood outside the original venue. Restates the " SolidGoldMagikarp" -> "distribute" behavior and cites the Rumbelow/Watkins posts as its sources. Thin on mechanism; useful only as a plain-language secondary retelling and a check that the behavior is reported consistently.
Paraphrase:  An independent writer repeats the core behavior and points back to the primary posts.
Locators:    Post body; its source links to the LessWrong series.
Quote:       "'Glitch tokens' are words (well, strings of characters) that cause GPT and other LLMs to behave particularly weirdly."
```

## Contradictions

Real tension exists between the popular framing and what the primaries say. None
of it sinks the commissioned angle, but the writer must not overstate.

- **"GPT-2 has the glitch token" is loose.** Land & Bartolo's Table 1 does not
  list " SolidGoldMagikarp" among GPT-2's verified under-trained tokens. It
  appears as verified only in GPT-J 6B and Phi-2, two models that reuse the
  GPT-2 tokenizer but train on different data (The Pile and Microsoft's mix),
  "likely due to their training data being further removed from the data used to
  train the tokenizer." The original behavior was observed on GPT-3 models
  (davinci-instruct-beta) and ChatGPT, with the embedding geometry examined on
  GPT-J. So the shared tokenizer is the constant; the specific model determines
  whether a given string is actually dead. The lesson should attribute the
  behavior to a tokenizer-model *pairing*, not to "GPT-2".

- **Under-training is one cause, not the only one.** Land & Bartolo separate
  several failure classes: intermediate BPE "junk" fragments that survive a
  merge, "unreachable" tokens that normal text never produces (blocked in pre-
  tokenization), tokenizer configuration errors, and tokens highly sensitive to
  leading-space splitting in the cl100k tokenizer (e.g. $PostalCodesNL,
  \tTokenNameIdentifier). Some of these are a tokenization mismatch between
  training and inference rather than a token that was simply rare. "In the
  vocabulary but absent from training" is the cleanest and most common case, not
  a universal one.

- **Vocabulary presence does not prove under-training; you must measure.** The
  paper found special tokens such as <mask>, which they expected to be untrained,
  showing signs of having been seen in training, because code and tutorials use
  those strings as plain text. The direction runs both ways: a token can look
  exotic and be fine, or look ordinary and be dead. The indicator, not the
  string's appearance, is what settles it.

- **The precise-mechanism claim is a hypothesis on one side and a measurement on
  the other.** The original posts say the embedding sits near the centroid and
  stayed near initialization. Land & Bartolo give a sharper account for the
  output side: untrained embeddings are pushed to a common direction so the model
  emits strongly negative logits for them. "Stays near random initialization"
  is true enough for the input embedding but is a simplification of the trained
  output-side behavior. Keep the two sides distinct if the lesson goes that deep.

- **Angle-breaking search came up mostly empty, which favors the commission.**
  The counter-hypothesis (glitch behavior on *well-trained* tokens) is not
  supported: Figure 2 shows the detection indicators tracking training frequency
  across ten orders of magnitude, i.e. the effect really is about how little the
  token was trained. The one genuine exception is the pre-tokenization-mismatch
  class above, where the token may not be under-trained so much as unreachable or
  split differently at inference.

## Numbers

```text
Figure: 50,257 tokens
Owner:  GPT-2 paper (Radford et al., 2019), Sec. 2.2 / architecture
Scope:  The full fixed GPT-2 byte-level BPE vocabulary. Reused by GPT-3, GPT-J, Phi-2, and others.
```

```text
Figure: 141 tokens
Owner:  Rumbelow & Watkins, SolidGoldMagikarp I
Scope:  The size of the "weird tokens" cluster they reproduce in the post, found nearest the centroid of the GPT-J / GPT-2 token embedding space. Treat as the original list's size, not a census of all glitch tokens.
```

```text
Figure: 0.1-1% of vocabulary
Owner:  Land & Bartolo, Sec. 5 (Discussion)
Scope:  Share of the vocabulary that is "severely under-trained", holding across all 25 tested models under their conservative verification threshold.
```

```text
Figure: 191 of 49,575 tokens verified (175 of 993 in the top-2% candidate set)
Owner:  Land & Bartolo, Sec. 2.4
Scope:  OLMo v1.7 7B, the model with public training-data counts used to validate that the indicator tracks true training frequency.
```

```text
Figure: per-model verified/tested counts
Owner:  Land & Bartolo, Table 1
Scope:  Examples: GPT-2 XL 67/999; GPT-J 6B 200/999; Phi-2 103/999; GPT-NeoX 20B 10/993; Pythia 6.7B 14/993; Llama3 8B 556/2540; Gemma 2B 3161/5117. GPT-NeoX and Pythia are low because their tokenizer was trained on the same corpus (The Pile) as the model, the cleanest confirmation of the alignment mechanism.
```

```text
Figure: Reddit outbound links with >= 3 karma
Owner:  GPT-2 paper, Sec. 2.1
Scope:  The construction rule for WebText, GPT-2's training corpus. Relevant because the tokenizer's source data and this training set overlap but differ, which is where the dead tokens live.
```

## Source assets

```text
Asset: Table 1, "Detection of under-trained tokens", in Fishing for Magikarp (p. 5)
Shows: Per-model confirmed/tested counts and example dead tokens, side by side across 25 models. Makes visible that GPT-NeoX/Pythia (aligned tokenizer) sit near the bottom while GPT-J/Phi-2/Gemma/Qwen sit high, i.e. the alignment mechanism in one grid.
Crop:  Must retain the model name, the #Confirmed column, and the "Tied Emb." column; may omit the architecture footnote rows. A crop to only GPT-2/GPT-J/Phi-2/GPT-NeoX/Pythia would carry the argument cleanly.
```

```text
Asset: Figure 2, indicators vs. training-data frequency (OLMo v1.7), in Fishing for Magikarp
Shows: The under-training indicator plotted against how many times each token appeared in training, correlated across ten orders of magnitude. This is the single strongest piece of evidence that the cause is under-training and not something else.
Crop:  Keep both axes and their labels; the correlation is the point and is lost without the training-frequency axis.
```

```text
Asset: The verbatim token-cluster list and the k-means/centroid scatter in SolidGoldMagikarp I
Shows: The actual strings (r/counting usernames, backend identifiers) and their geometric clustering near the centroid. Good for a concrete "these are real usernames" moment.
Crop:  If using the list, present it as a short excerpt (a dozen strings), not all 141; exact spelling and leading spaces must be preserved.
```

```text
Asset: Screenshot dialogues in SolidGoldMagikarp I (e.g. repeat ' SolidGoldMagikarp' -> "distribute")
Shows: The behavior in the model's own words. Concrete and immediately legible to a lay reader.
Crop:  Must retain both the prompt and the response; keep the exact token string visible.
```

## Discarded

```text
URL: https://medium.com/@solidgoldmagikarp/glitch-tokens-the-words-ai-refuses-to-say-...  Rejected: personal Medium reblog, no independent reporting or primary access; adds nothing the primaries do not own.
URL: https://www.themoonlight.io/en/review/fishing-for-magikarp-...  Rejected: auto-generated "literature review" of the paper; use the paper itself.
URL: https://github.com/NiluK/SolidGoldMagikarp  Rejected: a personal link collection, not a source for any claim.
URL: https://www.youtube.com/shorts/6PRgC3eJR7k  Rejected: short-form video restating the popular version; no primary value.
URL: https://notes.suhaib.in/docs/tech/latest/the-tokenization-trap-...  Rejected: third-party notes duplicating the secondary explainers already read; would be a third retelling of one origin, which the source policy counts as one.
```
