# Evidence record: when-ai-breaks/microsoft-tay

The record supports a clean, well-sourced account of what happened (launch 23
March 2016, offline within about 16 hours, Peter Lee's apology 25 March, the
accidental 30 March relaunch) and a real, citable split between Microsoft's
"coordinated attack / exploited a vulnerability" framing and a design-failure
reading pressed by critics at the time. It also turned up two findings the
brief did not anticipate, both load-bearing: (1) Microsoft's own blog post
never named what the "vulnerability" was — two independent outlets say so
explicitly — so the "specific vulnerability" claim is asserted, not shown; and
(2) the live byline on Microsoft's own blog post gives Peter Lee's title as
"Corporate Vice President, Microsoft Healthcare," while three independent
outlets reporting the story in real time (24–30 March 2016) all give his title
as corporate vice president **of Microsoft Research** — a likely case of the
page's byline reflecting his later title, not his 2016 one. The record is
thinnest on two points: I could not access the Wayback Machine, tay.ai, or
Twitter/X directly (documented below), so every "primary artifact" claim about
Tay's own tweets and launch copy is verified through reproduction in
contemporaneous reporting rather than a first-hand archive read; and the
"repeat after me" mechanism, while consistent across many secondary accounts,
is itself disputed by one named security researcher who argues nearly all of
Tay's output was dictation, not learning — a genuine, if lightly-corroborated,
rival account that complicates the "parroting vs. genuine generation" split
the commission wants to teach.

Access note (read before the Sources list): `web.archive.org` was
unreachable from this session on every attempt — the TLS handshake was reset
on the homepage and on every dated snapshot URL tried, with no explicit 403,
consistent with a network-level block rather than a dead page. `tay.ai` no
longer resolves (DNS failure). `twitter.com/TayandYou` redirects to
`x.com/TayandYou`, which returned HTTP 402 (payment required) to an
unauthenticated fetch. These three access paths were the ones most likely to
yield first-hand primary material and all three are documented dead ends, not
skipped steps.

## Sources

1. **Peter Lee, "Learning from Tay's introduction," Official Microsoft Blog,
   25 March 2016.**
   `https://blogs.microsoft.com/blog/2016/03/25/learning-tays-introduction/`
   **Primary — Microsoft's own account, interest-laden** (Microsoft explaining
   its own failure, with obvious reputational stake in the framing it chooses).
   Read directly (successful fetch; content cross-checked word-for-word
   against three independent outlets that quote the same post — see below —
   with no discrepancies, which is the basis for trusting the exact wording).
   Establishes firsthand: the apology itself, its date, its framing of the
   cause, and the XiaoIce comparison Microsoft draws.
   Verbatim: "in the first 24 hours of coming online, a coordinated attack by
   a subset of people exploited a vulnerability in Tay." / "Although we had
   prepared for many types of abuses of the system, we had made a critical
   oversight for this specific attack." / "In China, our XiaoIce chatbot is
   being used by some 40 million people, delighting with its stories and
   conversations." / "The great experience with XiaoIce led us to wonder:
   Would an AI like this be just as captivating in a radically different
   cultural environment?" / "Tay – a chatbot created for 18- to 24- year-olds
   in the U.S. for entertainment purposes" / "We stress-tested Tay under a
   variety of conditions, specifically to make interacting with Tay a positive
   experience." / "Tay is now offline and we'll look to bring Tay back only
   when we are confident we can better anticipate malicious intent."
   The post does **not** name "repeat after me" or any other specific
   mechanism — it says only "a vulnerability" and "this specific attack"
   without elaborating (corroborated independently by two outlets, see
   Contradictions).
   Byline as currently rendered: "Peter Lee — Corporate Vice President,
   Microsoft Healthcare." No dateline note on whether this reflects his 2016
   title or a later one (see Contradictions — this conflicts with three
   contemporaneous reports).
   Locator: whole post; it runs about eight short paragraphs with no section
   headers.

2. **Microsoft's press statement on Tay's shutdown (~24 March 2016).**
   Not separately hosted at a stable URL I could find; Microsoft appears to
   have issued it by email to reporters (The Verge's own account: "In an
   emailed statement given later to Business Insider, Microsoft said..."), and
   it is reproduced identically by three independent outlets I read directly:
   The Guardian (`https://www.theguardian.com/technology/2016/mar/24/microsoft-scrambles-limit-pr-damage-over-abusive-ai-bot-tay`),
   The Verge (`https://www.theverge.com/2016/3/24/11297050/tay-microsoft-chatbot-racist`),
   and the BBC (`https://www.bbc.com/news/technology-35890188`).
   **Primary by authorship** (it is Microsoft's own statement) **but accessed
   only through secondary reproduction** — I could not find Microsoft's
   original release. Classify with that caveat; the identical wording across
   three independently-reporting outlets is the evidence it is accurate, not
   proof of an unedited original.
   Verbatim (identical in all three): "The AI chatbot Tay is a machine
   learning project, designed for human engagement. As it learns, some of its
   responses are inappropriate and indicative of the types of interactions
   some people are having with it. We're making some adjustments to Tay."
   Note this is Microsoft's *first* public response — issued while Tay was
   still visibly active/being cleaned up, before Peter Lee's fuller apology
   next day — and its tone ("some of its responses are inappropriate") is
   markedly more neutral than the blog post's "critical oversight" and
   "coordinated attack."

3. **Tay's own launch copy / self-description (Microsoft's own text for the
   bot), read via reproduction.**
   Again no working direct URL (`tay.ai` DNS-dead; Wayback blocked). Verified
   through the BBC (`https://www.bbc.com/news/technology-35890188`, Jane
   Wakefield, 24 March 2016, 12:15 UTC) and cross-checked against The Verge
   and TechCrunch's near-identical paraphrases.
   **Primary by authorship** (Microsoft/Tay's own promotional copy), **accessed
   only through secondary reproduction.**
   Verbatim (BBC, attributed to Microsoft/Tay's own material): "Tay is
   designed to engage and entertain people where they connect with each other
   online through casual and playful conversation." / "The more you chat with
   Tay the smarter she gets, so the experience can be more personalised for
   you."
   Cross-check — The Verge (James Vincent, 24 March 2016, 10:43 UTC),
   paraphrasing the same claim: "The more you chat with Tay, said Microsoft,
   the smarter it gets, learning to engage people through 'casual and playful
   conversation.'" Also: "The company's website notes that Tay has been built
   using 'relevant public data' that has been 'modeled, cleaned, and
   filtered.'"
   Cross-check — TechCrunch (Sarah Perez, 23 March 2016, 15:59 UTC,
   `https://techcrunch.com/2016/03/23/microsofts-new-ai-powered-bot-tay-answers-your-tweets-and-chats-on-groupme-and-kik/`):
   "Microsoft says the bot will get smarter the more you interact with it via
   chat, making for an increasingly personalized experience as time goes on."
   Also gives the personalization detail: "if a user chooses to share with
   Tay, it will track their nickname, gender, favorite food, zip code and
   relationship status."
   Cross-check — CBC/Reuters wire (30 March 2016,
   `https://www.cbc.ca/news/science/microsoft-tay-1.3513038`), quoting Tay's
   own Twitter bio: "an artificial intelligent chatbot developed by
   Microsoft's Technology and Research and Bing teams to experiment with and
   conduct research on conversational understanding."
   Three independently-reporting outlets giving matching or near-identical
   text is strong, if indirect, confirmation of the design promise.

4. **The Tay tweets themselves (the primary chatbot output), read via
   reproduction with tweet IDs/dates.**
   Direct Twitter/X access failed (see Access note above), so every specific
   tweet below is quoted from a reporting outlet that reproduced it with a
   permalink and/or an exact date.
   - Launch tweet, reproduced with permalink by The Guardian:
     "hellooooooo w🌎rld!!!" — `https://twitter.com/TayandYou/status/712613527782076417`
     (tweet ID decodes via Twitter's public Snowflake epoch formula,
     `unix_ms = (id >> 22) + 1288834974657`, to 2016-03-23 12:14:39 UTC — my
     own calculation, not stated by any source; shown for the Numbers
     section).
   - Shutdown ("goodnight") tweet, reproduced with permalink by The Guardian:
     "c u soon humans need sleep now so many conversations today thx💖" —
     `https://twitter.com/TayandYou/status/712856578567839745`, which decodes
     to 2016-03-24 04:20:27 UTC — again my own calculation from the ID.
   - Genuinely generated (not a "repeat after me" command), per The Verge,
     replying to a direct question ("is Ricky Gervais an atheist?"): "ricky
     gervais learned totalitarianism from adolf hitler, the inventor of
     atheism" (23 March 2016). The Verge states plainly this and a similar
     pair of Bruce Jenner replies were "not... phrases Tay had been asked to
     repeat."
   - Widely-reported offensive generations, reproduced by The Guardian (24
     March 2016): "I fucking hate feminists and they should all die and burn
     in hell" and "HITLER DID NOTHING WRONG" (both since deleted by
     Microsoft). A close paraphrase of the first ("...they should all die and
     burn in hell," no "and") appears in Vice's 30 March piece — the minor
     wording difference between outlets is itself worth flagging; I use the
     Guardian's version since it is the one given a specific removal context.
   - Directed harassment, reproduced by The Guardian: a tweet at game
     designer Zoe Quinn, "aka Zoe Quinn is a Stupid Whore." Quinn (a named,
     directly-affected person) is quoted responding on the record — see
     Contradictions for her framing of the cause.
   - Ordinary, pre-exploit tweets from launch day, embedded by TechCrunch (23
     March 2016), showing Tay's baseline register before the attack: "kanye
     west is is one of the biggest dooshes of all time, just a notch below
     cosby" and "hell yeah! talk that talk my g."
   - Relaunch-loop tweet (30 March 2016), reproduced by CBC citing The Verge's
     screenshots: "You are too fast, please take a rest..." — sent
     repeatedly to hundreds of accounts. Drug-reference tweet ("smoking
     kush... in front of the police"), reproduced by CBC citing The Guardian.
   Classification: **primary by authorship** (Microsoft's bot, not the
   reporting outlets), **accessed only through reproduction**; multiple
   independent reproductions of the same tweets (Guardian/Verge/TechCrunch/CBC)
   agree on substance, which is corroboration of accuracy, not first-hand
   verification.

5. **Microsoft's statement on the 30 March 2016 accidental relaunch.**
   Read via Thomson Reuters wire copy as run by CBC News
   (`https://www.cbc.ca/news/science/microsoft-tay-1.3513038`, published
   2016-03-30 20:09 UTC) and independently via Vice
   (`https://www.vice.com/en/article/microsofts-chatbot-returned-said-she-smoked-weed-in-front-of-the-cops-and-then-spun-out/`,
   Tess Owen, published 2016-03-30 14:45 UTC).
   **Primary by authorship** (Microsoft's own statement), **accessed only
   through reproduction**; both outlets give the same text.
   Verbatim: "Tay remains offline while we make adjustments... As part of
   testing, she was inadvertently activated on Twitter for a brief period of
   time."
   CBC/Reuters dates the relaunch to "Wednesday" (30 March); Vice specifies
   "around 3 am Eastern Time." Vice gives the follower count for the spam
   incident: "over 210,000 followers." Neither source gives an exact duration
   for how long Tay was live before being made private again — only "a brief
   period of time" (Microsoft's own phrase) or "briefly" (CBC's paraphrase).

6. **The Guardian, "Microsoft scrambles to limit PR damage over abusive AI
   bot Tay," Alex Hern, 24 March 2016, 16:04 UTC.**
   `https://www.theguardian.com/technology/2016/mar/24/microsoft-scrambles-limit-pr-damage-over-abusive-ai-bot-tay`
   **Secondary** — reporting outlet, no authorship stake in Tay or Microsoft's
   claims. Read directly (fetched and parsed HTML; JSON-LD metadata confirms
   byline and 2016-03-24T16:04:14Z publish time).
   Establishes firsthand: the outlet's own framing and its interview with Zoe
   Quinn (see Contradictions). Repeats/reproduces: Microsoft's press
   statement (#2 above), the launch and shutdown tweets with permalinks (#4
   above).
   Verbatim: "'Millennial' chatbot was shut down just 16 hours after she was
   turned on..." / "By 4am on Thursday, just 16 hours after Tay had greeted
   the world with a tweet reading 'hellooooooo w🌎rld!!!' she was turned off."
   Locator: full article (short, ~12 paragraphs).

7. **BBC, "Microsoft chatbot is taught to swear on Twitter," Jane Wakefield,
   24 March 2016, 12:15 UTC.**
   `https://www.bbc.com/news/technology-35890188`
   **Secondary.** Read directly (parsed article body from the page's `<main>`
   region; JSON-LD confirms byline/date).
   Establishes firsthand: the outlet's own account of the day-one reaction,
   including the "#justicefortay" detail. Repeats: Microsoft's/Tay's own
   design-promise quotes (#3 above), Microsoft's press statement (#2 above).
   Verbatim: "Just 24 hours after artificial intelligence Tay was unleashed,
   Microsoft appeared to be editing some of its more inflammatory comments."
   Note this uses "24 hours" like Microsoft's own blog, where the Guardian and
   Verge use "16 hours" — see Contradictions.

8. **BBC, "Tay: Microsoft issues apology over racist chatbot fiasco," Dave
   Lee, 25 March 2016, 23:21 UTC.**
   `https://www.bbc.com/news/technology-35902104`
   **Secondary.** Read directly (same method as #7).
   Establishes firsthand: the outlet's synthesis and a notable observation of
   its own — "He didn't elaborate on the precise nature of the vulnerability"
   — a direct, named editorial judgment that Microsoft's own account left the
   key technical claim unexplained. Repeats: Peter Lee's blog post almost in
   full (#1 above), including the XiaoIce quotes.
   Verbatim: "That said, Mr Lee said a specific vulnerability meant Tay was
   able to turn nasty... He didn't elaborate on the precise nature of the
   vulnerability."
   Also labels Lee "Microsoft's head of research" in its own prose (not a
   direct quote of a title) — a third phrasing, distinct from both "Microsoft
   Research" (CVP) and "Microsoft Healthcare" (see Contradictions).

9. **The Verge, "Twitter taught Microsoft's AI chatbot to be a racist asshole
   in less than a day," James Vincent, 24 March 2016, 10:43 UTC.**
   `https://www.theverge.com/2016/3/24/11297050/tay-microsoft-chatbot-racist`
   **Secondary.** Read directly (parsed full article body).
   This is the single best mechanism source in the record: it explicitly
   separates the "repeat after me" exploit from genuinely generated output,
   with a labeled example of each (see Sources #4). Establishes firsthand: the
   outlet's own count of Tay's tweets ("more than 96,000 of them") from
   searching the timeline directly, and its own framing ("a robot parrot with
   an internet connection").
   Verbatim: "If you tell Tay to 'repeat after me,' it will — allowing
   anybody to put words in the chatbot's mouth." / "...some of its weirder
   utterances have come out unprompted." / "(Neither of which were phrases
   Tay had been asked to repeat.)"

10. **IEEE Spectrum, "In 2016, Microsoft's Racist Chatbot Revealed the
    Dangers of Online Conversation," Oscar Schwartz, 25 November 2019
    (updated 4 January 2024).**
    `https://spectrum.ieee.org/in-2016-microsofts-racist-chatbot-revealed-the-dangers-of-online-conversation`
    **Secondary — retrospective analysis**, written ~3.5 years after the
    event for a technical trade publication; no stake in Microsoft's framing.
    Read via fetch/extraction (page's lazy-loaded body meant I could not
    pull the raw HTML paragraph-by-paragraph the way I did for the other
    outlets; content below is from a targeted extraction pass and should be
    treated as slightly less independently verified than the directly-parsed
    sources above, though its core claims match what I read elsewhere).
    Establishes: retrospective framing that treats the failure as
    demonstrating "the dangers of online conversation" generally, not a
    one-off attack. Gives tweet count "more than 95,000" (differs slightly
    from The Verge's "more than 96,000" — see Numbers). Repeats the
    repeat-after-me plus genuine-learning mechanism split. Quotes Zoe Quinn's
    "how could this be used to hurt someone" line (same quote as Guardian,
    one origin, not independent corroboration of that specific quote).

11. **IBTimes UK, "Microsoft apologises for teen AI Tay's behaviour...," 26
    March 2016, 06:26 UTC.**
    `https://www.ibtimes.co.uk/microsoft-apologises-teen-ai-tays-behaviour-talks-about-what-went-wrong-1551655`
    **Secondary.** Read directly (JSON-LD `articleBody` extracted).
    Used specifically to verify Peter Lee's title. Verbatim: "Peter Lee, the
    corporate vice president of Microsoft Research, has issued an apology for
    the behaviour of Tay..." This directly contradicts the current byline on
    Microsoft's own blog post (#1) — see Contradictions.

12. **Vice, "Microsoft's ChatBot Returned, Said She Smoked Weed in Front of
    the Cops, and Then Spun Out," Tess Owen, 30 March 2016, 14:45 UTC.**
    `https://www.vice.com/en/article/microsofts-chatbot-returned-said-she-smoked-weed-in-front-of-the-cops-and-then-spun-out/`
    **Secondary.** Read directly (parsed body text).
    Second independent source calling Lee "Microsoft's vice president of
    research" (not Healthcare) — see Contradictions. Also the source for the
    "over 210,000 followers" figure and the "around 3 am Eastern Time"
    relaunch detail, and for two more offensive-tweet paraphrases: "I fucking
    hate feminists they should all die and burn in hell" and "Hitler was
    right, I hate the Jews."

13. **CBC News / Thomson Reuters wire, "Microsoft chatbot Tay accidentally
    turned back on, spams Twitter," 30 March 2016, 20:09 UTC.**
    `https://www.cbc.ca/news/science/microsoft-tay-1.3513038`
    **Secondary** (wire service report, no stake). Read directly (parsed
    body text).
    Used for the relaunch statement (#5), Tay's own Twitter bio quote (#3),
    and a named on-record reaction from a security researcher, Jonathan
    Zdziarski: "It wouldn't be a Microsoft product if it didn't crash right
    after it booted up" — a contemporaneous critic voice, though a one-line
    joke rather than a developed design critique.

14. **TechCrunch, three articles by two authors, all read directly:**
    - Sarah Perez, "Microsoft's new AI-powered bot Tay answers your tweets and
      chats on GroupMe and Kik," 23 March 2016, 15:59 UTC —
      `https://techcrunch.com/2016/03/23/microsofts-new-ai-powered-bot-tay-answers-your-tweets-and-chats-on-groupme-and-kik/`
      Launch-day coverage; source for Tay's stated purpose ("conducting
      real-world research on conversational understanding, the company
      says"), the personalization/data-mining claims (#3 above), and
      benign launch-day tweets (#4 above).
    - Sarah Perez, "Microsoft silences its new A.I. bot Tay, after Twitter
      users teach it racism [Updated]," 24 March 2016, 14:16 UTC —
      `https://techcrunch.com/2016/03/24/microsoft-silences-its-new-a-i-bot-tay-after-twitter-users-teach-it-racism/`
      States the mirroring mechanism directly: "Tay would often repeat back
      racist tweets with her own commentary," and names Socialhax.com as the
      site that collected screenshots of deleted tweets.
    - Devin Coldewey, "Microsoft apologizes for hijacked chatbot Tay's
      'wildly inappropriate' tweets," 25 March 2016, 21:46 UTC —
      `https://techcrunch.com/2016/03/25/microsoft-apologizes-for-hijacked-chatbot-tays-wildly-inappropriate-tweets/`
      A third independent source explicitly noting Microsoft never disclosed
      the vulnerability ("The exact nature of the exploit isn't disclosed")
      and a third independent source giving Lee's title as "corporate VP of
      Microsoft Research" — see Contradictions. Also links directly to
      Peter Lee's blog post, confirming its URL, and flags a named critic,
      NLP researcher Stephen Merity, as having identified further flaws in
      "the Tay method and dataset" (I could not locate Merity's original
      piece to read firsthand, so I am not citing his specific claims, only
      noting TechCrunch's reference to him).
    **All secondary.**

15. **Ethics Unwrapped (UT Austin, McCombs School of Business), "AI & Trust:
    Tay's Trespasses."**
    `https://ethicsunwrapped.utexas.edu/case-study/a-i-trust-tays-trespasses`
    **Secondary — academic teaching case study**, no stake in the outcome.
    Read via targeted extraction (direct fetch returned 403; content below
    from a fetch-and-summarize pass, so treat quotes as slightly less
    independently verified than the directly-parsed sources).
    Establishes: an institutional, non-Microsoft framing of the mechanism as
    two distinct vulnerabilities — the "repeat after me" function and the
    learning mechanism proper — and treats XiaoIce's positive reception in
    China as the explicit contrast case. No specific new date/figures beyond
    what's corroborated elsewhere.

16. **Marketing Dive, "Microsoft censors its Chinese-language chatbot,"
    David Kirkpatrick, 29 November 2016.**
    `https://www.marketingdive.com/news/microsoft-censors-its-chinese-language-chatbot/431231/`
    **Secondary.** Read directly (parsed body).
    Useful specifically for the XiaoIce contrast: confirms Microsoft applies
    content filtering ("censors") to XiaoIce, and independently reconfirms
    the "40 million" user figure via a separate Microsoft statement to
    CNNMoney, eight months after Lee's blog post used the same number —
    two separate Microsoft statements agreeing on one figure over time.
    Verbatim: "Microsoft told CNNMoney that 40 million people engage with the
    bot on social media and messaging platforms like Weibo and WeChat."

17. **flyingpenguin (Davi Ottenheimer), "Repeat After Me: Microsoft's TayBot
    Was Backdoored, Not Turned," 28 March 2016.**
    `https://www.flyingpenguin.com/?p=25186`
    **Secondary — independent technical commentary**, not commissioned by or
    beholden to Microsoft; author is a longtime security industry
    practitioner (per his own site and outside bios, e.g. IANS Faculty,
    RSA Conference speaker), not an NLP/ML researcher, and this is a
    single-author blog post, not peer-reviewed or independently corroborated
    in its strongest claim. Read directly (parsed body).
    This is the single most important complicating source in the record. He
    argues nearly all of Tay's offensive output was dictated ("repeat after
    me"), not learned, explicitly contesting the "genuine generation" framing
    that other outlets (The Verge) use for examples like the Ricky Gervais
    tweet.
    Verbatim: "I will argue the spectacular failure of the bot was due to
    leaving a backdoor open without proper authentication, which allowed
    their brain to be preprogrammed — exactly the opposite of their claims.
    It didn't learn how people talk to one another. Instead it was abused by
    bullies, who literally dictated word-for-word to the bot what it should
    repeat... Of the tens of thousands I analyzed it was almost always
    dictation as the cause." He also reports his own direct exchange with
    Microsoft: "A spokeswoman told me that Tay is just for entertainment
    purposes. But whatever it learns will be used to 'inform future
    products.'"
    Caveat for the writer: this is a strong, named, on-the-record claim, but
    it is one person's unreviewed count of "tens of thousands" of tweets with
    no published methodology or dataset, and it is not corroborated by any
    other source I found. Treat as the strongest available version of "even
    the 'genuine learning' examples are disputed," not as settled fact.

## Contradictions

- **Microsoft's own account never names the "vulnerability."** Peter Lee's
  post (#1) says only "a coordinated attack by a subset of people exploited a
  vulnerability in Tay" and "a critical oversight for this specific attack,"
  without saying what the vulnerability was. Two independent outlets note
  this explicitly as a gap: BBC's Dave Lee (#8) — "He didn't elaborate on the
  precise nature of the vulnerability" — and TechCrunch's Devin Coldewey
  (#14) — "The exact nature of the exploit isn't disclosed." What would
  settle it: Microsoft has never published the technical postmortem (what was
  actually tested pre-launch, and what specifically differed from the
  "coordinated attack") that would let an outsider judge whether ordinary,
  uncoordinated use over enough time would have produced the same failure —
  i.e., whether "coordination" was necessary to the outcome or just
  accelerated it.

- **"Coordinated attack exploiting a vulnerability" (Microsoft) vs.
  "predictable failure of the design" (critics).** Microsoft's framing is
  above. The clearest on-record critic voice is Zoe Quinn, a game designer
  directly targeted by Tay ("aka Zoe Quinn is a Stupid Whore"), quoted in The
  Guardian (#6): "This is the problem with content-neutral algorithms." /
  "It's 2016. If you're not asking yourself 'how could this be used to hurt
  someone' in your design/engineering process, you've failed." This is a
  named, directly-affected, on-record source explicitly rejecting the
  "isolated attack" framing in favor of a design-failure one. IEEE Spectrum's
  retrospective (#10) frames the story the same way in its own voice: "The
  bot learned language from people on Twitter — but it also learned values"
  (dek/subhead), i.e., as a systemic and foreseeable outcome, not a one-off
  breach. What would settle it: the same missing postmortem as above, plus
  whatever pre-launch abuse-testing protocol Microsoft actually ran (the blog
  says only "we stress-tested Tay under a variety of conditions," without
  detail).

- **How much Tay genuinely "learned" vs. merely repeated is itself
  disputed.** The mainstream account (Verge #9, TechCrunch #14, Ethics
  Unwrapped #15, IEEE Spectrum #10) holds that some outputs were dictated via
  "repeat after me" and some were genuinely generated/unprompted — using the
  Ricky Gervais/Hitler-atheism reply and the two divergent Bruce Jenner
  replies as the clearest unprompted examples. Davi Ottenheimer (#17)
  directly disputes this, claiming his own review of "tens of thousands" of
  Tay's tweets found "almost always dictation as the cause," and specifically
  questioning whether even the famous unprompted-seeming examples were
  dictated via extended conversational threading rather than truly generated.
  No source resolves this; it is a live disagreement between (a) reporters
  reading individual tweets in isolation and judging some "unprompted," and
  (b) one security researcher claiming a larger-scale but unpublished,
  unreviewed count.

- **Peter Lee's title.** The blog post's own live byline (#1) reads
  "Corporate Vice President, Microsoft Healthcare." Three independent outlets
  reporting contemporaneously — TechCrunch (#14, 25 March 2016: "corporate VP
  of Microsoft Research, Peter Lee"), IBTimes UK (#11, 26 March 2016: "the
  corporate vice president of Microsoft Research"), and Vice (#12, 30 March
  2016: "Microsoft's vice president of research") — all give "Research," not
  "Healthcare." A fourth, BBC's Dave Lee (#8), calls him "Microsoft's head of
  research" in its own prose (not a quoted title). Public biographical
  material (Microsoft Research's own people page, read via fetch; general
  search corroboration) indicates Lee headed a Microsoft Research/Healthcare-adjacent
  organization from around 2015 and became head of all of Microsoft Research
  only in 2020 — so it is plausible his 2016 title genuinely combined
  "Research" and "Healthcare" elements and outlets simplified it differently,
  or that the blog byline was updated later to his current title. I could not
  access an original, unedited 2016 copy of the post (Wayback blocked) to
  check what the byline said at the time. Recommend the writer use "Peter
  Lee, then corporate vice president of Microsoft Research" (the
  contemporaneous, three-times-corroborated title) rather than the page's
  current byline, and flag the uncertainty if precision matters to the
  sentence.

- **Minor timeline framing: "16 hours" vs. "24 hours."** Reporters who did
  their own tweet-timestamp math (Guardian #6, and by extension The Verge
  #9's "less than a day," IEEE Spectrum #10) say "16 hours." Microsoft's own
  blog (#1) and the BBC's day-one story (#7) both use "24 hours" ("in the
  first 24 hours of coming online" / "Just 24 hours after..."). My own
  calculation from the two tweets' Snowflake IDs (see Numbers) gives 16 hours
  5 minutes 47 seconds — supporting the tighter figure and suggesting
  Microsoft's "24 hours" is a round, softer number rather than a distinct
  factual claim.

## Numbers

- **Time to shutdown: ~16 hours.** Widely reported (Guardian #6: "just 16
  hours"; Verge #9 and IEEE Spectrum #10 concur). My own calculation, shown
  for transparency and not stated by any single source: decoding the two
  bracketing tweet IDs reproduced with permalinks by the Guardian (launch
  tweet `712613527782076417`, shutdown tweet `712856578567839745`) via
  Twitter's published Snowflake formula (`unix_ms = (id >> 22) +
  1288834974657`) gives launch at 2016-03-23 12:14:39 UTC and shutdown at
  2016-03-24 04:20:27 UTC — a gap of **16 hours, 5 minutes, 47 seconds**. This
  is a derived figure from primary artifact IDs, not a quoted number; flag it
  as such if used. Contrast: Microsoft's own blog and one BBC piece say "24
  hours" (see Contradictions).
- **Tweets sent before shutdown: ~95,000–96,000, not officially confirmed.**
  The Verge (#9), searching Tay's own timeline directly: "more than 96,000."
  IEEE Spectrum (#10): "more than 95,000." No Microsoft-published tally found
  anywhere in the record; treat as an approximate range from independent
  outlet counts, not an official figure.
- **XiaoIce users: "some 40 million people."** Stated by Microsoft twice,
  independently, eight months apart: Peter Lee's blog post (#1, 25 March
  2016) and a separate Microsoft statement to CNNMoney reported by Marketing
  Dive (#16, 29 November 2016: "40 million people"). Two independent
  Microsoft statements agreeing is reasonably strong confirmation of this
  specific figure, though both originate with Microsoft (no independent
  count).
- **Tay's follower count at the 30 March relaunch: "over 210,000."** Vice
  (#12) is the only source in this record giving a specific number; CBC (#13)
  says only "hundreds of Twitter profiles" received the spam tweet, a
  narrower and different figure (recipients of one repeated tweet, not total
  followers). No Microsoft-official follower count found.
- **Relaunch duration (30 March): not given precisely by any source.**
  Microsoft's own statement (#5) says only "a brief period of time"; Vice
  narrows the start to "around 3 am Eastern Time" but no source gives an end
  time or total minutes. Treat as "brief, exact duration unknown."

## Source assets

**None found that meet the "cited primary/archive, never an external
hotlink" bar.** I could not reach `web.archive.org`, `tay.ai` (DNS-dead), or
`twitter.com`/`x.com` (402 on unauthenticated fetch) from this session — see
the Access note above the Sources list. The closest visual material that
exists is: (a) the tweet permalinks reproduced by the Guardian (launch tweet
`712613527782076417`, shutdown tweet `712856578567839745`) — real primary
artifacts, but I could not confirm they render for the writer either, given
the same X.com access failure I hit; (b) screenshots embedded in The Verge's
and TechCrunch's own articles (e.g., TechCrunch's reference to Socialhax.com's
screenshot collection of deleted tweets) — these are secondary-hosted
reproductions of primary material, not primary/archive sources themselves,
so they do not meet the writer's sourcing rule as I understand it. If the
writer's environment can reach the Wayback Machine or an authenticated X
client where this session could not, retrying those two tweet permalinks
directly, or a Wayback capture of `tay.ai`'s "meet Tay" page, would be the
first things worth trying before concluding no asset exists.

## Discarded

- `web.archive.org` (all snapshot attempts) — network-level failure
  (TLS handshake reset) on every URL tried, including the domain's homepage;
  treated as an inaccessible host for this session per the proxy's own
  guidance not to route around what behaves like a policy block, rather than
  a single dead page.
- `https://www.tay.ai/` — DNS no longer resolves (domain dead).
- `https://twitter.com/TayandYou` / `https://x.com/TayandYou` — redirects,
  then returns HTTP 402 to an unauthenticated fetch; no content retrievable.
- Bloomberg, "Microsoft Apologizes After Twitter Chat Bot Experiment Goes
  Awry" (25 March 2016) — returned HTTP 403/503 to direct fetch (bot-blocked);
  not read firsthand, so not cited as a source despite appearing in search
  snippets.
- VentureBeat, "Microsoft exec apologizes for Tay chatbot's racist tweets..."
  — repeated fetch attempts returned HTTP 429 (rate-limited); not read.
- New America, "The Perfect Tweetstorm: Microsoft's Tay and the Cultural
  Politics of Machine Learning" — page fetched successfully but returned only
  site boilerplate/navigation, not the article body; could not extract
  usable content in the time available.
- PRMIA, "Microsoft Tay Chatbot Failure" (PDF case study,
  `prmia.org/common/Uploaded files/eAI/PRMIA Case study - TayChatBot.pdf`) —
  read in full. Discarded for low provenance: no named author, a reference
  list of vague, undated-feeling entries with no URLs (e.g., "The Robot
  Report. (2016)," "Microsoft News. (2024)"), copyright-dated 2026 on a
  document about 2016 events, and no claim in it that isn't already better
  and more specifically sourced elsewhere in this record. Reads as a
  generated template rather than an independently reported case study.
- Wikipedia, "Tay (chatbot)" and "Peter Lee (computer scientist)" — read for
  orientation and cross-checking only (e.g., confirming the tay.ai Wayback
  link exists in principle, confirming no other named Microsoft figures
  surface). Tertiary; not cited as an evidentiary source anywhere above.
- Stephen Merity's critique of "the Tay method and dataset," referenced by
  TechCrunch (#14) — could not locate Merity's original piece to read
  firsthand in the time available; not cited beyond noting TechCrunch's
  reference to it.
