# Evidence: the-mechanics/agent-loops (01)

The evidence supports the commission's spine directly. ReAct owns the loop shape
(model proposes reasoning + action, a harness executes, the result is appended,
the model is called again) and documents the exact failure the article starts
from: ReAct "repetitively generates the previous thoughts and actions" and
"fails to reason about what the proper next action to take and jump out of the
loop." Huang et al. own the weak-signal claim, but with a limit the writer must
respect: intrinsic (self-judged) self-correction degrades accuracy, yet
self-correction with an oracle signal improves it, so the finding is about the
quality of the error signal, not an inability to revise. Reflexion, SWE-agent,
and LangGraph own the "what breaks the loop" side: an explicit memory of past
attempts, a harness guardrail on the action, and a blunt step cap. The angle
that looping is the default of the stateless-predictor-plus-harness design holds,
with two refinements recorded under Contradictions: ReAct's authors attribute
part of the loop to greedy decoding (the token-level cousin the article
contrasts), and models do revise when handed a reliable external signal. The
evidence is thinnest on a clean, quotable public transcript of an autonomous
runner looping: the strongest concrete instances are the peer-reviewed error
analyses (SWE-agent, AgentBench, ReAct); the AutoGPT report is real but a single
unreplicated user log.

## Sources

```text
URL:         https://arxiv.org/abs/2210.03629
Kind:        primary. The authors own ReAct, its loop design, and its error
             analysis; the failure percentages are their own manual labeling.
Establishes: The agent loop as an architecture (interleave reasoning traces and
             task-specific actions; actions "interface with external sources,
             such as knowledge bases or environments"; reasoning traces "induce,
             track, and update action plans as well as handle exceptions"). Also
             establishes the article's opening behavior firsthand: a repetitive
             action/thought loop ReAct falls into and cannot exit.
Paraphrase:  In an error analysis of 50 sampled ReAct trajectories on HotpotQA,
             the authors name one frequent failure specific to ReAct: the model
             keeps regenerating its previous thoughts and actions and cannot
             reason its way to a different next action, i.e. cannot leave the
             loop. They fold this into the "reasoning error" category. In a
             footnote they attribute it to greedy decoding and suggest better
             decoding (e.g. beam search) might help.
Locators:    Abstract (loop definition). Section 3.3 "Results and Observations,"
             subsection "ReAct vs. CoT," and Table 2, whose "Reasoning error"
             row is defined "Wrong reasoning trace (including failing to recover
             from repetitive steps)" at 47% for ReAct vs 16% for CoT. Footnote 6.
Quote:       "we note that there is one frequent error pattern specific to ReAct,
             in which the model repetitively generates the previous thoughts and
             actions, and we categorize it as part of ''reasoning error'' as the
             model fails to reason about what the proper next action to take and
             jump out of the loop." Footnote 6: "We suspect that this could be
             due to the sub-optimal greedy decoding procedure, and future work
             using better decoding (e.g. beam search) might help address this
             issue."
```

```text
URL:         https://arxiv.org/abs/2303.11366
Kind:        primary. The authors own the Reflexion method and its measured
             gains.
Establishes: Exactly what breaks the loop by changing the context: a verbal
             self-reflection step plus an episodic memory of past attempts,
             added on top of a base agent loop (including ReAct). The measured
             effect isolates the missing ingredient: memory of what was already
             tried.
Paraphrase:  Reflexion reinforces an agent not by updating weights but through
             linguistic feedback: after a failed trial the agent verbally
             reflects on the feedback and stores that reflective text in an
             episodic memory buffer, which it conditions on in later trials. The
             Actor generates actions from observations; an Evaluator scores the
             output; a Self-Reflection model turns that into verbal feedback. The
             long-term memory is a sliding window with a maximum capacity.
Locators:    Abstract; Section 3 (Actor, Evaluator, Self-Reflection, Memory
             definitions); Figure 2 ("(a) Diagram of Reflexion. (b) Reflexion
             reinforcement algorithm"); Table 1 (programming results); Section
             4.1 (AlfWorld); the sliding-window note in the limitations
             discussion.
Quote:       "Reflexion agents verbally reflect on task feedback signals, then
             maintain their own reflective text in an episodic memory buffer to
             induce better decision-making in subsequent trials." "ReAct +
             Reflexion significantly outperforms ReAct by completing 130 out of
             134 tasks using the simple heuristic to detect hallucinations and
             inefficient planning."
```

```text
URL:         https://arxiv.org/abs/2310.01798
Kind:        primary. Google DeepMind and UIUC authors; the experiments and
             claim are their own.
Establishes: Why an appended error is weak signal, stated precisely and with the
             counter-case attached. Without an external/oracle signal,
             self-correction usually does not help and often lowers accuracy; the
             stated cause is that the model cannot reliably judge whether its own
             reasoning is correct. With an oracle signal, self-correction helps.
Paraphrase:  The authors define "intrinsic self-correction": the model tries to
             fix its own answer using only its own capabilities, no external
             feedback. In that setting accuracy stagnates or drops across
             correction rounds. They attribute prior positive results to oracle
             labels and show the gains vanish without them. The mechanism they
             give: the model is likelier to change a correct answer to a wrong
             one than the reverse, because it cannot properly judge its own
             reasoning's correctness.
Locators:    Abstract; Section 2 (definition of intrinsic self-correction);
             Table 2 (with oracle labels, gains) and Table 3 (intrinsic,
             degradation); Section 3.3 (the "cannot properly judge" mechanism).
Quote:       "LLMs struggle to self-correct their responses without external
             feedback, and at times, their performance even degrades after
             self-correction." "The fundamental issue is that LLMs cannot
             properly judge the correctness of their reasoning." "the
             improvements in these studies result from using oracle labels to
             guide the self-correction process, and the improvements vanish when
             oracle labels are not available."
```

```text
URL:         https://arxiv.org/abs/2405.15793
Kind:        primary. The SWE-agent authors own the interface, the benchmark
             runs, and the failure statistics.
Establishes: The strongest concrete, faithful looping instance for the writer:
             an autonomous coding agent that repeatedly edits the same code
             after an errant edit introduces a syntax error. Also establishes a
             harness-level fix (a guardrail on the edit action), which locates
             part of the cause in the harness, not only the model.
Paraphrase:  A prominent failure mode of SWE-agent is repeatedly editing the same
             snippet, usually after the agent introduced a syntax error (wrong
             indentation, an extra parenthesis) with an errant edit. Failed edits
             are common: of 2942 SWE-bench task instances, 1185 (51.7%) of the
             GPT-4-Turbo trajectories contain one or more failed edits, and the
             chance of recovery falls as failed edits accumulate. The authors add
             a guardrail to the edit logic that applies a modification only if it
             does not produce major errors, and report it improves performance
             considerably.
Locators:    Abstract and Section 1 (12.47% of SWE-bench test tasks resolved with
             GPT-4 Turbo; pass@1 12.5%; prior non-interactive best 3.8%);
             Section 5.2 (repeated-edit failure mode and the edit-logic
             intervention; Figure 6 compares edit-with-linting vs edit-without
             vs no-edit; Figure 8 notes late turns are mostly "edit, then
             execute" loops); Section 3 (the code linter integrated into the edit
             function).
Quote:       "A prominent failure mode occurs when models repeatedly edit the
             same code snippet. The usual suspect for this behavior is an agent
             introducing a syntax error (e.g., incorrect indentation, extra
             parenthesis) via an errant edit. As discussed in Section 3, we add
             an intervention to the edit logic that lets a modification apply
             only if it does not produce major errors." "out of 2942 task
             instances, 1185 (51.7%) of SWE-agent w/ GPT-4 Turbo trajectories
             have 1+ failed edits."
```

```text
URL:         https://arxiv.org/abs/2308.03688
Kind:        primary. The AgentBench authors own the benchmark and its
             finish-reason accounting.
Establishes: A second documented, measured looping instance across many
             environments, and that it is a leading cause of incompletion. When
             an agent fails, one named reason is that it "begins to do repeated
             generations for many turns."
Paraphrase:  AgentBench classifies why a run ends. One category, Task Limit
             Exceeded, covers a run that either hits the maximum interaction
             turns without solving the task or starts producing repeated
             generations for many turns. The authors say Task Limit Exceeded
             dominantly caused incompleteness and that it often indicates weak
             multi-turn ability. They test plain chain-of-thought prompting,
             without multiple trials or reflection, as the common deployment.
Locators:    Section 2 "LLM-as-Agent: Definition and Preliminary" (the finish
             reasons IF / IA / TLE / Complete; TLE defined as "the agent does not
             solve the problem after reaching the predefined maximum interaction
             turns or begins to do repeated generations for many turns"); Table 4
             (finish-reason portions, TLE ranging up to 82.5% across tasks).
             Published at ICLR 2024.
Quote:       "Task Limit Exceeded (TLE): the agent does not solve the problem
             after reaching the predefined maximum interaction turns or begins to
             do repeated generations for many turns." "TLE often indicates a weak
             multi-turn ability in certain tasks."
```

```text
URL:         https://docs.langchain.com/oss/python/langgraph/graph-api
Kind:        primary. LangChain's own documentation of its own framework's
             behavior; authorship and stake sit with the framework owner.
Establishes: A harness-level guard against a runaway loop as shipped default
             engineering, and its shape: a blunt cap on total steps, not loop
             detection. This supports the article's line between a real fix and a
             cosmetic one, and shows the base loop ships with no built-in "already
             tried, do not repeat" check.
Paraphrase:  LangGraph's recursion_limit sets the maximum number of super-steps a
             graph can run in a single execution; when the limit is reached the
             framework raises GraphRecursionError. The errors page says this is
             "often due to an infinite loop" and tells the developer that if they
             did not expect many iterations they "likely have a cycle" and should
             check for infinite loops.
Locators:    graph-api page, recursion-limit discussion ("the maximum number of
             super-steps"; "Once the limit is reached, LangGraph will raise
             GraphRecursionError"; "Starting in version 1.0.6, the default
             recursion limit is set to 1000 steps"). Errors page
             (docs.langchain.com/oss/python/langgraph/errors/GRAPH_RECURSION_LIMIT):
             "This is often due to an infinite loop" and "you likely have a
             cycle. Check your logic for infinite loops."
Quote:       "The recursion limit sets the maximum number of super-steps the
             graph can execute during a single execution." "Once the limit is
             reached, LangGraph will raise GraphRecursionError."
```

```text
URL:         https://github.com/Significant-Gravitas/AutoGPT/issues/1994
Kind:        primary, as a firsthand public report: the reporter ran the agent
             and pasted their own console log. It is primary evidence that a user
             observed this behavior, not proof of how common it is.
Establishes: The AutoGPT-style real-world instance the commission invokes. An
             autonomous runner re-issued an identical search command in
             consecutive turns after it had already received results, i.e. an
             action-level loop in the wild.
Paraphrase:  A user (login AoiRei) opened "Gets stuck in a loop" on 2023-04-16,
             reporting that AutoGPT re-ran the same Google query across
             consecutive turns although it had already retrieved results. The
             pasted log shows the same command (COMMAND = google with an
             identical input argument) at three successive timestamps. The issue
             was later closed as not planned / stale.
Locators:    Issue #1994, title "Gets stuck in a loop," opened by AoiRei
             2023-04-16; the pasted console log in the issue body showing the
             repeated google command at three timestamps.
Quote:       Reporter: "It loops the same queries although it successfully got the
             google results." (The exact repeated log line, per the issue body:
             COMMAND = google ARGUMENTS = {'input': 'personal income tax rates in
             countries with low business tax rates'}, at three consecutive
             timestamps.)
```

```text
URL:         https://arxiv.org/abs/2407.01502
Kind:        primary. Kapoor et al. (Princeton) own the critique and the
             re-analyses of agent evaluations.
Establishes: The counter-frame the writer needs when separating a real fix from a
             cosmetic one: retrying is often used deliberately and can match
             complex agents at lower cost, so a repeated action is not always an
             unintended loop. Also that the top WebArena agent (STeP) succeeds by
             hardcoding a brittle per-task policy, a different failure than
             looping.
Paraphrase:  The paper argues agent evaluations must be cost-controlled because
             complex agents reach high accuracy through many expensive calls, and
             that simple repeated-sampling retry strategies can match or beat
             reported agents more cheaply. It documents no repeated-action loop
             transcript; its concrete failure case is a brittle hardcoded policy
             (append "/user/user_name" to a base URL) that breaks if the site
             changes.
Locators:    Section 2 / 2.1 (cost control, retries); Section 5.1 (STeP hardcoded
             WebArena policy). arXiv:2407.01502, 2024.
Quote:       (No looping quote; recorded specifically as the source that does not
             document a loop, to guard against citing it as one.)
```

```text
URL:         https://github.com/vectara/awesome-agent-failures/blob/main/docs/case-studies/autogpt-planning-failures.md
Kind:        secondary. A community-curated case study maintained by Vectara that
             reports on AutoGPT looping from outside; it aggregates other
             people's reports and papers rather than owning any observation.
Establishes: Context only: that repeated-action looping in autonomous runners is
             a recognized, catalogued failure mode, described as agents that
             "got stuck in infinite loops, repeatedly performing the same actions
             without making progress," including recursive self-verification
             loops. Used for framing, not for any figure.
Paraphrase:  The document characterizes AutoGPT as frequently stuck in infinite
             loops that repeat actions without progress, including verify-then-
             re-verify cycles, and points to underlying GitHub issues, Reddit
             threads, and papers. Treat its specific downstream claims (e.g. a
             named incident-database entry) as unverified here.
Locators:    Case-study markdown, "autogpt-planning-failures"; sections on loop
             behavior and cited sources.
Quote:       "the agent frequently got stuck in infinite loops, repeatedly
             performing the same actions without making progress toward its
             goals."
```

## Contradictions

- Against overstating the model's inability to revise: Huang et al. Table 2
  shows self-correction with an oracle signal improves accuracy (GPT-3.5 GSM8K
  75.9 to 84.3; CommonSenseQA 75.8 to 89.7; HotpotQA 26.0 to 29.0), while their
  Table 3 shows intrinsic self-correction degrading it. The failure is specific
  to self-judged feedback, not to error feedback in general. The writer must not
  round this to "models cannot self-correct." It supports, rather than
  undercuts, the article's claim that a real fix supplies a better signal.
- Against locating the whole cause in statelessness: ReAct's authors attribute
  their loop partly to greedy decoding and suggest better decoding might help
  (footnote 6). This is the token-level cousin the article contrasts
  (the-mechanics/repetition-loops), and it means some action-level looping is
  decoding-level and harness-addressable, not a pure consequence of the model
  re-reading a transcript. Consistent with the angle, but the writer should not
  claim the transcript is the only driver.
- Against "it is purely a model behavior": SWE-agent's edit-logic guardrail and
  LangGraph's step cap are harness changes that reduce or bound looping. This
  supports the article's real-fix / cosmetic-fix distinction, and also shows the
  cause is shared between the model and the harness. AgentBench, by contrast,
  reads Task Limit Exceeded as "weak multi-turn ability," placing more of the
  cause in the model. Both are recorded; they disagree on where the weight sits.
- Kapoor et al. do not document a looping transcript; their nearest point is that
  simple repeated retries can match complex agents on accuracy at lower cost.
  That is retrying by design, not an unintended loop, and should not be cited as
  a looping instance.

## Numbers

```text
Figure: ReAct HotpotQA "reasoning error" rate 47% (ReAct) vs 16% (CoT)
Owner:  ReAct, Yao et al. 2022, Table 2
Scope:  50 randomly sampled ReAct trajectories and 50 CoT trajectories on
        HotpotQA, human-labeled. The category is "Wrong reasoning trace
        (including failing to recover from repetitive steps)"; the repetitive
        loop is a subset of this row, not the whole 47%. Do not report 47% as
        the looping rate.
```

```text
Figure: Reflexion 91.0 pass@1 on HumanEval (Python) vs 80.1 prior GPT-4 SOTA
Owner:  Reflexion, Shinn et al. 2023, Table 1
Scope:  HumanEval Python, pass@1. Same table: MBPP Python 77.1 (below the 80.1
        GPT-4 baseline), so the gain is not uniform across benchmarks.
```

```text
Figure: ReAct + Reflexion completes 130 of 134 AlfWorld tasks
Owner:  Reflexion, Shinn et al. 2023, Section 4.1
Scope:  AlfWorld, over 12 trials, versus plain ReAct; the gain isolates the
        memory-of-attempts ingredient.
```

```text
Figure: Intrinsic self-correction, GPT-4 GSM8K: 95.5 -> 91.5 -> 89.0
Owner:  Huang et al. 2023, Table 3
Scope:  Standard prompting (1 call) then two self-correction rounds (3 and 5
        calls). Companion drops: GPT-3.5 GSM8K 75.9 -> 75.1 -> 74.7; GPT-3.5
        CommonSenseQA 75.8 -> 38.1 -> 41.8 (the sharpest fall); GPT-4 HotpotQA
        49.0 -> 49.0 -> 43.0. All are the no-external-signal setting.
```

```text
Figure: Oracle self-correction lifts accuracy, e.g. GPT-3.5 CommonSenseQA
        75.8 -> 89.7
Owner:  Huang et al. 2023, Table 2
Scope:  With a correct-label oracle deciding when to stop. This is the
        counter-case; keep it beside the Table 3 figures so neither is
        misread.
```

```text
Figure: 1185 of 2942 SWE-bench trajectories (51.7%) contain 1+ failed edits
Owner:  SWE-agent, Yang et al. 2024, Section 5.2
Scope:  SWE-agent with GPT-4 Turbo over the full SWE-bench test set; recovery
        odds fall as failed edits accumulate.
```

```text
Figure: SWE-agent resolves 12.47% of SWE-bench test tasks (pass@1 12.5%)
Owner:  SWE-agent, Yang et al. 2024, Abstract / Section 1
Scope:  Full SWE-bench test set with GPT-4 Turbo; prior non-interactive
        retrieval-augmented best was 3.8%. Context for how often these agents
        finish at all, which is where looping eats the budget.
```

```text
Figure: LangGraph default recursion_limit = 1000 super-steps (was 25 earlier)
Owner:  LangChain LangGraph docs
Scope:  Default as of version 1.0.6; earlier versions defaulted to 25. Record
        the change; do not state a single fixed default as timeless.
```

## Limits

- No single peer-reviewed, quotable step-by-step transcript of one autonomous
  run looping was found in a form the writer can reproduce line by line. The
  faithful concrete instances are the described failure modes (SWE-agent's
  repeated edits after a syntax error; AgentBench's repeated generations; ReAct's
  repeated thoughts and actions) plus the AutoGPT user log. The SWE-agent case is
  the most defensible to describe in prose; the AutoGPT log is the most vivid but
  is a single unreplicated report.
- The commission wants the cause chain to reach ground at "the model predicts the
  next action from the transcript and the harness runs it." No source states that
  ground proposition as such; it is the article's synthesis. ReAct supplies the
  loop mechanics and Huang et al. supply the weak-signal step, but the final
  reduction is the writer's own work, to be presented as reasoning from the
  sources, not as a sourced claim.
- Why models under-weight their own error feedback is left open by the sources.
  Huang et al. give a proximate cause (the model cannot judge its own reasoning's
  correctness) but not a mechanism below it. Mark this as an open question, as
  the commission asks.
- "Sampling temperature adds noise, not strategy" is not established by these
  four papers; it is taught in the-mechanics/sampling-temperature, which the
  writer links. ReAct's footnote 6 touches decoding but does not prove the
  temperature claim.
- Statelessness itself is taught in the-mechanics/conversation-memory and hangman
  (linked), not re-established here.

## Source assets

```text
Asset: Reflexion Figure 2(a), the diagram of the Actor / Evaluator /
       Self-Reflection loop with the episodic memory buffer.
Shows: The base loop with the two added parts (a reflection step and a memory of
       past attempts) that break the repeat. This is the visual that matches the
       "what breaks the loop" section.
Crop:  Likely better rebuilt as a numbered-steps component than captured, so the
       four base-loop steps and the two Reflexion additions read in the paper's
       own labels. If captured, keep the memory buffer and the arrow from
       self-reflection back into the next trial; omit the algorithm box in 2(b).
```

```text
Asset: SWE-agent Figure 6, comparing edit-with-linting against edit-without-
       linting and no-edit.
Shows: A harness change (the edit guardrail) moving performance, i.e. a real fix
       operating on the harness rather than the prompt. Direct support for the
       real-fix / cosmetic-fix distinction.
Crop:  Keep the three conditions and the outcome axis; keep the axis label and
       cite the source in the caption.
```

```text
Asset: Huang et al. Tables 2 and 3 (oracle vs intrinsic self-correction).
Shows: Accuracy rising with an oracle signal and falling or flat without one,
       side by side. The single clearest picture of "the signal quality is the
       variable."
Crop:  If rebuilt as a small chart, keep both settings in one frame so the
       contrast is unmissable; label rounds/calls and cite the table.
```

```text
Asset: AutoGPT issue #1994 console log, the same google command at three
       consecutive timestamps.
Shows: An action-level loop as it appeared to a user: identical command, back to
       back, after results were already returned.
Crop:  If shown, keep the three repeated COMMAND lines and their timestamps;
       omit surrounding stack noise. Treat as one user's log, not a rate.
```

```text
Asset: ReAct Table 2 (success/failure modes, ReAct vs CoT on HotpotQA).
Shows: Where ReAct's errors concentrate (reasoning error 47%) versus CoT's
       (hallucination 56%), with the repetitive loop living inside ReAct's
       reasoning-error row.
Crop:  If used, keep the category definitions, especially "including failing to
       recover from repetitive steps," so the row is not misread as generic
       reasoning error.
```

## Discarded

```text
URL: https://github.com/Significant-Gravitas/AutoGPT/issues/2726 — read; the
     "loop" there is an API bad-gateway wait/retry, not an action-level loop, so
     it is weaker than #1994 for the article's behavior. Not cited.
URL: https://langchain-ai.github.io/langgraph/concepts/low_level/ — returned only
     a redirect stub; superseded by the docs.langchain.com graph-api and errors
     pages, which carry the current recursion_limit text.
```
