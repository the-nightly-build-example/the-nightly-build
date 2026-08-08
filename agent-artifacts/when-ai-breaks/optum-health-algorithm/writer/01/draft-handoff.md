# Draft handoff: when-ai-breaks/optum-health-algorithm (01)

## Original work
The piece recasts the study's separately reported results into one "hold the
risk score fixed" walkthrough that keeps three figures the record warns are
easy to conflate in visibly distinct frames, the observed health gap (4.8 vs
3.8 at the 97th percentile), the simulated enrollment share (17.7 to 46.5%
against the observed 19.2%), and the manufacturer's 3.7M-patient replication
(48,772 excess conditions), then turns the label-choice swing (14.1 to 26.7%)
into a transferable rule about proxy labels that no single passage of the paper
states that way.

## Proof
`./nb check ... --series when-ai-breaks --library /home/user/library-checkout`
(links included), after `./nb stamp`: **BLOCK: 0, WARN: 0, PUBLISHABLE.**
Stamped words=1734 (band 1200-2200), reading_minutes=8, sources=8 (5 primary,
3 secondary; policy min 8 / primary >=4 / secondary >=1 met).

No warnings left standing.

## Decisions worth flagging to the editor
- **Figure vs. furniture.** I did not capture the paper's risk-score figure as a
  source asset. The brief steered away from the recent figure+note closing habit
  and toward a stat strip or small table. The mechanism is instead carried by a
  stat strip (observed vs. simulated shares, each labeled) and a table (cost is
  near-equal across race at equal score while illness is not). If the editor
  wants the Fig. 3B cost-vs-conditions picture, it is available in the record and
  can be captured with `./nb asset`.
- **Vendor naming.** The article states plainly that the study named no vendor
  and attributes "Optum / Impact Pro" to later reporting (s4) and the NY DFS/DoH
  letter (s5), never to the paper. No-villain register held: the vendor's defense
  is quoted as restating the paper's mechanism, and the manufacturer's own
  replication and 84% reduction are reported as engagement, not indictment.
- **Frames kept honest.** 17.7 to 46.5% is marked a simulation in prose and in
  the stat-strip label; 48,772 is attributed to the manufacturer's 3.7M-patient
  replication, not the study sample; the study-sample figures (49,618 patients,
  4.8 vs 3.8, $1,801 wedge, race excluded) stay in their own frame.
- **Links, not retellings.** apple-card, nh-predict, and amazon-hiring-tool are
  linked in plain prose in the closing section; nh-predict and amazon-hiring-tool
  also seed the Background band.

## Open questions
None blocking. The claim set is the evidence record as delivered; I did not
expand it.
