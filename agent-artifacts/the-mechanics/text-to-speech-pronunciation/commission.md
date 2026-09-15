# Commission: the-mechanics/text-to-speech-pronunciation

## The behavior

A text-to-speech (TTS) voice reads a written word aloud with the wrong
pronunciation. The clean, everyday case: a homograph, one spelling with two
pronunciations that depend on meaning. "I will lead the team" read with the
vowel of the metal *lead*; "she plays bass" read as the fish; "he read it
yesterday" read in the present tense; "a tear in her eye" read as *tear* meaning
to rip. Anyone who has used a screen reader, an audiobook voice, a car
navigation system, or a voice assistant has heard this. The lesson works backward
from the wrong sound to what produced it.

## The angle (work backward to ground, per the series prompt)

Start from the behavior and name a real part of the system at each step down,
with a small concrete example at each step, until nothing below would change the
answer. Mark which steps are settled engineering and which are open even for the
people who build these systems. No code.

The chain to teach (writer sets order and depth from the evidence):

- **The pipeline reads letters, not meaning, first.** A written sentence is not
  sound. Before any audio, the system must decide how each written word is
  pronounced. Teach that classic TTS is a pipeline with a front end (text →
  linguistic description) and a back end (that description → audio), and that the
  pronunciation error is almost always a front-end error, decided before a single
  sample of audio is generated.
- **Text normalization: turning written forms into words.** "Dr." "St." "$5"
  "2010" "III" are not words to sound out; the front end must expand them into
  spoken words, and the expansion is ambiguous ("Dr." = doctor or drive; "St." =
  saint or street; "2010" = twenty-ten or two thousand ten). Use the well-known
  primary evidence here (Sproat & Jaitly's RNN text-normalization challenge, which
  documents systems that "read" a number or unit as the wrong words). Give a
  concrete before/after.
- **Grapheme-to-phoneme (G2P): letters to sounds.** English spelling maps
  irregularly to sound, so a component predicts the phonemes for each word. Teach
  what a phoneme is in plain words (the distinct sound units), and that G2P
  handles unseen words and names by generalizing spelling-to-sound patterns, which
  is why rare names and loanwords are a common failure. A concrete example (a
  surname the system mangles).
- **Homograph disambiguation: the step that needs the sentence's meaning.** The
  core of the lesson. For a true homograph, spelling alone cannot decide the
  sound; the correct sound depends on the word's sense or part of speech in that
  sentence (*lead* verb vs *lead* noun). Teach that resolving it requires reading
  the rest of the sentence, and that this is a known, named NLP subtask with its
  own accuracy numbers (cite a primary homograph-disambiguation paper with a real
  figure). Show why a system that pronounces each word in isolation cannot win it.
- **Ground, and what modern end-to-end / neural TTS changes.** Mark the settled
  part: front-end normalization, G2P, and homograph disambiguation as distinct,
  studied steps. Mark the open/updated part honestly: neural and end-to-end TTS
  (WaveNet, Tacotron 2, and newer LLM-style TTS) can fold more sentence context in
  and have raised naturalness sharply, yet still mispronounce rare words, names,
  and genuine homographs, and vendors bolt on lexicons and normalization rules to
  patch specific errors. Reach the floor: for a genuinely ambiguous sentence where
  even a careful human needs more context, no system can reliably choose. That is
  the step below which nothing changes the answer.

## Required contribution

The evidence carries the mechanism. This piece's own work is to take one wrong
sound the reader has actually heard and trace it to the exact step that produced
it, separating the two very different failures the reader lumps together: a
normalization/G2P failure (the system never had the right sound available for
that written form) and a homograph failure (the sound existed but choosing it
needed the sentence's meaning). The reader should leave able to hear a
mispronunciation and say which of those two just happened.

## Boundaries

- This is TTS (writing → speech). It is not speech recognition or transcription;
  the paper already covers Whisper's failures on the input side, so link, do not
  re-teach. Keep the two directions distinct.
- No code. Explain the phoneme, G2P, and normalization ideas in plain words with
  small examples; do not show a phoneme alphabet table unless one genuinely helps
  a single comparison.
- Ground the accessibility stakes concretely and briefly (screen readers,
  audiobooks) without turning the piece into an advocacy essay.
- Keep reported fact and estimate distinct: where the literature reports a
  homograph-accuracy figure, cite it; do not invent one.

## Source policy (the-mechanics / lesson)

Floor: at least 8 sources, at least 4 primary, at least 1 secondary. Primaries
are the papers that own each step: a text-normalization paper (e.g. Sproat &
Jaitly 2016), a G2P paper, a homograph-disambiguation paper with a real accuracy
figure, and a neural-TTS paper (WaveNet and/or Tacotron 2). Cite documentation of
a real, named pronunciation failure where available. Every figure from its owner.

## Production policy

Profile balanced. Roles run as Claude Code sub-agents using this checkout's `nb`.
Model "capable" for every stage. Actual models this run: writing-coach sonnet
(low), researcher opus (high), writer sonnet (medium), editor opus (high). No
`required` directive to deviate from.

## Recent-pattern habits not to inherit

- The-mechanics openers often name the withheld behavior ("The answer it won't
  give" / "A sentence the doctor never heard"). Name this lesson's first heading
  for its own first step, not that mold.
- Closer headings shaped "The tendency no decoding rule removes" / "Where the same
  X lives" recur, and the series prompt invites a "where it lives today" close.
  Write the close around this lesson's own nouns and vary its construction.
- `spec/headlines.md` bans the comma-triad and semicolon-reversal dek molds.
  Commit the dek to this lesson's specific find (a written form read as the wrong
  word before any audio exists).

## Neighboring articles in tonight's run (keep distinct)

the-evidence/computing-machinery-and-intelligence; the-instruments/training-cost;
what-could-go-wrong/recommender-radicalization; when-ai-breaks/amazon-recruiting.
This is tonight's only how-does-it-work mechanics piece.
