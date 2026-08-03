# Evidence: when-ai-breaks/amazon-hiring-tool (02)

The evidence strongly supports the commissioned angle: a resume-scoring model trained
on Amazon's own decade of hiring decisions learned to penalize signals of being a
woman (the token "women's," two all-women's colleges), Amazon's engineers could not
guarantee the model would not find new proxies, and the effort was disbanded. The
fairness literature owns the mechanism precisely: Barocas & Selbst (2016) name
"redundant encodings" and "garbage in, garbage out," and Dwork et al. (2012) name the
same failure as a "successful attack against 'fairness through blindness.'" The
weakness is demonstrably live today: NYC Local Law 144 and the EEOC's 2023 Title VII
guidance exist because automated screening is now routine, and a 2024 University of
Washington study found the same proxy bias in current LLM resume screeners.

The record's central limitation is single-origin sourcing. Every factual specific of
the Amazon incident (the 500 models, the 1–5 stars, the "women's" penalty, the
disbandment) traces to one 2018 Reuters investigation by Jeffrey Dastin, attributed to
five anonymous people. No independent party in a position to know has corroborated
those specifics; every later account is a retelling of that one origin. The harm is
bounded: the tool was experimental, its ratings were never the sole basis for hiring,
and Amazon says recruiters never used it to evaluate candidates at all. Nothing in the
record supports a claim that the tool rejected real applicants at scale. There is a
genuine contradiction between what Reuters' sources describe (recruiters "looked at the
recommendations") and what Amazon later asserted (it was "never used ... to evaluate
candidates"); both are recorded below.

Round 02 note (the only change from researcher/01): source [6], the EEOC "Select
Issues" technical assistance, is unchanged in substance but its recorded address is now
a link-resolvable Internet Archive (Wayback Machine) capture of the EEOC's own page,
because eeoc.gov bot-gates the canonical URL with a hard 404 and the deterministic link
check blocks on 404/410. The document's content was re-verified firsthand this round
from a verbatim reproduction of the EEOC page (the four-fifths / adverse-impact Q&A is
identical to what was read in round 01). Everything else below is copied forward
unchanged.

## Sources

```text
URL:         https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G
Kind:        primary — the origin investigative report; it owns every factual claim about the Amazon tool. It is primary as the record of the reporting, not as a neutral verifier: its own basis is anonymous sourcing (see Contradictions/limitation).
Establishes: The entire Amazon incident, firsthand as reporting. Built starting 2014; 500 models scoring 1–5 stars; trained on 10 years of resumes mostly from men; learned to prefer men; penalized "women's" and downgraded two all-women's colleges; edits gave "no guarantee"; recruiters looked at but never relied solely on the rankings; team disbanded by the start of 2017; Amazon declined to comment on specifics.
Paraphrase:  Amazon machine-learning specialists found their new recruiting engine "did not like women." A team built programs from 2014 to score resumes 1–5 stars. The group created 500 models tied to job functions and locations, each taught to recognize some 50,000 terms. Trained on ten years of resumes, most from men, the system "taught itself that male candidates were preferable," penalized resumes containing "women's," and downgraded graduates of two all-women's colleges. Amazon edited the programs to neutralize those terms, but that was no guarantee the machines would not find other discriminatory sorts. Recruiters looked at the tool's recommendations but never relied solely on them. Amazon disbanded the team by the start of 2017 after executives lost hope.
Locators:    Reuters, Oct. 10, 2018, "Amazon scraps secret AI recruiting tool that showed bias against women," by Jeffrey Dastin. Text verified via outlets that carried the wire verbatim (RTÉ and The Irish Times, below); the Reuters page itself returns HTTP 401 to automated fetch (gated, not dead).
Quote:       "five people familiar with the effort" (sourcing). "the company's computer models were trained to vet applicants by observing patterns in [CVs] submitted to the company over a 10-year period. Most came from men." "In effect, Amazon's system taught itself that male candidates were preferable." "penalised [CVs] that included the word 'women's,' as in 'women's chess club captain'" and "downgraded graduates of two all-women's colleges." "Amazon edited the programs to make them neutral to these particular terms. But that was no guarantee that the machines would not devise other ways of sorting candidates that could prove discriminatory." "Amazon's recruiters looked at the recommendations generated by the tool when searching for new hires, but never relied solely on those rankings." "The Seattle company ultimately disbanded the team by the start of last year because executives lost hope for the project." "Amazon declined to comment on the recruiting engine or its challenges, but the company says it is committed to workplace diversity and equality."
```

```text
URL:         https://www.rte.ie/news/business/2018/1010/1002144-amazon-ai-bias/
Kind:        secondary — RTÉ's carriage of the Reuters wire. Same origin as Reuters, not independent confirmation. Used only to read the origin text verbatim where the Reuters page is gated.
Establishes: The exact wording of the Reuters report (quotes above), nothing independently.
Paraphrase:  Reproduces the Reuters story in full, including the 500 models, 50,000 terms, 1–5 stars, the "women's" penalty, the "no guarantee" line, and the disbandment.
Locators:    RTÉ Business, Oct. 10, 2018. Byline: Reuters wire.
Quote:       (see Reuters entry; all quotes confirmed here word for word)
```

```text
URL:         https://www.irishtimes.com/business/technology/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-1.3658651
Kind:        secondary — Irish Times carriage of the same Reuters wire. Same origin; used to confirm the "never relied solely" and disbandment wording and the anonymous sourcing.
Establishes: Confirms "recruiters looked at the recommendations ... but never relied solely on those rankings," "disbanded the team by the start of last year," and "five people familiar with the effort" speaking anonymously. Confirms the primary text does NOT state a team size or an office location (only Seattle as headquarters).
Paraphrase:  Same as Reuters. Notably contains no headcount for the team and no Edinburgh/engineering-hub detail; those appear only in later secondary retellings, not in the origin text I verified.
Locators:    Irish Times, Oct. 10, 2018.
Quote:       "Amazon's recruiters looked at the recommendations generated by the tool when searching for new hires, but never relied solely on those rankings." "disbanded the team by the start of last year because executives lost hope for the project." "five people familiar with the effort."
```

```text
URL:         https://www.vice.com/en/article/amazon-ai-recruitment-hiring-tool-gender-bias/
Kind:        secondary for the bias account (relies on Reuters), but it carries Amazon's own on-the-record statement, which is primary to Amazon. Recorded here because Amazon declined to give Reuters those specifics.
Establishes: Amazon's public position after the Reuters story: it confirmed the program existed but characterized it as experimental and disputed operational use.
Paraphrase:  VICE/Motherboard's account of the bias is sourced entirely to Reuters ("five people close to the project"). Amazon told the outlet the system was only ever used in a trial and developmental phase, never independently, and was never rolled out to a larger group; it stated the tool was never used by Amazon recruiters to evaluate candidates.
Locators:    VICE (Motherboard), Oct. 2018.
Quote:       Amazon spokesperson: "This was never used by Amazon recruiters to evaluate candidates." Amazon also said the system "was only ever used in a trial and developmental phase, and never independently" and "was never rolled out to a larger group."
```

```text
URL:         https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page  (FAQ PDF: https://www.nyc.gov/assets/dca/downloads/pdf/about/DCWP-AEDT-FAQ.pdf)
Kind:        primary — the NYC Department of Consumer and Worker Protection is the regulator that owns Local Law 144 and its rules.
Establishes: The regulatory response to widespread automated hiring: definition of an AEDT, the bias-audit and notice requirements, and the operative dates.
Paraphrase:  Local Law 144 of 2021 prohibits employers and employment agencies from using an AEDT in New York City unless a bias audit was done and required notices are provided. An AEDT is a computer-based tool that (a) uses machine learning, statistical modeling, data analytics, or artificial intelligence, (b) helps employers make employment decisions, and (c) substantially assists or replaces discretionary decision-making. "Employment decision" includes screening, not just the final hire. A bias audit is an impartial evaluation by an independent auditor that at minimum calculates selection or scoring rates and the impact ratio across sex categories, race/ethnicity categories, and intersectional categories. The law was enacted in 2021, took effect January 1, 2023, and enforcement began July 5, 2023. The law requires the audit but "does not require any specific actions based on the results."
Locators:    DCWP AEDT FAQ, dated 06/29/2023, Sections I–II (Overview; General Bias Audit Requirements). The FAQ points to the Rules of the City of New York for the full definitions.
Quote:       "An AEDT is a computer-based tool that: Uses machine learning, statistical modeling, data analytics, or artificial intelligence. AND Helps employers and employment agencies make employment decisions. AND Substantially assists or replaces discretionary decision-making." "A bias audit is an impartial evaluation by an independent auditor. At a minimum, an independent auditor's evaluation must include calculations of selection or scoring rates and the impact ratio across sex categories, race/ethnicity categories, and intersectional categories." "It took effect on January 1, 2023. Enforcement begins on July 5, 2023."
```

```text
URL:         https://web.archive.org/web/20250125163154/https://www.eeoc.gov/laws/guidance/select-issues-assessing-adverse-impact-software-algorithms-and-artificial  (archived copy of the EEOC's own canonical page https://www.eeoc.gov/laws/guidance/select-issues-assessing-adverse-impact-software-algorithms-and-artificial, which bot-gates to a hard 404)
Kind:        primary — EEOC technical assistance; the federal enforcement agency (EEOC) owns the interpretation of Title VII it states here. The recorded address is a verbatim Internet Archive (Wayback Machine) snapshot of the EEOC's own page; an archived capture reproduces the EEOC's own text, so the claim's owner is still the EEOC. Recorded deliberately as an archived copy of the EEOC primary because eeoc.gov bot-gates the canonical URL with a 404 (see Locators).
Establishes: The federal frame for AI hiring bias: algorithmic tools are "selection procedures" under the 1978 Uniform Guidelines; the four-fifths (80%) rule of thumb; and that employers stay liable even when a vendor built the tool.
Paraphrase:  The EEOC uses "algorithmic decision-making tool" broadly for software using AI/statistics to evaluate or rate applicants and employees. Selection rate is the proportion of a group hired, promoted, or otherwise selected. The four-fifths rule is a general rule of thumb: one group's selection rate is "substantially" different if its ratio to the highest group's rate is less than four-fifths (80%). It is "merely a rule of thumb" and may be inappropriate, e.g., for large numbers of selections. An employer "may be responsible under Title VII for its use of algorithmic decision-making tools even if the tools are designed or administered by another entity, such as a software vendor," and can still be liable if a vendor's assessment was wrong.
Locators:    EEOC, "Select Issues: Assessing Adverse Impact in Software, Algorithms, and Artificial Intelligence Used in Employment Selection Procedures Under Title VII of the Civil Rights Act of 1964," OLC Control Number EEOC-NVTA-2023-2, issued May 18, 2023. Q&A 3–6. The canonical eeoc.gov page returns HTTP 404 to any automated fetch (the entire eeoc.gov /laws/guidance/ tree is bot-gated), so the address recorded is the Wayback capture dated 2025-01-25 (timestamp 20250125163154), which the Internet Archive availability API confirms is a status-200 capture of the exact EEOC URL. Round-02 content re-verification: the full document text was read firsthand from a verbatim reproduction of the same EEOC page (data.aclum.org PDF whose stored filename is the eeoc.gov path); the title, OLC number, issue date, and the Q4–Q6 four-fifths / adverse-impact text match round 01 exactly. Automated GET to the Wayback address from the research environment returns HTTP 403 ("Blocked by egress policy," a restricted/non-blocking status), never 404/410; for an ordinary reader outside that egress policy the snapshot resolves 200.
Quote:       "The four-fifths rule, referenced in the Guidelines, is a general rule of thumb ... The rule states that one rate is substantially different than another if their ratio is less than four-fifths (or 80%)." "The four-fifths rule is merely a rule of thumb." "Is an employer responsible under Title VII for its use of algorithmic decision-making tools even if the tools are designed or administered by another entity, such as a software vendor? In many cases, yes."
```

```text
URL:         https://www.cs.yale.edu/homes/jf/BarocasSelbst.pdf  (California Law Review 104:671; scholarly home: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2477899)
Kind:        primary — foundational peer-reviewed scholarship that owns the proxy / redundant-encoding mechanism for employment specifically.
Establishes: Two of the lesson's core teachings: a model trained on prior decisions inherits their prejudice ("garbage in, garbage out"), and removing the protected attribute does not remove bias because class membership is redundantly encoded in correlated features.
Paraphrase:  Data is frequently imperfect in ways that let algorithms inherit the prejudices of prior decision makers, and data mining can surface preexisting patterns of exclusion. Inferring a rule from past decisions swayed by prejudice turns that prejudice into a formalized rule applied to all future applicants. Even careful data miners can pick out proxy variables for protected classes. The specific obstacle is "redundant encodings," cases where membership in a protected class happens to be encoded in other, correlated data, so a model can reconstruct the protected trait from ostensibly neutral features.
Locators:    Solon Barocas & Andrew D. Selbst, "Big Data's Disparate Impact," 104 Calif. L. Rev. 671 (2016). Intro (p. 674) and Part I.D "Proxies" (pp. 691, 720); footnote 81.
Quote:       "There is an old adage in computer science: 'garbage in, garbage out.'" "data mining can reproduce existing patterns of discrimination, inherit the prejudice of prior decision makers, or simply reflect the widespread biases that persist in society." "The problem stems from what researchers call 'redundant encodings,' cases in which membership in a protected class happens to be encoded in other data." "automating the process in this way would turn the conscious prejudice or implicit bias of individuals involved in previous decision making into a formalized rule that would systematically alter the prospects of all future applicants."
```

```text
URL:         https://arxiv.org/abs/1104.3913  (PDF: https://www.cs.toronto.edu/~zemel/documents/fairAwareItcs2012.pdf)
Kind:        primary — foundational peer-reviewed computer-science paper (ITCS 2012) that names the same mechanism in formal terms.
Establishes: A second, independent scholarly owner of the mechanism: ignoring a protected attribute ("fairness through blindness") fails because a near-equivalent test can be built from redundant/correlated data.
Paraphrase:  The authors' fairness notion is meant to interdict "discrimination based on redundant encodings of membership in the protected set." They describe "Discrimination Based on Redundant Encoding," where an explicit test for membership in the protected group is replaced by a test that is in practice essentially equivalent — "a successful attack against 'fairness through blindness,' in which the idea is to simply ignore protected attributes such as sex or race."
Locators:    Cynthia Dwork, Moritz Hardt, Toniann Pitassi, Omer Reingold, Richard Zemel, "Fairness Through Awareness," ITCS 2012. Section 1.2 / Appendix A (catalogue of discriminatory practices).
Quote:       "Discrimination Based on Redundant Encoding. Here the explicit test for membership in S is replaced by a test that is, in practice, essentially equivalent. This is a successful attack against 'fairness through blindness,' in which the idea is to simply ignore protected attributes such as sex or race."
```

```text
URL:         https://www.washington.edu/news/2024/10/31/ai-bias-resume-screening-race-gender/
Kind:        primary — reports firsthand original research (peer-reviewed, AAAI/ACM AIES 2024) by its own authors; the finding is theirs.
Establishes: The commissioned "where it lives today" claim, with fresh numbers: current large language models used to screen resumes reproduce proxy bias by the perceived race and gender of applicant names.
Paraphrase:  University of Washington researchers tested three open-source LLMs (from Mistral AI, Salesforce, and Contextual AI) on more than 550 real resumes with 120 names associated with white and Black men and women, generating over 3 million comparisons across nine occupations. The models favored white-associated names 85% of the time versus Black-associated names 9%, and male-associated names 52% versus female-associated names 11%; Black male-associated names were never favored over white male-associated names.
Locators:    UW News, Oct. 31, 2024. Lead author Kyra Wilson; senior author Aylin Caliskan. Presented Oct. 22 at the AAAI/ACM Conference on AI, Ethics, and Society (AIES).
Quote:       "The use of AI tools for hiring procedures is already widespread, and it's proliferating faster" than regulation can address.
```

## Contradictions

- **What Amazon confirmed vs. what only the sources assert.** Reuters reports Amazon
  "declined to comment on the recruiting engine or its challenges." Amazon later told
  VICE the tool "was never used by Amazon recruiters to evaluate candidates" and was
  "only ever used in a trial and developmental phase." Reuters' anonymous sources, by
  contrast, say "Amazon's recruiters looked at the recommendations generated by the
  tool ... but never relied solely on those rankings." These are in tension: the sources
  say recruiters saw the output; Amazon says recruiters never used it to evaluate
  candidates. The writer should not collapse them. What both accounts agree on is the
  bounded claim the commission requires: the ratings were never the sole basis for
  hiring, and the tool was experimental.

- **Single-origin sourcing (the record's most important limitation).** Every specific
  of the incident originates in the one 2018 Reuters investigation, attributed to five
  anonymous "people familiar with the effort." No independent party in a position to
  know has confirmed the 500 models, the "women's" penalty, or the two colleges. Amazon
  neither confirmed nor denied those specifics; it acknowledged only that a trial system
  existed. Every later article (VICE, CNBC, Irish Times, RTÉ, academic case studies) is
  a retelling of Reuters and counts as one origin, not corroboration. Attribute the
  account to Reuters explicitly; do not present the specifics as independently verified
  fact.

- **Disbandment date.** The origin text says the team was disbanded "by the start of
  last year" (the article ran Oct. 10, 2018, so early 2017). The commission's "scrapped
  by 2018" is consistent as a reporting date but is looser than the primary; prefer
  "disbanded by early 2017, reported in October 2018."

- **Details absent from the origin that circulate in retellings.** A team headcount
  (often given elsewhere as "a dozen") and an Edinburgh engineering-hub location do NOT
  appear in the Reuters text I verified. Do not state a team size or a location as if
  the primary supports it; the record supports "a team" and "Seattle" (headquarters)
  only.

- **Prevalence figures.** Widely quoted numbers ("83% of employers," "99% of Fortune
  500 use an ATS") trace to vendor marketing and blog posts, not to a primary survey.
  For "automated screening is now routine," rely on the primary institutional
  statements instead: the EEOC guidance's own premise that "employers increasingly
  utilize these tools," the existence of NYC Local Law 144, and the 2024 UW study's
  finding that AI hiring use "is already widespread."

## Numbers

```text
Figure: Programs built starting 2014
Owner:  Reuters (Dastin, 2018)
Scope:  Amazon's experimental resume-scoring project; development began ~2014.

Figure: 500 computer models
Owner:  Reuters (Dastin, 2018)
Scope:  Models "focused on specific job functions and locations," each taught ~50,000 terms.

Figure: ~50,000 terms per model
Owner:  Reuters (Dastin, 2018)
Scope:  Terms recognized from past candidates' resumes.

Figure: 1–5 stars
Owner:  Reuters (Dastin, 2018)
Scope:  The tool's candidate score range, "much like shoppers rate products on Amazon."

Figure: 10-year training window
Owner:  Reuters (Dastin, 2018)
Scope:  Resumes submitted to Amazon over roughly a decade, "most came from men."

Figure: Bias recognized by 2015; team disbanded by the start of 2017; reported Oct. 10, 2018
Owner:  Reuters (Dastin, 2018)
Scope:  Timeline of the project.

Figure: Five anonymous sources
Owner:  Reuters (Dastin, 2018)
Scope:  "five people familiar with the effort," speaking on condition of anonymity — the entire evidentiary base for the incident.

Figure: Local Law 144 — enacted 2021, effective Jan. 1, 2023, enforcement from July 5, 2023
Owner:  NYC DCWP (AEDT FAQ, 06/29/2023)
Scope:  NYC bias-audit and notice mandate for automated employment decision tools.

Figure: Four-fifths / 80% rule
Owner:  EEOC (2023 Title VII AI technical assistance); originates in the 1978 Uniform Guidelines, 29 C.F.R. § 1607.4(D)
Scope:  A group's selection rate below 80% of the highest group's rate is a rule-of-thumb indicator of adverse impact.

Figure: White names favored 85% vs. Black names 9%; male names 52% vs. female names 11%
Owner:  University of Washington (Wilson & Caliskan, AIES 2024; UW News, 2024)
Scope:  3M+ comparisons over 550+ resumes, 120 names, 9 occupations, three open-source LLMs — evidence the proxy mechanism persists in current resume screeners.
```

## Source assets

```text
Asset: EEOC four-fifths worked example (Q&A 4–5): 80 White and 40 Black applicants, 48 vs. 12 advance, giving selection rates of 60% and 30% and a ratio of 50% (< 80%).
Shows: How adverse impact is measured in one concrete numeric example — useful if the lesson explains the audit standard.
Crop:  Retain both selection rates and the ratio; this is text/table, not a designed graphic, so reproduce as prose or a small table rather than an image.
```

```text
Asset: University of Washington study result bars (favored-rate percentages by race and by gender: 85%/9%, 52%/11%).
Shows: That current LLM resume screeners still encode the proxy bias the Amazon tool showed — the "lives today" payoff.
Crop:  If used, retain the axis labels and the source/venue (AIES 2024); a chart-N.py rebuild from the reported percentages would be honest, not a lifted image.
```

```text
Asset: Reuters article — None found.
Shows: The origin report carries no chart, diagram, or photograph internal to the claim; it is text only.
Crop:  n/a
```

Note: this story is not naturally chart-driven. There is no released Amazon dataset to
visualize; the training-data gender imbalance is described, not quantified in the
primary. Any chart should come from the EEOC example or the UW study, both of which
publish their own numbers.

## Discarded

```text
https://www.cnbc.com/2018/10/10/amazon-scraps-a-secret-ai-recruiting-tool-that-showed-bias-against-women.html: Reuters-wire retelling, same origin; returned HTTP 403 to fetch. RTÉ and Irish Times already gave the verbatim origin text.
https://blog.theinterviewguys.com/how-many-companies-are-using-ai-to-review-resumes/: "83% of companies" prevalence stat is a marketing blog aggregation with no primary survey behind the figure. Not citable.
https://www.nycbiasaudit.com/ and vendor compliance blogs (Deloitte, Littler, Epstein Becker): secondary summaries of Local Law 144 and EEOC guidance; the primary DCWP FAQ and EEOC document own those claims directly.
https://www.researchgate.net/publication/373896468 (Gender Bias in Hiring: An Analysis of Amazon's Recruiting Algorithm): secondary academic analysis built on Reuters; adds no in-a-position-to-know facts about the incident.
https://www.imd.org/research-knowledge/digital/articles/amazons-sexist-hiring-algorithm-could-still-be-better-than-a-human/: opinion/analysis piece, not a source of new fact about the incident.
https://museumoffailure.com/exhibition/amazon-ai-recruiter: popular retelling of Reuters, no independent reporting.
https://data.aclum.org/storage/2025/01/EOCC_www_eeoc_gov_laws_guidance_select-issues-assessing-adverse-impact-software-algorithms-and-artificial.pdf (ACLU-MA stored copy of the EEOC "Select Issues" page): used ONLY this round to re-read the EEOC text verbatim and confirm the Wayback capture holds the identical document; NOT recorded as source [6]'s address because it is an advocacy-org host, not the government primary or a neutral archive of it. The recorded [6] address is the Internet Archive (Wayback) capture of the EEOC's own page.
```
