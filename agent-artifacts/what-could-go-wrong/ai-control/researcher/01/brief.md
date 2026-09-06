# researcher brief: what-could-go-wrong/ai-control (01)

Inputs:
- .nb-work/what-could-go-wrong/ai-control/agent-artifacts/what-could-go-wrong/ai-control/editorial-direction.md
- .nb-work/what-could-go-wrong/ai-control/agent-artifacts/what-could-go-wrong/ai-control/commission.md

Output:
- .nb-work/what-could-go-wrong/ai-control/agent-artifacts/what-could-go-wrong/ai-control/researcher/01/evidence.md

Read firsthand and record with locators:
- Greenblatt, Shlegeris, et al. 2023, "AI Control: Improving Safety Despite
  Intentional Subversion" (arXiv 2312.06942): the threat model (untrusted
  powerful model, trusted weaker model, limited human auditing), the definition
  of a control evaluation (blue team protocol vs red team subversion), the APPS
  backdooring task, the protocols compared (trusted monitoring, untrusted
  monitoring, trusted editing, defer-to-trusted), and the exact safety and
  usefulness numbers for each, with the audit budget (e.g. the % of cases
  audited) and denominators.
- At least two follow-up primaries (2024-2025): e.g. Bhatt et al. "Ctrl-Z:
  Controlling AI Agents via Resampling" or other subversion-strategy work; a
  "control tax" / cost study; and/or a safety-case paper that uses control
  evaluations. Record their settings and headline results.
- The proponents' own stated limits: where control is expected to fail
  (sufficiently superhuman untrusted models, un-auditable tasks, collusion
  between untrusted instances). Quote the limitation as stated.
- A skeptical or contrasting primary if one exists (critique of control as a
  safety case). Record what it argues.

For every safety/usefulness figure, record the red-team setup and the human/
trusted-monitor budget that produced it. A control number without its adversary
setup is meaningless. Confirm every URL resolves to the source's own page.
Classify each primary/secondary. Meet the 8-source, 4-primary / 1-secondary floor
with sources that change the interpretation, not padding.
