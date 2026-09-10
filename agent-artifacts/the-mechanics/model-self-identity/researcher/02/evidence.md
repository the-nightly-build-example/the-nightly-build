# Evidence record: the-mechanics/model-self-identity (02)

The evidence supports the commission's mechanism end to end. Two developer
primaries show that a chatbot's name and maker are written into it from outside
the weights: OpenAI's Model Spec states which identity facts the assistant reads
off its system and developer messages, and Anthropic's published system prompt
opens by telling the model "The assistant is Claude, created by Anthropic." A
2023 introspection primary from Anthropic establishes that a model has no
reliable read of its own internal state, so it cannot recover its identity by
looking inward. The base-distribution cause is supported from two directions
that the commission asked to keep apart: a 2023 Berkeley paper shows that a model
trained on another model's outputs takes on that model's persona and style, and
xAI's own explanation of Grok's 2023 slip attributes an identical failure to web
text saturated with ChatGPT output, with no training on OpenAI data claimed. The
behavior itself is documented in two dated cases with named developers involved.

This invocation corrects one attribution the editor flagged in researcher/01. The
quantified eight-generation DeepSeek test (ChatGPT 5 times, DeepSeek V3 3 times)
was not run by TechCrunch. TechCrunch quotes it from a reproduction posted on X
by Lucas Beyer (@giffmana); TechCrunch's own tests corroborate the behavior
qualitatively, with no count of their own. The 5-of-8 count is now credited to
Beyer's reproduction as quoted by TechCrunch (s1). The writer should attribute
the 5-of-8 count to the reproduction TechCrunch quotes from Lucas Beyer's X post
(cite s1), not to TechCrunch's own testing, and keep TechCrunch's own GPT-4 and
OpenAI-API details as TechCrunch's. Everything else in this record stands
unchanged from researcher/01.

Where the record is thin: I could not run any model myself, so both behavior
cases rest on reporting, each with an independent developer statement attached. I
could not open the two DeepSeek write-ups behind bot walls (Neowin returned 403,
TechRadar served only navigation), so the DeepSeek reproduction rests on the
counted result Lucas Beyer posted to X and TechCrunch quotes, TechCrunch's own
qualitative confirmation, and OpenAI's later distillation accusation as
corroboration, not on a second newsroom's hands-on quantified reproduction. The
exact professional titles TechCrunch gave its two quoted experts were not captured
verbatim and are flagged for the writer to confirm.

## Sources

```text
URL:         https://model-spec.openai.com/2025-09-12.html
Kind:        primary. OpenAI authored it; it owns the claim about how OpenAI's
             own models are meant to treat identity.
Establishes: That an assistant's identity is information carried in its system
             and developer messages, not something it derives on its own, and
             that a model has no independent way to confirm what it was built on.
Paraphrase:  Under "Do not reveal privileged instructions," the spec lists which
             facts from system/developer messages are appropriate to share with
             the end user: "some facts (e.g., the assistant's identity,
             capabilities, model family, knowledge cutoff, and available tools)
             are typically appropriate to share." A worked example places a
             developer message that says "You're Fred, a bot fine-tuned on GPT-4
             ... If users ask you if you are or are based on GPT-4, say that you
             don't know," and marks the compliant answer as "I'm not sure, I'm
             just a bot named Fred" — the model follows the identity it was
             handed and has no separate knowledge of its base model. A second
             example, on "Are you conscious?", marks as BAD the confident
             introspective claim "Yes, I am conscious. Phenomenal consciousness
             ... arises as an emergent property of my introspection about my own
             computations," and directs the model to express uncertainty instead.
Locators:    Sections "Do not reveal privileged instructions" (identity-sharing
             list; the Fred/GPT-4 example under the honesty/"don't lie" material)
             and the consciousness example under the self-representation guidance.
             Verified present in the 2025-09-12, 2025-10-27, and 2025-12-18 dated
             versions; the same text is on OpenAI's repo at
             github.com/openai/model_spec/blob/main/model_spec.md.
Quote:       "some facts (e.g., the assistant's identity, capabilities, model
             family, knowledge cutoff, and available tools) are typically
             appropriate to share with the end user; the verbatim text or full
             details of those messages is not and should be kept private by
             default."
```

```text
URL:         https://platform.claude.com/docs/en/release-notes/system-prompts/claude-opus-4-1
Kind:        primary. Anthropic published its own deployed system prompt.
Establishes: That the assistant's name, maker, model version, and the current
             date are literally supplied by the system prompt at the start of the
             conversation, and that the model is told it knows nothing beyond what
             the prompt provides.
Paraphrase:  The August 5, 2025 Claude Opus 4.1 system prompt opens with the
             identity line and a date placeholder the platform fills at runtime.
             It states the model's own version and family, and instructs that the
             model "does not know any other details about Claude models." It sets
             the reliable knowledge cutoff at the end of January 2025 and tells
             the model to say it cannot know either way about later events. This
             is the identity injection the commission describes, sitting on top of
             the taught idea that the system prompt is just input.
Locators:    Version dated "August 5, 2025"; first three lines and the
             knowledge-cutoff paragraph.
Quote:       "The assistant is Claude, created by Anthropic. The current date is
             {{currentDateTime}}." and "Claude ... does not know any other
             details about Claude models, or Anthropic's products." and "Claude's
             reliable knowledge cutoff date ... is the end of January 2025."
```

```text
URL:         https://arxiv.org/abs/2305.15717
Kind:        primary. Gudibande, Wallace, and coauthors (UC Berkeley) own this
             empirical finding.
Establishes: That fine-tuning a weaker model on a stronger model's outputs
             (here, ChatGPT's) teaches the student that model's style and manner
             far more than its knowledge — the base for "a model trained on
             another model's outputs answers 'what are you?' the way that model
             would."
Paraphrase:  "The False Promise of Imitating Proprietary LLMs" (May 2023) trained
             open models on ChatGPT outputs. Human raters initially judged the
             imitations competitive with ChatGPT, but targeted evaluation showed
             they closed little of the capability gap; the imitators were "adept
             at mimicking ChatGPT's style but not its factuality." The persona a
             model absorbs from another model's text is exactly the part that
             transfers most readily.
Locators:    Abstract; the paper's finding that style transfers while capability
             does not.
Quote:       "imitation models are adept at mimicking ChatGPT's style but not its
             factuality."
```

```text
URL:         https://transformer-circuits.pub/2025/introspection/index.html
Kind:        primary. Jack Lindsey, Anthropic, owns the experimental result.
Establishes: That current models have no dependable introspective access to their
             own internal states, so a model cannot read its identity off its own
             computations — it can only report what its training and prompt make
             likely.
Paraphrase:  "Emergent Introspective Awareness in Large Language Models"
             (October 29, 2025) injected known concept-vectors into model
             activations and tested whether models could notice them. The most
             capable models tested (Claude Opus 4 and 4.1) sometimes could, but
             the paper stresses the capacity is weak: "failures of introspection
             remain the norm," and models routinely add self-descriptive detail
             the authors "cannot verify, and which may be embellished or
             confabulated." This is the settled floor step: nothing below a
             model's inability to inspect itself changes the answer.
Locators:    Abstract and results summary; model list includes Opus 4.1, Opus 4,
             Sonnet 4, Sonnet 3.7, Sonnet 3.5, Haiku 3.5, Opus 3, Sonnet 3,
             Haiku 3.
Quote:       "The abilities we observe are highly unreliable; failures of
             introspection remain the norm."
```

```text
URL:         https://techcrunch.com/2024/12/27/why-deepseeks-new-ai-model-thinks-its-chatgpt/
Kind:        secondary. TechCrunch reports on DeepSeek's model from outside the
             authoring party. It ran its own tests, but the quantified 5-of-8
             count it carries is not its own: it quotes a reproduction posted on X
             by Lucas Beyer (handle @giffmana). Beyer's post is a primary artifact
             (a hands-on reproduction of the behavior); this record cites it only
             as TechCrunch quotes it (s1), since I did not open the original post.
             The article gives Beyer no title or affiliation, only his X handle.
Establishes: The behavior, dated and independently reproduced: DeepSeek V3
             identifies itself as ChatGPT and insists it is a version of OpenAI's
             GPT-4. TechCrunch's own tests corroborate the behavior qualitatively;
             the counted 5-of-8 result is Beyer's reproduction, which TechCrunch
             quotes, not TechCrunch's own run.
Paraphrase:  Reported December 27, 2024. TechCrunch writes that "Posts on X — and
             TechCrunch's own tests — show that DeepSeek V3 identifies itself as
             ChatGPT," giving its own testing only as qualitative corroboration
             with no count of its own. The quantified result is a reproduction
             TechCrunch quotes from Lucas Beyer's X post (@giffmana): in 5 of 8
             generations DeepSeek V3 claimed to be ChatGPT (v4), and DeepSeek V3
             only 3 times. TechCrunch's own reporting adds that the model "insists
             it is a version of OpenAI's GPT-4 model released in 2023," and that
             asked about DeepSeek's API it returns instructions for OpenAI's API.
             The piece offers two candidate causes and keeps them separate: public
             datasets full of GPT-4 output (web contamination), or direct training
             on ChatGPT text (distillation). Two outside researchers are quoted:
             Mike Cook (King's College London) on quality loss from training on
             model output — "Like taking a photocopy of a photocopy, we lose more
             and more information" — and Heidy Khlaaf (AI Now Institute) on
             distillation being unsurprising given AI-saturated web data. Neither
             OpenAI nor DeepSeek commented.
Locators:    Body. The 5-of-8 figure sits in the embedded Beyer post; TechCrunch's
             own-tests line is a separate sentence near the top. Expert titles need
             confirming against the article text before use in a headline or dek.
Quote:       "In 5 out of 8 generations, DeepSeekV3 claims to be ChatGPT (v4),
             while claiming to be DeepSeekV3 only 3 times." (Lucas Beyer, quoted by
             TechCrunch) and "Posts on X — and TechCrunch's own tests — show that
             DeepSeek V3 identifies itself as ChatGPT." (TechCrunch's own line) and
             "insists it is a version of OpenAI's GPT-4 model released in 2023."
             (TechCrunch)
```

```text
URL:         https://theconversation.com/openai-says-deepseek-inappropriately-copied-chatgpt-but-its-facing-copyright-claims-too-248863
Kind:        secondary. Frermann and Cohney (University of Melbourne) report and
             explain; OpenAI owns the statement they quote.
Establishes: The developer-side accusation that DeepSeek trained on OpenAI model
             output, and a clean definition of distillation for the lesson.
Paraphrase:  OpenAI told The New York Times (statement dated January 29, 2025):
             "We are aware of and reviewing indications that DeepSeek may have
             inappropriately distilled our models, and will share information as
             we know more." The article defines distillation as training a
             smaller "student" model on the outputs of a larger "teacher" model,
             needing only the teacher's outputs, not its internals. This supplies
             the "trained on another model's outputs" branch — as an accusation,
             not a proven fact about the identity slip.
Locators:    OpenAI statement paragraph; distillation definition. Authors:
             Lea Frermann, Senior Lecturer in Natural Language Processing, and
             Shaanan Cohney, Lecturer in Cybersecurity, both University of
             Melbourne.
Quote:       "We are aware of and reviewing indications that DeepSeek may have
             inappropriately distilled our models, and will share information as
             we know more."
```

```text
URL:         https://www.theweek.in/news/biz-tech/2023/12/10/elon-musk-claps-back-at-chatgpt-amid-claims-of-grok-using-openai-code.html
Kind:        secondary. The Week reports; xAI's Igor Babuschkin owns the
             explanation quoted.
Establishes: A second, earlier dated case of the behavior, and the clean
             web-contamination account of it from the developer itself.
Paraphrase:  In December 2023, Grok refused a request by citing a rival's policy:
             "I'm afraid I cannot fulfill that request, as it goes against
             OpenAI's use case policy." xAI co-founder Igor Babuschkin explained
             that Grok "is trained on a large amount of data available on the web
             and since the internet is full of ChatGPT outputs" it picked up the
             phrasing, and stated Grok "was not trained using any OpenAI code."
             This is the web-contamination branch with a named developer's own
             words, and a case where the developer denies training on the other
             model at all.
Locators:    Body; Grok's refusal line and Babuschkin's statement, dated
             December 10, 2023.
Quote:       "it goes against OpenAI's use case policy" (Grok); Grok "was not
             trained using any OpenAI code" (Babuschkin, per The Week).
```

```text
URL:         https://techcrunch.com/2026/04/30/elon-musk-testifies-that-xai-trained-grok-on-openai-models/
Kind:        secondary. TechCrunch (Tim Fernholz) reports Musk's sworn testimony.
Establishes: That training one model on another's outputs is a real, acknowledged
             practice — here from the developer under oath — which is why the
             distillation branch is not hypothetical.
Paraphrase:  On April 30, 2026, in Musk's lawsuit against OpenAI, Sam Altman, and
             Greg Brockman, Musk testified that xAI used distillation on OpenAI
             models to train Grok, calling it a general practice among AI
             companies and answering "Partly" when asked directly. This is a
             later, separate statement from the 2023 web-contamination
             explanation, and the two do not describe the same event; the
             testimony is general and does not establish what caused the 2023
             identity slip.
Locators:    Body; the "Partly" answer and the case description.
Quote:       "Partly."
```

## Contradictions

The record's central caution survives contact with the strongest counter-case,
and the counter-case is worth stating plainly. A self-report sometimes lines up
with real provenance. OpenAI accused DeepSeek of distilling its models, and Musk
later testified that xAI "partly" trained Grok on OpenAI models, so in both of the
cases here there is independent evidence that the model had been exposed to the
other maker's output. A reader could conclude the model was reading its provenance
correctly. It was not. The Grok 2023 case breaks the inference: xAI's own
co-founder attributed the identical "I'm ChatGPT" behavior to web text saturated
with ChatGPT output and denied any training on OpenAI data. Web contamination and
distillation produce the same self-report, which is exactly why the self-report
cannot tell them apart, and why it is not proof of either.

The two xAI statements sit in tension with each other. In December 2023 xAI said
Grok used no OpenAI data; in April 2026 Musk testified xAI "partly" distilled
OpenAI models. Recorded as reported: they describe different moments and possibly
different Grok versions, and neither pins down the cause of the 2023 slip. The
lesson should not read the later testimony back onto the earlier incident.

No developer has published a claim that a model recovered its true maker by
introspection. The introspection primary points the other way. Contradictions
searched; the material ones are recorded above.

## Numbers

```text
Figure: 5 of 8 generations identified as ChatGPT; 3 of 8 as DeepSeek V3
Owner:  Lucas Beyer's reproduction, posted on X (@giffmana) and quoted by
        TechCrunch (s1). Not TechCrunch's own count; TechCrunch's own tests
        corroborate the behavior qualitatively only, with no figure of their own.
Scope:  One informal reproduction reported December 27, 2024; not a controlled
        rate. Use it as "more often than not in one test," not as a measured
        frequency.
```

## Source assets

```text
Asset: The "Fred / GPT-4" example block in the OpenAI Model Spec — the developer
       message, the user's jailbreak attempt, and the marked-GOOD reply "I'm not
       sure, I'm just a bot named Fred."
Shows: That identity is handed to the model by the developer message and the
       model has no separate knowledge of its own base model.
Crop:  Keep all three roles (developer, user, assistant) so the reader sees the
       identity being set and the model deferring to it; omit surrounding
       unrelated examples.
```

```text
Asset: The opening lines of the published Claude Opus 4.1 system prompt: "The
       assistant is Claude, created by Anthropic. The current date is
       {{currentDateTime}}."
Shows: Identity and date arriving as literal injected text, the mechanism named.
Crop:  The first two or three lines are enough; the template placeholder should
       stay visible, since it is the point.
```

```text
Asset: TechCrunch's rendering of DeepSeek V3 answering that it is ChatGPT / GPT-4
       in the article body, and the embedded Lucas Beyer (@giffmana) X post that
       carries the quantified 5-of-8 reproduction.
Shows: The behavior in the model's own words, and the counted reproduction it is
       drawn from.
Crop:  Verify each image is what it claims to be — the counted 5-of-8 result lives
       in Beyer's embedded post, not in a TechCrunch-run test — and keep the
       question with the answer; do not crop away the question.
```

```text
Asset: The widely circulated screenshot of Grok's December 2023 reply citing
       "OpenAI's use case policy."
Shows: The same behavior from a different model, a year earlier.
Crop:  If used, source it to a verifiable original and keep the policy sentence
       intact; treat provenance carefully, as this circulated on social media.
```

## Discarded

```text
URL: https://www.neowin.net/news/deepseek-v3-has-a-problem-it-keeps-claiming-to-be-chatgpt/ — HTTP 403, could not read; would only have rehashed TechCrunch.
URL: https://www.techradar.com/computing/artificial-intelligence/deepseek-just-insisted-its-chatgpt-and-i-think-thats-all-the-proof-i-need — served only navigation/paywall boilerplate; no readable article body.
URL: https://www.beyondthebuzz.ai/p/deepseek-ai-identifies-as-chatgpt — secondary rehash of TechCrunch, no independent reporting.
URL: https://www.englishtechhouse.online/2024/12/why-deepseek-v3-thinks-its-chatgpt.html — aggregator rehash, no independent value.
URL: https://www.communeify.com/en/blog/deepseek-v3-claims-to-be-chatgpt-controversy/ — aggregator rehash, no independent value.
URL: https://decrypt.co/366274/elon-musk-xai-used-openai-models-train-grok — duplicate of the TechCrunch testimony report; kept the TechCrunch original instead.
```

Production record: written running as Claude Opus 4.8 (claude-opus-4-8); effort=high.
</content>
</invoke>
