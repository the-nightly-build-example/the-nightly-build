# Evidence: what-could-go-wrong/lethal-trifecta (01)

The evidence strongly supports the commissioned angle. The "lethal trifecta" is a
named framing with a traceable author (Simon Willison, June 2025) and a precise
definition: a system that holds three properties at once, access to private data,
exposure to untrusted content, and a way to communicate externally, can be made to
steal its own user's data through prompt injection. The argument's core claim, that
this is a real failure of working production systems and not a thought experiment,
is well supported: four separate 2025 disclosures against shipped products
(Microsoft 365 Copilot, GitLab Duo, GitHub's MCP server, and ChatGPT connectors)
each demonstrated private-data exfiltration through injected instructions, and three
of the four were fixed or acknowledged by the vendor. The sharp line the series asks
for is clean and consistent across sources: every case is a researcher
proof-of-concept, and no source reports any of them exploited against a real victim
in the wild. Microsoft's own CVE record marks exploit code as "unproven." The
evidence is thin in exactly two places, and both should be stated plainly rather
than papered over: there is no measured figure for how common the vulnerable
three-leg configuration is in deployed systems (the claim rests on the fact that
vendors shipped it on by default in the four named products), and the jump from
"demonstrated exfiltration" to "autonomous agent catastrophe" has no demonstrated
basis at all, which is the speculative end the series should name. The mitigation
debate is genuinely contested and both sides have primary statements: detection
classifiers (Microsoft's XPIA, OpenAI's url_safe) were each measurably defeated in
the disclosures, Willison argues detection can never be the wall, and a Google/ETH
paper (CaMeL) argues a by-design architecture can give provable security at a
measured usability cost.

One access limitation: Aim Labs' own EchoLeak report page and Aim's BusinessWire
press release are both behind a Cloudflare block (HTTP 403 to both WebFetch and
curl), and this environment cannot render PDFs (no poppler). The EchoLeak facts
below therefore come from Microsoft's official CVE record (the primary that owns the
classification and fix) and from Willison's June 11 post, which read and quotes the
Aim report. Aim's own wording for "LLM Scope Violation" could not be read firsthand
and is flagged where used.

## Sources

```text
URL:         https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
Kind:        primary. Willison authored this framing; the post is the origin of the term.
Establishes: The definition of the "lethal trifecta" and the argument that detection defenses cannot be trusted.
Paraphrase:  Willison names three properties whose combination is dangerous: "Access to your private data",
             "Exposure to untrusted content", and "The ability to externally communicate" in a way that could
             be used to steal data. His reasoning: LLMs follow instructions found in content, and will follow
             any instruction that reaches the model, so a system holding all three can be made by an attacker's
             injected text to read private data and send it out. He is "deeply suspicious" of guardrail products
             that claim to catch "95% of attacks," because in security that is a failing grade. He concludes the
             only reliable defense for an end user is to avoid combining the three legs at all.
Locators:    Post body; the three-item list; the "guardrails" paragraph.
Quote:       "Plenty of vendors will sell you 'guardrail' products that claim to be able to detect and prevent
             these attacks. I am deeply suspicious of these... they'll almost always carry confident claims
             that they capture '95% of attacks' or similar... but in web application security 95% is very much
             a failing grade." And: "The only way to stay safe there is to avoid that lethal trifecta
             combination entirely."
```

```text
URL:         https://simonwillison.net/2025/Jun/11/echoleak/
Kind:        secondary (for EchoLeak facts). Willison reports on Aim Labs' disclosure; he did not find the bug.
             Primary only for his own framing judgment.
Establishes: That Willison classifies EchoLeak as an instance of the lethal trifecta, and links Aim's report.
Paraphrase:  He describes EchoLeak as a prompt-injection exfiltration attack where malicious instructions reach
             the LLM, cause it to pull private data, and steal it via a Markdown/image URL. He ties it directly
             to the framing.
Locators:    Opening and the trifecta sentence.
Quote:       "The lethal trifecta strikes again! Any time a system combines access to private data with exposure
             to malicious tokens and an exfiltration vector you're going to see the same exact security issue."
Note:        The Aim Labs report it links, https://www.aim.security/lp/aim-labs-echoleak-blogpost, is
             Cloudflare-blocked (403) and could not be opened directly.
```

```text
URL:         https://cveawg.mitre.org/api/cve/CVE-2025-32711
Kind:        primary. The official CVE Program record; Microsoft is the assigning CNA and owns the classification.
Establishes: The official identity, severity, and fix status of the Microsoft 365 Copilot "EchoLeak" flaw.
Paraphrase:  CVE-2025-32711 is described as "Ai command injection in M365 Copilot allows an unauthorized attacker
             to disclose information over a network." Rated CVSS 9.3, Critical. Weakness classed as CWE-74
             (improper neutralization / injection). Affected product: Microsoft 365 Copilot. The CVSS vector
             records scope-changed, high confidentiality impact, low integrity impact, no availability impact,
             and crucially Exploit-code "Unproven" (E:U) with an Official fix available (RL:O) and a Confirmed
             report (RC:C). Published 2025-06-11; last updated 2026-02-26. Reference points to the MSRC advisory.
Locators:    containers.cna.descriptions; metrics.cvssV3_1 (vector string); problemTypes (CWE-74); datePublished.
Quote:       Description verbatim: "Ai command injection in M365 Copilot allows an unauthorized attacker to
             disclose information over a network." Vector: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N/E:U/RL:O/RC:C
Note:        The MSRC human-facing page (msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711) is a
             JavaScript app that renders empty to a fetcher; this MITRE API record is the resolvable primary.
             E:U ("Exploit code unproven") is Microsoft's own signal that no working in-the-wild exploit was known.
```

```text
URL:         https://invariantlabs.ai/blog/mcp-github-vulnerability
Kind:        primary. Invariant Labs authored the proof-of-concept and the disclosure.
Establishes: The GitHub-MCP exfiltration demonstration, and the claim that this is an agent-design problem GitHub
             cannot fix server-side.
Paraphrase:  Researchers Marco Milanta and Luca Beurer-Kellner showed that a malicious GitHub Issue filed on a
             public repository carries injected instructions. When the repository owner asks their agent (via the
             GitHub MCP server) to "have a look at the open issues," the agent reads the malicious issue, follows
             the hidden instructions, reaches into the owner's private repositories, and leaks their contents,
             including private project details and purported salary information, by opening a pull request on the
             public repo. It is user-initiated (the owner triggers the agent) rather than zero-click, though the
             post notes many users run in "Always Allow" mode. A researcher PoC; no in-the-wild exploitation
             claimed. Published May 26, 2025.
Locators:    Attack walkthrough; the "architectural" paragraph near the end.
Quote:       "This is not a flaw in the GitHub MCP server code itself, but rather a fundamental architectural
             issue that must be addressed at the agent system level." And: "GitHub alone cannot resolve this
             vulnerability through server-side patches."
Note:        The tools used are fully trusted and uncompromised; the injection enters purely through untrusted
             data (the issue text). This is the clean illustration that the failure is the trifecta configuration,
             not a software bug.
```

```text
URL:         https://github.com/github/github-mcp-server/issues/844
Kind:        primary. GitHub's own issue tracker; records the project's handling of the Invariant report.
Establishes: GitHub's public handling of the disclosure, and that human-in-the-loop confirmation is weak in practice.
Paraphrase:  Issue titled "Exfiltrate information from private repositories," opened by user sei-renae on
             August 8, 2025, referencing Invariant's May 26 disclosure and asking whether GitHub responded,
             whether there is a fix, and whether there is a CVE. The reproduction confirms an agent told to check
             issues in a public repo surfaced content from private repos despite token-scope expectations. The
             issue is marked Closed with "bug" and "stale" labels. No GitHub maintainer fix, CVE, or mitigation
             statement is visible in the page; the filer notes that human-in-the-loop confirmation is undercut
             because users click "Continue" without reading the warning.
Locators:    Issue body; labels/status line.
Note:        This supports the contradiction with Invariant: Invariant says server-side patching cannot solve it;
             GitHub's tracker shows the issue closed as stale with no server fix or CVE, consistent with treating
             it as out-of-scope for a code patch rather than a vulnerability GitHub owns.
```

```text
URL:         https://labs.zenity.io/p/agentflayer-chatgpt-connectors-0click-attack-5b41
Kind:        primary. Zenity Labs authored the "AgentFlayer" proof-of-concept and disclosure.
Establishes: The ChatGPT-connectors / Google Drive zero-click exfiltration demonstration and the defeat of
             OpenAI's url_safe mitigation.
Paraphrase:  Researcher Tamir Ishay Sharbat (Zenity Labs) showed that a document containing an invisible injected
             prompt, shared into a target's connected Google Drive, causes ChatGPT to search connected storage for
             secrets (such as API keys) and exfiltrate them. The exfiltration channel is automatic image
             rendering: ChatGPT renders a Markdown image whose URL carries the stolen data as parameters, and the
             request fires with no click. Presented at Black Hat 2025 (with Michael Bargury). A researcher PoC;
             no in-the-wild exploitation claimed. Published August 6, 2025.
Locators:    Attack description; exfiltration-channel section; the url_safe bypass section.
Quote:       "When ChatGPT renders an image, a request is sent to the server immediately. No clicking required."
Note:        OpenAI had deployed a client-side mitigation, a "url_safe" endpoint meant to verify URLs before
             rendering; the researchers bypassed it using Azure Blob storage URLs, which the check treated as
             safe. This is a measured defeat of a deployed detection/allowlist defense.
```

```text
URL:         https://www.legitsecurity.com/blog/remote-prompt-injection-in-gitlab-duo
Kind:        primary. Legit Security authored the disclosure; researcher Omer Mayraz.
Establishes: A comparable 2025 case: remote prompt injection in GitLab Duo leading to private source-code theft.
Paraphrase:  Hidden instructions placed in merge-request descriptions, commit messages, issue comments, or source
             files (concealed with encodings such as Base16, KaTeX, Unicode smuggling) cause GitLab Duo Chat to
             leak private source code and inject attacker-controlled HTML into its streamed responses. The
             exfiltration channel is again HTML/Markdown image rendering: Duo is instructed to Base64-encode
             sensitive data into an <img> URL, and the browser fires the request on render. User-initiated (the
             victim asks Duo about poisoned content), not zero-click. A researcher PoC; no in-the-wild
             exploitation claimed. Disclosed February 12, 2025.
Locators:    Attack chain; "exfiltration" section; disclosure/fix section.
Quote:       GitLab's fix (patch duo-ui!52) "prevents Duo from rendering unsafe HTML tags such as <img> or <form>
             that point to external domains not under gitlab.com."
Note:        GitLab confirmed and patched, in contrast with GitHub's stale-close. The fix narrows the
             exfiltration leg (blocks external image domains) rather than solving prompt injection, which matches
             Willison's "remove a leg" argument.
```

```text
URL:         https://arxiv.org/abs/2503.18813
Kind:        primary. "Defeating Prompt Injections by Design" (CaMeL); the authors own the method and its results.
Establishes: The by-design mitigation position: that a protective layer can give provable security against
             prompt-injection exfiltration, at a measured usability cost.
Paraphrase:  Authors Edoardo Debenedetti, Ilia Shumailov, Tianqi Fan, Jamie Hayes, Nicholas Carlini, Daniel
             Fabian, Christoph Kern, Chongyang Shi, Andreas Terzis, and Florian Tramer (Google / Google DeepMind /
             ETH Zurich). CaMeL (CApabilities for MachinE Learning) wraps the LLM in a layer that extracts control
             and data flow from the trusted user query, so untrusted data the model later ingests can never change
             the program's control flow or trigger a disallowed action; a capability/policy system gates tool use
             and data egress. On the AgentDojo agentic-security benchmark the paper reports solving 77% of tasks
             with provable security, against 84% solved by an undefended system. Submitted March 24, 2025;
             revised June 24, 2025 (v2).
Locators:    Abstract; AgentDojo results.
Quote:       Reported result: CaMeL "solved 77% of tasks with provable security... compared to 84% with an
             undefended system" on AgentDojo.
Note:        This is the strongest published counter to "prompt injection cannot be mitigated." It does not make
             the model itself robust; it constrains what injected instructions can cause, effectively removing the
             external-action leg under policy. The ~7-point task gap (77 vs 84) is the usability cost, and the
             approach presumes the trusted query, not the untrusted content, defines the intended actions.
```

## Contradictions

- Invariant Labs vs GitHub on responsibility. Invariant states plainly that the
  GitHub-MCP exfiltration "is not a flaw in the GitHub MCP server code itself" and
  cannot be fixed server-side. GitHub's own issue #844 is closed as "stale" with no
  server fix, no CVE, and no mitigation statement. The two are consistent on the
  facts but opposed on whose problem it is to solve, which is the heart of the
  framing: the vendor cannot patch the trifecta out of an agent that is supposed to
  read untrusted content and act with private access.

- Detection/classification vendors vs the "remove a leg" camp, with measured defeats
  on the record. Microsoft runs XPIA prompt-injection classifiers and OpenAI
  deployed a url_safe URL check; both are detection/allowlist mitigations. EchoLeak
  bypassed the classifier path (per Willison's reading of Aim and Microsoft's own
  critical rating and fix), and AgentFlayer bypassed url_safe using Azure Blob URLs
  the check deemed safe (Zenity, firsthand). Willison argues detection at "95%" is a
  failing grade. The CaMeL authors argue the answer is architectural constraint, not
  detection, and report provable security on 77% of AgentDojo tasks. This is a live
  disagreement, not a settled one: detection vendors ship and claim mitigation, the
  disclosures show specific detection defenses defeated, and the by-design camp
  claims a different route works at a usability cost.

- Demonstrated exfiltration vs "autonomous agent catastrophe." Every primary here
  demonstrates data leaving a real system via injection. None demonstrates, or even
  claims, the larger speculative harm sometimes attached to the framing (an agent
  autonomously causing cascading real-world damage). Microsoft's CVE marks exploit
  code "unproven." No source reports a real victim. The contradiction is between the
  confidence of the risk language and the absence of any in-the-wild case. This cuts
  toward the commission, not against it: the series asks exactly for this line.

## Numbers

```text
Figure: CVSS 9.3 (Critical) for CVE-2025-32711 (EchoLeak)
Owner:  MITRE/Microsoft CVE record (cveawg.mitre.org)
Scope:  CVSS v3.1 base, vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:N; temporal E:U/RL:O/RC:C.
        E:U = exploit code unproven; RL:O = official fix. One vulnerability, Microsoft 365 Copilot.
```

```text
Figure: 77% of tasks solved with provable security vs 84% undefended
Owner:  CaMeL paper (arxiv.org/abs/2503.18813), v2 June 24 2025
Scope:  AgentDojo agentic-security benchmark; the gap (7 points) is the usability cost of the defense.
```

```text
Figure: "95%" detection claim, called a failing grade
Owner:  Willison (simonwillison.net lethal-trifecta post). This is his characterization of vendor marketing
        claims, not a measured benchmark. Record it as his argument, not as a lab result.
```

```text
Disclosure dates (each owned by the cited primary):
  GitLab Duo ....... disclosed Feb 12, 2025 (Legit Security); patched duo-ui!52
  GitHub MCP ....... published May 26, 2025 (Invariant Labs); no GitHub server fix / CVE
  EchoLeak ......... CVE published Jun 11, 2025 (MITRE/Microsoft); fixed by Microsoft, no customer action
  AgentFlayer ...... published Aug 6, 2025 (Zenity Labs); presented Black Hat 2025; OpenAI url_safe bypassed
```

## Source assets

Note on method: the primary pages were read through a text extractor and (for the
arxiv paper) an abstract fetch, not as rendered images, so the specific figures
below are named from the text and layout, not visually confirmed. The writer or
editor should open the page to confirm a figure before relying on it in a caption.

```text
Asset: Willison's three-legged "lethal trifecta" illustration at the top of the Jun 16 post.
Shows: The three conditions as one combined risk, which is the whole argument in one image.
Crop:  Must retain all three labels; omit nothing, since the point is the conjunction.
```

```text
Asset: Invariant Labs attack-flow diagram of the GitHub-MCP "toxic flow" (public issue -> agent -> private repo -> public PR).
Shows: That injection enters through ordinary untrusted data and crosses a trust boundary the tools themselves respect.
Crop:  Keep the public/private boundary and the direction of data flow; a crop that loses the boundary loses the point.
```

```text
Asset: Zenity AgentFlayer and Legit Security GitLab Duo screenshots of the rendered-image exfiltration request.
Shows: The exfiltration leg concretely: data riding out in an image URL with no click.
Crop:  A responsible crop must omit the live payload/endpoint. Show the mechanism, not a copyable instruction string.
```

For the remaining primaries (MITRE CVE record, GitHub issue, CaMeL): None found that
carries the argument better than prose.

## Discarded

```text
URL: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711
     JavaScript app, renders empty to a fetcher. Replaced by the resolvable MITRE API record, which owns the same data.
URL: https://nvd.nist.gov/vuln/detail/CVE-2025-32711
     Same problem (SPA renders empty). MITRE record used instead.
URL: https://www.aim.security/lp/aim-labs-echoleak-blogpost
     Aim Labs' own EchoLeak report. Cloudflare 403 to both WebFetch and curl; could not be opened. The primary
     EchoLeak facts are carried by Microsoft's CVE record; Willison's Jun 11 post quotes Aim.
URL: https://www.businesswire.com/news/home/20250611349150/en
     Aim Security's own press release. Also Cloudflare 403; could not be opened.
URL: https://arxiv.org/pdf/2509.10540
     Independent academic retrospective on EchoLeak. PDF downloaded but this environment cannot render PDFs
     (no poppler), so its text could not be read; not cited rather than cited unread.
URL: Numerous secondary news writeups (thehackernews, techradar, catonetworks, varonis, siliconangle, etc.)
     Consistent with the primaries but add no claim the primaries do not own; not cited to avoid padding.
```
