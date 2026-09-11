# researcher brief: what-could-go-wrong/lethal-trifecta (01)

Inputs:
- editorial-direction.md (citation standard, the What Could Go Wrong territory, declared reader)

Output: researcher/01/evidence.md

Source floor (from nb source-policy --series what-could-go-wrong): at least 8
sources, at least 4 primary and at least 1 secondary. Exceed it where a source
changes the interpretation.

Research questions to answer from primary documents:

1. The framing. Simon Willison's "lethal trifecta" posts (2025): the exact three
   conditions and his reasoning. Cite his post as the origin of the framing.
   Record his definition precisely.
2. The demonstrated exploits. For each, read the technical disclosure, not
   coverage: the Microsoft 365 Copilot "EchoLeak" vulnerability (Aim Security
   disclosure and the assigned CVE — get the CVE id and what Microsoft said and
   when it was fixed); the ChatGPT connectors / Google Drive exfiltration
   demonstration; the GitHub MCP exfiltration demonstration (Invariant Labs); and
   one or two comparable 2025 cases. For each record: what data could leave, the
   injection vector, whether it was zero-click, whether it was a researcher PoC or
   exploited in the wild, and the vendor response. This is the "what real systems
   actually do" core; be exact.
3. The mitigation debate. The argument that prompt injection cannot be reliably
   patched and the defense is to remove one leg of the trifecta; versus vendor
   claims that detection/classification mitigates it. Get primary statements on
   both sides and any measured defeat of a proposed defense.
4. The honest gap. Whether any lethal-trifecta attack has caused real-world harm
   yet versus being demonstrated, and how common the vulnerable configuration is.

Hunt for contradictions: vendors disputing severity, researchers disagreeing on
whether a class of defense works, and the distinction between demonstrated
exfiltration and speculative "autonomous agent catastrophe." Record in full.

The reader already has the-mechanics/instructions-are-data (the mechanism) and
what-could-go-wrong/jailbreaks; note where a Background link replaces
re-teaching. Do not browse the archive beyond confirming those slugs. Record the
threat model and mitigations only; do not record working injection payloads or a
reproducible exploit recipe.
