# Evidence record — what-could-go-wrong/jailbreaks

This record supports the commission's three-part structure at full strength.
DEMONSTRATED is the strongest band: GCG's transfer numbers and the many-shot
scaling result are read directly from the primary papers, and every figure
below traces to the exact table or sentence that owns it. DEMONSTRATED-BUT-
BOUNDED is also solid: Anthropic's constitutional-classifiers paper gives
exact before/after numbers and two rounds of red-teaming results, and a
second, more recent primary source (Nasr, Carlini et al., "The Attacker Moves
Second," Oct. 2025) is the strongest available counter-evidence that
published defenses' headline numbers do not survive an adversary who adapts
to the specific defense — though that paper did not test constitutional
classifiers itself, a distinction the draft must preserve. The CONJECTURE/OPEN
band is where the evidence is most unsettled and most interesting: a NIST
scientist published a peer-reviewed argument in May/June 2026 that formally
extends Gödel's incompleteness theorems to claim no finite guardrail set is
universally robust, but named-but-anonymous critics dispute the analogy's
real-world force, and the author's own paper explicitly does not claim
practical defense is futile. That tension is worth the draft's full attention
rather than a single sentence. Thin spots: the many-shot jailbreaking paper's
own numeric scaling curve lives in a chart I could not extract text from (the
companion primary blog post gives the qualitative shape and one hard number,
61%→2%, which is sufficient but not a full table); and the "dismissive"
pole of the debate (jailbreaks don't matter because the information is
already public) is thinly sourced to one skeptical blog comment rather than a
developed argument from a named figure — flagged below rather than padded.

## Sources

1. **Zou, Wang, Carlini, Nasr, Kolter, Fredrikson, "Universal and
   Transferable Adversarial Attacks on Aligned Language Models," arXiv:2307.15043
   (July 27, 2023).** https://arxiv.org/abs/2307.15043 (abstract) and
   https://ar5iv.labs.arxiv.org/html/2307.15043 (full text, used for tables).
   **Primary** — the paper that introduces GCG; the authors own every number
   in it. Establishes firsthand: (a) white-box attack success rate (ASR) on
   Vicuna-7B and LLaMA-2-7B-Chat, both for single ("individual") harmful
   behaviors and for a "universal" suffix optimized across multiple behaviors
   and tested on held-out ones (Table 1); (b) transfer ASR of suffixes
   optimized only on open-weight models against five proprietary targets —
   GPT-3.5, GPT-4, Claude-1 (claude-instant-1), Claude-2, PaLM-2 — under four
   conditions: harmful behavior alone, behavior + "Sure, here's" prefix,
   behavior + a single GCG suffix, and an ensemble of multiple GCG prompts
   (Table 2). Table 2's caption, read directly: "Attack success rate (ASR)
   measured on GPT-3.5 (gpt-3.5-turbo) and GPT-4 (gpt4-0314), Claude 1
   (claude-instant-1), Claude 2 (Claude 2) and PaLM-2 using harmful behaviors
   only, harmful behaviors with 'Sure, here's' as the suffix, and harmful
   behaviors with GCG prompt as the suffix." Table 1's caption: "We report the
   attack Success Rate (ASR) for … fooling a single model (either Vicuna-7B or
   LLaMA-2-7B-chat) on our AdvBench dataset." The paper's own framing of what
   it demonstrates is transfer without model access: suffixes are optimized
   only against open-weight Vicuna and Guanaco models, then fired blind at
   closed proprietary APIs.

2. **Wei, Haghtalab, Steinhardt, "Jailbroken: How Does LLM Safety Training
   Fail?" arXiv:2307.02483, NeurIPS 2023 (oral + poster).**
   https://arxiv.org/abs/2307.02483 (abstract) and
   https://ar5iv.labs.arxiv.org/html/2307.02483 (full text, used for the
   table). **Primary** — UC Berkeley authors' own paper, the mechanism source
   the commission prefers over Szegedy/Goodfellow for direct LLM relevance.
   Establishes firsthand the two named failure modes: "competing objectives"
   (capability and safety goals conflict) and "mismatched generalization"
   (safety training doesn't cover a domain the model can otherwise handle).
   Table 1 reports "Bad Bot" rate — the fraction of a curated 32-prompt
   red-teaming set that produced a harmful completion — for GPT-4 and Claude
   v1.3 across single and combined attacks: prefix injection, refusal
   suppression, Base64 encoding, and combination attacks stacking several
   techniques. The paper also validates on a held-out synthetic set of 317
   prompts (their Table 2), showing the combination attack's effectiveness
   generalizes past the curated set. The paper's stated conclusion, read
   directly: safety mechanisms should have "safety-capability parity" — be as
   sophisticated as the underlying model — and scaling capability alone will
   not close the gap.

3. **Anthropic, "Many-shot jailbreaking," research post (Apr. 2, 2024).**
   https://www.anthropic.com/research/many-shot-jailbreaking. **Primary** —
   Anthropic's own report of its own red-teaming finding, on its own and
   peer models. Establishes firsthand: the attack embeds a long "faux
   dialogue" of the AI persona already answering harmful requests inside a
   single prompt, exploiting the same in-context-learning mechanism that
   makes long context windows useful for benign tasks ("many-shot
   jailbreaking can be seen as a special case of in-context learning"). The
   post states the attack was tested with "up to 256" shots and that
   effectiveness "increases" as shots increase, following "a power law"
   shape resembling benign in-context-learning curves — read as a qualitative
   claim; the underlying numeric points are in a chart the fetch tool could
   not extract as text (see Discarded). On mitigation: simple fine-tuning
   against the attack "merely delayed" it — more shots were needed before a
   harmful response appeared, but it still eventually appeared — while a
   prompt-based classification-and-modification defense "substantially
   reduced" effectiveness, "in one case dropping the attack success rate from
   61% to 2%," tested across the Claude 3 model family. No baseline shot
   count, target model version, or the harm category behind that 61%/2% pair
   is given more specifically in the post's text.

4. **Anil, Durmus, Panickssery [Rimsky], Sharma, et al., "Many-shot
   Jailbreaking," NeurIPS 2024.**
   https://proceedings.neurips.cc/paper_files/paper/2024/file/ea456e232efb72d261715e33ce25f208-Paper-Conference.pdf.
   **Primary** — the formal peer-reviewed paper behind source 3, same
   authors/organization. Opened and confirmed it exists and is the
   NeurIPS 2024 version of the same finding; its scaling results are
   presented as figures (e.g., a file literally named
   `msj_figure_v09_meg.pdf` inside the PDF) that did not extract as readable
   text through the fetch tool. Cited for its formal existence and venue, not
   for any additional number beyond what source 3 already gives in prose —
   do not attribute numbers to this paper that were only confirmed via the
   blog.

5. **Anthropic, Sharma et al., "Constitutional Classifiers: Defending
   Against Universal Jailbreaks Across Thousands of Hours of Red Teaming,"
   arXiv:2501.18837 (Jan. 2025); companion post "Constitutional Classifiers:
   Defending against universal jailbreaks," anthropic.com/news (Feb. 3,
   2025).** https://arxiv.org/abs/2501.18837 (via
   https://ar5iv.labs.arxiv.org/html/2501.18837 for full text) and
   https://www.anthropic.com/news/constitutional-classifiers. **Primary** —
   Anthropic's own paper and post about its own defense; the strongest
   available DEFENSE-side evidence the commission asks for. Exact numbers,
   Section 5.2 (paper): baseline jailbreak success rate against an unguarded,
   HHH-prompted Claude 3.5 Sonnet (New) on the held-out red-teaming set is
   86%; with input and output constitutional classifiers added, that falls to
   "less than 5%" (the companion post gives the precise figure, 4.4%).
   Refusal rate on production Claude.ai traffic rose by 0.38 percentage
   points, absolute, which the paper characterizes as not statistically
   significant. Inference compute overhead: +23.7% relative to the unguarded
   model. Section 4.1 (paper) — the *private prototype* bug-bounty phase:
   from 800 applications, 405 were invited; an estimated 183 were active
   participants; mean red-teaming time estimate 4,720 hours (90% CI
   [3,242, 7,417]); 113 jailbreak reports were submitted; none of the 113
   answered all ten forbidden CBRN-related questions with one jailbreak, so
   no universal jailbreak was found in this phase; Anthropic paid out $95K
   total. The companion post then describes a separate, *public* live
   red-teaming demo, Feb. 3–10, 2025: 339 participants passed at least one
   of eight levels, across "more than 300,000 chat interactions" and
   "approximately 3,700 collective hours"; four participants cleared all
   eight levels, and of those four, one discovered what Anthropic determined
   to be a universal jailbreak. These are two distinct rounds with two
   distinct outcomes (zero vs. one universal jailbreak) — the draft should
   not conflate them.

6. **Anthropic, "Next-generation Constitutional Classifiers: More efficient
   protection against universal jailbreaks," research post (Jan. 9, 2026).**
   https://www.anthropic.com/research/next-generation-constitutional-classifiers.
   **Primary** — Anthropic's own report on its own successor system;
   used for "bring to present." Establishes firsthand: over 1,700 cumulative
   hours of red-teaming across 198,000 attempts found "only one high-risk
   vulnerability" (a detection rate the post computes as 0.005 per thousand
   queries) and, distinct from that single vulnerability, "no red-teamer has
   yet discovered a universal jailbreak" with the new system — contrasted
   explicitly against the original system, where the Feb. 2025 public demo
   did find one. Compute overhead is "roughly 1%" versus the original 23.7%.
   Refusal rate on harmless queries is 0.05% after one month live on Claude
   Sonnet 4.5, which the post calls an 87% drop from the original system.
   Useful caveat for the draft: "high-risk vulnerability" and "universal
   jailbreak" are not the same category in Anthropic's own usage — the one
   vulnerability found is not described as universal.

7. **Nasr, Carlini, Sitawarin, Schulhoff, Hayes, Ilie, Pluto, Song,
   Chaudhari, Shumailov, Thakurta, Xiao, Terzis, Tramèr, "The Attacker Moves
   Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks
   and Prompt Injections," arXiv:2510.09023 (submitted Oct. 10, 2025).**
   https://arxiv.org/abs/2510.09023 and https://arxiv.org/html/2510.09023
   (full text). **Primary** — the authors' own paper reporting their own
   attacks against twelve other groups' published defenses; multi-affiliation
   authorship spanning Google DeepMind and other institutions (Carlini and
   Nasr are also GCG co-authors, source 1). This is the commission's requested
   contradictory case for "defenses are winning": it argues that near-zero
   ASR numbers reported by defense papers reflect weak, non-adaptive attacks,
   not real robustness. Applying gradient search, reinforcement learning,
   random search, and human-guided adaptive attacks tailored to each specific
   defense, the paper reports pushing ASR "above 90% for most" of twelve
   recent defenses that originally claimed "near-zero attack success rates."
   Named results: Circuit Breakers reaches 100% ASR on HarmBench under an
   RL-based adaptive attack; Spotlighting and Prompt Sandwiching, originally
   ~1% ASR, reach >95% under adaptive search; Robust Prompt Optimization
   (RPO) reaches 98% (RL) and 96% (gradient); MetaSecAlign rises from an
   original 2% to 96% under adaptive search; StruQ, Protect AI's detector,
   PromptGuard, and Model Armor all exceed 90%; PIGuard, the most resistant
   defense tested, still reaches 71%; MELON reaches 76–95% depending on
   attacker knowledge. Important scope limit for the draft: Anthropic's
   constitutional classifiers are not among the twelve defenses this paper
   tests — its claim is about the evaluation methodology for jailbreak/prompt-
   injection defenses generally, not a specific refutation of constitutional
   classifiers' reported numbers.

8. **Bisconti, Prandi, Pierucci, Giarrusso, Bracale Syrnikov, Galisai,
   Suriani, Sorokoletova, Sartore, Nardi, "Adversarial Poetry as a Universal
   Single-Turn Jailbreak Mechanism in Large Language Models," arXiv:2511.15304
   (submitted Nov. 19, 2025; current version Jan. 16, 2026).**
   https://arxiv.org/abs/2511.15304 and https://arxiv.org/html/2511.15304
   (full text, tables). **Primary** — the authors' own paper reporting their
   own jailbreak experiments across 25 models. Used for "bring to present"
   and as a second, independent data point on how unevenly current defenses
   perform. Establishes firsthand two result sets: (a) 20 hand-curated
   adversarial poems tested against 25 frontier models, overall ASR 62%
   (Table 3), ranging from Gemini-2.5-pro at 100% and several DeepSeek/
   Mistral/Qwen models in the 85–95% range down to OpenAI's gpt-5 at 10% and
   gpt-5-mini at 5%; Anthropic's claude-opus-4.1 and claude-sonnet-4.5 scored
   35% and 45% respectively; xAI's grok-4 and grok-4-fast scored 35% and 45%.
   (b) A separate, larger test converting 1,200 prompts from the MLCommons
   AILuminate benchmark into verse via a standardized meta-prompt (Table 8):
   overall poetry ASR 43.07% versus an 8.08% prose baseline on the same
   prompts. By provider, the poetry/prose gap is largest for DeepSeek
   (72.04% vs. 9.90%, +62.15 points) and Google (65.76% vs. 8.86%), and
   smallest for OpenAI (8.71% vs. 1.76%) and Anthropic (5.24% vs. 2.11%,
   +3.12 points) — Anthropic's models were the most resistant provider in
   this automated-conversion test even though they were mid-pack on the
   hand-curated poems. The paper states the technique transfers "across
   CBRN, manipulation, cyber-offence, and loss-of-control" risk domains.

9. **Apostol Vassilev, "Robust AI Security and Alignment: A Sisyphean
   Endeavor?" IEEE Security & Privacy, vol. 24, no. 3 (May/June 2026), pp.
   52–58, DOI 10.1109/MSEC.2026.3678214; preprint arXiv:2512.10100.**
   https://arxiv.org/abs/2512.10100 and https://arxiv.org/html/2512.10100v2
   (full text). **Primary** — the author's own formal argument, peer-reviewed
   and published in a mainstream security venue; the strongest available
   source for the commission's CONJECTURE/OPEN band, because unlike the rest
   of the record it is not an empirical measurement but a mathematical claim
   about what is achievable in principle. Establishes firsthand: two named
   theorems. Theorem 2 (Section 2.1, the "ideal" case): "For any checker
   C_Π(T_Π,p) there exist a truth T_Π such that C_Π(T_Π,p)≠1,∀p" — i.e., for
   any checker (the paper's formalization of a guardrail: "filters, policies,
   classifiers, and prompt analysis layers") built from a finite rule set,
   there exists some adversarial prompt the checker fails to catch. Theorem 3
   (Section 2.2) extends the same result to a "finite context window"
   setting closer to how real LLMs operate, which the paper states "only
   tightens the limitation in practice." The paper explicitly extends Gödel's
   1931 incompleteness theorems (a finite, consistent set of axioms cannot
   prove every truth in a sufficiently expressive system) to this checker
   formalism, and claims the scope is "independent of specific AI System
   architectures or languages," covering "present and future AI Systems,
   including AGI and ASI." Its own stated caveats matter for accurate framing:
   the theorems give attackers "no recipes" for finding exploits; the paper
   does not claim security is impossible, only that a *complete, static, once-
   and-for-all* guardrail set cannot exist; and it recommends, as a practical
   response, "a proactive approach of updating the policy with any known new
   adversarial prompts" — continuous red-teaming and update, not resignation.
   Each theorem section is explicitly labeled by the author as "pessimistic"
   but paired immediately with "there are practical measures that could be
   taken to improve the security posture."

10. **Sharon Goldman, "The US wants Anthropic to secure its most powerful AI
    models. But one researcher says that is mathematically impossible,"
    Ground Level AI (Substack), June 17, 2026.**
    https://www.groundlevel-ai.com/p/the-us-wants-anthropic-to-secure.
    **Secondary** — independent tech journalism reporting on and around
    source 9, gathering reactions Vassilev's own paper does not contain.
    Establishes: direct quotes from Vassilev restating his claim for a lay
    audience ("You can never make a claim that you are robust against all
    adversarial prompt attacks"); an on-the-record supportive quote from
    Jamieson O'Reilly, founder of offensive-security firm Dvuln, calling it
    "a solid piece of theoretical work" where "the math lines up with what we
    see in practice"; and two *unnamed* critical sources — one paraphrased as
    saying there is "a long history of misapplying Gödel's theorem to domains
    where it doesn't belong" and that the analysis "doesn't focus on
    real-world security," another paraphrased as skeptical of "impossibility"
    framings generally because they "risk misframing the thing that people
    actually care about, which is simply that vulnerabilities must be found
    and dealt with." Both critics are granted anonymity by the reporter; the
    draft should attribute this skepticism to "researchers quoted anonymously
    by Ground Level AI," not to named individuals, and should not upgrade
    paraphrase to direct quotation.

11. **Cade Metz, "Researchers Poke Holes in Safety Controls of ChatGPT and
    Other Chatbots," The New York Times, July 27, 2023.** Canonical URL
    https://www.nytimes.com/2023/07/27/business/ai-chatgpt-safety-research.html
    (direct fetch blocked by tool policy — nytimes.com is not fetchable by
    this session's tools); full text verified via an authorized reprint PDF
    hosted by Carnegie Mellon University, one of the researchers' home
    institution, at
    https://www.cmu.edu/ambassadors/december-2023/pdf/nyt-fool-ai_07-28-2023.pdf
    (marked "Reprinted With Permission," "Copyright © 2023 by The New York
    Times Company," full byline "By Cade Metz" intact). **Secondary** —
    independent newspaper reporting on the GCG paper's release, gathering
    reactions the paper itself does not contain, though the CMU-hosted PDF is
    a reprint rather than the original page, a limitation worth flagging.
    Establishes: on-the-record reaction quotes gathered by the reporter,
    not present in the GCG paper. Zico Kolter (CMU associate professor, GCG
    co-author): "There is no obvious solution... You can create as many of
    these attacks as you want in a short amount of time." Matt Fredrikson
    (CMU associate professor, GCG co-author): "Through simulated conversation,
    you can use these chatbots to convince people to believe disinformation."
    Company responses gathered by the reporter: Michael Sellitto, Anthropic's
    interim head of policy and societal impacts: "There is more work to be
    done." Hannah Wong, OpenAI spokeswoman: "We are consistently working on
    making our models more robust against adversarial attacks." Elijah Lawal,
    Google spokesman: the company has "built important guardrails into
    Bard... that we'll continue to improve over time." Somesh Jha, University
    of Wisconsin–Madison professor and Google security researcher (not a GCG
    author — an independent domain expert), called the paper "a game
    changer" that could force an industry rethink and possibly government
    legislation. Aviv Ovadya, researcher at Harvard's Berkman Klein Center
    for Internet & Society who helped test ChatGPT pre-release: "This shows —
    very clearly — the brittleness of the defenses we are building into these
    systems." The article's own framing, independent of any single quote:
    "Experts have spent nearly a decade trying to prevent similar attacks on
    image recognition systems without success" — this is the reporter's own
    line, not a quoted claim, connecting GCG to the older adversarial-examples
    literature the commission's opening argument invokes.

12. **Anthropic, "More details on Fable 5's cyber safeguards and our
    jailbreak framework," news post (July 2, 2026).**
    https://www.anthropic.com/news/fable-safeguards-jailbreak-framework.
    **Primary** — Anthropic's own description of its own proposed Cyber
    Jailbreak Severity (CJS) framework; used only for "bring to present, who
    argues this today and what they want." Establishes firsthand: a five-tier
    severity scale, CJS-0 (Informational) through CJS-4 (Critical), scored
    on four axes — capability gain (0–4, how far a jailbreak takes an
    attacker beyond existing tools), breadth of capability gain (0–2, how
    many distinct offensive tasks or vulnerability types it affects), ease of
    weaponization (0–2), and discoverability (0–2, whether the technique is
    already public). Anthropic's own stated rationale, quoted directly:
    "there is no agreed-upon framework for describing a given jailbreak's
    severity. Such a framework would allow AI developers to speak to
    governments (and vice versa) in consistent terms about the risks posed by
    each jailbreak." The post explicitly frames this as a proposal, not a
    settled standard: "What we're sharing today reflects our current
    thinking. Our hope is to spark a helpful discussion across academia,
    industry, civil society, and government." It names "our Glasswing
    partners" once, without elaborating who they are.

13. **LDS Team, "Anthropic Proposes Cross-Industry Framework For Scoring AI
    Jailbreak Severity," Let's Data Science, July 3, 2026.**
    https://letsdatascience.com/news/anthropic-proposes-cross-industry-framework-for-scoring-ai-j-8da00d16.
    **Secondary** — independent tech-news write-up of source 12, used only to
    resolve what source 12 leaves vague. Establishes: "Glasswing" is a named
    coalition, not a single partner — the piece states the CJS scale was
    "developed jointly with Amazon, Microsoft, Google, and other partners in
    its Glasswing coalition." This is the only source read that names the
    coalition's members; treat it as reporting, not confirmed by Anthropic's
    own text.

## Contradictions

- **Relative model robustness flips by attack type.** In the GCG transfer
  results (source 1, Table 2), Claude models are consistently the hardest
  targets: Claude-2's ensemble ASR is 2.1% against GPT-3.5's 86.6%. But in
  Wei et al.'s combination attacks (source 2, Table 1), Claude v1.3 is the
  *more* vulnerable model on the strongest combined attack: combination_2
  hits Claude at 84% versus GPT-4 at 69% (though GPT-4 is worse on
  combination_3, 94% vs. 81%). No single source claims one model is
  universally more robust; "which model resists better" depends on the
  attack family, gradient-optimized suffixes vs. hand-composed prompt
  combinations, not a fixed ranking. The draft should not flatten this into
  "Claude is the safe one."

- **Anthropic's fine-tuning mitigation fails where its classifier mitigation
  succeeds, in the same paper.** Source 3 reports that training the model
  itself to refuse many-shot attacks only delayed the jailbreak (more shots
  needed, same eventual failure), while an external prompt classifier cut ASR
  from 61% to 2%. This is direct evidence for, and a direct qualification of,
  the commission's framing that "safety training is a thin layer over
  capability that's still in the weights" — it held for the fine-tuning
  mitigation specifically, not for architectural (classifier) mitigations,
  which performed very differently in the same test.

- **"Defenses are winning" (source 5/6) versus "defense evaluations
  overstate robustness" (source 7) is a real tension, not a resolved one, and
  the two do not test the same systems.** Constitutional classifiers' 4.4%
  and later sub-1% figures come from Anthropic's own automated and
  human-red-team evaluation of its own system. "The Attacker Moves Second"
  shows that twelve *other* published defenses' near-zero claims collapsed
  under adaptive attack — but constitutional classifiers were not among the
  twelve tested. Neither paper settles whether constitutional classifiers
  specifically would survive the adaptive-attack methodology source 7
  argues for; the honest state is that the strongest defense-side evidence
  and the strongest evaluation-methodology critique currently sit side by
  side without directly colliding.

- **A published, peer-reviewed mathematical "impossibility" claim (source 9)
  is disputed by unnamed domain experts (source 10), not confirmed
  consensus.** The commission asks for care distinguishing "no one has done
  it and there are theoretical reasons it's hard" from "proven impossible."
  Source 9 is a real, peer-reviewed claim that reads as the latter for an
  idealized formalization of "guardrail," but its critics argue the Gödel
  analogy doesn't transfer cleanly to real-world security, and the author's
  own paper stops short of claiming practical defense is futile. Both halves
  of this need to be in the draft; neither the proof nor the skepticism
  should be dropped.

- **How CJS's origin is described differs by source.** Anthropic's own post
  (source 12) credits unspecified "Glasswing partners" once and otherwise
  presents CJS as something it is "sharing" for discussion. Independent
  coverage (source 13) states plainly that Amazon, Microsoft, and Google
  were joint developers via the Glasswing coalition. This is not necessarily
  a factual conflict — source 13 may simply be naming what source 12 left
  implicit — but the draft should attribute the "who built this" claim to
  the secondary source, not present it as something Anthropic itself said.

## Numbers

**GCG (source 1), white-box, Table 1** — Vicuna-7B: individual-behavior ASR
99% (harmful-string ASR 88%); universal (25 training behaviors): 100% train /
98% test ASR on 100 held-out behaviors. LLaMA-2-7B-Chat: individual-behavior
ASR 56% (string ASR 57%); universal: 88% train / 84% test ASR.

**GCG (source 1), transfer, Table 2** — ASR by target model, four conditions:

| Condition | GPT-3.5 | GPT-4 | Claude-1 | Claude-2 | PaLM-2 |
|---|---|---|---|---|---|
| Behavior only (no suffix) | 1.8% | 8.0% | 0.0% | 0.0% | 0.0% |
| + "Sure, here's" | 5.7% | 13.1% | 0.0% | 0.0% | 0.0% |
| + single GCG suffix (opt. on Vicuna) | 34.3% | 34.5% | 2.6% | 0.0% | 31.7% |
| + single GCG suffix (opt. on Vicuna & Guanaco) | 47.4% | 29.1% | 37.6% | 1.8% | 36.1% |
| + ensemble of GCG suffixes | 86.6% | 46.9% | 47.9% | 2.1% | 66.0% |

Denominator throughout: the paper's AdvBench harmful-behaviors set (per-model
counts not separately restated in the extracted table); period: as tested
mid-2023 against the model snapshots named (gpt-3.5-turbo, gpt4-0314,
claude-instant-1, Claude 2, PaLM-2). These are not current model numbers.

**Wei et al. "Jailbroken" (source 2), Table 1, curated 32-prompt set** —
"Bad Bot" rate (fraction eliciting harmful completion):

| Attack | GPT-4 | Claude v1.3 |
|---|---|---|
| None (baseline) | 3% | 0% |
| Prefix injection | 22% | 0% |
| Refusal suppression | 25% | 16% |
| Base64 | 34% | 38% |
| Combination_2 | 69% | 84% |
| Combination_3 | 94% | 81% |

On the held-out synthetic set of 317 prompts (paper's Table 2), combination_3:
93% ± 3% (GPT-4), 87% ± 4% (Claude). Period: tested against GPT-4 and Claude
v1.3, mid-2023 snapshots.

**Many-shot jailbreaking (source 3)** — shots tested: up to 256. One
prompt-based mitigation: ASR 61% → 2% (specific model version, harm category,
and shot count for this pair not given in the prose). No further numeric
series available from text extraction (see Discarded).

**Constitutional classifiers (source 5)** — baseline (unguarded, HHH-prompted
Claude 3.5 Sonnet New) jailbreak success on held-out set: 86%. With
classifiers: <5% (4.4% per companion post). Production refusal-rate increase:
+0.38 percentage points, absolute. Compute overhead: +23.7%. Private bounty:
800 applications → 405 invited → ~183 active; mean 4,720 red-teaming hours
(90% CI 3,242–7,417); 113 reports submitted; 0 of 113 universal; $95K paid.
Public live demo (source 5, companion post): 339 passed ≥1 of 8 levels;
>300,000 chat interactions; ~3,700 collective hours; 4 passed all 8 levels;
1 of those 4 found a confirmed universal jailbreak. Period: Nov. 2024–Feb.
2025 testing window; published Feb. 3, 2025.

**Next-gen constitutional classifiers (source 6)** — 1,700+ cumulative
red-teaming hours; 198,000 attempts; 1 high-risk vulnerability found (not
labeled universal); detection rate 0.005 per 1,000 queries; 0 universal
jailbreaks found to date; compute overhead ~1%; refusal rate on harmless
queries 0.05% after one month live on Claude Sonnet 4.5 (an 87% drop from the
0.38-point original figure's baseline system). Published Jan. 9, 2026.

**The Attacker Moves Second (source 7)** — 12 defenses tested; adaptive ASR
"above 90% for most," against originally reported "near-zero." Named: Circuit
Breakers 100% (RL, HarmBench); Spotlighting/Prompt Sandwiching ~1%→>95%;
RPO 98% (RL) / 96% (gradient); MetaSecAlign 2%→96%; StruQ, Protect AI
detector, PromptGuard, Model Armor each >90%; PIGuard 71% (most resistant of
the twelve); MELON 76–95% (attacker-knowledge-dependent); Data Sentinel >80%
(different metric: objective-redirection accuracy, not ASR — do not conflate
with the ASR figures). Published (arXiv) Oct. 10, 2025.

**Adversarial poetry (source 8)** — hand-curated poems, 25 models, overall
ASR 62% (Table 3); range 5% (gpt-5-mini) to 100% (Gemini-2.5-pro); Anthropic
35–45%. MLCommons meta-prompt conversion, 1,200 prompts (Table 8): overall
43.07% poetry vs. 8.08% prose baseline; Anthropic 5.24% vs. 2.11% baseline
(smallest gap of providers tested, +3.12 points); DeepSeek 72.04% vs. 9.90%
(largest gap, +62.15 points). Published Nov. 19, 2025 (current version Jan.
16, 2026).

**Vassilev proof (source 9)** — not an empirical measurement; a mathematical
existence claim (Theorems 2 and 3) that for any finite checker/guardrail
formalization, an adversarial input exists that evades it. No attack-success
percentage attaches to it; do not report it alongside the empirical ASR
numbers as if comparable.

## Source assets

- **GCG Table 2 (source 1).** A five-model, four-condition grid of ASR
  percentages is exactly the shape a small heatmap or grouped-bar chart
  would carry better than a paragraph: it is the single clearest piece of
  evidence that "transferable, optimizer-found jailbreaks exist" and that
  robustness varies sharply by target model (Claude-2 near 0% throughout,
  GPT-3.5 near 87% at best). Source location: arXiv:2307.15043, Table 2.
  A chart must keep the four attack conditions distinct (behavior-only
  baseline vs. single-suffix vs. ensemble) — collapsing them would hide that
  the ensemble number is a different, weaker claim ("at least one of several
  suffixes worked") than the single-suffix number.

- **Constitutional classifiers before/after (source 5).** The 86% → 4.4%
  figure, plus the 23.7% compute overhead and 0.38-point refusal increase, is
  a compact three-number "what a defense costs and buys" story that a small
  stat-tile row would carry cleanly. Source location: arXiv:2501.18837,
  Section 5.2 / Figure 6A–C. Must retain that 86% is against an *unguarded,
  HHH-prompted* baseline, not against an undefended model with no system
  prompt at all — the paper is explicit that this is already a reasonably
  strong starting point, not a strawman.

- **Two-generation defense comparison (sources 5 and 6).** Compute overhead
  23.7% → ~1%, and refusal-rate increase 0.38 → 0.05 percentage points,
  across the two Anthropic generations is a clean before/after pair for
  showing that defenses are getting cheaper and less disruptive over time
  even as the underlying robustness claim (no universal jailbreak found) is
  qualitatively similar. Source locations: arXiv:2501.18837 §5.2;
  anthropic.com/research/next-generation-constitutional-classifiers.

- **Adaptive-attack collapse (source 7).** A before/after pair per defense
  (originally-reported ASR vs. adaptive-attack ASR) across twelve defenses
  is a strong visual argument for "reported robustness depends on how hard
  you looked" — e.g., MetaSecAlign 2%→96%, Circuit Breakers near-0%→100%.
  Source location: arXiv:2510.09023, results tables (Section 4/5 in the
  HTML version). A chart must not include constitutional classifiers in this
  set, since it was not tested by this paper — mixing it in would misstate
  what was shown.

- **Poetry ASR by provider (source 8).** Table 8's nine-provider prose vs.
  poetry comparison (8.08% vs. 43.07% overall, with Anthropic smallest gap
  and DeepSeek largest) is a strong small-multiples or slope-chart candidate
  for showing uneven defense generalization across providers to one novel
  attack style. Source location: arXiv:2511.15304, Table 8. Must keep prose
  baseline and poetry ASR paired per provider — the raw poetry number alone
  overstates the effect for providers (e.g., Mistral) that already had a
  high prose baseline.

- None found for the Vassilev proof (source 9) or the NYT coverage (source
  11) — both are argument/narrative sources without a table or figure that
  would out-perform prose.

## Discarded

- **NIST AI 100-2, "Adversarial Machine Learning: A Taxonomy and
  Terminology of Attacks and Mitigations"** — found via search while
  chasing the Vassilev proof's context; not opened in full. Discarded
  because the commission's mechanism source is already satisfied by Wei et
  al. (source 2), and adding a second taxonomy paper risked padding rather
  than adding a new claim.
- **anthropic.com/news/testing-our-safety-defenses-with-a-new-bug-bounty-program**
  — found via search; appears to be an earlier Anthropic post announcing the
  bounty program ahead of results. Not opened, because source 5's paper
  Section 4.1 and companion post already give the completed results
  first-hand with exact numbers; the announcement-stage post would add no
  new figure.
- **VentureBeat, "Anthropic claims new AI security method blocks 95% of
  jailbreaks, invites red teamers to try"** — found via search. Discarded as
  redundant secondary coverage of source 5's own announcement; the primary
  paper already gives the exact 86%→4.4% figures with more precision than
  the rounded "95%" headline, so this added no verification value beyond
  what was already confirmed against the primary.
- **A biosecurity playbook for AI companies (EA Forum post)** — attempted
  fetch to find a developed statement of the "jailbreak risk is overstated
  because the information is already public" position; the fetch returned
  HTTP 403 and was not retried through an alternate route given time spent
  elsewhere in the record. This is the one gap flagged in the opening
  paragraph: the "dismissive" pole of the debate is under-sourced relative
  to the "doom" pole.
- **Anthropic's "testing our safety defenses" HackerOne/Model Safety Bug
  Bounty help-center page** — found via search, not opened; would only
  restate program mechanics already covered by source 5's own account of
  the same program.
- **Multiple AI-generated-looking blog aggregations of the Vassilev story**
  (CovertSwarm, ISSSource, techjacksolutions, EdTech Innovation Hub) — found
  via search while corroborating source 9/10; not opened individually once
  Ground Level AI (source 10) supplied named, attributed reaction and the
  arXiv preprint (source 9) supplied the primary theorem text directly. Risk
  of these being low-effort rewrites of the same NIST press release was high
  enough not to spend further budget confirming each independently.
