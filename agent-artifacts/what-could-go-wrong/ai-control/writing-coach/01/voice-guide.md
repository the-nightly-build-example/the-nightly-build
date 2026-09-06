# Voice guide: what-could-go-wrong/ai-control

## How this piece should sound

This lesson has two jobs that pull against each other: lay out control's case at
full strength, then hold the APPS backdooring numbers to what they actually
proved. The exemplars below all do that same double move in a security setting,
and several of their habits transfer directly.

Hedge in exact proportion to what is known, the way Rescorla answers his own FAQ
questions with "Yes," "Sort of," "Probably" before explaining why. The honest
answer to "does a control evaluation show the protocol would hold against a
smarter model" is not a clean yes or no, and smoothing it into one erases the
finding. When a claim depends on an assumption nobody has verified rather than on
something the paper measured, say which is which the way Rescorla separates what
NeuralHash's math guarantees from what only holds if Apple's policy controls
behave: the trusted monitor staying competitive with the untrusted model is that
kind of assumption, not a result.

Give every scope claim its exact edges before extending it, the way Green marks
where his iMessage attack's demonstrated reach stops and where he is reasoning
past it. The APPS backdooring result is a demonstration in one setting, with one
red team, one pair of models, one set of protocols. State that setting exactly,
the way Green gives the precise message count and hours his attack took rather
than calling it "slow," then extend only as far as the evidence allows and in the
same hedged register used to state it. This is where the piece can name control's
own proponents saying the agenda fails once the untrusted model is sufficiently
superhuman: that is their scope claim on their own result, not a hostile
addition.

Ground the mechanism against what it replaces before judging it, in concrete
comparison rather than abstraction, the way Green sets iMessage's encryption
against the plaintext SMS it replaced before asking whether iMessage's own
scheme holds up. Control's whole pitch is a contrast with alignment: instead of
trying to verify what a model wants, assume it may be adversarial and design the
deployment to catch it anyway. State that contrast in what each approach
concretely asks you to trust, not in the abstract terms "wanting" and
"behavior" invite.

Do the definitional work in plain declarative sentences before any verdict, the
way Schneier lays out trust's several meanings before he uses the word to argue
anything. "Safety," "usefulness," and "control evaluation" are terms the whole
argument rests on, each with a specific meaning in the Redwood paper that an
everyday reading of the word would get wrong. Set each one the same plain way,
in the sentence that first needs it, before it carries any argument.

When the piece states what a failed protocol would mean, name the failure the
way Schneier names what a lost bitcoin key costs, concretely and more than once,
rather than reaching for "the stakes are high." A control evaluation's safety
number has an exact denominator: some number of red-team attempts, some fraction
caught. State it that way, the way Green states his attack in exact messages and
hours instead of calling it "slow." That is what the commission's own sourcing
rule asks for from every figure in the piece, and Green's habit is what it
looks like on the page.

One thing to leave behind: Rescorla's honesty comes wrapped in "I read the paper
and think I mostly understand it, but I haven't studied the proofs." The lesson
body never speaks as an "I." The two bookends are the only place this piece
addresses anyone directly, so the same calibrated hedging has to survive
without the first person. "The paper measures this on the toy setting; whether
it holds elsewhere is untested" carries the same honesty as Rescorla's
disclaimer without his frame.

## Bruce Schneier, "There's No Good Reason to Trust Blockchain Technology"

Source: https://www.schneier.com/essays/archives/2019/02/theres_no_good_reaso.html

> "The word 'trust' is loaded with many meanings. There's personal and intimate
> trust. When we say we trust a friend, we mean that we trust their intentions
> and know that those intentions will inform their actions. There's also the
> less intimate, less personal trust—we might not know someone personally, or
> know their motivations, but we can trust their future actions. Blockchain
> enables this sort of trust: We don't know any bitcoin miners, for example, but
> we trust that they will follow the mining protocol and make the whole system
> work."

Before Schneier argues anything about blockchain, he splits "trust" into the
senses that matter and states which one blockchain actually offers. Each
sentence adds one distinction and stops; nothing is asserted before it is
defined. The care is visible in how late the verdict arrives: the paragraph
does definitional work only, and the argument waits for it.

> "When that trust turns out to be misplaced, there is no recourse. If your
> bitcoin exchange gets hacked, you lose all of your money. If your bitcoin
> wallet gets hacked, you lose all of your money. If you forget your login
> credentials, you lose all of your money. If there's a bug in the code of your
> smart contract, you lose all of your money. If someone successfully hacks the
> blockchain security, you lose all of your money."

Five sentences, one structure, one concrete consequence named each time. Schneier
could have written "the risks are severe and varied"; instead he lists the actual
ways the risk materializes, and the repetition is what makes the claim land:
each new clause is a different demonstrated failure, not a restatement of the
same one.

> "To answer the question of whether the blockchain is needed, ask yourself: Does
> the blockchain change the system of trust in any meaningful way, or just shift
> it around? Does it just try to replace trust with verification? Does it
> strengthen existing trust relationships, or try to go against them? How can
> trust be abused in the new system, and is this better or worse than the
> potential abuses in the old system? And lastly: What would your system look
> like if you didn't use blockchain at all?"

Instead of closing with a slogan, Schneier hands the reader the actual test he
ran on blockchain claims, phrased so it works on the next claim too. Each
question isolates one thing a proponent might be conflating with another:
changing trust versus moving it, verification versus trust itself. That
precision is where his own analytical method becomes visible on the page.

## Matthew Green, "Attack of the Week: Apple iMessage"

Source: https://blog.cryptographyengineering.com/2016/03/21/attack-of-week-apple-imessage/

> "Before iMessage, the vast majority of text messages were sent via SMS or MMS,
> meaning that they were handled by your cellular provider. Although these
> messages are technically encrypted, this encryption exists only on the link
> between your phone and the nearest cellular tower. Once an SMS reaches the
> tower, it's decrypted, then stored and delivered without further protection."

Green sets up what iMessage's encryption actually improved on before he attacks
it, so the reader can weigh the coming flaw against a real baseline instead of
an assumed one. The precision is in "only on the link between your phone and the
nearest cellular tower": a sentence that could have said "SMS isn't very
secure" instead states exactly where the protection stops.

> "The need for an online response is why our attack currently works against
> attachment messages only: those are simply the messages that make the phone do
> visible things. However, this does not mean the flaw in iMessage encryption is
> somehow limited to attachments — it could very likely be used against other
> iMessages, given an appropriate side-channel."

This is Green marking the exact line between what his team demonstrated and what
they believe without having shown it. "Currently works against attachment
messages only" is the demonstrated result; "could very likely be used against
other iMessages" is the extrapolation, and he keeps it in hedged language
("could very likely," "given an appropriate side-channel") rather than letting it
borrow the first claim's certainty.

> "As much as I wish I had more to say, fundamentally, security is just plain
> hard. Over time we get better at this, but for the foreseeable future we'll
> never be ahead. The only outcome I can hope for is that people realize how hard
> this process is — and stop asking technologists to add unacceptable complexity
> to systems that already have too much of it."

The essay ends on a genuine limit rather than a verdict dressed as one. Green
does not say the attack proves encryption is broken or that iMessage is fine
now that it's patched; he says what the whole exercise shows about the
difficulty of the underlying problem, which is the actual scope of what he
found. The personal note ("as much as I wish I had more to say") is Green
declining to inflate the finding past what one team's attack actually
demonstrates.

## Eric Rescorla, "Overview of Apple's Client-side CSAM Scanning"

Source: https://educatedguesswork.org/posts/apple-csam-intro/

> "As a disclaimer, I've read the paper and think I mostly understand it, but I
> haven't studied the proofs and even though it was designed by some well-known
> people, the system was just released and thus hasn't been widely analyzed, so
> there's of course some chance there's a mistake."

Rescorla states his own confidence level before explaining a cryptographic
system whose guarantees he is about to describe as if they hold. The sentence
does real work: it tells the reader the difference between "I read this" and "I
verified this," a distinction most technical writing collapses. His caution is
visible in the specific reasons given, not widely analyzed, proofs unchecked,
rather than a general disclaimer.

> "Yes. The threat model here is a bit odd because usually we assume endpoints
> are uncompromised, but in this case uncompromised is kind of an ambiguous
> concept."

Asked whether a device in the system could simply lie, Rescorla answers directly
and then explains why the honest answer complicates the usual security
assumption rather than fitting neatly inside it. He does not soften "yes" into
a hedge, and he does not stop at "yes" either. The second sentence is where he
shows the reader why the question was worth asking.

> "However, they can certainly send a database that has non-CSAM images, as well
> as fill in the empty rows in the table with real values and just hope to get
> lucky. Presumably Apple has some policy controls to prevent this, but that's
> not something that is technically enforced or that is readily publicly
> verifiable."

This is the sentence that separates what the cryptography actually guarantees
from what only holds if a company behaves as promised. "Presumably" and "not
something that is technically enforced" mark the line precisely: one is a
mechanism, the other is trust in a policy, and Rescorla refuses to let the
second borrow the first's certainty.
