# This paper's shared furniture

## Lesson bookends (`rs-bookend`)

Two cards frame every lesson: Why this matters opens it, The takeaway
closes it. Both are written after the body; the lesson template's
identity.md carries the writing rules. The name lines, the band labels
(Background, Go deeper), and the words "optional reading" are fixed
chrome. Reading rows are editorial: each row is a link and one line on
what it covers. Background rows may point into this library or beyond;
Go deeper rows always point beyond this paper.

```html
<section class="rs-bookend" data-nb-section="why" id="why">
  <p class="rs-bookend-name">Why this matters</p>
  <div class="rs-bookend-rule"></div>
  <p>THE OPENER, TO THE READER, THIS LESSON'S PARTICULARS ONLY.</p>
  <div class="rs-bookend-band">
    <span class="rs-bookend-label">Background</span>
    <span class="rs-bookend-note">optional reading</span>
  </div>
  <dl class="rs-bookend-reading">
    <dt>01</dt>
    <dd><a href="../SERIES-ID/SLUG.html">TITLE</a> — WHAT IT COVERS.</dd>
  </dl>
</section>
```

The takeaway card is the same markup with `data-nb-section="takeaway"`,
`id="takeaway"`, the name line "The takeaway", and the band label
"Go deeper".

## Prior Context card (`rs-prior`) — legacy

Opens every framed article, written last, from the finished piece. One
passage under the card's name: why the subject matters, what knowing it
unlocks later, and which details return, each given its consequence. It is
never a summary, never an instruction about what to notice, and never
mentions the paper or any reader. The reading rows hold two true
prerequisites, internal (relative library link) or external (a lasting
public text): the link, then what from that text is needed here. Drop the
list only when nothing honest qualifies. The "Prior Context" name and
"Prior" chips are fixed chrome. The card carries no citations.

```html
<section class="rs-prior" data-nb-section="prior" id="prior">
  <p class="rs-prior-name">Prior Context</p>
  <p class="rs-prior-context">
    WHY THE SUBJECT MATTERS, WHAT KNOWING IT UNLOCKS LATER, AND WHICH
    DETAILS RETURN, EACH GIVEN ITS CONSEQUENCE.
  </p>
  <ul class="rs-prior-reading">
    <li>
      <span class="rs-prior-chip">Prior</span>
      <a href="../SERIES-ID/SLUG.html">TITLE</a>: WHAT FROM IT IS NEEDED HERE.
    </li>
    <li>
      <span class="rs-prior-chip">Prior</span>
      <a href="https://example.org/replace">TITLE</a>: WHAT FROM IT IS NEEDED
      HERE.
    </li>
  </ul>
</section>
```
