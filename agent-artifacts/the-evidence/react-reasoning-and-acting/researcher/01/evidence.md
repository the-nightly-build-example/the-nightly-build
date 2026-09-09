# Evidence: the-evidence / react-reasoning-and-acting

Reading the ReAct paper, Yao et al., "ReAct: Synergizing Reasoning and Acting in
Language Models" (arXiv 2210.03629; v1 6 Oct 2022; published as a conference
paper at ICLR 2023). All numbers below were read from the paper PDF itself
(extracted and quoted, not from coverage). Every source URL was opened and
returned 200 before recording. github.com avoided per environment block; arXiv
and official docs used.

## Source list (6 total; 5 primary, 1 secondary)

### S1 — PRIMARY
arXiv · Yao, Zhao, Yu, Du, Shafran, Narasimhan, Cao, "ReAct: Synergizing
Reasoning and Acting in Language Models"
URL: https://arxiv.org/abs/2210.03629  (opened, 200; PDF at /pdf/2210.03629 also opened, 33 pp.)
Supports: the whole method and every ReAct number below.

Key facts quoted / read:
- Method: interleave reasoning traces ("thought") with task-specific actions,
  reading results ("observation") back, in a loop. Abstract: "generate both
  reasoning traces and task-specific actions in an interleaved manner."
- Base model: "large language model, PaLM-540B (Chowdhery et al., 2022) ... is
  prompted with few-shot in-context [examples]." Few-shot PROMPTING, not
  fine-tuning, for the main results. "learning solely from one to six in-context
  examples." Footnote: "We show some GPT-3 (Brown et al., 2020) results in
  Appendix A.1, which outperforms PaLM-540B." (Appendix Table 5: ALFWorld
  success rate 70.9 PaLM-540B vs 78.4 GPT-3 text-davinci-002.)
- Action API for HotpotQA / FEVER (a Wikipedia API): three actions —
  `search[entity]`, `lookup[string]`, `finish[answer]`. (Section 3.1.)
- Table 1 (PaLM-540B prompting; HotpotQA Exact Match / FEVER Accuracy):
    Standard        28.7 / 57.1
    CoT (Wei et al.) 29.4 / 56.3
    CoT-SC           33.4 / 60.4
    Act              25.7 / 58.9
    ReAct            27.4 / 60.9
    CoT-SC → ReAct   34.2 / 64.6
    ReAct → CoT-SC   35.1 / 62.0
    Supervised SoTA  67.5 / 89.5
  Paper's own words: "ReAct outperforms CoT on Fever (60.9 vs. 56.3) and
  slightly lags behind CoT on HotpotQA (27.4 vs. 29.4)." And: "the best
  prompting method on HotpotQA and Fever are ReAct→CoT-SC and CoT-SC→ReAct
  respectively."
- Hallucination analysis, Table 2 (manual labels on 50 correct + 50 incorrect
  trajectories each for ReAct and CoT on HotpotQA, 200 total):
    Success / True positive:    ReAct 94%  CoT 86%
    Success / False positive (hallucinated): ReAct 6%  CoT 14%
    Failure / Hallucination:    ReAct 0%   CoT 56%
    Failure / Reasoning error:  ReAct 47%  CoT 16%
    Failure / Search result error: ReAct 23%  CoT —
  Paper: "Hallucination is a serious problem for CoT, resulting in much higher
  false positive rate than ReAct (14% vs. 6%) in success mode, and make up its
  major failure mode (56%)." Also names ReAct's own tradeoff: the structural
  constraint "reduces its flexibility ... leading to more reasoning error rate
  than CoT," and non-informative search "counts for 23% of the error cases."
- ALFWorld, Table 3 (success rate %, overall "All" column): ReAct best-of-6 71,
  Act best-of-6 45, BUTLER best-of-8 37, ReAct-IM best-of-6 53, ReAct avg 57.
  Paper: "the best ReAct trial achieves an average success rate of 71%,
  significantly outperforming the best Act (45%) and BUTLER (37%) trials." "even
  the worse ReAct trial (48%) beats the best trial of both methods." Advantage
  over Act "averaging 62%" relative gain across six trials.
- WebShop, Table 4 (Score / Success Rate): Act 62.3/30.1, ReAct 66.6/40.0,
  IL 59.9/29.1, IL+RL 62.4/28.7, Human (expert) 82.1/59.6. Paper: ReAct gives
  "an absolute 10% improvement over the previous best success rate"; "existing
  methods are still far from the performance of expert humans."
- Abstract headline: on ALFWorld and WebShop, "ReAct outperforms imitation and
  reinforcement learning methods by an absolute success rate of 34% and 10%
  respectively, while being prompted with only one or two in-context examples."
  (34 pts = ALFWorld 71 vs BUTLER 37; 10 pts = WebShop 40.0 vs 30.1.)
- Novelty claim: "To our knowledge, ReAct is the first demonstration of combined
  reasoning and action using an LLM applied to an interactive environment within
  a closed-loop system."
- Worked trace (Figure 1, HotpotQA, the "Apple Remote" example), read verbatim
  from the PDF:
    Question: "Aside from the Apple Remote, what other device can control the
    program Apple Remote was originally designed to interact with?"
    Thought 1: I need to search Apple Remote and find the program it was
    originally designed to interact with.
    Act 1: Search[Apple Remote]
    Obs 1: The Apple Remote is a remote control introduced in October 2005 ...
    originally designed to control the Front Row media center program ...
    Thought 2: Apple Remote was originally designed to control the Front Row
    media center program. I need to search Front Row next ...
    Act 2: Search[Front Row]
    Obs 2: Could not find [Front Row]. Similar: [Front Row Seat to Earth, Front
    Row Motorsports, Front Row (software) ...]
    Thought 3: Front Row is not found. I need to search Front Row (software).
    Act 3: Search[Front Row software]
    Obs 3: Front Row is a discontinued media center software ...
    Thought 4: Front Row software is controlled by an Apple Remote or the
    keyboard function keys. So the answer is keyboard function keys.
    Act 4: Finish[keyboard function keys]

### S2 — PRIMARY
arXiv · Wei, Wang, Schuurmans, Bosma, Ichter, Xia, Chi, Le, Zhou,
"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
URL: https://arxiv.org/abs/2201.11903  (opened, 200)
Supports: identifies the CoT baseline ReAct is measured against — prompting a
model with worked intermediate reasoning steps. Used only as the baseline; the
CoT lesson already teaches it and is linked, not re-taught.

### S3 — PRIMARY
arXiv · Chowdhery et al., "PaLM: Scaling Language Modeling with Pathways"
URL: https://arxiv.org/abs/2204.02311  (opened, 200)
Supports: the base model behind ReAct's main results is PaLM, "a 540-billion
parameter, densely activated, Transformer language model."

### S4 — PRIMARY
Anthropic · "Tool use with Claude" (platform documentation)
URL: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview  (opened, 200)
Supports: how today's agents actually run the loop — the model returns a
structured `tool_use` block, "Your code executes the operation and sends back a
`tool_result`," and a second request continues. A native, schema-driven round
trip, not the paper's hand-written thought/act/observation text format.

### S5 — PRIMARY
OpenAI · "Function calling" (platform documentation)
URL: https://developers.openai.com/api/docs/guides/function-calling  (opened, 200)
Supports: the same modern loop stated as five steps — request with tools, model
returns a tool call, your code executes it, second request with the output,
final response. Confirms native function-calling is the shared industry format
that replaced prompted ReAct traces.

### S6 — SECONDARY
IBM Think · "What is a ReAct Agent?"
URL: https://www.ibm.com/think/topics/react-agent  (opened, 200)
Supports: context for how "ReAct" is invoked today — "an AI agent that uses the
'reasoning and acting' (ReAct) framework to combine chain of thought (CoT)
reasoning with external tool use," positioned as a foundational pattern for
current agents. Shows the term now names a general pattern, looser than the
paper's specific prompted method.

## Notes on honesty / discrepancies
- An automated summarizer initially reported HotpotQA numbers of 78/69/39 for
  ReAct/CoT/Standard. These are WRONG. The real Table 1 exact-match figures
  (read from the PDF) are 27.4 / 29.4 / 28.7. Multi-hop QA exact match is low;
  the 78% figure was a fabrication and is not used.
- The paper's headline "34% and 10%" gains are the two INTERACTIVE benchmarks
  only (ALFWorld, WebShop). On the QA benchmark it is most associated with,
  ReAct alone slightly lost to plain CoT. The lesson holds both facts.
