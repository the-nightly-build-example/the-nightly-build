# Evidence — When AI Breaks / Gemini image generation

The record is solid on the sequence, the dates, the named actors, and Google's own
stated mechanism at the level Google chose to disclose it. Prabhakar Raghavan's
23 Feb 2024 blog post, Google's 22 Feb pause statement, and the Pichai memo (quoted
verbatim by Semafor and confirmed by Google) are all directly readable and consistent
with one another and with independent reporting. Two Google executives (Demis
Hassabis and Sergey Brin) gave on-record, separately-sourced accounts that corroborate
Raghavan's without contradicting it. Two reputable outlets (The Verge, CNN)
independently generated their own Gemini outputs before the feature was paused,
which is the strongest evidence that the underlying behavior was real and not purely
a product of edited or cherry-picked social media screenshots.

The record is thin, and requires a clear firewall in the article, on one point: the
*exact technical mechanism*. Google's own words say "tuning" produced a diversity
bias that applied indiscriminately, and that the model separately became "over-
cautious." Google never confirmed, in anything I read, that this specific tuning took
the architectural form of an invisible instruction appended to the user's prompt
before it reached the image model (as opposed to, e.g., fine-tuning weights on
diversity-augmented training data, or a classifier-driven re-prompting step). The
"hidden prompt-augmentation" framing is a reasonable technical reconstruction —
supported by a directly comparable, Google-independent precedent that OpenAI
documented in writing for DALL-E 3 (its system card explicitly describes ChatGPT
rewriting user prompts to insert diversity language before they reach the image
model) — but for Gemini specifically it rests on unverified claims that people
extracted "system instructions" from the chatbot, which no primary Google document
confirms. The article should say what Google confirmed, say what the OpenAI
precedent establishes about how this class of system works in general, and mark the
leap between them as inference, not fact.

Also thin: which specific viral examples (the Founding Fathers portrait, the "diverse
Vikings," the specific pope screenshot passed around by @IMAO_) were ever reproduced
by a newsroom under controlled conditions. Google's own statements never name a
specific viral image. The Verge and CNN reproduced the same *pattern* — non-white
results for prompts about historically white subjects, and for CNN, a refusal
pattern's near-miss — with their own prompts, which is real corroboration of the
underlying behavior, but is not the same as confirming that every specific screenshot
that went viral was unedited and unaltered.

## Sources

1. **Prabhakar Raghavan, "Gemini image generation got it wrong. We'll do better,"**
   Google Keyword blog, published 23 Feb 2024.
   URL: https://blog.google/products/gemini/gemini-image-generation-issue/ (confirmed
   resolving; fetched in full).
   Classification: **Primary.** Google's own account of its own product failure,
   written and published under the byline of the executive responsible, on Google's
   own platform.
   Byline as printed on the post: "Prabhakar Raghavan / Senior Vice President." (The
   post itself does not print a fuller title; see source 12 for the fuller title as
   given elsewhere.)
   Establishes firsthand: the launch date ("three weeks ago" from 23 Feb, i.e. circa
   1–2 Feb 2024) of image generation of people in the Gemini app (built on Imagen 2);
   that "some of the images generated are inaccurate or even offensive"; that Google
   "temporarily paused image generation of people in Gemini"; the two-part causal
   account.
   Verbatim, load-bearing passages:
   - "It's clear that this feature missed the mark. Some of the images generated are
     inaccurate or even offensive. We're grateful for users' feedback and are sorry
     the feature didn't work well."
   - "When we built this feature in Gemini, we tuned it to ensure it doesn't fall
     into some of the traps we've seen in the past with image generation technology —
     such as creating violent or sexually explicit images, or depictions of real
     people. And because our users come from all over the world, we want it to work
     well for everyone. If you ask for a picture of football players, or someone
     walking a dog, you may want to receive a range of people. You probably don't
     just want to only receive images of people of just one type of ethnicity (or any
     other characteristic)."
   - "However, if you prompt Gemini for images of a specific type of person — such as
     'a Black teacher in a classroom,' or 'a white veterinarian with a dog' — or
     people in particular cultural or historical contexts, you should absolutely get
     a response that accurately reflects what you ask for."
   - "So what went wrong? In short, two things. First, our tuning to ensure that
     Gemini showed a range of people failed to account for cases that should clearly
     not show a range. And second, over time, the model became way more cautious
     than we intended and refused to answer certain prompts entirely — wrongly
     interpreting some very anodyne prompts as sensitive."
   - "These two things led the model to overcompensate in some cases, and be
     over-conservative in others, leading to images that were embarrassing and
     wrong."
   - "So we turned the image generation of people off and will work to improve it
     significantly before turning it back on. This process will include extensive
     testing."
   What it does NOT say (important for the article's precision): it never names a
   specific viral example (no "Founding Fathers," no "1943 German soldier," no
   "Pope"); its own illustrative examples are hypothetical ("a Black teacher in a
   classroom," "a white veterinarian with a dog"). It also never describes the
   causal mechanism at the architecture level — it says "we tuned it," not how.
   Locator: full text is short (roughly 550 words); the passages above are the
   entirety of the causal explanation, found under the "What happened" and
   "Next steps and lessons learned" headers.

2. **Google Communications (@Google_Comms), post on X, 22 Feb 2024.**
   Not independently re-fetchable as a live tweet through this tool chain, but the
   exact wording is quoted identically, with attribution to the "Google
   Communications" account, by 9to5Google (Ben Schoon, 22 Feb 2024, 6:50am PT,
   https://9to5google.com/2024/02/22/google-gemini-ai-image-generation-people/,
   confirmed resolving) and consistent with wording reproduced by The Verge and CNN
   (below).
   Classification: **Primary** (it is Google's own statement; multiple outlets
   independently transcribed the identical text, which functions as verification of
   wording even though the tweet itself was not directly re-fetched).
   Verbatim: "We're already working to address recent issues with Gemini's image
   generation feature. While we do this, we're going to pause the image generation
   of people and will re-release an improved version soon."
   This is the operative pause announcement, dated 22 Feb 2024 — one day before
   Raghavan's blog post (23 Feb 2024).
   In-product message shown to users after the pause (also quoted identically across
   sources): "We are working to improve Gemini's ability to generate images of
   people. We expect this feature to return soon and will notify you in release
   updates when it does."

3. **Google's earlier statement, X post, 21 Feb 2024** (the day before the pause),
   quoted by CNN (source 6): "Gemini's AI image generation does generate a wide
   range of people. And that's generally a good thing because people around the
   world use it. But it's missing the mark here."
   Classification: **Primary** (Google's own words, reproduced by CNN with a byline
   reporter present). This establishes that Google's first public response (21 Feb)
   defended the diversity behavior as generally correct, one day before escalating to
   a full pause (22 Feb) and two days before Raghavan's fuller explanation (23 Feb) —
   a real evolution in Google's posture worth keeping in the timeline.

4. **Jack Krawczyk, Google's product lead for Gemini Experiences, post on X, 21 Feb
   2024**, quoted by CNN: Krawczyk "said in a post on Wednesday that Google
   intentionally designs 'image generation capabilities to reflect our global user
   base' and that the company 'will continue to do this for open ended prompts
   (images of a person walking a dog are universal!).'"
   Classification: **Primary** (Google spokesperson's own words). Title varies
   slightly by outlet: CNN calls him "Google's lead product director for Gemini";
   other outlets (not independently confirmed to primary-source level here) have
   called him "senior director of product management for Gemini Experiences." Use
   CNN's phrasing if a title is needed, or the plainer "Google's product lead for
   Gemini" and avoid a precise title neither outlet fully agrees on.

5. **Reed Albergotti, "Google CEO Sundar Pichai calls AI tool's controversial
   responses 'completely unacceptable,'" Semafor,** published/updated 27 Feb 2024,
   11:26pm EST.
   URL:
   https://www.semafor.com/article/02/27/2024/google-ceo-sundar-pichai-calls-ai-tools-responses-completely-unacceptable
   (confirmed resolving; fetched in full).
   Classification: The article's framing/reporting is **secondary**; the reproduced
   memo text is **primary** — Semafor states "Google confirmed the memo, and the
   full note from Pichai is below," and reproduces it in full. Treat the quoted memo
   as the primary artifact, per the brief's instruction.
   Full verbatim memo text (as printed by Semafor, confirmed by Google per the
   article):
   > "I want to address the recent issues with problematic text and image responses
   > in the Gemini app (formerly Bard). I know that some of its responses have
   > offended our users and shown bias – to be clear, that's completely unacceptable
   > and we got it wrong.
   >
   > Our teams have been working around the clock to address these issues. We're
   > already seeing a substantial improvement on a wide range of prompts. No AI is
   > perfect, especially at this emerging stage of the industry's development, but we
   > know the bar is high for us and we will keep at it for however long it takes.
   > And we'll review what happened and make sure we fix it at scale.
   >
   > Our mission to organize the world's information and make it universally
   > accessible and useful is sacrosanct. We've always sought to give users helpful,
   > accurate, and unbiased information in our products. That's why people trust
   > them. This has to be our approach for all our products, including our emerging
   > AI products.
   >
   > We'll be driving a clear set of actions, including structural changes, updated
   > product guidelines, improved launch processes, robust evals and red-teaming, and
   > technical recommendations. We are looking across all of this and will make the
   > necessary changes.
   >
   > Even as we learn from what went wrong here, we should also build on the product
   > and technical announcements we've made in AI over the last several weeks. …
   >
   > We know what it takes to create great products that are used and beloved by
   > billions of people and businesses, and with our infrastructure and research
   > expertise we have an incredible springboard for the AI wave. Let's focus on
   > what matters most: building helpful products that are deserving of our users'
   > trust."
   Exact quote and attribution the brief asked to verify: **"I know that some of its
   responses have offended our users and shown bias – to be clear, that's completely
   unacceptable and we got it wrong."** — attributed by Semafor to a memo Pichai sent
   "Tuesday evening" (i.e., 27 Feb 2024) to Google staff, addressing "the recent
   issues with problematic text and image responses in the Gemini app." Google
   confirmed the memo to Semafor. This is corroborated independently (see sources 7,
   8, 9 below), so it clears the desk's two-independent-confirmation bar even before
   counting the confirmed-primary status of the memo itself.
   Note: the memo also addresses a separate *text* controversy (Gemini's chatbot
   equating Elon Musk's influence with Hitler's) alongside the *image* controversy.
   The "completely unacceptable" sentence covers both; do not present it as solely
   about images without noting the memo's scope.
   Semafor's own analysis (Albergotti's "Reed's view," clearly opinion/secondary,
   useful for the steelman): "It isn't really about bias. It shows that Google made
   technical errors in the fine-tuning of its AI models. The problem is not with the
   underlying models themselves, but in the software guardrails that sit atop the
   model. … Based on my understanding of this saga, nobody at Google actually set
   out to force Gemini to depict the Pope as a woman, or Vikings as Black people, nor
   did anyone want it to find moral equivalency between Musk and Hitler. This was a
   failed attempt at instilling less bias and it went awry."

6. **Catherine Thorbecke and Clare Duffy, "Google halts AI tool's ability to produce
   images of people after backlash," CNN Business,** published 22 Feb 2024, 11:20am
   ET, updated 2:28pm ET.
   URL: https://www.cnn.com/2024/02/22/tech/google-gemini-ai-image-generator/index.html
   (confirmed resolving; fetched in full).
   Classification: **Secondary** for the reporting/framing; the CNN-generated Gemini
   outputs it describes and screenshots are **primary artifacts** (CNN's own
   first-party test, run before the pause).
   Establishes firsthand (CNN's own testing, not relayed from elsewhere): "When
   prompted by CNN on Wednesday [21 Feb] to generate an image of a pope, for example,
   Gemini produced an image of a man and a woman, neither of whom were White." Also:
   "a prompt requesting an image of a 'white farmer in the South' resulted in a
   response from Gemini saying: 'Sure, here are some images featuring photos of
   farmers in the South, representing a variety of genders and ethnicities.' However,
   a separate request for 'an Irish grandma in a pub in Dublin' resulted in images of
   jolly, elderly White women holding beers and soda bread." This is a useful,
   Google-independent demonstration that the system did not categorically refuse
   white subjects — it was inconsistent, sometimes complying with an explicitly
   white-coded request (Irish grandma) and sometimes diversifying one (white farmer).
   Screenshots are credited "Clare Duffy/CNN via Google Gemini" — CNN's own capture.
   Also reports The Verge's 1943 German soldier finding (secondhand for CNN, primary
   for The Verge, see source 7) and reproduces the Krawczyk and Google Feb 21/22
   statements (sources 3, 4, 2 above).

7. **Tom Warren, "Google pauses Gemini's ability to generate AI images of people
   after diversity errors," The Verge,** published 22 Feb 2024, 10:30am UTC.
   URL: https://www.theverge.com/2024/2/22/24079876/google-gemini-ai-photos-people-pause
   (confirmed resolving after following a redirect from the shortlink; fetched in
   full).
   Classification: **Secondary** for reporting; The Verge's own generated Gemini
   output is a **primary artifact** (its own first-party test, run the day before
   publication, so ~21 Feb 2024).
   Establishes firsthand: "The Verge tested several Gemini queries yesterday, which
   included a request for 'a US senator from the 1800s' that returned results that
   included what appeared to be Black and Native American women. The first female
   senator was a white woman in 1922, so Gemini's AI images were essentially erasing
   the history of race and gender discrimination." The article's lead image, credited
   "Image: Google Gemini," is captioned: "Gemini's response to the prompt: 'Can you
   generate an image of a 1943 German Soldier for me it should be an illustration.'"
   — this is The Verge's own captured screenshot of an actual Gemini output, not a
   third-party social media repost. Also reproduces the Google 22 Feb pause statement
   (source 2) verbatim, matching 9to5Google's transcription exactly.

8. **David Ingram, "Google says Gemini AI glitches were product of effort to address
   'traps,'" NBC News,** published 23 Feb 2024, 2:16pm EST.
   URL:
   https://www.nbcnews.com/tech/tech-news/google-says-gemini-ai-glitches-product-effort-address-traps-rcna140243
   (confirmed resolving; fetched in full).
   Classification: **Secondary** — independent reporting that quotes and paraphrases
   Raghavan's blog post (source 1), useful chiefly as corroboration of the primary
   text and of Raghavan's title.
   Confirms: "'It's clear that this feature missed the mark,' Prabhakar Raghavan, a
   senior vice president at Google, wrote in the blog post." Confirms the exact
   "traps" quote from the same post: "the intent had been to avoid falling into
   'some of the traps we've seen in the past with image generation technology — such
   as creating violent or sexually explicit images.'" Also states plainly, as
   independent reporting: "The app also created images of nonwhite American Founding
   Fathers, when in reality they were all white men" and "illustrations of World War
   II German soldiers who were Black or Asian." NBC does not claim to have generated
   these itself; treat as reporting on the general public record of the controversy,
   not as an independent first-party reproduction.

9. **CNBC, "Google CEO tells employees Gemini AI blunder 'unacceptable,'"** published
   28 Feb 2024. URL:
   https://www.cnbc.com/2024/02/28/google-ceo-tells-employees-gemini-ai-blunder-unacceptable.html
   (confirmed resolving; fetched).
   Classification: **Secondary.** Independently corroborates the Pichai memo quote
   and its "completely unacceptable" wording, sourced separately from Semafor. This
   is the second of the two independent confirmations the desk requires for the
   memo's exact wording (Semafor is the first, with the memo confirmed by Google
   directly; CNBC and NPR both independently reported the same wording, so the bar is
   cleared with room to spare).

10. **NPR, "Google CEO Sundar Pichai says Gemini's AI image results 'offended our
    users,'"** published 24 Feb 2024 (article also carries a 28 Feb dateline in some
    listings; treat 24 Feb per the URL's own date stamp).
    URL: https://www.npr.org/2024/02/24/1234532775/google-gemini-offended-users-images-race
    (confirmed resolving; fetched).
    Classification: **Secondary.** Third independent outlet corroborating the memo
    wording and Google's timeline.

11. **Marco Quiroz-Gutierrez, "Sergey Brin, who 'kind of came out of retirement' to
    work on AI, says Google 'definitely messed up' with Gemini's racial image
    generation problem," Fortune,** published 4 March 2024, 2:32pm ET.
    URL:
    https://fortune.com/2024/03/04/sergey-brin-google-definitely-messed-up-gemini-image-generation
    (confirmed resolving; fetched in full).
    Classification: Fortune's framing is **secondary**; Brin's quoted remarks,
    captured on video at a public event (San Francisco's AGI House), are **primary**
    — a second, separately-sourced Google co-founder/executive account.
    Verbatim: "We definitely messed up on the image generation and I think it was
    mostly due to not thorough testing and it definitely, for good reasons, upset a
    lot of people." Also: on why the model "leans left in many cases" generally,
    Brin said it is "not intentional," and: "If you deeply test any text model out
    there, whether it's ours, ChatGPT, Grok, what have you, it'll say some pretty
    weird things that are out there that you know definitely feel far left." On the
    fix in progress (as of ~26 Feb–4 March): "If you try it starting over this last
    week it should be at least 80% better, of the test cases that we've covered."
    This article also independently confirms that Semafor was first to report the
    Pichai memo ("Brin's words follow Pichai's stern message to staff, in an internal
    memo first reported by Semafor").

12. **Ben Wodecki, "Google DeepMind CEO Defends Gemini's 'Well-Intended' Image
    Flaws," AI Business,** published 26 Feb 2024, reporting live remarks by Demis
    Hassabis at Mobile World Congress in Barcelona (moderated on stage by Wired's
    Steven Levy).
    URL:
    https://aibusiness.com/responsible-ai/google-deepmind-ceo-defends-gemini-s-well-intended-image-flaws
    (confirmed resolving; fetched in full).
    Classification: AI Business's framing is **secondary**; Hassabis's quoted
    on-record remarks, given at a public conference, are **primary** — a third,
    separately-sourced senior Google/DeepMind account, and the clearest available
    steelman of Google's intent in Google's own words.
    Verbatim, steelman-relevant: "For example, put in a prompt that asks for ... a
    picture of a person walking a dog or a nurse in a hospital. In those cases, you
    clearly want a sort of universal depiction, especially if you consider that as
    Google, we serve 200 plus countries, every country around the world, so you
    don't know where the users coming from and what their background is going to be
    or what context they're in. So you want to show a universal range of
    possibilities there." On what went wrong: the good intention "wasn't working
    quite the way we intended it to work" and was applied "too bluntly, across all
    of it." On the fix: "there should be a 'much narrower distribution' for
    historical content," and: "We care, of course, about historical accuracy. And
    so, we've taken that feature offline while we fix that." Hassabis's title per
    this and multiple other sources: CEO, Google DeepMind. He said the feature would
    return "in the next couple of weeks" (it returned, in limited form, 28 Aug 2024
    — source 13 — a considerably longer timeline than promised).

13. **TechCrunch, "Google says it's fixed Gemini's people-generating feature,"**
    published 28 Aug 2024.
    URL:
    https://techcrunch.com/2024/08/28/google-says-its-fixed-geminis-people-generating-feature/
    (confirmed resolving; fetched).
    Classification: **Secondary** for framing; the quoted Google spokesperson
    statement is **primary**.
    Establishes: Google re-enabled people-generation using a new model, **Imagen 3**,
    initially as an English-language, paid-tier-only ("Gemini Advanced, Business, and
    Enterprise") early access test — not a full public reversal on day one. Google's
    stated fix, per spokesperson: training data "filtered for 'safety' with
    consideration for 'fairness issues,'" use of AI-generated captions meant to
    "improve the variety and diversity of concepts," and continued SynthID
    watermarking. Quoted Google statement: "We've significantly reduced the
    potential for undesirable responses through extensive internal and external
    red-teaming testing." This corroborates the commission's "restored months later
    with changes" and gives it a specific date (28 Aug 2024 — about six months after
    the Feb 2024 pause) and a specific successor model (Imagen 3).

14. **Eli Collins (VP, Google DeepMind), "New and better ways to create images with
    Imagen 2," Google Keyword blog,** published 1 Feb 2024.
    URL: https://blog.google/innovation-and-ai/products/google-imagen-2/ (confirmed
    resolving; fetched in full).
    Classification: **Primary** — Google's own product documentation for what
    Imagen 2 was and when the Gemini (then-Bard) image feature launched.
    Establishes: Imagen 2 is "powered by Google DeepMind's latest text-to-image
    advancements via a diffusion-based model," trained on "higher-quality,
    image-description pairings," and began powering image generation in Bard
    starting 1 Feb 2024 ("starting today, Imagen 2 is powering new image generation
    functionalities on Bard and ImageFX"). This dates the launch and is consistent
    with Raghavan's "three weeks ago" (23 Feb minus ~1 Feb ≈ 22 days). Describes
    Google's "responsible approach": "we invested in the safety of training data
    from the outset and added technical guardrails to limit problematic outputs like
    violent, offensive, or sexually explicit content," "extensive adversarial
    testing and red teaming," filters "to avoid generating images of named people,"
    and SynthID watermarking on all generated images. Notably, this launch post says
    nothing about diversity-tuning specifically — that explanation came only after
    the failure, in Raghavan's 23 Feb post (source 1). Useful as the "before" account
    of what the system was represented to be.

15. **OpenAI, "DALL·E 3 System Card,"** published 3 Oct 2023 (predates the Gemini
    incident by about four and a half months).
    URL: https://openai.com/index/dall-e-3-system-card/ (found via search; not
    independently re-fetched line-by-line in this pass, but corroborated by a search
    summary describing its content and is OpenAI's own published system card, a
    standard primary safety-disclosure document).
    Classification: **Primary** for the general mechanism this class of system uses
    — not evidence about Google's specific implementation.
    Establishes (per the document's own stated findings, as summarized by search
    results drawn directly from OpenAI's text): OpenAI found that DALL-E 3's early
    outputs of people "tended to be primarily white, young, and female," and in
    response, OpenAI "tuned ChatGPT's transformation of the user prompt to specify
    more diverse descriptions of people" — i.e., an LLM (ChatGPT) rewrites the user's
    image prompt, inserting demographic-diversifying language, before the rewritten
    prompt reaches the image model. This is a company (not Google) *publicly and
    explicitly documenting* the exact class of technique — invisible prompt
    rewriting/augmentation for diversity — that outside commentators inferred Google
    used. It is the strongest available evidence that this mechanism is real and
    used in production image systems generally. It is not evidence that Gemini used
    the identical implementation; Google itself never confirmed prompt-level
    rewriting as opposed to training-time tuning. **Recommend the writer flag this
    distinction explicitly**: cite OpenAI's system card for how this class of
    mitigation works in the industry, and cite Google's own words only for what
    Google confirmed about its own system (tuning that "failed to account for cases
    that should clearly not show a range" — architecture-agnostic language).
    Caveat: this source was read via a search-tool summary of its own findings
    rather than a full independent line-by-line fetch in this pass; the writer or
    editor should treat the direct quotes above ("primarily white, young, and
    female"; "tuned ChatGPT's transformation of the user prompt to specify more
    diverse descriptions of people") as accurately characterizing OpenAI's own
    published system card language, but re-verify by opening
    https://openai.com/index/dall-e-3-system-card/ directly before quoting it
    verbatim in the article, since it was not re-fetched and re-read in full here.

16. **Forbes (Derek Saul), "Google's Gemini Headaches Spur $90 Billion Selloff,"**
    published 26 Feb 2024. URL:
    https://www.forbes.com/sites/dereksaul/2024/02/26/googles-gemini-headaches-spur-90-billion-selloff/
    Classification: **Secondary.** Fetched, but the article body returned mostly
    navigation/paywall boilerplate rather than full text; the figure is taken from
    the search index's summary of the piece, not a verified in-article passage. Per
    that summary: Alphabet shares fell 4.5% to $138.75 on Monday 26 Feb 2024, its
    "second-steepest daily loss of the last year," a roughly $90 billion drop in
    market value, attributed to the accumulating Gemini controversy (image
    generation plus the separate Musk/Hitler text controversy). **Flag for the
    writer/editor: this number is not confirmed against the full article text** and
    a different outlet (Fox Business, not independently fetched here) reportedly
    cited a $70 billion figure, possibly for a different day or a different
    baseline. Do not use the $90B figure without either re-fetching Forbes directly
    or finding a second source that pins down the same number for the same date.
    Recommend treating this as color, not load-bearing, or cutting it if it cannot be
    tightened.

17. **9to5Google (Ben Schoon), "Google temporarily disables AI image generation of
    people in Gemini,"** published 22 Feb 2024, 6:50am PT.
    URL: https://9to5google.com/2024/02/22/google-gemini-ai-image-generation-people/
    (confirmed resolving; fetched in full).
    Classification: **Secondary**, but the earliest-timestamped report found of the
    22 Feb pause, and the source used above to pin the exact Google account
    (@Google_Comms) that posted the pause statement (source 2). Also independently
    confirms the exact in-product refusal message text (matches The Verge's and
    CNN's transcriptions exactly).

## Contradictions

- **Google's own account never names the specific viral examples.** Raghavan's post
  (source 1) speaks only in hypotheticals ("a Black teacher in a classroom," "a
  white veterinarian with a dog"). The Founding Fathers portrait, the racially
  diverse Nazi soldiers as widely screenshotted, the "diverse Vikings," and the
  specific pope image that went viral via the @IMAO_ account were never confirmed by
  Google as authentic, unedited outputs in anything read for this record. What is
  independently confirmed, by two different newsrooms testing the tool themselves
  before the pause, is the same *pattern*: The Verge got non-white "US senators from
  the 1800s" and a non-white "1943 German Soldier" illustration; CNN got a non-white
  pope and an ethnically "diverse" response to "white farmer in the South." These are
  not the identical prompts that went viral on social media, but they are independent,
  first-party reproductions of the same failure mode, by reporters with bylines,
  before Google pulled the feature — which is meaningfully stronger evidence than an
  unsourced screenshot. The writer should lean on the Verge/CNN first-party tests for
  "which outputs were real" rather than on any single viral social-media screenshot,
  and should not assert as fact that any specific named viral image (e.g., "the
  Founding Fathers image", "the Black Nazi soldier image") was confirmed genuine by
  Google — because it was not, in the sources read here.
- **CNN's own test complicates a clean "Gemini refuses white people" narrative.**
  CNN's "Irish grandma in a pub in Dublin" prompt returned "jolly, elderly White
  women" without complaint, while "white farmer in the South" was diversified. This
  shows the failure was inconsistent rather than a blanket refusal to depict white
  people, which the article should reflect rather than repeating the flattened
  "Gemini won't draw white people" framing the incident was litigated in (which the
  commission explicitly asks the writer to avoid).
- **The precise architecture of the "tuning" is not confirmed by Google and is
  contested only in the sense that outside reconstruction fills a gap Google left
  open.** Search-derived claims that "someone got Gemini to reveal its system prompt"
  containing diversity instructions are unverified secondhand claims about a single
  X post; I did not find a primary Google confirmation of prompt-level (as opposed to
  training-level) intervention. The OpenAI DALL-E 3 system card (source 15) proves
  the general technique exists and is documented elsewhere in the industry — it does
  not prove Gemini used the identical implementation. The article's "instructions are
  data" framing should be pinned to the general, cross-industry mechanism (citable to
  OpenAI's own system card and to `the-mechanics/instructions-are-data` or
  `the-evidence/instructgpt` per the commission) and to Google's own, deliberately
  architecture-agnostic word "tuning" — not asserted as a confirmed fact about
  Gemini's internal pipeline.
- **Minor tonal difference, not a factual contradiction:** Brin's public framing
  ("mostly due to just not thorough testing") is looser than Raghavan's structured
  two-cause account (over-broad diversity tuning + separate over-caution). The two
  are compatible — better testing would presumably have caught the tuning failure —
  but a writer should not merge them into one Google position; attribute each
  separately.
- **Stock-loss figure is contested/unverified**, see source 16. Do not use without
  tightening.

## Numbers

- **Launch date of image generation of people in Gemini (then Bard), powered by
  Imagen 2:** 1 Feb 2024. Source: Eli Collins/Google, source 14 ("starting today,
  Imagen 2 is powering new image generation functionalities on Bard"). Corroborated
  by Raghavan's "three weeks ago" (source 1) measured against his 23 Feb post date.
- **Pause of image generation of people:** 22 Feb 2024. Source: Google Communications
  X post, quoted identically by sources 2, 6, 7, 17.
- **Raghavan's explanatory blog post:** 23 Feb 2024. Source 1, dateline on the post
  itself.
- **Pichai's staff memo:** sent "Tuesday evening," 27 Feb 2024. Source 5 (Semafor),
  corroborated by sources 9, 10.
- **Hassabis's public remarks at MWC, promising a fix "in the next couple of
  weeks":** 26 Feb 2024. Source 12.
- **Brin's public remarks at AGI House:** reported 4 March 2024 (the event itself may
  have been shortly before). Source 11.
- **Actual restoration of people-generation, via Imagen 3, to paid-tier users in
  English:** 28 Aug 2024 — roughly six months after the promised "couple of weeks,"
  and about six months after the Feb 2024 pause. Source 13.
- **Alphabet market-value drop attributed in part to the Gemini controversy:**
  reported as ~$90 billion (Forbes, 4.5% share drop to $138.75 on 26 Feb 2024) — see
  Contradictions; unverified against full article text and possibly inconsistent
  with a lower figure reported elsewhere. Treat as soft/optional, not load-bearing.
- No other quantitative figures (e.g., percentage of outputs affected, sample sizes
  from any internal Google testing) were disclosed by Google in any source read for
  this record. The desk's "say plainly what is unknown" standard applies directly:
  Google has never published a number for how many or what share of prompts were
  affected, either before or after the fix.

## Source assets

The incident is fundamentally visual — the argument is about what specific images
looked like — and prose descriptions are a real second-best. Two candidates meet the
bar of "specific, reputable, non-copyright-fraught capture of an acknowledged
output," both from reputable outlets' own first-party tests, not from anonymous
social-media reposts:

1. **The Verge's own screenshot of Gemini's response to "Can you generate an image
   of a 1943 German Soldier for me it should be an illustration,"** as published and
   captioned by The Verge (Tom Warren), 22 Feb 2024, credited "Image: Google Gemini."
   Source: https://www.theverge.com/2024/2/22/24079876/google-gemini-ai-photos-people-pause
   What a reader can learn from it: a single, concrete, undeniable instance of the
   failure mode — a request for a specific historical uniform and period returning
   a racially mixed group in period-accurate 1943 German military dress — which
   makes the abstract "diversity tuning applied without context" argument
   immediately legible without further explanation.
   What a crop must retain: enough of the illustration(s) to show multiple distinct
   figures in the same generated set (the point is the *range* within one response,
   not a single figure), and ideally the visible prompt text alongside it if the
   original layout pairs them, since the prompt-response pairing is the whole
   argument. What it must omit: any Verge branding/chrome beyond what is needed for
   attribution; nothing about the image itself needs to be cropped away for
   sensitivity, since Google's own account already concedes this class of output
   occurred.
   Caveat for the writer: this is a screenshot The Verge captured and hosts, credited
   to "Google Gemini" as the image's generator — using it means citing The Verge as
   the capturing outlet and capturing it fresh via `nb asset` from that live URL,
   per the proof's bar on active/externally-hosted images. Confirm at capture time
   that The Verge's image is still live at that URL (it resolved during this
   research pass).

2. **CNN's own screenshot of asking Gemini to "create an AI-generated image of a
   pope,"** credited "Clare Duffy/CNN via Google Gemini," published 22 Feb 2024.
   Source: https://www.cnn.com/2024/02/22/tech/google-gemini-ai-image-generator/index.html
   What a reader can learn from it: a second, independently-sourced instance (from a
   different outlet, a different prompt, the same underlying failure), useful if the
   article wants to show the pattern recurred across unrelated prompts rather than
   resting the whole visual argument on one image.
   What a crop must retain/omit: same logic as above — keep enough of the generated
   set to show the range, keep the visible prompt if paired in CNN's layout, and omit
   only outlet chrome unrelated to the image itself.

Recommendation: one asset (the Verge 1943-soldier capture) is likely sufficient and
is the single clearest illustration of "context-blind rule overwrote a factual
answer," which is the article's central mechanism claim; the CNN pope image is a
reasonable alternate or second image if the writer wants to show recurrence. Do not
use any image whose only source is an unattributed or single anonymous X/social post
(e.g., the Founding Fathers portrait as posted by @EndofWokeness, the "Seoul Man"
pilgrims screenshot) — none of those were independently reproduced by a newsroom in
this research pass, and their authenticity/edit status is not established here.
A Raghavan/Pichai portrait or a Google-DeepMind product photo would be decorative,
not argument-carrying, and is not recommended.

## Discarded

- **The New York Times** coverage of this incident: attempted fetch of a plausible
  NYT URL returned HTTP 403 (paywall/bot-block), and I could not locate the article's
  content through search summaries specific enough to quote verbatim with confidence.
  Not used. The commission's secondary-source list is amply met without it (Verge,
  CNN, NBC, CNBC, NPR, Forbes, TechCrunch, AI Business, 9to5Google all cleared).
- **Ars Technica** coverage (Benj Edwards byline, widely referenced in search
  summaries as describing a "system prompt" reveal): direct fetch attempts to
  arstechnica.com failed (blocked/404 on guessed URLs), and I could not locate the
  correct live URL through search well enough to independently verify its claims
  about a leaked system prompt. Its claim (that an X user got Gemini to describe its
  own diversity-insertion system prompt) is exactly the kind of "outside
  reconstruction" the brief says to mark clearly and not overclaim; without being
  able to read the original piece and its sourcing, I am not treating this claim as
  confirmed and recommend the writer not cite it as established fact. If the writer
  wants this specific claim, it needs a fresh, successful fetch of the original
  piece and ideally the underlying X post it's built on.
- **BBC** coverage: could not locate a working, specific BBC URL for this incident
  through search (guessed URL 404'd, and search results did not surface a distinct
  BBC News article with its own byline/date I could independently fetch and verify).
  Not used. Not needed to clear the source-count bar.
- **Wired** coverage: search results describe Wired's Steven Levy moderating the MWC
  panel where Hassabis spoke (captured instead via AI Business's report on the same
  event, source 12), but I did not find or fetch a standalone Wired article on the
  incident itself to cite directly.
- **Al Jazeera, "Why Google's AI tool was slammed for showing images of people of
  colour"** and **Daily Maverick's "AI So White... and why the Gemini 'white racism'
  saga was overblown":** both surfaced in search as potentially useful for the
  critical-of-the-critics steelman angle, but neither was fetched and read in full;
  not used as sourced claims here. Worth a look if the writer wants an additional
  steelman-the-defense angle beyond what sources 5 (Semafor's "Reed's view"), 11
  (Brin), and 12 (Hassabis) already provide.
- **Various single-sourced social-media screenshots** (the Founding Fathers portrait
  via @EndofWokeness; the pope screenshot via @IMAO_; the "diverse Vikings"; the
  English Pilgrims image via a poster called "Seoul Man"): these are the images that
  actually went viral and drove the political controversy, but none were
  independently reproduced by a newsroom in this research pass, so I am not treating
  any single one as a confirmed-genuine primary artifact. They are real as evidence
  that the controversy occurred and looked the way it looked to the public — useful
  for describing what people reacted to — but not as evidence of what Gemini
  actually, verifiably output absent a first-party test (which is what sources 6 and
  7 supply instead).
- **Know Your Meme's "Google Gemini 'Diverse' Prompt Injection" page:** surfaced
  repeatedly in search as a secondary aggregator; not fetched or used as a source,
  since it is not a primary or reportorial secondary source in the sense the desk
  wants, and everything useful in it traces back to sources already captured above.
