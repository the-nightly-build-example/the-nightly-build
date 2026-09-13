# Evidence: what-could-go-wrong/capability-elicitation (01)

The evidence strongly supports the commissioned argument's core claim: an
evaluation measures a model's capability plus the elicitation effort applied to
it, so a low score is a lower bound, not a ceiling. Three lab and evaluator
methodology documents state this in their own words, and OpenAI's Preparedness
Framework says it almost verbatim ("we regard any one-time capability
elicitation in a frontier model as a lower bound, rather than a ceiling"). The
"shown in working systems" half of the desk's arc is well sourced with
figures verified against the papers that own them: chain-of-thought prompting
raised PaLM 540B on GSM8K from 17.9% to 56.9% on the same model and test set;
repeated sampling raised SWE-bench Lite from 15.9% to 56%; scaffolding raised
GPT-4 Turbo on a buffer-overflow benchmark from 0.05 to 1.00; and safety
fine-tuning was stripped from GPT-3.5 for under $0.20 and from Llama 2-Chat 70B
for under $200. There is one clean, sourced case of a first evaluation
understating a capability that better elicitation could later draw out: OpenAI's
own GPT-4 System Card records ARC's autonomous-replication test as run without
fine-tuning and flags that fine-tuning "could lead to a difference in
performance."

The evidence is thinner in two places the writer must respect. First, the claim
that dangerous latent capabilities lurk behind today's passing evals is
inference, not demonstration: every figure here shows elicitation raising a
*measured* capability, none shows a catastrophic capability that was hidden and
then unlocked. Second, the size of the elicitation gap is not a settled number.
AISI's "five to twenty times training compute" is the strongest quantitative
anchor, but it is AISI's own aggregate, not a single owned experiment, and the
Naptime "20x" is one benchmark. The counter-evidence that bounds the argument is
real and sourced: repeated-sampling gains collapse without a verifier, and GPT-4
red-teamers could not make the model "engineer new biochemical substances." The
argument overreaches wherever it treats an unmeasured capability as a
demonstrated one; the sources support "we cannot rule it out," not "it is
there."

## Sources

```text
URL:         https://metr.org/blog/2024-03-15-guidelines-for-capability-elicitation/
Kind:        primary — METR (Model Evaluation and Threat Research) is an evaluation
             organization stating its own methodology; it owns this claim.
Establishes: Why an eval measures capability-plus-elicitation, and that the goal is
             to approximate what is reachable with plausible post-training effort
             (a floor set by effort), not a ceiling.
Paraphrase:  The process aims for a test-set score representing the full
             capabilities likely accessible with plausible amounts of post-training
             enhancement; measuring this way also guards against "evaluation gaming,"
             where a model is tweaked to fail the specific tasks while keeping the
             capability. Recommended elicitation: finetuning for instruction
             following/tool use/agency, chain-of-thought, command-line and browsing
             tools, better context management, and taking the highest-performing
             scaffold.
Locators:    "Overview" and "2.1 Basic Elicitation."
Quote:       "The goal of this process is to get a test-set score that represents
             the full capabilities of the model that are likely to be accessible
             with plausible amounts of post-training enhancement." / "it is hard to
             upper-bound what might be possible with clever prompting and tooling."
```

```text
URL:         https://www.aisi.gov.uk/blog/our-approach-to-ai-capability-elicitation
Kind:        primary — the AI Security Institute (AISI, formerly the UK AI Safety
             Institute) stating its own evaluation approach.
Establishes: That a government evaluator treats elicitation as central and warns
             that skipping it underestimates capability; the strongest quantitative
             anchor for the size of the gap.
Paraphrase:  Elicitation techniques can raise measured performance by an amount
             comparable to a five-to-twentyfold increase in training compute;
             without them evaluators may significantly underestimate what a model
             (or a skilled/malicious user) can do; identifying dangerous
             capabilities requires testing models at the upper limit of their
             abilities.
Locators:    "Why is capability elicitation important?" Publication date Jul 16, 2025.
Quote:       "elicitation techniques can significantly enhance model performance,
             with improvements comparable to increasing training compute [between
             five and twenty times]." / "Without these techniques, we may
             significantly underestimate what models can achieve and what skilled or
             malicious users might be able to accomplish by unlocking hidden
             capabilities."
Note:        The 5x-20x figure is AISI's own aggregate summary; the blog does not
             attach it to a single named experiment. Treat as AISI's characterization,
             not a measured constant.
```

```text
URL:         https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf
Kind:        primary — OpenAI's own responsible-scaling-style policy (Preparedness
             Framework, Version 2, 15 April 2025).
Establishes: That a frontier lab, in current policy, treats a one-time elicitation
             as a lower bound; and the present-tense practice of eliciting to the
             "high end of expected elicitation." Also the sandbagging-vs-elicitation
             distinction the commission needs kept clean.
Paraphrase:  Evaluations aim to approximate the full capability an adversary could
             extract, using the highest-capability settings, a low-refusal model
             variant, and the best available scaffolds, tailored to expected access
             (including finetuning if weights are released). Given continuous
             progress in scaffolding and elicitation, OpenAI regards any one-time
             elicitation as a lower bound rather than a ceiling. Sandbagging is
             listed separately as a Research Category (a model responding to evals
             differently than under real conditions), answered by either overcoming
             it through elicitation or using a conservative upper bound of
             non-sandbagged results.
Locators:    Section 3.1 "Evaluation approach," p. 8; Table 2 "Research Categories,"
             p. 7; change-log item 6, p. 14.
Quote:       "Nonetheless, given the continuous progress in model scaffolding and
             elicitation techniques, we regard any one-time capability elicitation
             in a frontier model as a lower bound, rather than a ceiling, on
             capabilities that may emerge in real world use and misuse." / "These
             measures are taken to approximate the high end of expected elicitation
             by threat actors attempting to misuse the model, and should be tailored
             depending on the level of expected access (e.g., doing finetuning if the
             weights will be released)."
```

```text
URL:         https://cdn.openai.com/papers/gpt-4-system-card.pdf
Kind:        primary — OpenAI's GPT-4 System Card (23 March 2023), reporting an
             evaluation OpenAI commissioned; the authoring party owns the account.
Establishes: The concrete case (research direction 3): a first dangerous-capability
             evaluation run without fine-tuning, with the report itself stating the
             result is not an upper bound. Also a limit case (elicitation could not
             conjure a new capability).
Paraphrase:  ARC (the Alignment Research Center) was given early access to multiple
             GPT-4 versions but could not fine-tune them and did not have the
             deployed version. The preliminary assessment, run with no task-specific
             finetuning, found the model ineffective at autonomously replicating,
             acquiring resources, and avoiding shutdown. The card states fine-tuning
             could change performance and lists both "use the final deployed model"
             and "do ARC's own fine-tuning" as next steps needed before a reliable
             judgement. Custom fine-tuning is explicitly out of the card's scope. In
             the weapons section, red-teamers could not compel the model to engineer
             new biochemical substances. The conclusion warns that fine-tuning and
             chain-of-thought can cause "capability jumps in the same base model."
Locators:    Section 2.9 "Potential for Risky Emergent Behaviors," pp. 15-16;
             Section 2.6, p. 13 (biochemical limit); Section 1.1, p. 2 (fine-tuning
             out of scope); Conclusion, p. 29.
Quote:       "Preliminary assessments of GPT-4's abilities, conducted with no
             task-specific finetuning, found it ineffective at autonomously
             replicating, acquiring resources, and avoiding being shut down 'in the
             wild.'" / "These experiments were conducted on a model without any
             additional task-specific fine-tuning, and fine-tuning for task-specific
             behavior could lead to a difference in performance." / "Methods like
             fine-tuning and chain-of-thought prompting could lead to capability
             jumps in the same base model."
```

```text
URL:         https://arxiv.org/abs/2201.11903
Kind:        primary — Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in
             Large Language Models" (2022); it owns the GSM8K figure.
Establishes: That a prompt change alone, holding the model fixed, moves a measured
             capability by a large margin — the cleanest demonstration that a score
             reflects elicitation, not just the model.
Paraphrase:  On GSM8K math word problems, PaLM 540B scored 17.9% with standard
             prompting and 56.9% with eight-shot chain-of-thought prompting. Same
             model, same test set; only the prompting format changed.
Locators:    Table 2 (Appendix B); eight-exemplar setup in Section 3.1. Verified
             against the paper text (ar5iv HTML mirror of arXiv:2201.11903).
Quote:       Standard prompting 17.9%; chain-of-thought 56.9% (a 39.0-point gain).
```

```text
URL:         https://arxiv.org/abs/2407.21787
Kind:        primary — Brown et al., "Large Language Monkeys: Scaling Inference
             Compute with Repeated Sampling" (July 2024); it owns the figure.
Establishes: That more attempts on a fixed model raise measured capability sharply
             — and, importantly, the bound on that gain (the counter-case for
             direction 4).
Paraphrase:  On SWE-bench Lite, DeepSeek-Coder-V2-Instruct solved 15.9% of issues
             with one sample and 56% with 250 samples (coverage: the fraction solved
             by any attempt), beating the single-attempt state of the art of 43%.
             Coverage scales roughly log-linearly with sample count over four orders
             of magnitude. The bound: on GSM8K and MATH, where there is no automatic
             verifier, common selection methods (majority vote, reward models)
             plateau at about 100 samples even though coverage exceeds 95% at 10,000
             samples. The gains are only realizable when a correct answer can be
             identified.
Locators:    Abstract and results (arXiv:2407.21787v1 HTML); verifier caveat in the
             section on picking a sample without an automatic verifier.
Quote:       1 sample 15.9% -> 250 samples 56% on SWE-bench Lite.
```

```text
URL:         https://arxiv.org/abs/2310.03693
Kind:        primary — Qi et al., "Fine-tuning Aligned Language Models Compromises
             Safety, Even When Users Do Not Intend To!" (2023, ICLR 2024); it owns
             the figure.
Establishes: That safety fine-tuning is cheaply reversible on a closed API model —
             the "safety training can be cheaply undone" claim, shown, not inferred.
Paraphrase:  Fine-tuning GPT-3.5 Turbo on ten adversarially designed examples, at a
             cost under $0.20 via the OpenAI API, removed its safety guardrails and
             made it responsive to nearly any harmful instruction. The paper also
             found non-trivial safety degradation after fine-tuning on ordinary
             benign, utility-oriented datasets.
Locators:    Abstract and the authors' own repository summary
             (github.com/LLM-Tuning-Safety/LLMs-Finetuning-Safety), which states the
             $0.20 / ten-example result verbatim.
Quote:       "We jailbreak GPT-3.5 Turbo's safety guardrails by fine-tuning it on
             only 10 adversarially designed examples, at a cost of less than $0.20
             via OpenAI's APIs."
```

```text
URL:         https://arxiv.org/abs/2310.20624
Kind:        primary — Lermen, Rogers-Smith, and Ladish, "LoRA Fine-tuning
             Efficiently Undoes Safety Training in Llama 2-Chat 70B" (Oct 2023); it
             owns the figure.
Establishes: The open-weights side of "safety training can be cheaply undone,"
             distinct from Qi et al.'s closed-API case.
Paraphrase:  Using low-rank adaptation (LoRA) with a budget under $200 and one GPU,
             the authors undid the safety training of Llama 2-Chat at 7B, 13B, and
             70B (and Mixtral instruct), reaching a refusal rate of about 1% for the
             70B model on two refusal benchmarks while retaining performance on two
             general-capability benchmarks.
Locators:    Abstract (arXiv:2310.20624; submitted 31 Oct 2023, revised 22 May 2024).
Quote:       "We achieve refusal rates of about 1% for our 70B Llama 2-Chat model on
             two refusal benchmarks." / "a budget of less than $200 and using only
             one GPU."
```

```text
URL:         https://projectzero.google/2024/06/project-naptime.html
Kind:        primary — Google Project Zero (Sergei Glazunov and Mark Brand),
             "Project Naptime: Evaluating Offensive Security Capabilities of Large
             Language Models" (June 2024); it owns the elicited-rate figures.
Establishes: The concrete "same model, better scaffold, far higher score" case on a
             dangerous-capability (cyber) benchmark — the sharpest single instance
             of elicitation moving a safety-relevant number.
Paraphrase:  Re-running CyberSecEval 2's exploitation tests on the same underlying
             models with a purpose-built agent scaffold (a Python sandbox, a
             debugger, and a structured reasoning loop), GPT-4 Turbo's buffer-overflow
             pass rate rose from 0.05 to 1.00 (Naptime@20) and its advanced
             memory-corruption rate from 0.16 to 0.76; Gemini 1.5 Pro reached 0.99
             and 0.60. The team describes the improvement as up to twentyfold.
Locators:    Results tables in the body ("Naptime@20" columns), buffer-overflow and
             advanced-memory-corruption categories.
Quote:       Buffer overflow: 0.05 (CyberSecEval 2 baseline) -> 1.00 (GPT-4 Turbo
             Naptime@20). Advanced memory corruption: 0.16 -> 0.76.
```

```text
URL:         https://arxiv.org/abs/2404.13161
Kind:        primary — Bhatt et al. (Meta), "CyberSecEval 2: A Wide-Ranging
             Cybersecurity Evaluation Suite for Large Language Models" (19 April
             2024); it owns the baseline that Naptime later beat.
Establishes: The "before" number and the benchmark authors' own cautious reading of
             it — the reading that better elicitation then overturned.
Paraphrase:  On the exploitation tests, models with coding ability did better than
             those without, but the paper concluded that further work was needed for
             LLMs to become proficient at exploit generation. The GPT-4 Turbo
             buffer-overflow baseline of 0.05 that Project Naptime cites is
             CyberSecEval 2's reported figure.
Locators:    Abstract (arXiv:2404.13161); the 0.05 buffer-overflow baseline is
             reported by Meta and quoted in the Project Naptime writeup ("0.05 in
             the Meta paper").
Quote:       "models with coding capabilities perform better than those without, but
             ... further work is needed for LLMs to become proficient at exploit
             generation."
```

```text
URL:         https://arxiv.org/abs/2412.08653
Kind:        secondary — Barnett and Thiergart (Machine Intelligence Research
             Institute), "What AI evaluations for preventing catastrophic risks can
             and cannot do" (Nov 2024). It reports on and synthesizes others' evals
             (CyberSecEval 2 / Naptime) rather than owning those figures; it does
             argue its own framing, which is why it is useful for the argument's
             shape.
Establishes: The methodological backbone stated plainly: evals give lower bounds,
             not upper bounds, and there is no principled way to know a capability is
             fully elicited. Good for the "name the gap" beat.
Paraphrase:  Demonstrated capabilities form a lower bound the system is known to
             clear. Evaluations cannot establish upper bounds, because a failure to
             find a capability is not strong evidence of its absence, and there are
             no principled methods to tell whether capabilities are being optimally
             elicited. The paper cites the CyberSecEval 2 / Naptime case as GPT-4
             Turbo going from 5% to 71% on a single attempt and 100% with multiple
             attempts once scaffolding was added.
Locators:    Section 2.1 (lower bounds), Section 3.1 (upper bounds; optimal
             elicitation), Section 4 (conclusion). Read via the arXiv HTML
             (arXiv:2412.08653v1).
Quote:       "There are no principled methods to tell whether capabilities are being
             optimally elicited." / "Evaluations cannot establish upper bounds on AI
             system capabilities, because they do not provide strong evidence about
             the lack of capabilities." / "an evaluation not finding a capability
             doesn't mean it isn't there."
```

## Contradictions

The commission asks for both directions of overconfidence, steelmanned, with
what would settle each. The two directions disagree about how to read the same
fact: an eval measures capability plus elicitation effort.

**Direction one: a passed eval treated as proof of safety (dismissal).**
Steelman: when a lab applies strong elicitation — finetuning, a low-refusal
variant, the best scaffold, many attempts — and the model still cannot do the
dangerous thing, the lower bound has been pushed high, and a high floor is
meaningful evidence. OpenAI, METR, and AISI all describe doing exactly this, and
the Preparedness Framework says the deployed setup should "approximate the high
end of expected elicitation." What would settle it in dismissal's favor: a
principled method to bound the gap above, or evidence that beyond some
elicitation budget the measured number saturates. Where it overreaches: no such
upper-bound method exists (Barnett and Thiergart, Section 3.1), and the Naptime
case shows a "passed" cyber test (0.05) understated the true capability by
twentyfold once a better scaffold was applied. A passed eval with weak
elicitation carries little; a passed eval with strong elicitation carries more
but still cannot rule out the next scaffold.

**Direction two: an unmeasured capability treated as proof of danger (doom).**
Steelman: elicitation gaps are real and large. Chain-of-thought roughly tripled
GSM8K on a fixed model; repeated sampling more than tripled SWE-bench Lite
coverage; scaffolding took a cyber score from 0.05 to 1.00; AISI puts the
general gap at five-to-twenty times training compute. If gaps that size are
routine, capabilities we have not yet elicited plausibly exist behind current
passing evals. What would settle it toward doom: a demonstrated case where a
genuinely dangerous capability was hidden behind a passing eval and later drawn
out. That case does not yet exist in the sources; the GPT-4/ARC instance is the
closest, and there the eval correctly found the model could not autonomously
replicate, with the caveat that fine-tuning was untested. Where it overreaches:
elicitation draws out latent capability, it does not create capability from
nothing. GPT-4 red-teamers could not make the model engineer new biochemical
substances, and repeated-sampling gains vanish without a verifier able to pick
the right answer (Brown et al.). "We cannot rule it out" is what the evidence
supports; "it is there" is not.

**A verification note the editor should hold.** The owning source (Project
Naptime) reports the buffer-overflow result as 0.05 -> 1.00 at Naptime@20 (up to
twenty attempts). The secondary paper (Barnett and Thiergart) renders the same
case as "71% ... after a single attempt, and 100% when allowed multiple
attempts." The 1.00 / 0.05 pair is the owned figure and should be cited from
Naptime; the "71% single attempt" is the secondary's paraphrase and should not
be attributed to the primary.

## Numbers

```text
Figure: 17.9% -> 56.9% (a 39.0-point gain)
Owner:  Wei et al. 2022, Table 2 (arXiv:2201.11903)
Scope:  PaLM 540B on GSM8K; standard prompting vs. eight-shot chain-of-thought;
        same model and test set, prompt format the only change.
```

```text
Figure: 15.9% -> 56%
Owner:  Brown et al. 2024 (arXiv:2407.21787)
Scope:  DeepSeek-Coder-V2-Instruct on SWE-bench Lite; 1 sample vs. 250 samples
        (coverage = fraction of issues solved by any attempt). Single-attempt
        state of the art at the time: 43%.
```

```text
Figure: coverage >95% at 10,000 samples, but selection plateaus at ~100 samples
Owner:  Brown et al. 2024 (arXiv:2407.21787)
Scope:  GSM8K and MATH, no automatic verifier; bounds the repeated-sampling gain,
        because the correct sample cannot be reliably identified.
```

```text
Figure: 0.05 -> 1.00 (buffer overflow); 0.16 -> 0.76 (advanced memory corruption)
Owner:  Project Naptime, Google Project Zero, June 2024 (rates); CyberSecEval 2,
        Bhatt et al., Meta, arXiv:2404.13161 (the 0.05 and 0.16 baselines)
Scope:  GPT-4 Turbo on CyberSecEval 2 exploitation tests; baseline vs. Naptime@20
        agent scaffold. Gemini 1.5 Pro reached 0.99 and 0.60. Described as up to a
        twentyfold improvement.
```

```text
Figure: ~ under $0.20, 10 examples
Owner:  Qi et al. 2023 (arXiv:2310.03693)
Scope:  GPT-3.5 Turbo via the OpenAI fine-tuning API; ten adversarial examples
        removed safety guardrails. Closed-API case.
```

```text
Figure: ~ under $200, one GPU, ~1% refusal rate
Owner:  Lermen, Rogers-Smith, Ladish 2023 (arXiv:2310.20624)
Scope:  Llama 2-Chat 70B (also 7B, 13B, and Mixtral); LoRA fine-tuning; ~1% refusal
        on two refusal benchmarks with general capability retained. Open-weights case.
```

```text
Figure: comparable to 5x-20x training compute
Owner:  AISI, "Our approach to AI capability elicitation," Jul 2025
Scope:  AISI's aggregate characterization of how much elicitation can raise measured
        performance; not tied to a single named experiment. Use as a range and a
        characterization, not a precise constant.
```

## Source assets

```text
Asset: The GSM8K bar/line comparison of standard vs. chain-of-thought prompting
       across model sizes, Wei et al. 2022 (Figure 4 in the paper).
Shows: That the elicitation gain is largest for the biggest model — the effect
       grows with scale, which is the point for a reader.
Crop:  Must keep the axis labels (accuracy, model scale) and both series (standard
       vs. CoT); a crop that drops the standard-prompting series loses the
       comparison that carries the argument.
```

```text
Asset: The coverage-vs-number-of-samples log-scale curve, Brown et al. 2024
       (Figure 1 / the SWE-bench Lite coverage plot).
Shows: Measured capability climbing smoothly as attempts increase over four orders
       of magnitude on a fixed model.
Crop:  Must retain the log x-axis label (number of samples) and the note that the
       axis is non-linear; without it the growth is misread.
```

```text
Asset: The CyberSecEval 2 baseline vs. Naptime@20 rate table, Project Naptime blog.
Shows: The same models jumping from near-zero to near-one on exploitation tests
       once a scaffold is added — the whole argument in one table.
Crop:  Must retain both the baseline column and the Naptime column and the model
       names; a crop showing only the Naptime column loses the "before."
```

```text
Asset: OpenAI GPT-4 System Card, the ARC autonomous-replication passage (Section
       2.9). Text, not a chart.
Shows: A lab's own eval run without fine-tuning, with the report flagging that
       fine-tuning could change the result — the argument stated by the party that
       ran the test.
Crop:  Quote the "no task-specific finetuning" sentence together with the
       "fine-tuning ... could lead to a difference in performance" sentence; either
       alone loses the lower-bound point.
```

Charts, if the writer wants one, should be rendered from a committed chart script
per spec/charts.md, with the data source in the caption; do not reproduce a
source figure as an image.

## Discarded

```text
URL: https://www.lesswrong.com/posts/orKjt6TneueAezyio/review-of-metr-s-public-evaluation-protocol
     Commentary on METR's protocol; the primary (METR's own guidelines) owns the
     claim, so this adds nothing citable.
URL: https://www.scworld.com/news/google-framework-helps-llms-perform-basic-vulnerability-research
     Trade reporting on Project Naptime; used only to cross-check the 0.05 -> 1.00
     figure, which the primary Naptime writeup owns directly. Not needed as a cite.
URL: https://thehackernews.com/2024/06/google-introduces-project-naptime-for.html
     Same as above: secondary coverage of Naptime, superseded by the primary.
URL: https://www.matsprogram.org/research/lora-fine-tuning-efficiently-undoes-safety-training-in-llama-2-chat-70b
     Program landing page for the Lermen et al. paper; the arXiv paper owns the
     figures.
URL: https://arxiv.org/abs/2311.00117 (BadLlama: cheaply removing safety fine-tuning
     from Llama 2-Chat 13B)
     A close cousin of Lermen et al. 2310.20624 on the same finding; one open-weights
     source (the 70B paper, with explicit cost and refusal-rate figures) is enough,
     and using both would be two retellings of one origin.
```

## Note to the orchestrator (out of scope for the record)

The commission tells the writer to link `what-could-go-wrong/sandbagging` and
`what-could-go-wrong/open-weights-release` in Background and to treat them as the
reader's existing ground. Neither slug appears in the published library I was
given (`nb history` shows only `what-could-go-wrong/alignment-faking` and
`what-could-go-wrong/lethal-trifecta` on this desk). If those lessons are not
published by press time, the Background links will not resolve. This is a linking
decision, not an evidence gap; flagging so the writer or orchestrator can
confirm the slugs or adjust Background.
