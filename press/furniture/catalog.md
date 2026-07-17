# This paper's shared furniture

## Prior Context card (`rs-prior`)

Opens every framed article. Three parts, written last, from the finished
piece. The hook is one sentence carrying the stake: the judgment or decision
the subject decides. The context motivates the learning ahead, never the
piece itself: what becomes intelligible once this subject is held, and which
details go on to matter, each tied to its later stakes. It is never a
summary, never an instruction about what to notice, and never mentions the
paper or any reader. The reading rows hold two true prerequisites, internal
(relative library link) or external (a lasting public text): the link, then
what from that text is needed here. Drop the list only when nothing honest
qualifies. The "Prior Context" name and "Prior" chips are fixed chrome. The
card carries no citations.

```html
<section class="rs-prior" data-nb-section="prior" id="prior">
  <p class="rs-prior-name">Prior Context</p>
  <p class="rs-prior-hook">ONE SENTENCE CARRYING THE STAKE.</p>
  <p class="rs-prior-context">
    WHAT BECOMES INTELLIGIBLE AFTER THIS SUBJECT, AND WHICH DETAILS GO ON TO
    MATTER, EACH TIED TO ITS LATER STAKES.
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

## Worked table (`rs-worked`)

Hand-worked numeric material set as compact rows: steps of a computation, a
record, a mapping, a two-column comparison, per-item deltas. Digits are
spaced, never parenthesized, so the table fits a phone. Use it only when the
material is rows of one shape, three or more rows deep. Two before/after
numbers belong in a sentence; a worked example whose narration is the
teaching stays prose; heterogeneous single facts belong in a stat strip.
Tokens in the first column wear `rs-token` chips. `rs-left` left-aligns a
column; `rs-wrap` lets a cell wrap. The caption states what the rows show and
carries the citation.

```html
<table class="rs-worked">
  <caption>
    WHAT THE ROWS SHOW.<sup class="nb-cite"><a href="#s1">1</a></sup>
  </caption>
  <thead>
    <tr><th>STEP</th><th>VALUE</th><th>VALUE</th></tr>
  </thead>
  <tbody>
    <tr><td><span class="rs-token">ROW</span></td><td>1 0 0 1</td><td>0.25</td></tr>
    <tr><td><span class="rs-token">ROW</span></td><td>1 0 1 1</td><td>0.0625</td></tr>
    <tr><td><span class="rs-token">ROW</span></td><td>0 1 1 0</td><td>0.0156</td></tr>
  </tbody>
</table>
```
