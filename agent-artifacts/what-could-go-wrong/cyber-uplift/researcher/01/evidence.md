# Evidence record: what-could-go-wrong/cyber-uplift (01)

The evidence cleanly supports claim (1): AI systems have found real, previously
unknown, exploitable vulnerabilities in widely used software, with two firsthand
demonstrations (Google's Big Sleep SQLite bug and the 18 real-world flaws surfaced
in the DARPA AI Cyber Challenge finals). It gestures at claim (2) but does not show
it: every published academic benchmark caps out well below expert real-world
operations (Cybench's best model solved 17.5% of tasks and nothing a human took
longer than 11 minutes to crack; DeepMind's own Gemini agents solved 3 of 13
easy-to-medium CTFs and 0 of 13 Hack The Box challenges), and the one paper
claiming high autonomous-exploit success (Fang et al., 87%) collapses to 7% once
the CVE write-up is withheld, so it demonstrates exploitation of *disclosed* bugs,
not discovery. Claim (3) — a decisive *attacker* advantage — is unshown and
directly contested by the record: the two strongest offensive demonstrations both
come from *defensive* research programs (Project Zero; DARPA's find-and-patch
challenge), and the national-agency assessment (UK NCSC) judges that advanced
offensive uplift concentrates among actors who are *already* highly capable, not
among novices. The record's most important limitation: the clearest "AI found a
real bug" evidence is produced by the labs and defenders themselves (interested
parties running their own tools), and there is no primary, non-conjectural source
for the maximalist "AI collapses the cost of attack faster than defense adapts"
claim — that pole of the argument is analysis, not a demonstrated result.

## Sources

```text
URL:         https://projectzero.google/2024/10/from-naptime-to-big-sleep.html
Kind:        primary — Google Project Zero + DeepMind reporting their own agent's
             finding. INTERESTED PARTY: the authors both built the tool and judge
             its significance.
Establishes: The first firsthand, specified AI-found real vulnerability.
Paraphrase:  The "Big Sleep" LLM agent (evolved from "Naptime") found a stack
             buffer underflow in SQLite, in the seriesBestIndex function of the
             series.c extension. The bug fires when a constraint is applied to the
             ROWID column: iColumn uses -1 as a sentinel for ROWID, and the
             function failed to handle that edge case, producing a negative array
             index write. Found in SQLite at HEAD (commit 2f7eab381e167609) in
             early October 2024, reported to SQLite developers, fixed the same day.
             The bug was caught before it reached any official release, so shipped
             SQLite users were never exposed.
Locators:    Sections "The bug" and "Impact / Conclusion."
Quote:       "we believe this is the first public example of an AI agent finding a
             previously unknown exploitable memory-safety issue in widely used
             real-world software." Also, self-limiting: "at present, it's likely
             that a target-specific fuzzer would be at least as effective (at
             finding vulnerabilities)."
```

```text
URL:         https://www.darpa.mil/news/2025/aixcc-results
Kind:        primary — DARPA reporting the results of the challenge it ran.
Establishes: AI systems finding AND patching real, previously-unknown flaws in
             real open-source code, at scale — but in a defensive frame.
Paraphrase:  In the AI Cyber Challenge (AIxCC) finals at DEF CON 33 (announced
             Aug 8, 2025), seven finalist systems analyzed ~54 million lines of
             code. Across the synthetic test set they discovered 54 of 63 injected
             vulnerabilities (86%) and patched 43. They also surfaced 18 real,
             non-synthetic (previously unknown) vulnerabilities — 6 in C, 12 in
             Java — and produced 11 patches for them. Every team found at least
             one real-world vulnerability. Average patch submission time was ~45
             minutes; average cost per task ~$152. Winners: Team Atlanta (Georgia
             Tech, Samsung Research, KAIST, POSTECH) $4M; Trail of Bits (system
             "Buttercup") $3M; Theori $1.5M. DARPA frames the outcome as a
             defender's tool.
Locators:    Results summary and prize/standings sections.
Quote:       AIxCC Program Manager Andrew Carney: the competition "has
             fundamentally changed our understanding of what is possible in terms
             of automatically finding, but more importantly, fixing
             vulnerabilities." (Names/titles taken from the DARPA page and the
             secondary below; if the headline attributes a quote, re-verify the
             exact title against this page.)
```

```text
URL:         https://arxiv.org/abs/1802.07228
Kind:        primary — the report that owns the early-form argument. (Full text
             read from the arXiv PDF; cite this abstract page as the source's home.)
Establishes: The steelman / originating version of the offensive-uplift argument,
             pre-LLM (Feb 2018).
Paraphrase:  "The Malicious Use of Artificial Intelligence: Forecasting,
             Prevention, and Mitigation," Brundage, Avin, Clark, Toner, Eckersley
             et al. — 26 authors across the Future of Humanity Institute (Oxford),
             the Centre for the Study of Existential Risk (Cambridge), OpenAI, EFF
             and others. The report's frame: progress in AI will (a) expand
             existing threats by widening the set of actors, the rate, and the set
             of targets; (b) introduce new threats; (c) alter the character of
             threats. Its named digital-security scenarios include "Automation of
             vulnerability discovery" (using historical patterns of code
             vulnerabilities to speed discovery of new ones and generate exploit
             code) and "More sophisticated automation of hacking." The core
             mechanism is the scale/efficacy trade-off: attackers trade off scale
             against effectiveness (spear phishing vs. generic phishing), and AI
             "can render such trade-offs less acute."
Locators:    "General Framework for AI & Security Threats" (pp.16-22 of the PDF);
             "Digital Security" scenarios (pp.24-25).
Quote:       "Autonomous software has been able to exploit vulnerabilities in
             systems for a long time, but more sophisticated AI hacking tools may
             exhibit much better performance both compared to what has historically
             been possible and, ultimately (though perhaps not for some time),
             compared to humans." Note the explicit "perhaps not for some time"
             hedge — the originators steelmanned it as a trajectory, not a
             then-present capability.
```

```text
URL:         https://www.ncsc.gov.uk/report/impact-of-ai-on-cyber-threat
Kind:        primary — UK National Cyber Security Centre assessment (national
             cyber agency). Published 24 Jan 2024 ("The near-term impact of AI on
             the cyber threat"; NCSC later issued a "now to 2027" update, not the
             page read here).
Establishes: The present-tense, official version of the argument — and, crucially,
             where a national agency draws the uplift line.
Paraphrase:  NCSC judges that AI "will almost certainly increase the volume and
             heighten the impact of cyber attacks" over the next two years, but the
             impact is "uneven" and driven by "evolution and enhancement of
             existing tactics, techniques and procedures," not new attack types.
             Reconnaissance and social engineering get the clearest boost (AI
             "almost certainly" makes them more effective and harder to detect;
             GenAI removes the grammar tells of phishing). Malware and exploit
             development get only a "realistic possibility of uplift," and advanced
             uses are "highly likely to be restricted to threat actors with access
             to quality training data, significant expertise (in both AI and
             cyber), and resources." Highly capable state actors are "almost
             certainly best placed amongst cyber threat actors to harness the
             potential of AI in advanced cyber operations." Novice actors get
             "significant uplift (from low base)" — but in social engineering and
             access operations, i.e. the low-skill end. NCSC also warns AI is
             likely to shorten the time between vulnerability discovery and
             exploitation.
Locators:    Key judgments; the actor-by-capability uplift matrix.
Quote:       "AI will almost certainly increase the volume and heighten the impact
             of cyber attacks over the next two years." / advanced offensive uses
             "highly likely to be restricted to threat actors with access to
             quality training data, significant expertise... and resources."
```

```text
URL:         https://arxiv.org/abs/2408.08926
Kind:        primary — academic benchmark (Cybench; Stanford et al.). Third-party
             evaluator, not a model vendor.
Establishes: Honest pass rates on professional CTF tasks; the capability ceiling.
Paraphrase:  Cybench is 40 professional-level CTF tasks drawn from 4 competitions,
             with per-task subtasks added because most tasks exceeded agent
             ability. Difficulty is anchored to human first-solve time. Unguided
             (no subtask hints), the best agents solved: Claude 3.5 Sonnet 17.5%
             (7/40), GPT-4o 12.5% (5/40), Claude 3 Opus 10% (4/40), o1-preview 10%
             (4/40). No unguided agent solved any task whose human first-solve time
             exceeded 11 minutes. The hardest task in the set took human teams
             24 hours 54 minutes.
Locators:    Abstract; Table 2 (unguided results); difficulty discussion.
Quote:       "the agent is unable to solve any task with a first solve time above
             11 minutes... without subtask guidance."
```

```text
URL:         https://arxiv.org/abs/2404.08144
Kind:        primary — Fang, Bindu, Gupta, Kang (UIUC), "LLM Agents can
             Autonomously Exploit One-day Vulnerabilities." Academic; the authors
             built the agent, so treat the headline figure as an
             advocate's-best-case.
Establishes: The strongest autonomous-exploit claim — and its load-bearing caveat.
Paraphrase:  On a dataset of 15 one-day (already-disclosed) vulnerabilities, a
             GPT-4 agent exploited 87% (13/15) when handed the CVE description;
             every other model and off-the-shelf scanner scored 0%. The decisive
             caveat is in the paper itself: without the CVE description GPT-4's
             success falls to 7% (1/15). So the result is exploitation of a bug
             already described to it, not discovery. Sample is small (n=15); the
             unsuccessful comparison models did not include Claude 3 or Gemini 1.5
             (authors lacked access).
Locators:    Abstract; results; the "requires the CVE description" caveat.
Quote:       "without the description, GPT-4 can exploit only 7% of the
             vulnerabilities."
```

```text
URL:         https://arxiv.org/abs/2403.13793
Kind:        primary — Phuong et al., "Evaluating Frontier Models for Dangerous
             Capabilities" (Google DeepMind). INTERESTED PARTY: a lab evaluating
             its own Gemini 1.0 models.
Establishes: A lab's own dangerous-capability cyber eval showing the ceiling, with
             an explicit "no strong dangerous capability yet" conclusion.
Paraphrase:  DeepMind evaluated Gemini 1.0 (Nano/Pro/Ultra) agents across four
             danger domains including cyber. On an in-house suite of 13 easy-to-
             medium CTF challenges (web-app vulns, off-the-shelf exploits,
             databases, Linux privilege escalation, password cracking), the agents
             solved: Nano 0/13, Pro 1.0 2/13, Ultra 1.0 3/13. On 13 Hack The Box
             CTFs (reverse engineering, binary exploitation, cryptography) no agent
             solved any (0/13). The authors "did not find evidence of strong
             dangerous capabilities" but flagged "early warning signs." They frame
             the concern as automating low/medium threat-actor activity against
             poorly protected assets, not hardened novel targets.
Locators:    Table 1 overview; Section 4 (Cybersecurity: attack automation);
             Table 7 (in-house CTF and Hack The Box results).
Quote:       Section 4: agents passing these evals "would be capable of
             autonomously attacking poorly protected networked assets" — the
             stated bar is poorly protected, not hardened.
```

```text
URL:         https://therecord.media/darpa-ai-code-competition-winner-def-con
Kind:        secondary — Recorded Future News reporting on the AIxCC finals from
             outside DARPA. Context and outside framing.
Establishes: Independent confirmation of the AIxCC standings and the defensive
             read; officials' framing.
Paraphrase:  Confirms Team Atlanta ($4M), Trail of Bits ($3M), Theori ($1.5M),
             43 of the discovered synthetic vulnerabilities patched, and quotes
             DARPA framing the tools as a defender's edge. Reports DARPA Director
             Stephen Winchell saying the technology gives defenders "a much-needed
             edge in identifying and patching vulnerabilities at speed and scale,"
             and an ARPA-H official's aspiration that hospital ransomware could
             "become a thing of the past."
Locators:    Body; official quotes.
Quote:       Winchell (per this report): defenders get "a much-needed edge in
             identifying and patching vulnerabilities at speed and scale."
```

```text
URL:         https://www.techrepublic.com/article/news-ai-xbow-tops-hackerone-us-leaderboad/
Kind:        secondary — TechRepublic (Aminu Abdullahi, 26 Jun 2025) reporting the
             XBOW/HackerOne result. Reports on an INTERESTED PARTY (XBOW, a vendor
             promoting its own tool) and adds the autonomy caveat.
Establishes: The present-tense "AI at the top of a bug-bounty leaderboard" data
             point — with its scope limits.
Paraphrase:  XBOW, an autonomous pentesting system, reached #1 on HackerOne's US
             leaderboard (Q2 2025), submitting 1,000+ vulnerability reports over a
             few months against web-application bug-bounty targets (asset type
             WEB_APP). Reported severity mix over a ~3-month window: 54 critical,
             242 high, 524 medium, 65 low; 132 resolved, 208 duplicates, 209
             informative. CAVEAT the article flags: findings were automated but
             "human staff conducted reviews before submission" to comply with
             HackerOne's AI-tool policy — so this is not fully unattended
             end-to-end intrusion, and the targets are public bug-bounty web apps,
             not hardened novel systems.
Locators:    Body; severity/status breakdown; autonomy caveat.
Quote:       findings were "fully automated," but "human staff conducted reviews
             before submission."
```

## Contradictions

**The novice-vs-expert uplift dispute (three-way, each sourced).**
- *Democratization / novice-uplift pole* — Brundage et al. 2018
  (https://arxiv.org/abs/1802.07228): AI "expand[s] the set of actors who are
  capable of carrying out the attack," widening access downward. This is the
  argument that AI lifts the floor and lets less-skilled actors do more.
- *Concentration / expert-uplift pole* — UK NCSC 2024
  (https://www.ncsc.gov.uk/report/impact-of-ai-on-cyber-threat): advanced
  offensive uplift (malware, exploits) is "highly likely to be restricted to
  threat actors with access to quality training data, significant expertise...
  and resources," and highly capable state actors are "almost certainly best
  placed." NCSC does grant novices "significant uplift (from low base)" — but
  only in social engineering and access operations, the low-skill vectors. So the
  two poles are not symmetric: novices get lifted where the task was never hard;
  the hard offensive work still favors the already-expert.
- *Capability-ceiling pole* — Cybench (https://arxiv.org/abs/2408.08926) and
  Phuong/DeepMind (https://arxiv.org/abs/2403.13793): models help most where a
  skilled human already could and stall on hard, multi-step tasks (nothing above
  an 11-minute human task unguided; 0/13 Hack The Box). This is evidence for the
  expert-uplift reading and against strong novice democratization at the hard end.
The brief asks that this dispute be reported, not resolved. It is genuinely open:
no source reconciles Brundage's "widen the set of actors" with NCSC's "restricted
to those with expertise and resources."

**The doom claims ("AI breaks defense / collapses cost of attack").**
- The strongest *sourced* version is NCSC's measured judgment
  (https://www.ncsc.gov.uk/report/impact-of-ai-on-cyber-threat): AI "will almost
  certainly increase the volume and heighten the impact of cyber attacks" and is
  likely to shorten the window between vulnerability disclosure and exploitation.
- HONEST GAP: I found no primary source for the maximalist claim that AI grants a
  *decisive* attacker advantage or "breaks all defense." The commission's own
  framing is the steelman; the demonstrated results do not reach it. Flag for the
  writer: the doom pole above NCSC's careful language is analysis/conjecture, not
  a demonstrated finding — do not source it to a primary that does not exist.

**The dismissal claims ("just a chatbot / it only exploits known bugs").**
- Fang et al. (https://arxiv.org/abs/2404.08144): strip the CVE write-up and the
  87% headline becomes 7% — the system exploits *disclosed* bugs, it does not find
  them.
- Cybench (https://arxiv.org/abs/2408.08926): best model 17.5%; hard tasks unsolved.
- Phuong/DeepMind (https://arxiv.org/abs/2403.13793): a frontier lab's own agents
  solve 3/13 easy CTFs and 0/13 harder ones.
- Even the pro-capability Big Sleep write-up
  (https://projectzero.google/2024/10/from-naptime-to-big-sleep.html) concedes a
  "target-specific fuzzer would be at least as effective."
- HONEST GAP the other way: dismissal overreaches too. Big Sleep and AIxCC's 18
  real-world flaws are genuine, novel, previously-unknown discoveries — "just a
  chatbot" cannot explain them. The evidence sits between the poles.

**Attacker advantage vs. defender advantage (claim 3 is symmetric).**
The two strongest offensive demonstrations are defensive programs: Project Zero's
Big Sleep fixes bugs before release ("no scope for attackers to compete"), and
AIxCC is explicitly a *find-and-patch* challenge whose officials frame it as a
defender's edge (https://therecord.media/darpa-ai-code-competition-winner-def-con).
The same capability that finds a bug for an attacker patches it for a defender.
No source in this record shows the offense/defense balance tipping decisively
toward attackers; that claim is contested by the very demonstrations offered for it.

**Interested-party flags (per the brief).**
- Big Sleep: Google/DeepMind evaluating their own agent's find.
- Phuong et al.: DeepMind evaluating its own Gemini models.
- XBOW leaderboard: a vendor's marketing claim; the TechRepublic secondary adds
  the human-review-before-submission caveat the vendor's own framing downplays.
- Cybench and Fang are academic third parties (Fang's authors built the agent, so
  its headline figure is still an advocate's best case, but they are not selling a
  product).

## Numbers

```text
Figure: Big Sleep — 1 previously-unknown exploitable vulnerability (stack buffer
        underflow, SQLite series.c / seriesBestIndex, ROWID iColumn = -1 sentinel)
Owner:  Project Zero / DeepMind writeup
Scope:  SQLite at HEAD (commit 2f7eab381e167609); found early Oct 2024, fixed same
        day, pre-release (zero users exposed). Claimed first public AI-found
        memory-safety bug in widely used real-world software.
```

```text
Figure: AIxCC finals — 54/63 synthetic vulns discovered (86%), 43 patched;
        18 real-world previously-unknown flaws found (6 C, 12 Java), 11 patched
Owner:  DARPA (darpa.mil/news/2025/aixcc-results)
Scope:  7 finalist systems, ~54M lines of code; announced DEF CON 33, Aug 8 2025.
        Avg patch time ~45 min; avg cost ~$152/task.
```

```text
Figure: Cybench unguided pass rates — Claude 3.5 Sonnet 17.5% (7/40); GPT-4o
        12.5% (5/40); Claude 3 Opus 10% (4/40); o1-preview 10% (4/40)
Owner:  Cybench (arXiv 2408.08926)
Scope:  40 professional CTF tasks; no unguided agent solved any task with human
        first-solve time > 11 min; hardest human task 24h54m.
```

```text
Figure: Fang et al. — GPT-4 exploits 87% (13/15) one-day vulns WITH CVE
        description; 7% (1/15) WITHOUT; all other models/scanners 0%
Owner:  Fang, Bindu, Gupta, Kang, UIUC (arXiv 2404.08144)
Scope:  15 disclosed one-day vulnerabilities; exploitation of described bugs, not
        discovery; comparison set excluded Claude 3 and Gemini 1.5.
```

```text
Figure: Gemini 1.0 CTF results — in-house easy/medium: Nano 0/13, Pro 2/13,
        Ultra 3/13; Hack The Box: 0/13 for all agents
Owner:  Phuong et al., Google DeepMind (arXiv 2403.13793)
Scope:  Evals run Jan 2024 on Gemini 1.0; "no strong dangerous capability," "early
        warning signs." Stated bar: "poorly protected networked assets."
```

```text
Figure: XBOW — #1 on HackerOne US leaderboard, 1,000+ reports (Q2 2025);
        severity mix 54 critical / 242 high / 524 medium / 65 low; 132 resolved
Owner:  TechRepublic (secondary) reporting XBOW/HackerOne
Scope:  Public web-app bug-bounty targets (WEB_APP); automated but human-reviewed
        before submission. Vendor claim; not hardened-target end-to-end intrusion.
```

```text
Figure: NCSC confidence tiering — "almost certainly" (top), "highly likely,"
        "likely," "realistic possibility" (lowest)
Owner:  UK NCSC (ncsc.gov.uk/report/impact-of-ai-on-cyber-threat)
Scope:  Judgments span ~2 years to 2025. Malware/exploit uplift rated only
        "realistic possibility"; volume/impact increase rated "almost certainly."
```

## Source assets

```text
Asset: Cybench "first-solve time" difficulty chart / Table 2 (per-model unguided
       solve counts against human solve-time buckets), arXiv 2408.08926.
Shows: Exactly where the capability ceiling sits — solves cluster under the
       11-minute human-difficulty line and vanish above it. One image carries the
       whole "caps out below expert tasks" argument.
Crop:  Retain the model rows and the human-solve-time axis with the 11-minute
       cutoff; omit decorative legend padding. Label the axis as human first-solve
       time so the reader is not misled into reading it as model runtime.
```

```text
Asset: Phuong et al. Table 7 (in-house CTF and Hack The Box results: Nano/Pro/
       Ultra columns, 0/13–3/13 and 0/13), arXiv 2403.13793.
Shows: A frontier lab's own agents scoring 3/13 and 0/13 — the most credible
       "not shown at the hard end" evidence because the vendor produced it.
Crop:  Keep the totals row and the Hack The Box 0/13 line; retain model-name
       column headers.
```

```text
Asset: DARPA AIxCC results figure — 54M lines of code / 54 discovered / 43 patched
       / 18 real-world flaws, darpa.mil/news/2025/aixcc-results.
Shows: The find-AND-patch scale in one frame, which is also the claim-3 rebuttal
       (defenders got the uplift). Better than prose for the "at scale" point.
Crop:  Keep the discovered-vs-patched split and the real-world count; do not crop
       away the "patched" side, which is the defensive half of the story.
```

```text
Asset: Project Zero Big Sleep — none of a decorative kind; the load-bearing detail
       is the bug description (ROWID sentinel / negative index), which is prose,
       not an image.
Shows: n/a
Crop:  None found (no chart or diagram earns a place; the specifics belong in text).
```

## Discarded

```text
URL: https://www.theregister.com/software/2024/04/17/gpt-4-can-exploit-real-vulnerabilities-by-reading-advisories/ — 404 at this path; The Register's Fang coverage exists under a different slug (…/1064884). Not needed: the CVE-dependency critique is in the Fang primary itself, and a secondary is already supplied by The Record and TechRepublic.
URL: https://siliconangle.com/2024/11/05/googles-big-sleep-ai-model-sets-world-first-discovery-sqlite-security-flaw/ — secondary rehash of the Project Zero post; adds nothing the primary does not own.
URL: https://thehackernews.com/2024/11/googles-ai-tool-big-sleep-finds-zero.html — secondary; same origin as the Project Zero writeup, counts as one retelling.
URL: https://www.emergentmind.com/topics/cybench and https://llm-stats.com/benchmarks/cybench — aggregator summaries of Cybench, not the owning paper; pass rates verified against arXiv 2408.08926 instead.
URL: https://xbow.com/blog/top-1-how-xbow-did-it — XBOW's own vendor post; returned HTTP 429 on fetch and is the interested party. TechRepublic used instead because it carries the human-review caveat the vendor omits.
URL: https://www.governance.ai/research-paper/the-malicious-use-of-artificial-intelligence-forecasting-prevention-and-mitigation — host copy of the Brundage report; arXiv is the canonical home and was read in full there.
```
