# Voice guide: when-ai-breaks/deloitte-ai-report

## How this piece should sound

This lesson opens on a document that was supposed to be trustworthy precisely
because someone paid for it to be checked: a firm hired to give an independent
assurance opinion on a government program. Molly White's FTX piece spends its
first paragraph establishing exactly that kind of manufactured credibility —
what Bankman-Fried said, who believed him, what he was doing in Washington —
before a single sentence of the collapse. Do the same with the report itself:
what DEWR paid for, what "assurance review" is supposed to mean, who signed
off on it, before the fabricated references enter the piece. Let the contrast
between the report's billing and its actual footnotes do the work; nothing
needs to call it ironic.

Name the mechanism the way Greenberg names EternalBlue: one move, defined the
moment it appears, in a sentence a reader who has never heard the term can
follow without re-reading. This lesson's version of that sentence is what a
language model is actually doing when it produces a citation — generating a
plausible string of words, not retrieving a record — and it should get exactly
that kind of single, concrete pass, at the point where the fabricated
references first need explaining, not before. Where the course has already
taught this (mata-v-avianca, galactica), a plain link carries the weight
instead of a second explanation.

Numbers land the way Greenberg's do: pinned to something the reader already
has a feel for. He doesn't just give NotPetya's $10 billion cost, he sets it
against the Atlanta ransomware attack it dwarfed and the WannaCry worm it
outspent. This piece has a fee, a refund amount, and a scope of what the
refund did and didn't cover — each of those is a number the reader cannot
independently size, so anchor at least one to something comparable before
moving on.

When the piece quotes the people who caught the fabrications — an academic
whose paper doesn't exist, a judgment misattributed to a case that says
something else, a DEWR or Senate statement about the review — let the
quotation carry the assessment, the way White lets the Financial Times
reporter's own words do the judging and adds only a dry aside around them.
Angwin, Larson, Mattu and Kirchner do the equivalent by showing the actual
check performed, not just the fact that a check happened: they ran the
statistical test and reported what it isolated. If the piece can say what an
academic actually did to confirm their name was attached to a paper they never
wrote, or what verification step Deloitte's corrected report describes, that
belongs in the piece in that form, not summarized as "the errors were caught."

Machine Bias also earns its general claims by returning to a named case: a
judge's blanket warning about relying on a score gets tested against exactly
what happened to one defendant, sentence and outcome both. This lesson has
its own instance to return to the same way — the specific misattributed
Federal Court quotation, checked against what the judgment actually says — so
a general claim about what went wrong in the report has a concrete result
sitting next to it, not just beside a similar-sounding one.

The series prompt sets the close: name the recurring failure in systems the
reader commissions or drafts inside right now, not a moral about care or
diligence in general. Whatever that failure turns out to be here — AI drafting
inside consulting or government work without anyone checking a single
citation against a source — say what it is, in this report's own terms, and
stop there.

## Molly White, "Why did one of the world's biggest cryptocurrency exchanges just collapse?"

Source: https://www.theguardian.com/commentisfree/2022/nov/14/why-did-one-of-the-worlds-biggest-cryptocurrency-exchanges-just-collapse

> "FTX seemed to be a shining example of a cryptocurrency exchange that was
> doing everything right. Run by Sam Bankman-Fried – a multibillionaire,
> believed by many to be a once-in-a-generation genius, who rubbed shoulders
> with congresspeople and called for "thoughtful regulatory leadership" – FTX
> and its sister companies were bringing crypto to the mainstream."

This is the opening paragraph, and it contains no verdict at all — just what
people believed and why, with the specific claim ("thoughtful regulatory
leadership") doing the work a judgment word would otherwise have to do. The
reader supplies the irony because the facts already carry it. White is
visible in the restraint: she had the ending in hand when she wrote this and
still didn't reach for it early.

> "A leaked balance sheet from Alameda Research, Bankman-Fried's quantitative
> trading firm, allegedly showed that a massive portion of Alameda's assets
> were denominated in tokens that FTX themselves created. It was already an
> open secret that FTX and Alameda were tightly intertwined, but there was
> little hard evidence as to how tightly they were linked, and regulators had
> not made any substantial moves to investigate the ties."

Two sentences, two different pieces of the mechanism: what leaked, and why no
one had caught it earlier. "Allegedly" and "open secret" are doing real
disclosure work, not hedging — the first marks what's still unproven, the
second marks what people suspected but couldn't show. Nothing here waits for
a later paragraph to explain itself.

> "The Financial Times' Alexandra Scaggs was generous when she wrote on
> Thursday that this "stretches the limits of credible belief" coming from
> someone who ran a platform popular for leveraged trading."

The judgment is Scaggs's, quoted and named; White's own contribution is one
word, "generous," dropped in front of it. That word tells you exactly how far
White thinks the assessment should have gone, without her ever writing her
own harsher version of it. It's a model for holding an opinion at arm's
length while still making clear where you stand.

## Andy Greenberg, "The Untold Story of NotPetya, the Most Devastating Cyberattack in History"

Source: https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/

> "'I saw a wave of screens turning black. Black, black, black. Black black
> black black black,' he says. The PCs, Jensen and his neighbors quickly
> discovered, were irreversibly locked. Restarting only returned them to the
> same black screen."

The repetition inside the quote is doing something a paraphrase couldn't:
it's the rhythm of watching it happen, not a report of having watched it.
Greenberg doesn't touch it up or explain why he's including all five
"blacks" — he trusts the reader to hear it, then moves straight to the
technical fact of what the blackout meant.

> "NotPetya was propelled by two powerful hacker exploits working in tandem:
> One was a penetration tool known as EternalBlue, created by the US National
> Security Agency but leaked in a disastrous breach of the agency's
> ultrasecret files earlier in 2017. EternalBlue takes advantage of a
> vulnerability in a particular Windows protocol, allowing hackers free rein
> to remotely run their own code on any unpatched machine."

This is a technical mechanism handed to a reader who has never heard of
EternalBlue, in three sentences: what it is, where it came from, what it lets
an attacker do. Nothing here is simplified into uselessness — "a vulnerability
in a particular Windows protocol" is vague on purpose, because the protocol
itself isn't the point and naming it would cost a sentence the explanation
doesn't need.

> "The result was more than $10 billion in total damages, according to a
> White House assessment confirmed to WIRED by former Homeland Security
> adviser Tom Bossert, who at the time of the attack was President Trump's
> most senior cybersecurity-focused official."

The figure arrives with its source and that source's standing attached in
the same sentence, not footnoted or left to a citation. A reader knows
immediately why this number is worth believing before they're asked to
believe it.

## Julia Angwin, Jeff Larson, Surya Mattu, and Lauren Kirchner, "Machine Bias"

Source: https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing

> "Two years later, we know the computer algorithm got it exactly backward.
> Borden has not been charged with any new crimes. Prater is serving an
> eight-year prison term for subsequently breaking into a warehouse and
> stealing thousands of dollars' worth of electronics."

Three short declaratives, no adjective doing the arguing. The word "backward"
is the only judgment in the passage, and it's earned by the two sentences on
either side of it, which are just what happened. This is what letting the
record make the point looks like when the record is damning enough on its
own.

> "Could this disparity be explained by defendants' prior crimes or the type
> of crimes they were arrested for? No. We ran a statistical test that
> isolated the effect of race from criminal history and recidivism, as well
> as from defendants' age and gender. Black defendants were still 77 percent
> more likely to be pegged as at higher risk of committing a future violent
> crime and 45 percent more likely to be predicted to commit a future crime
> of any kind."

The question-and-one-word-answer is a real move here, not a rhetorical
flourish, because the paragraph immediately shows the test that earned the
"no." The figures that follow are specific enough that another researcher
could go check them, because the method that produced them is stated first.

> "That is almost exactly what happened to Zilly, the 48-year-old
> construction worker sent to prison for stealing a push lawnmower and some
> tools he intended to sell for parts."

This sentence reaches back across several paragraphs to a general warning a
prosecutor gave earlier in the piece and ties it to one specific person's
sentence. The generalization doesn't get to stand alone; it has to survive
contact with a name and an outcome, and here it does.

## Production record

Model: claude-sonnet-5. Effort: low.
