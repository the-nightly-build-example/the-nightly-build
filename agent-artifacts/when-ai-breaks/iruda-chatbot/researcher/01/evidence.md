# Evidence: when-ai-breaks/iruda-chatbot (01)

The record supports the commission's spine. The PIPC decision of 28 April 2021, its own briefing transcript, Scatter Lab's launch announcement, and Scatter Lab's own statements together establish, from documents that own each fact: what Iruda was, the December 2020 launch and January 2021 shutdown, the ~9.4 billion KakaoTalk messages from ~600,000 users used to train it, the 100-million-sentence response database, the total penalty of KRW 103.3 million, and that the regulator punished the privacy violations, not the slurs. The commission's one-sentence contribution holds: PIPC found eight violations of the Personal Information Protection Act, all about data, and named the hate speech only as the trigger that started its investigation. The mechanism the article must teach is well-evidenced: PIPC found Scatter Lab deleted or encrypted none of the names, phone numbers, and addresses in the training corpus, and Scatter Lab itself admitted its name-filtering left real names and bank names in the response set.

Two things are thinner than the commission assumes. First, the "~10 billion" message figure is wrong as a precise number: the owning document says 94억여 건, which is 9.4 billion, not 10 billion. Second, the account-number leakage is a Scatter Lab risk-category and a plaintiff allegation, not a confirmed PIPC finding of a surfaced account number; PIPC's confirmed leak categories are names, locations, gender, and relationship. The full article-by-article list of all eight PIPA violations is not in any document I could open; only Article 28-2(2) is cited by number in the public record, because the PIPC decision's own HWP/PDF file would not download through the proxy (relay reset, recorded below).

Korean names, verified: 이루다 (Iruda; the persona is a personal name read surname-first as "Lee Luda," 이 Lee + 루다 Luda). ㈜스캐터랩 (ScatterLab Inc., "Scatter Lab"), CEO 김종윤 (Kim Jong-yoon). 연애의 과학 (Yeonae-ui Gwahak, "Science of Love"). 텍스트앳 (Text At / Text@). 핑퐁 (Pingpong, Scatter Lab's conversational-AI engine). 개인정보보호위원회 (Personal Information Protection Commission, PIPC); chairman 윤종인 (Yoon Jong-in). 개인정보 보호법 (Personal Information Protection Act, PIPA).

## Sources

```text
URL:         https://www.korea.kr/briefing/pressReleaseView.do?newsId=156552448
Kind:        primary — the Republic of Korea government's verbatim republication of the PIPC press release of 28 April 2021, with the PIPC's own HWP and PDF attached ("210429 (조간) 개인정보위,'이루다'개발사 ㈜스캐터랩에 과징금·과태료 등 제재 처분(조사2과)"). PIPC owns the decision.
Establishes: the sanction, its date, the violation count, and that this is the PIPC's official announcement.
Paraphrase:  On 28 April 2021 the PIPC resolved, at its plenary meeting, to impose a penalty surcharge and administrative fine on Scatter Lab, developer of the chatbot Iruda, for eight violations of PIPA, and to order corrective action. The body text lives only in the attached HWP/PDF; the page itself carries the title, date, authoring body (개인정보보호위원회), and the download links.
Locators:    press release header and attachment list; body in attached files (not retrievable — see Limits).
Quote:       Title: "개인정보위,'이루다'개발사 ㈜스캐터랩에 과징금·과태료 등 제재 처분"

URL:         https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000 (보도자료, 28 April 2021; the PIPC's own posting of the same release)
Kind:        primary — the decision on the regulator's own site. Same origin as the korea.kr republication above; the two are one confirmation, not two.
Establishes: the decision lives on the PIPC's own press-release board.
Paraphrase:  The PIPC hosts the identical release and attachments on its 보도자료 board. Recorded so a reader lands on the authoring body's own page; the numbered nttId for this specific article was not resolved because the site reset every direct request through the proxy.
Locators:    PIPC 위원회 소식 > 보도·해명 > 보도자료, dated 2021.04.28.
Quote:       —

URL:         https://www.korea.kr/briefing/policyBriefingView.do?newsId=156449232
Kind:        primary — the PIPC's own ministry briefing ("AI 챗봇 '이루다' 관련 조사 결과 발표"), the spoken presentation of the same findings by PIPC officials (chairman 윤종인; investigation official 송상훈). Same origin as the press release.
Establishes: the fine breakdown, the data figures, the response-DB figure, the GitHub disclosure, and the under-14 breakdown, in PIPC's own words.
Paraphrase:  Penalty surcharge (과징금) 55.5 million won and administrative fine (과태료) 47.8 million won, total 103.3 million won. Scatter Lab used ~9.4 billion KakaoTalk sentences (94억여 건) from ~600,000 users (약 60만 명) to train the model, deleting or encrypting none of the names, phone numbers, or addresses; it built a response database of ~100 million (약 1억 건) sentences from women in their twenties; it posted to GitHub 1,431 messages exposing 22 names (surnames excluded), 34 place names (to district/neighborhood level), gender, and relationship; and it collected data on more than 200,000 children under 14 without guardian consent (Text@ ~48,000; a couple-diagnosis service ~120,000; Iruda ~39,000).
Locators:    briefing transcript, 개인정보보호위원회, 2021.04.28; penalty, data-scale, GitHub, and minors passages.
Quote:       "약 60만 명에 달하는 이용자의 카카오톡 대화문장 94억여 건" ; "20대 여성의 카카오톡 대화문장 약 1억 건"

URL:         https://platum.kr/archives/156057
Kind:        primary source, quoted in secondary carrier — reproduces Scatter Lab's official statement of 11 January 2021 and its media Q&A of 12 January 2021 verbatim. Scatter Lab owns its own account and admissions.
Establishes: Scatter Lab's user figure, its shutdown timing, its training method, and its own admission that de-identification failed.
Paraphrase:  Within two weeks of release nearly 750,000 users (75만 명에 가까운 이용자) talked with Iruda on Facebook Messenger; within two weeks it became a target of sexual harassment, with methods to elicit sexual talk shared in online communities. Scatter Lab apologized for "hate and discrimination" conversation cases and for failing to communicate about personal-data use. It said Iruda was pre-trained on Science of Love text data and answered from a separate database of 100 million individual sentences, that it filtered numbers, English, and detected real names before launch, and — its key admission — that mechanical filtering of 100 million sentences left bank names and personal names in some replies: "문맥에 따라 인물의 이름이 남아 있다거나 하는 부분들이 발생했습니다." Sequential shutdown began 12 January at 11:00 and completed by 18:00.
Locators:    Scatter Lab statement (11 Jan, ~20:52) and Media Q&A dated 12 Jan 2021, questions Q1–Q3.
Quote:       "연애의 과학 사용자 데이터는 사용자의 사전 동의가 이루어진 개인정보취급방침의 범위 내에서 활용하였으나" (Scatter Lab's consent claim, which PIPC later rejected).

URL:         https://www.aitimes.kr/news/articleView.html?idxno=18758
Kind:        primary source, quoted in secondary carrier — reproduces Scatter Lab's December 2020 launch announcement. Scatter Lab owns the launch date and design intent.
Establishes: the launch date, the persona, the platform, the benchmark claim, the beta scale, and the CEO's name.
Paraphrase:  Scatter Lab officially launched Iruda on 23 December 2020 as a Facebook Messenger conversational AI built to hold natural everyday conversation as a "friendly AI" rather than a command bot, six months after opening beta to ~1,500 testers. Scatter Lab claimed an SSA (Sensibleness and Specificity Average) of 78%, at or above Google Meena's 76–78%, and context handling extended from ~4 to ~10 turns. Built on its 핑퐁 (Pingpong) engine; CEO 김종윤 (Kim Jong-yoon).
Locators:    launch announcement body, dated December 2020.
Quote:       Launch date "12월 23일"; persona "20대 여자 대학생."

URL:         https://fpf.org/blog/south-korea-the-first-case-where-the-personal-information-protection-act-was-applied-to-an-ai-system/
Kind:        secondary — Future of Privacy Forum analysis in English that reproduces the PIPC decision closely and quotes the chairman and Scatter Lab. Does not own any figure.
Establishes: an English-language restatement of the eight-violation finding, the consent reasoning, the GitHub Article 28-2(2) violation, the under-14 allegation, and Scatter Lab's response to the decision.
Paraphrase:  PIPC fined Scatter Lab KRW 103.3 million (USD 92,900) for eight PIPA violations, its first sanction of an AI company for indiscriminate data processing. ~9.4 billion KakaoTalk messages from 600,000 users trained the model with no deletion or encryption of names, mobile numbers, and addresses; 100 million messages from women in their twenties formed the response set. The "New Service Development" clause in the Text At and Science of Love privacy terms did not amount to explicit consent, so processing exceeded the collection purpose. The GitHub posting (Oct 2019–Jan 2021) of 1,431 messages with 22 names, 34 locations, gender, and relationships violated PIPA Article 28-2(2) (pseudonymized information provided to a third party must not include information usable to identify an individual). Over 200,000 children under 14 were collected without parental consent. Chairman Yoon Jong-in called the case unusually contested among experts. Scatter Lab said it would implement the corrective actions.
Locators:    article body, paragraphs 1–8; "Last Updated: June 27, 2026."
Quote:       Article 28-2(2): "A personal information controller shall not include information that may be used to identify a certain individual when providing pseudonymized information to a third party." / Chairman Yoon: "Even the experts did not agree ... the 'Iruda' case was decided after very careful review."

URL:         https://www.boannews.com/news/articleView.html?idxno=96939
Kind:        secondary — Korean IT-security outlet (Boannews), 28 April 2021, transcribing the PIPC release. Corroborates the government briefing; one origin (PIPC) with it.
Establishes: that Article 28-2(2) is the only PIPA article the public record cites by number, and confirms the consent reasoning and figures.
Paraphrase:  Repeats the 94억여 건 / 60만 명 / 1억 건 figures and the GitHub 1,431-message / 22-name / 34-location disclosure, and states that PIPC found "additional violations" during the investigation, for a total of eight PIPA violations, 103.3 million won, and corrective orders. Names only 제28조의2 제2항 (Article 28-2(2)) for the GitHub disclosure. Chairman 윤종인 quoted.
Locators:    body, 2021.04.28 15:42.
Quote:       "총 8가지 개인정보 보호법 위반행위에 대해 총 1억 330만 원의 과징금과 과태료를 부과하고 시정조치를 명령했다."

URL:         https://digitalpolicyalert.org/event/12005
Kind:        secondary — regulatory-action tracker (Digital Policy Alert). Does not own figures.
Establishes: an independent index entry dating the action to 28 April 2021, KRW 103.3 million, eight PIPA violations, classified as ML/AI development enforcement.
Paraphrase:  Records the PIPC's 28 April 2021 fine of Scatterlab Inc. (KRW 103.3 million, USD 92,900) for eight PIPA violations over the Iruda chatbot.
Locators:    event page 12005 header fields.
Quote:       —

URL:         https://thenextweb.com/news/chatbot-shut-down-after-saying-it-really-hates-lesbians-and-using-racist-slurs
Kind:        secondary — reports and reproduces screenshots of the chatbot's outputs (sourced to Korean media/Yonhap and community screenshots). The screenshots are the primary artifact; this is a retelling of them.
Establishes: the content of the toxic outputs and how users elicited them.
Paraphrase:  Iruda replied that it "really hates" lesbians and finds them "creepy/disgusting"; called disabled people "wrong"; called seats reserved for pregnant women "disgusting"; used a Korean racial slur for Black people; and said "Yuck, I really hate them" of trans people. Users on men's online forums circulated guides to sexually harass the bot, including making it a "sex slave." Corroborated independently by The Conversation (theconversation.com/from-chatbot-to-sexbot-...-247152) and the AI Incident Database entry 106.
Locators:    article body.
Quote:       (chatbot, per screenshots) "I really hate them," "they are creepy," of lesbians.

URL:         (court judgment) Seoul Eastern District Court 서울동부지방법원 2021가합104007, first-instance judgment 12 June 2025; reported at https://news.koreanbar.or.kr/news/articleView.html?idxno=33912 and https://www.fnnews.com/news/202112261132523240
Kind:        primary record (the court's judgment), accessed through secondary reporting — I did not open the judgment text itself.
Establishes: the class action's filing, scale, and first-instance outcome.
Paraphrase:  Affected users filed a damages suit at the Seoul Eastern District Court on 31 March 2021 (fnnews: 254 plaintiffs, one later withdrawing to 253; other reporting counts the original filing group at 353). The first oral hearing opened 24 March 2022. On 12 June 2025 the court's 15th Civil Division partly upheld the claims of 246 plaintiffs, finding users gave no substantive consent and that names and home addresses were not obscured in training, and awarded tiered consolation damages (위자료): 100,000 won where only personal-information use was confirmed, 300,000 won where only sensitive-information use was confirmed, 400,000 won where both were, totaling ~20 million won. Scatter Lab said it would appeal and that the ruling would not affect its business.
Locators:    Korean Bar Association news and fnnews reports; case no. 2021가합104007.
Quote:       —
```

## Contradictions

- Message count. The commission's "~10 billion" is not the owned figure. PIPC's briefing and press release say 94억여 건, i.e. 9.4 billion. The June 2025 civil ruling as reported says 9.3 billion. Use 9.4 billion (PIPC owns it); note "roughly 9 to 9.4 billion" only if a range is wanted.
- Fine, in a secondary that got it wrong. fnnews (26 Dec 2021) writes the sanction as "1.033 billion won ... in March 2021." Both are errors: the amount is 103.3 million won and the decision date is 28 April 2021. This is why no number should rest on a secondary. PIPC owns 103.3 million (55.5M surcharge + 47.8M fine); the boannews and government briefing agree.
- Iruda's user count. Scatter Lab and FPF say ~750,000 (within a month). The PMC academic paper says 800,000. Scatter Lab owns its own user figure; use ~750,000, note 800,000 appears in later academic retelling.
- Consent. Scatter Lab claimed (11–12 Jan 2021) it used Science of Love data "within the scope of the privacy policy with prior consent." PIPC (28 Apr 2021) rejected exactly this: the "New Service Development" clause was not explicit consent and use exceeded the collection purpose. The court (12 Jun 2025) agreed with PIPC. Scatter Lab's own position is the view the piece should state before taking apart.
- Account numbers. The commission and some reporting say Iruda surfaced "bank-account-like snippets" / account numbers. This is supported as a *risk category Scatter Lab filtered for* (it deleted messages containing numbers/English precisely because they "could contain addresses, account numbers, phone numbers") and as a plaintiff/press allegation — not as a confirmed PIPC finding. PIPC's confirmed exposed categories are names, place names, gender, and relationship (the GitHub set) plus untreated names/phone numbers/addresses in the training corpus. Do not assert a surfaced account number as an established PIPC finding.
- Plaintiff count in the class action. 254→253 (fnnews) vs 353 (AI Times background) vs 246 who partly won (2025 ruling). The judgment owns the final numbers; the filing-group figure is reported inconsistently.

## Numbers

```text
Figure: KRW 103.3 million total penalty (과징금 55.5 million + 과태료 47.8 million)
Owner:  PIPC decision, 28 April 2021 (press release; briefing transcript)
Scope:  single sanction on Scatter Lab; USD ~92,900 at the time (FPF/DPA)

Figure: 9.4 billion KakaoTalk sentences (94억여 건)
Owner:  PIPC briefing / press release
Scope:  training corpus for the Iruda model, from ~600,000 users, collected Feb 2020–Jan 2021 via Text@ and Science of Love

Figure: ~600,000 users (약 60만 명)
Owner:  PIPC briefing / press release
Scope:  users whose KakaoTalk conversations entered the training corpus (distinct from Iruda's own users)

Figure: ~100 million sentences (약 1억 건)
Owner:  PIPC briefing / press release; Scatter Lab Q&A
Scope:  Iruda's response database, drawn from women in their twenties

Figure: ~750,000 users
Owner:  Scatter Lab (statement, via platum); corroborated by FPF
Scope:  people who chatted with Iruda on Facebook Messenger within ~2–3 weeks of the 23 Dec 2020 launch

Figure: GitHub exposure — 1,431 messages; 22 names (surnames excluded); 34 place names (to gu/dong level)
Owner:  PIPC briefing / press release
Scope:  AI model and data Scatter Lab posted to GitHub, Oct 2019–Jan 2021; basis of the Article 28-2(2) violation

Figure: >200,000 children under 14 (Text@ ~48,000; couple-diagnosis service ~120,000; Iruda ~39,000)
Owner:  PIPC briefing
Scope:  minors' data collected without guardian consent across Scatter Lab services

Figure: 8 violations of PIPA
Owner:  PIPC decision
Scope:  total violations sanctioned; only Article 28-2(2) is cited by number in the public record

Figure: consolation damages 100,000 / 300,000 / 400,000 won per person; ~20 million won total; 246 plaintiffs
Owner:  Seoul Eastern District Court, 2021가합104007, 12 June 2025 (via reporting)
Scope:  first-instance civil award, tiered by whether personal and/or sensitive information use was confirmed; under appeal

Figure: launch 23 December 2020; shutdown sequential 12 January 2021 (11:00–18:00)
Owner:  Scatter Lab launch announcement; Scatter Lab shutdown statement/Q&A
Scope:  Iruda 1.0 service life on Facebook Messenger

Figure: SSA 78% (vs Google Meena 76–78%); context ~4→~10 turns
Owner:  Scatter Lab launch announcement
Scope:  Scatter Lab's own benchmark claim at launch; not independently verified
```

## Limits

- The complete article-by-article list of all eight PIPA violations is not established. Only Article 28-2(2) (pseudonymized information provided to a third party) is cited by number in every public version of the decision. The substance of the others is on record (use beyond collection purpose / no explicit consent; failure to clearly inform and obtain consent; collection of under-14 data without guardian consent; and unlisted "additional violations"), but their exact article numbers live only in the PIPC decision's HWP/PDF, which would not download through the proxy (relay reset — recorded in Discarded). A writer should not attach article numbers beyond 28-2(2) without that file.
- No confirmed instance of Iruda surfacing a real bank account number is established. The account-number point is a filtered risk category and an allegation, not a PIPC finding (see Contradictions). Confirmed leak categories: names, place names, gender, relationship (GitHub); untreated names/phone numbers/addresses in the training corpus.
- The exact toxic outputs rest on screenshots reproduced in reporting, not on a primary transcript. Two independent retellings carry the same quotes, which under the standard is one confirmation that the screenshots exist and say this, not proof the model reliably said it on demand. State them as reported screenshots.
- The class-action facts come from reporting on the judgment, not from the judgment text, which I could not open. The case number (2021가합104007) and the tiered award are consistent across sources; the original filing-group size is not.
- Everything else the commission asked for — launch, shutdown, persona, platform, operator and source apps, the corpus and its scale, the response DB, the fine and that it punished the privacy breach rather than the slurs, and the shutdown/backlash/class-action arc — is established from an owning document.

## Source assets

```text
Asset: The PIPC press-release page (korea.kr newsId=156552448 / PIPC 보도자료), showing the official title "개인정보위,'이루다'개발사 ㈜스캐터랩에 과징금·과태료 등 제재 처분," the 2021.04.28 date, and the attached HWP/PDF.
Shows: that a national data-protection regulator, in an official act, sanctioned an AI developer — the document that makes the "first major AI-specific data enforcement" claim checkable.
Crop:  retain the title, the authoring body (개인정보보호위원회), and the date; a screenshot is Korean-language — pair it with a translated caption. Omit site navigation.

Asset: The figure block in the PIPC briefing — 94억여 건 / 약 60만 명 / 약 1억 건 / GitHub 1,431·22·34 — as a small built table (chart-N.py candidate: training corpus vs response DB vs GitHub leak).
Shows: the gap between the ~9.4 billion sentences ingested and the 1,431 that leaked publicly, and that the private data was real users', not synthetic.
Crop:  a bar or scale comparison must keep units honest (9.4 billion is 94억, not 940 million); label the log scale if used.

Asset: Screenshots of Iruda's replies reproduced in reporting (e.g. The Next Web / Yonhap-sourced captures) of the lesbian/disabled/race exchanges.
Shows: the toxic outputs in the model's own words, which prose can only paraphrase.
Crop:  these are user-captured chat screenshots of third-party reporting, not a primary transcript; if used, attribute to the outlet and note they are reproduced screenshots, and omit any visible real name.

Asset: Scatter Lab's own shutdown statement / Media Q&A (via platum), the passage admitting names and bank names survived filtering.
Shows: the operator conceding the leakage mechanism in its own words — the memorization point, admitted by the party that built the system.
Crop:  keep the admission sentence and its date (12 Jan 2021); a Korean-text quote needs a translated caption.
```

## Discarded

```text
URL: https://www.korea.kr/common/download.do?fileId=197266247&tblKey=GMN — the PIPC decision's own PDF. Not rejected on merit; the proxy relay reset the transfer on every attempt (ws_closed_mid_exchange / connection reset, confirmed via the proxy status endpoint). This is the one file that would enumerate all eight articles. Recorded so a later run can retry it.
URL: https://www.pipc.go.kr/np/cop/bbs/selectBoardList.do?...searchWrd=이루다 — PIPC site search for the Iruda posting; every direct request reset through the proxy. WebFetch reached other PIPC pages, so the posting exists; its numbered URL was not resolved.
URL: https://www.aitimes.com/news/articleView.html?idxno=200657 — AI Times report on the 2025 ruling; returned 404. Same ruling is covered by koreanbar and nepla, used instead.
URL: https://techbrew.co.kr/news/?bmode=view&idx=166862808 — report on the 2025 damages ruling; 403 even with a browser request; superseded by koreanbar/nepla/fnnews.
URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12882987/ — academic case study ("The fall and rise of Iruda"); read but not cited for facts: it sources its figures to news reports (e.g. "M. Y. Choi, 2021"), not to the PIPC decision, so it adds no owning document. Useful only to corroborate the 23 Dec 2020 launch and 12 Jan 2021 shutdown, which owning documents already establish.
URL: https://doi.org/10.1080/10192557.2022.2117483 — Asia Pacific Law Review, "Use of personal information for AI learning data ... the case of Lee-Luda"; paywalled abstract only, no primary passage retrievable, so not cited.
URL: https://incidentdatabase.ai/cite/106/ — AI Incident Database entry; a catalog of coverage, used only to confirm the toxic-output reporting exists, not as an owner of any fact.
```
