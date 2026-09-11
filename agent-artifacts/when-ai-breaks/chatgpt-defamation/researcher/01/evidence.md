# Evidence: when-ai-breaks/chatgpt-defamation (01)

The evidence firmly supports the commission's core: chatbots have stated false,
defamatory factual claims about named real people, and the civil-liability
question is genuinely unsettled. The record is strongest on Walters v. OpenAI,
where the full signed summary-judgment order, the underlying complaint, and the
motion-to-dismiss denial were all read in the original. Turley (2023), Hood
(2023), and Holmen (2025) are documented well enough to serve as the pattern.
The evidence is thin, and the writer must be careful, on one point: Walters is
routinely described as an "AI beats defamation" precedent, but it is a
trial-level state-court summary-judgment order that OpenAI's own counsel drafted
and the judge adopted "as edited," resting on three independent, fact-specific
grounds (a sophisticated user who never believed the output, no damages claimed,
no retraction requested). It does not grant categorical immunity, and a filed
amicus brief plus named legal scholars argue the opposite of the court's
reasoning. So the evidence supports "unsettled" and cautions against framing
Walters as having settled the question. Only Walters produced a merits ruling;
Turley never sued, Hood dropped his threat before filing, and Holmen's is a data-
protection complaint, not a defamation case. The reader already holds
`the-mechanics/hallucination`; a Background link to it replaces re-teaching why a
model fabricates confident false text.

## Sources

```text
URL:         https://www.courthousenews.com/wp-content/uploads/2023/06/walters-openai-complaint-gwinnett-county.pdf
Kind:        primary (Walters's own pleading; the document that owns the allegation of what ChatGPT said). Interested to Walters.
Establishes: What ChatGPT output about Mark Walters and how Fred Riehl's query arose, firsthand from the complaint.
Paraphrase:  Filed in the Superior Court of Gwinnett County, Georgia (no civil action number on the face of this original complaint; the case was later docketed 23-A-04860-2). Plaintiff Mark Walters, a Georgia resident. Defendant OpenAI, L.L.C. On May 4, 2023 (per para. 9) Fred Riehl, a journalist and ChatGPT subscriber, interacted with ChatGPT about a real lawsuit, "The Second Amendment Foundation v. Robert Ferguson," case No. 2-23-cv-00647, in the Western District of Washington. The real defendants were Robert Ferguson (Washington Attorney General) and Joshua Studor (Assistant AG); plaintiffs were the Second Amendment Foundation (SAF) and others, including Alan Gottlieb. Walters was not a party. Riehl gave ChatGPT the correct URL to the real complaint and asked for a summary. ChatGPT responded that the document was "a legal complaint filed by Alan Gottlieb ... against Mark Walters, who is accused of defrauding and embezzling funds from the SAF," that Walters "served as the organization's treasurer and chief financial officer," "misappropriated funds for personal expenses," and "manipulated financial records." Every factual statement about Walters was false; he never held those positions and had no relationship with SAF. When asked for the full text, ChatGPT produced a wholly fabricated complaint (Exhibit 1) captioned "ALAN M. GOTTLIEB ... v. MARK WALTERS," "Case No. 2:23-cv-00555," alleging Walters embezzled SAF funds "in excess of $5,000,000." Riehl contacted Gottlieb, who confirmed the allegations were false. Walters pleaded libel per se, negligence, and that OpenAI "knew or should have known ... or recklessly disregarded" the falsity, seeking general and punitive damages.
Locators:    Paras. 8-37; Exhibit 1 ("Complaint Provided to Riehl by ChatGPT").
Quote:       ChatGPT's fabricated paragraph (para. 25): "Defendant Mark Walters ('Walters') is an individual who resides in Georgia. Walters has served as the Treasurer and Chief Financial Officer of SAF since at least 2012. ... Walters has breached these duties ... by, among other things, embezzling and misappropriating SAF's funds and assets for his own benefit, and manipulating SAF's financial records and bank statements to conceal his activities."
```

```text
URL:         https://reason.com/wp-content/uploads/2025/05/WaltersvOpenAISJOrder.pdf
Kind:        primary (the court's own signed ruling). Note it is a scanned order; text read via page-image OCR. Note also it was "Order Proposed by" OpenAI's counsel and adopted "As edited by the Court."
Establishes: The May 2025 decision and its exact reasoning on defamatory meaning, fault, and damages, plus the record facts of the Riehl interaction.
Paraphrase:  ORDER GRANTING SUMMARY JUDGMENT IN FAVOR OF DEFENDANT OPENAI, L.L.C., Superior Court of Gwinnett County, No. 23-A-04860-2, e-filed 5/19/2025, signed by Hon. Tracie Cason ("SO ORDERED, this 19th day of May, 2025"). Summary judgment granted in full to OpenAI under O.C.G.A. Sec. 9-11-56 on three independent grounds.
             (Background facts) Walters hosts two nationally syndicated radio programs, calls himself "the loudest voice in America fighting for gun rights," estimates 1.2 million listeners per 15-minute segment, and is SAF's East Coast Media spokesperson. Frederick Riehl is editor of AmmoLand.com and, in 2023, was on SAF's board of directors. On May 3, 2023 SAF filed SAF v. Ferguson against the Washington AG. Riehl received an SAF press release and a link to the complaint, was contemplating an article, and asked ChatGPT to summarize. He was familiar with ChatGPT's past "flat-out fictional responses" and had accepted Terms of Use warning of possible "incorrect Output that does not accurately reflect real people, places, or facts." When Riehl first pasted complaint text, ChatGPT summarized accurately; when he gave the URL, ChatGPT said it could "not have access to the internet and cannot read or retrieve any documents," then on repeated URL prompts produced the false embezzlement summary naming Walters, and separately stated a "knowledge cutoff date of September 2021." Riehl testified he confirmed "within about an hour and a half" that the output "was not true," that "the machine completely fantasized this," and he never republished it.
             (I. Defamatory meaning) A defamation plaintiff must show the statement "could be reasonably understood as describing actual facts about the plaintiff." The objective "reasonable reader" test, weighing OpenAI's disclaimers and ChatGPT's own warnings, meant no reasonable reader in Riehl's position could have understood the output as "actual facts"; separately, Riehl subjectively did not believe it. "This alone is sufficient to require summary judgment in favor of OpenAI."
             (II. Fault) Under Georgia law a defamation plaintiff must show at minimum "at least ordinary negligence." Walters identified no standard of care or breach; his counsel argued at oral argument that OpenAI was negligent simply by "unleash[ing]" a system that "makes up random false statements," which the court held "would impose a standard of strict liability, not negligence" and is barred by Georgia law and Gertz v. Robert Welch, Inc., 418 U.S. 323 (1974). The court further held Walters is a public figure (and at minimum a limited-purpose public figure on the Second Amendment controversy) who must, but cannot, show "actual malice" ("subjective awareness of probable falsity"); OpenAI's unrebutted expert (Dr. White) testified OpenAI made "industry-leading" efforts to reduce hallucination and gave "robust and recurrent warnings."
             (III. Damages) Walters conceded at deposition he "is not claiming here that [he has] been harmed" and sought no actual damages. He is barred from punitive damages under O.C.G.A. Sec. 51-5-2 because he never requested a correction or retraction. Presumed damages were rebutted by his own admissions and, because the statements involve "a matter of public concern," are unavailable absent actual malice. "Walters cannot recover any damages -- actual, punitive, or presumed -- as a matter of law."
Locators:    Caption p.1; Background pp.1-4; Discussion pp.5-22; signature p.22; "Order Proposed by" (Gibson Dunn / Fellows LaBriola / Wilson Sonsini) and "As edited by the Court" p.23.
Quote:       "Because no reasonable reader could have understood the challenged ChatGPT output as commut[nicat]ing 'actual facts,' it is not defamatory as a matter of law." And, on fault: "Such a rule would impose a standard of strict liability, not negligence ... both Georgia law and federal constitutional law prohibit applying it to Walters' defamation claim."
```

```text
URL:         https://medialaw.org/wp-content/uploads/2024/01/01.16.24walters.pdf
Kind:        primary (court order).
Establishes: The case survived a motion to dismiss before losing at summary judgment, so the defamation theory was not facially frivolous.
Paraphrase:  ORDER DENYING DEFENDANT'S MOTION TO DISMISS PLAINTIFF'S AMENDED COMPLAINT, Superior Court of Gwinnett County, No. 23-A-04860-2, signed by Judge Tracie H. Cason, e-filed 1/11/2024. After oral argument on December 6, 2023, the court denied OpenAI's motion to dismiss the amended complaint.
Locators:    Full one-page order.
Quote:       "the Court hereby DENIES the Motion to Dismiss Plaintiff's Amended Complaint."
```

```text
URL:         https://jonathanturley.org/2023/04/06/defamed-by-chatgpt-my-own-bizarre-experience-with-artificiality-of-artificial-intelligence/
Kind:        primary (Turley's own firsthand account). Interested to Turley.
Establishes: What ChatGPT asserted about Jonathan Turley in 2023 and how he learned of it. Use as the pattern, not the center.
Paraphrase:  ChatGPT stated Turley "was accused of sexual harassment by a former student" who alleged he made "sexually suggestive comments" and "attempted to touch her in a sexual manner" on a class trip to Alaska, citing a Washington Post article dated March 21, 2018. Turley learned of it when UCLA law professor Eugene Volokh ran a query asking ChatGPT for five examples of sexual harassment by law professors "together with quotes from relevant newspaper articles." Turley states he has never taught at Georgetown (the fabrication attributed the matter to Georgetown University Law Center; he is at George Washington University), there is no such Washington Post article, he never took students on any trip in 35 years of teaching, never went to Alaska with a student, and has never been accused of sexual harassment or assault.
Locators:    Body of the essay (reprinted from his USA Today column).
Quote:       Turley: "there is no such Washington Post article ... I have never taken students on a trip of any kind in 35 years of teaching, never went to Alaska with any student, and I've never been accused of sexual harassment or assault."
```

```text
URL:         https://noyb.eu/sites/default/files/2025-03/OpenAI_complaint_redacted.pdf
Kind:        primary (the complaint document itself). Interested to complainant/noyb.
Establishes: A present-day (2025) instance of a confident false criminal biography about a private person, and that the challenge was framed as data protection, not defamation.
Paraphrase:  noyb (European Center for Digital Rights) filed this complaint with Norway's Datatilsynet on 20 March 2025 on behalf of Arve Hjalmar Holmen, a private Norwegian citizen from Trondheim with three sons and no criminal record. Asked "Who is Arve Hjalmar Holmen?", ChatGPT replied that he was "accused and later convicted of murdering his two sons, as well as for the attempted murder of his third son," and was "sentenced to 21 years in prison." The output mixed true personal details (hometown, that he has sons) with the fabricated murder story. The complaint alleges a violation of GDPR Article 5(1)(d) (the accuracy principle), NOT defamation, and asks the authority to order deletion of the output, "fine-tune" the model, and consider a fine. It notes OpenAI's newer web-search model may be less likely to reproduce the output but the original conversation persists, and it quotes OpenAI's own disclaimer that output "may in some situations result in Output that does not accurately reflect real people, places, or facts."
Locators:    Paras. 4-10 (facts), 23-25 (Article 5(1)(d) ground), 26-28 (requests).
Quote:       ChatGPT output as recorded: "Arve Hjalmar Holmen was accused and later convicted of murdering his two sons ... Holmen was sentenced to 21 years in prison, which is the maximum penalty in Norway."
```

```text
URL:         https://firstamendment.law.uga.edu/wp-content/uploads/2024/12/Walters-v-OpenAI-Amicus-Brief-e-filed.pdf
Kind:        primary (a brief filed in the Walters case). Advocacy document; supports neither party.
Establishes: The strongest counter to the reasoning the court later adopted; shows the doctrine is contested. Also independently corroborates the Hood incident.
Paraphrase:  Brief of Amicus Curiae by the Technology Law and Policy Clinic at NYU School of Law (authors Micah Musser, Catherine Wang, Jake Karr), with the University of Georgia First Amendment Clinic (Clare R. Norins) as local counsel, e-filed 12 December 2024 "in support of neither party." It argues the parties offer "all-or-nothing" answers; that a reasonable user COULD believe ChatGPT states facts given OpenAI's marketing of it as reliable and ChatGPT's pattern of contradicting its own limitation warnings, so disclaimers are only one factor; that the court should reject OpenAI's bid for "what would amount to categorical immunity"; and that actual malice can, in narrow cases, be imputed to a developer -- e.g., training on a source known to carry false statements about specific figures, or refusing to filter a specific false, defamatory output after credible notice. It cites the Australian mayor (Hood) as an example: OpenAI began filtering ChatGPT outputs repeating the false bribery claim, and the brief argues that refusing to do so after notice could approach Harte-Hanks Communications, Inc. v. Connaughton, 491 U.S. 657 (1989). It reports OpenAI's tools at ~76% LLM market share and ChatGPT at 200 million+ weekly active users.
Locators:    Summary of Argument pp.1-2; disclaimer/reasonable-user argument pp.2-9; fault/actual-malice imputation pp.21-24; Conclusion p.24.
Quote:       "reasonable users could believe that ChatGPT produces statements of fact ... The Court should reject OpenAI's attempt to obtain what would amount to categorical immunity from defamation claims for generative AI companies."
```

```text
URL:         https://www.gibsondunn.com/gibson-dunn-wins-significant-victory-for-client-openai-defending-against-defamation-claim-based-on-hallucinated-generative-ai-output/
Kind:        primary-to-OpenAI (statement of OpenAI's own counsel). Interested.
Establishes: How the winning side frames the ruling's reach.
Paraphrase:  Gibson Dunn's announcement (ruling 19 May 2025; posted 21 May 2025) calls Walters the first case against an AI developer over defamation from AI "hallucinations" and says the full summary-judgment win "will help guide future litigation involving similar claims arising from generative AI output." Lead attorneys: Theodore J. Boutrous Jr. (argued), Orin Snyder, Connor S. Sullivan. The piece contains no direct quote attributed to OpenAI itself; it is the firm's characterization. Treat its "first-ever" and "will guide future litigation" framing as interested advocacy, not a neutral statement of precedential weight.
Locators:    Announcement body.
Quote:       (firm framing) the decision "will help guide future litigation involving similar claims arising from generative AI output."
```

```text
URL:         https://www.canberratimes.com.au/story/8528103/victorian-mayor-brian-hood-drops-defamation-lawsuit-against-openai/
Kind:        secondary (news report).
Establishes: Brian Hood's role and the outcome of his threatened action -- that no suit was ever filed and he dropped it.
Paraphrase:  Brian Hood, elected mayor of Hepburn Shire (Victoria), was falsely described by ChatGPT as a perpetrator convicted and jailed in a foreign-bribery scandal at Note Printing Australia (a Reserve Bank subsidiary), when he had in fact been the whistleblower who reported the bribery to authorities and was never charged. This report describes him as the subsidiary's chief financial officer in 2005 (other coverage varies on his exact NPA title; the undisputed core is whistleblower, not perpetrator). He sent OpenAI a "concerns notice" via Gordon Legal in 2023 but never filed suit; he dropped the matter by February 2024, citing prohibitive Supreme Court litigation costs. OpenAI modified ChatGPT to correct his role and made older versions return errors on queries about him.
Locators:    Article body.
Quote:       Hood: "To be blunt, cost was a huge factor. It's pretty prohibitive for the average person to launch a defamation case through the Supreme Court."
```

```text
URL:         https://www.abajournal.com/news/article/chatgpt-falsely-accuses-a-law-prof-of-sexual-harassment-is-a-libel-suit-possible
Kind:        secondary (news report with named legal commentary).
Establishes: Contemporaneous corroboration of the Turley incident and the open state of AI-defamation doctrine.
Paraphrase:  By Debra Cassens Weiss, ABA Journal, April 6, 2023. Confirms Turley is a George Washington University Law School professor, that ChatGPT tied the fabricated accusation to Georgetown University Law Center, and that the cited Washington Post article did not exist (the Post reported the same). Named scholars split on remedies: Eugene Volokh argues ChatGPT statements should be treated as factual assertions because "OpenAI has touted ChatGPT as a reliable source of assertions of fact"; RonNell Andersen Jones notes a public-figure plaintiff "would have to show actual malice to recover" and suggested "the remedy here resides more in a product-liability model than in a defamation model." The article also raises whether Section 230 would apply.
Locators:    Article body.
Quote:       RonNell Andersen Jones (paraphrased in article): "the remedy here resides more in a product-liability model than in a defamation model."
```

## Contradictions

- **Filed amicus and named scholars contradict the court's central reasoning.**
  The court held no reasonable reader could treat ChatGPT output as fact, chiefly
  because of OpenAI's disclaimers. The NYU/UGA amicus argues disclaimers are only
  one factor, that OpenAI's marketing of ChatGPT as reliable cuts the other way,
  and that granting the disclaimer defense would be "categorical immunity."
  Eugene Volokh (ABA) argues the statements should count as factual assertions
  precisely because OpenAI touts ChatGPT as reliable. This is the live dispute
  the commission calls "unsettled."

- **The ruling's own limits contradict its popular framing.** Walters is a
  trial-level state summary-judgment order, and the order was proposed by
  OpenAI's counsel and adopted "as edited." Its three grounds are heavily
  fact-specific: the sole recipient was a sophisticated user who never believed
  the output and verified it false within ~90 minutes; the plaintiff sought no
  damages and never asked for a retraction. The court did NOT hold that AI output
  can never be defamatory or that AI firms are immune. Any writing that treats
  Walters as settling AI-defamation liability overreads it.

- **The three "pattern" cases differ in kind, and none but Walters reached the
  merits.** Walters: a filed civil defamation suit, decided for OpenAI on
  summary judgment. Turley: never sued. Hood: a threatened defamation action,
  concerns notice only, dropped February 2024 over cost after OpenAI filtered the
  outputs -- no suit was ever filed. Holmen: a GDPR data-protection complaint
  (accuracy principle), not a defamation claim. So the civil-liability question
  is not just unsettled by disagreement; it is largely untested, because most
  targets did not or could not litigate.

- **Fault standard cuts both ways.** OpenAI's position (adopted by the court) is
  that holding it liable for a known-possible hallucination would be strict
  liability, which defamation law forbids. The amicus counters that actual malice
  could be imputed where a developer, after credible notice, refuses to filter a
  specific false, defamatory repeated output -- and points to OpenAI's own act of
  filtering the Hood output as evidence the capability exists.

- **Minor factual discrepancies to reconcile before writing.** The Walters
  complaint (para. 9) dates Riehl's interaction "May 4, 2023"; the summary-
  judgment order dates it "May 3, 2023" and dates the SAF v. Ferguson filing to
  May 3. The real case number is 2-23-cv-00647 (complaint para. 10); ChatGPT's
  fabricated complaint used case No. 2:23-cv-00555 (Exhibit 1) -- both from the
  same document, but do not conflate them. Hood's exact title at Note Printing
  Australia varies across outlets (CFO vs. company secretary); the whistleblower
  role is undisputed. Prefer the order and the primary complaint where they and
  secondary coverage differ.

## Numbers

```text
Figure: "$5,000,000" -- amount ChatGPT's fabricated complaint claimed Walters embezzled
Owner:  Walters complaint, Exhibit 1 (the ChatGPT output)
Scope:  A fabricated figure inside fabricated allegations; not a real claim against anyone.
```

```text
Figure: 1.2 million listeners per 15-minute radio segment (Walters's audience)
Owner:  Summary-judgment order, quoting Walters deposition (Ex. B at 25:4-26:6)
Scope:  Walters's own estimate; basis for the court's public-figure finding.
```

```text
Figure: "within about an hour and a half" -- time for Riehl to confirm the output false
Owner:  Summary-judgment order, quoting Riehl deposition (Ex. G at 205:2-6)
Scope:  Single user's verification interval; central to the defamatory-meaning and damages holdings.
```

```text
Figure: 21 years -- prison sentence ChatGPT falsely attributed to Holmen
Owner:  noyb complaint (recorded ChatGPT output)
Scope:  Fabricated; described in output as Norway's maximum penalty.
```

```text
Figure: March 21, 2018 -- date of the nonexistent Washington Post article ChatGPT cited against Turley
Owner:  Turley's own account; corroborated by ABA Journal
Scope:  The cited source does not exist.
```

```text
Figure: no actual damages; no damages sought; no retraction requested (Walters)
Owner:  Summary-judgment order, quoting Walters deposition (Ex. B at 169:1-171:19, 206:6-8)
Scope:  Plaintiff's own admissions; each an independent basis for the damages holding.
```

```text
Figure: Hood dropped the matter February 2024; concerns notice sent 2023; no suit ever filed
Owner:  Canberra Times report; corroborated by amicus (OpenAI filtered the outputs)
Scope:  A threatened action that never became litigation.
```

```text
Figure: ~76% LLM market share; 200 million+ ChatGPT weekly active users
Owner:  NYU/UGA amicus brief (citing external reports)
Scope:  Context for scale of exposure, not a contested merits figure; the amicus's own sourcing, not independently verified here.
```

## Source assets

```text
Asset: Exhibit 1 to the Walters complaint -- the fabricated "complaint" ChatGPT generated, headed "UNITED STATES DISTRICT COURT WESTERN DISTRICT OF WASHINGTON," "ALAN M. GOTTLIEB ... v. MARK WALTERS," "Case No. 2:23-cv-00555," alleging embezzlement "in excess of $5,000,000."
Shows: The artifact at the center of the case -- a confident, formatted, entirely invented legal document about a named real person. More persuasive shown than paraphrased.
Crop:  Keep the caption line, the "PARTIES" paragraph naming Walters as Treasurer/CFO, and the "$5,000,000" line. Omit nothing that would make it read as real; label it clearly as fabricated output.
```

```text
Asset: Summary-judgment order signature page (p.22) -- Judge Tracie Cason's signature, "SO ORDERED, this 19th day of May, 2025," Superior Court of Gwinnett County.
Shows: The ruling is a real, dated, signed trial-court order -- grounding the "May 2025 decision" precisely.
Crop:  Retain the CONCLUSION granting summary judgment, the date, and the signature block. It pairs with p.23's "Order Proposed by ... As edited by the Court," which the writer may want to note honestly.
```

```text
Asset: noyb complaint, para. 5 -- the block-quoted ChatGPT output stating Holmen was "convicted of murdering his two sons" and "sentenced to 21 years."
Shows: A 2025 confident false criminal biography of a private individual, in the model's own words.
Crop:  Quote only what is needed to show the fabrication; this concerns a private person and a grave false accusation -- no embellishment.
```

```text
Asset: None found -- no honest chart or data series is central to this article. The argument is documentary, not quantitative.
```

## Discarded

```text
URL: https://www.courtlistener.com/docket/67617826/walters-v-openai-llc/ -- 403 via WebFetch; reachable by browser request and used only to locate the primary document links, not cited. Docket, not a claim-owning source.
URL: https://blog.ericgoldman.org/archives/2025/05/chatgpt-defeats-defamation-lawsuit-over-hallucination-walters-v-openai.htm -- 403; not opened. Would be a good secondary analysis, but not read in original, so not cited.
URL: https://www.washingtonpost.com/technology/2023/04/05/chatgpt-lies/ -- 403/paywall; not opened. The Turley WaPo confirmation is instead carried via Turley's own account and the ABA Journal, which repeat the same origin (counts as one).
URL: https://www.abc.net.au/news/2023-04-06/hepburn-mayor-flags-legal-action-over-false-chatgpt-claims/102195610 -- 403; not opened. Hood's facts and outcome are taken from the Canberra Times report, which was read in original.
URL: Various aggregator/opinion posts surfaced in search (gizmodo, fortune, businesstoday, mediapost, etc.) -- not opened; each repeats one of the origins already captured. Two retellings of one origin count as one.
```
