# Voice guide: the-mechanics/prompt-sensitivity

## How this piece should sound

This lesson starts from something the reader has already done. They reworded a prompt, or swapped a colon for a newline, or reordered a few examples, and the answer got worse. From there it walks back to the cause, which is how the model conditions on the exact token sequence it is given. Keep the register plain, the way all three exemplars are plain. Evans, Luu, and Ciechanowski each explain something they understand well without performing it. The article can take that plainness and leave behind the personal-blog enthusiasm in Evans's exclamations, since the body of a lesson is not speaking to anyone.

Ground the behavior before naming its cause. Ciechanowski does not introduce gears until the reader has seen that 2400 rotations are needed and a single gear pair cannot supply them, so the felt problem arrives first and the part that solves it second. The article has a measured spread to work from, and letting one concrete reformatted example and its different output sit on the page, the way Luu lets a write turn a bar into a boo or a far, keeps a claim about token conditioning from staying abstract. No code means those examples are shown as inline data, not as a harness the reader could run.

Be exact about what moved. When a reformatting drops a score, the thing that changed is the output for that particular input, and it is worth keeping that separate from any claim about the model's underlying competence at the task, since the two are easy to blur and mean different things here. Evans separates "there is no record" from "this resolver has not cached it" in the same sentence as her observation. The same care keeps "the surface form moved the score" distinct from "the model is genuinely worse."

Mark what is settled and what is open, in plain terms, at the step where each belongs. Luu shows how to state a limit without dressing it up: he reports what a measurement does and does not establish, and he admits where he himself might be wrong. Prompting carries a good deal of folklore alongside its measured results, and holding the two apart is the same move Luu makes when he reports a confident claim that no one could source. Where even the people who build these systems do not know why a given format helps, the honest thing is to say so in the flat voice Luu and Evans both use when they reach the edge of what is known.

Where the lesson ties the mechanism back to something the reader can see, it can land on the concrete behavior itself rather than on a restated summary of it. Ciechanowski, having built the movement, returns to the smooth sweep of the second hand that the reader already noticed and shows it as the output of the parts just explained. The reworded prompt the reader started from is that kind of concrete thing to return to.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "Here you can see we got a normal NOERROR response for google.com (which is in 8.8.8.8’s cache) but a SERVFAIL for homestarrunner.com (which isn’t). This doesn’t mean there’s no DNS record homestarrunner.com (there is!), it’s just not cached)."

Evans reads a result and heads off the wrong conclusion in the same sentence as the observation: the domain has a record, the resolver simply has not cached it. She states both facts flatly and lets the concrete example carry the distinction between "no record exists" and "this server has not cached it yet." The unadorned plainness is Evans; she adds no commentary on top of the example.

> "Here I’ve requested a nonexistent domain, and I got the extended error EDE: 12 (NSEC Missing): (Invalid denial of existence of xjwudh.com/a). I’m not sure what that means (it’s some DNSSEC Thing), but it’s cool to see an extra debug message like that."

In the middle of explaining a tool she knows well, Evans reaches an error code she does not, and says so in the same plain voice: she reads off what she can and marks the rest as something she has not learned. The admission costs the explanation nothing and it keeps moving. What is Evans here is the refusal to bluff past the edge of what she knows.

## Dan Luu, "Files are hard"

Source: https://danluu.com/file-consistency/

> "What happens? If nothing goes wrong, the file will contain a bar, but if there's a crash during the write, we could get a boo, a far, or any other combination."

Luu takes an abstract worry, that a half-finished write can leave a file corrupt, and pins it to concrete outcomes: instead of a bar you might get a boo or a far. The invented results are small enough to hold in mind and specific enough to prove what the abstraction only asserted. Luu shows the failing case rather than describing it in general terms.

> "The authors are careful to note that they can only determine when properties don't hold -- if they don't find a violation of a property, that's not a guarantee that the property holds."

Luu marks the exact limit of what the measurement establishes. He reports what the tool found, then says in the same sentence what a null result does and does not license, so a reader cannot treat "no violation detected" as a guarantee. Luu holds the claim to what the evidence supports and stops there.

> "In their OSDI 2014 talk, the authors of the paper we're discussing noted that when they reported bugs they'd found, developers would often respond “POSIX doesn't let filesystems do that”, without being able to point to any specific POSIX documentation to support their statement. […] Not being a filesystem dev myself, I'd be a bit surprised if I don't have at least one bug in this post."

Luu separates a documented behavior from a confident claim no one can source: he reports the developers' answer and, beside it, the fact that they could not point to the documentation for it. He then turns the same doubt on his own post and says he would not be surprised to be wrong somewhere. The plain admission is Luu, and it makes the reporting around it easier to trust.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> "If we wanted our watch to run continuously for around 40 hours on a single wind, we’d need the minute hand to complete 40 rotations in that time. Moreover, the second hand should cover around 40 × 60 = 2400 complete rotations in that time. We need to find a way to convert a small number of revolutions of the barrel into a large number of revolutions of the hands. This is where gears come in."

Ciechanowski turns a vague requirement, that the hands turn at the right speed, into two figures the reader can check, and only then names the part that will meet them. Each number is worked out before the mechanism arrives, so "this is where gears come in" answers a need the reader can already feel. Ciechanowski names nothing until the problem it solves has been shown.

> "In this watch movement the balance wheel does a full back and forth swing four times per second, hitting the pallet fork twice during each cycle, for a total of 8 beats per second or 28,800 beats per hour. While different watches may have different rates, they all do a tiny turn of the second hand many times per second, which gives mechanical watches the illusion of a very smooth hand motion."

Ciechanowski converts the mechanism he has just built into one figure, 28,800 beats an hour, and ties that figure to something the reader had already noticed, the smooth sweep of the hand. The internal count and the visible behavior are joined in a single sentence. Ciechanowski returns to the observed behavior at the end of each part he explains.

> "This causes the balance wheel to gain some energy, which prevents it from stopping after a while – it’s equivalent to giving a push to a person swinging on a swing. When the balance wheel comes back, it performs the same action, just in the other direction."

To explain how the escapement keeps the balance wheel swinging, Ciechanowski compares it to a push given to someone on a swing, and uses the comparison only for the one fact he needs, that each pass adds a little energy. The analogy is short and he drops it immediately. Ciechanowski keeps his comparisons brief and tied to a single mechanical point.
