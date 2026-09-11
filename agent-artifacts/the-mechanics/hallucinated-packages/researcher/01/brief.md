# researcher brief: the-mechanics/hallucinated-packages (01)

Inputs:
- editorial-direction.md (citation standard, The Mechanics territory, declared reader)

Output: researcher/01/evidence.md

Source floor (from nb source-policy --series the-mechanics): at least 8 sources,
at least 4 primary and at least 1 secondary. Exceed it where a source changes the
interpretation.

Research questions to answer from primary documents:

1. The rates. From the academic package-hallucination study/studies (e.g.,
   Spracklen et al., "We Have a Package for You! A Comprehensive Analysis of
   Package Hallucinations by Code Generating LLMs," 2024/USENIX Security 2025, and
   any companion work): how often assistants invent packages, across which models
   and which ecosystems (Python/PyPI, JavaScript/npm), and the denominators.
   Read the method, not the abstract.
2. The repeatability finding. The central mechanistic claim: what fraction of
   hallucinated package names recur across repeated generations, and the authors'
   explanation. Get the exact numbers and how they were measured. This is the
   lesson's distinct core; source it precisely.
3. Slopsquatting. Who coined/popularized the term and the threat model (an
   attacker pre-registers a predictable hallucinated name). Primary: the
   security-firm writeups (e.g., Socket, Lasso Security, Trend Micro) and the
   named researcher. Any documented real case of a hallucinated name being
   registered, or a controlled proof-of-concept, with the primary.
4. What reduces it. Evidence on grounding/retrieval or registry-checking reducing
   invented imports, and any measured mitigation. Mark what is settled versus
   open (e.g., whether rates can be driven to zero).

Hunt for contradictions: disputes over the rates, claims that repeatability is
overstated, or that no real-world slopsquatting attack has yet caused harm (the
honest state of the threat matters). Record them in full.

The reader already has the hallucination, tool-use, and retrieval lessons
(the-mechanics/hallucination, the-mechanics/tool-use, the-mechanics/retrieval);
note where a Background link replaces re-teaching. Do not browse the archive for
background beyond confirming those slugs exist. Record no live malicious package
names as something to install; names are evidence of the pattern, not a how-to.
