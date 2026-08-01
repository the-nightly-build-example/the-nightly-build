# Evidence record — the-mechanics/tool-use

The evidence supports the commission's full spine: tools are described to the
model as schema text in the prompt; the model's "call" is a structured text
span (JSON) it emits like any other tokens; a harness external to the model
parses that span, executes it, and pastes the result back as new tokens; the
model resumes on the extended context. Both major labs state this contract
explicitly and in near-identical language — Anthropic's docs say the model
"never executes anything on its own," and OpenAI's cookbook says the API
"will not actually execute any function calls." The ReAct paper is solid
primary ground for the reason+act+observe loop and supplies a verbatim
Thought/Action/Observation trace and hard numbers. The Toolformer paper is
solid primary ground that tool use is a trained (self-supervised
fine-tuning), not architectural, behavior, and its own results paper shows
that training does not universally help — Toolformer still loses to plain
GPT-3 on two of five QA benchmarks, a useful complication against a naive
"tools always help" gloss. MCP's docs are strong primary ground for the
"harness is a real, external program" claim, including pseudocode showing an
"AI application" intercepting a tool call, dispatching it to a server, and
handing the result back to the model. The thin spot: reliability of argument
filling and "why does the model decide to call a tool now" are, by the
commission's own framing, open engineering questions — the evidence here
establishes the boundary (Anthropic's docs concede models sometimes guess
missing parameters) but not a settled mechanistic answer, because none
exists in any source read. OpenAI's own platform docs (platform.openai.com)
returned persistent 503s across five attempts and an archive.org mirror was
unreachable in this environment; the equivalent OpenAI-authored content was
recovered instead from OpenAI's official cookbook, which is hosted under
OpenAI's own developers.openai.com domain and carries no separate byline —
treated here as an OpenAI primary source of equal standing.

## Sources

### 1. Anthropic — "Tool use with Claude" (overview)
- URL: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
  (canonical/marketed URL https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview
  302-redirects here; both resolve to the same document)
- Classification: **Primary.** Anthropic's own API documentation, the owning
  source of the Claude tool-use request/response format.
- Establishes firsthand: the exact JSON shapes for a tool definition
  (`input_schema`), the assistant's `tool_use` content block, and the
  follow-up `tool_result` block; the `stop_reason: "tool_use"` signal; the
  distinction between client tools (execute in the caller's application) and
  server tools (execute on Anthropic's infrastructure).
- Verbatim passages:
  - "Tool use lets Claude call functions that you define or that Anthropic
    provides. Claude determines when to call a tool based on the user's
    request and the tool's description. It then returns a structured call
    that your application executes (client tools) or that Anthropic
    executes (server tools)."
  - "Client tools ... run in your application. Claude responds with
    `stop_reason: "tool_use"` and one or more `tool_use` blocks. Your code
    executes the operation and sends back a `tool_result`."
  - Worked `get_weather` example (full request/response round trip, JSON
    verbatim below in Source assets / Numbers): tool schema defines a
    `location` string parameter; Claude's response contains a `tool_use`
    block `{"type":"tool_use","name":"get_weather","input":{"location":
    "San Francisco, CA"}}`-shaped object (id field also present); the
    caller executes the lookup out of band and returns
    `{"type":"tool_result","tool_use_id": ..., "content": "15 degrees
    Celsius, partly cloudy"}`; final output: "The current weather in San
    Francisco is 15 degrees Celsius with partly cloudy skies."
  - On unfilled arguments: "If the user's prompt doesn't include enough
    information to fill all the required parameters for a tool, Claude
    Opus is much more likely to recognize that a parameter is missing and
    ask for it. Claude Sonnet might ask ... But it might also infer a
    reasonable value ... This behavior is not guaranteed, especially for
    more ambiguous prompts and for less capable models."
- Locators: section "How tool use works" (JSON shapes, stop_reason);
  section "When Claude uses tools" and its "When required parameters are
  missing" accordion (argument-filling reliability).

### 2. Anthropic — "How tool use works" (conceptual/loop page)
- URL: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works
- Classification: **Primary.** Same owning source as #1; this page is
  Anthropic's explicit statement of the agentic loop and the
  model/harness division of labor, distinct content from the overview page.
- Establishes firsthand: the flat statement that the model never executes
  anything; the five-step client-tool loop keyed on `stop_reason`; the
  three buckets of "where tools run" (client user-defined, Anthropic-schema
  client, server-executed); that even server-executed tools run on
  Anthropic's servers, not inside the model.
- Verbatim passages:
  - "The model never executes anything on its own. It emits a structured
    request, your code (or Anthropic's servers) runs the operation, and the
    result flows back into the conversation." (section "The tool-use
    contract" — this is the single cleanest primary-source statement of the
    commission's load-bearing claim.)
  - The five-step loop: "1. Send a request with your `tools` array and the
    user message. 2. Claude responds with `stop_reason: "tool_use"` and one
    or more `tool_use` blocks. 3. Execute each tool. Format the outputs as
    `tool_result` blocks. 4. Send a new request containing the original
    messages, the assistant's response, and a user message with the
    `tool_result` blocks. 5. Repeat from step 2 while `stop_reason` is
    `"tool_use"`."
  - On server tools (the "is any of this built into the model" question):
    "For `web_search`, `web_fetch`, `code_execution`, and `tool_search`,
    Anthropic runs the code. You enable the tool in your request and the
    server handles everything else ... the server-side loop executes the
    operation and feeds the output back to the model before the response
    reaches you." — i.e., even "native"-feeling tools execute on a server,
    outside the model's weights; the model still only ever sees text.
- Locators: sections "The tool-use contract," "Where tools run," "The
  agentic loop (client tools)," "The server-side loop."

### 3. OpenAI — Cookbook, "How to call functions with chat models"
- URL: https://developers.openai.com/cookbook/examples/how_to_call_functions_with_chat_models
  (https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models
  308-redirects here)
- Classification: **Primary.** OpenAI's own official cookbook, hosted on
  OpenAI's developers.openai.com domain; it is the owning source for the
  `tools`/`tool_calls` request-response shape and for OpenAI's explicit
  execution-boundary statement. (platform.openai.com/docs/guides/
  function-calling, the guide this cookbook entry accompanies, returned
  HTTP 503 on five separate fetch attempts across two sessions and an
  archive.org mirror could not be fetched in this environment — see
  Discarded. The cookbook page carries the identical schema and the
  identical execution-boundary claim, so it stands in as the OpenAI
  primary.)
- Establishes firsthand: the `tools` array shape (`{"type":"function",
  "function":{"name":...,"description":...,"parameters":{JSON Schema}}}`);
  the model's output shape (a `tool_calls` array whose entries carry
  `function.name` and `function.arguments` as a JSON-encoded **string**,
  not a native object); and OpenAI's own statement that the API does not
  execute anything.
- Verbatim passages:
  - Tool definition: `{"type": "function", "function": {"name":
    "get_current_weather", "description": "Get the current weather",
    "parameters": {"type": "object", "properties": {"location": {"type":
    "string"}, "format": {"type": "string", "enum": ["celsius",
    "fahrenheit"]}}, "required": ["location", "format"]}}}`
  - Model output: `{"id": "call_k2QgGc9GT9WjxD76GvR0Ot8q", "function":
    {"name": "get_current_weather", "arguments": "{\"location\":
    \"Glasgow, Scotland\", \"format\": \"celsius\"}"}, "type": "function"}`
  - Execution boundary: "The API will not actually execute any function
    calls. It is up to developers to execute function calls using model
    outputs."
- Locators: body of the cookbook notebook, sections describing the request
  format and the `tool_calls` response field.

### 4. Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models" (arXiv:2210.03629)
- URLs: https://arxiv.org/abs/2210.03629 (abstract/landing page, confirmed
  live) and https://ar5iv.labs.arxiv.org/html/2210.03629 (arXiv-hosted
  HTML mirror of the same paper, used to read the full text, figures, and
  results tables cited below)
- Classification: **Primary.** The paper is the owning source of the
  reason+act+observe ("ReAct") prompting method named in the commission.
- Establishes firsthand: that interleaving free-text "Thought" reasoning
  steps with discrete "Action" steps (each of which queries an external
  environment, e.g., a Wikipedia API) and receiving back an "Observation"
  reduces hallucination and improves task success versus reasoning-only or
  acting-only baselines, across QA, fact verification, and two interactive
  environments.
- Verbatim passages:
  - Abstract: "While large language models (LLMs) have demonstrated
    impressive performance across tasks in language understanding and
    interactive decision making, their abilities for reasoning (e.g.
    chain-of-thought prompting) and acting (e.g. action plan generation)
    have primarily been studied as separate topics. In this paper, we
    explore the use of LLMs to generate both reasoning traces and
    task-specific actions in an interleaved manner, allowing for greater
    synergy between the two: reasoning traces help the model induce,
    track, and update action plans as well as handle exceptions, while
    actions allow it to interface with and gather additional information
    from external sources such as knowledge bases or environments. We
    apply our approach, named ReAct, to a diverse set of language and
    decision making tasks and demonstrate its effectiveness over
    state-of-the-art baselines in addition to improved human
    interpretability and trustworthiness."
  - Example trajectory (HotpotQA): "Thought 1 I need to search Colorado
    orogeny, find the area that the eastern sector of the Colorado orogeny
    extends into, then find the elevation range of the area. Action 1
    Search[Colorado orogeny] Observation 1 The Colorado orogeny was an
    episode of mountain building (an orogeny) in Colorado and surrounding
    areas."
  - Definition of an action: "actions allow it to interface with and
    gather additional information from external sources such as knowledge
    bases or environments."
  - Figure 1 caption: "(1) Comparison of 4 prompting methods, (a)
    Standard, (b) Chain-of-thought (CoT, Reason Only), (c) Act-only, and
    (d) [ReAct] (Reason+Act), solving a HotpotQA ... question. (2)
    Comparison of (a) Act-only and (b) [ReAct] prompting to solve an
    AlfWorld ... game."
  - Results, hallucination (Table 2 / Section 3.3): CoT's false-positive
    (hallucination-driven) rate on the sampled failure set is 14% versus
    6% for ReAct; hallucination accounts for 56% of CoT's failure modes
    versus 0% for ReAct in the same analysis.
  - Results, ALFWorld (Table 3): "the best [ReAct] trial achieves an
    average success rate of 71%, significantly outperforming the best Act
    (45%) and BUTLER (37%) trials" — a 34-percentage-point gap over the
    imitation-learning BUTLER baseline.
  - Results, WebShop (Table 4): ReAct reaches 40.0% success rate versus a
    28.7% imitation+reinforcement-learning baseline; the paper describes
    this as "an absolute 10% improvement over the previous best success
    rate."
- Locators: Abstract; Section 2 (method, action definition); Figure 1;
  Section 3.3 and Table 2 (HotpotQA/Fever hallucination analysis); Section
  4 and Tables 3–4 (ALFWorld, WebShop).

### 5. Schick et al., "Toolformer: Language Models Can Teach Themselves to Use Tools" (arXiv:2302.04761)
- URLs: https://arxiv.org/abs/2302.04761 (abstract/landing page, confirmed
  live) and https://ar5iv.labs.arxiv.org/html/2302.04761 (full-text
  mirror used for the passages and table numbers below)
- Classification: **Primary.** The paper is the owning source for the
  claim that tool-calling is produced by training (self-supervised
  fine-tuning on a base model), not by an architectural change.
- Establishes firsthand: how an API call is encoded purely as text inside
  the token stream using special marker tokens; that generation is
  paused, the call executed, and the result spliced back into the same
  text stream; and that the whole capability is taught to an existing
  pretrained model (GPT-J, 6.7B parameters) via a self-supervised
  fine-tuning procedure that keeps or discards each candidate API call
  based on whether it measurably helps predict the following tokens.
- Verbatim passages:
  - Abstract: "Language models (LMs) exhibit remarkable abilities to solve
    new tasks from just a few examples or textual instructions, especially
    at scale. They also, paradoxically, struggle with basic functionality,
    such as arithmetic or factual lookup, where much simpler and smaller
    models excel. In this paper, we show that LMs can teach themselves to
    use external tools via simple APIs and achieve the best of both
    worlds. We introduce Toolformer, a model trained to decide which APIs
    to call, when to call them, what arguments to pass, and how to best
    incorporate the results into future token prediction."
  - Text encoding of a call: an API call is represented as a tuple
    c=(ac, ic) — API name and input — written inline using the special
    tokens "<API>", "</API>" and "→", e.g. `<API>api_name(input)</API>`,
    and once executed, `<API>api_name(input)→result</API>`.
  - Execution interrupts generation: "When generating text with M after
    finetuning with our approach, we perform regular decoding until M
    produces the '→' token, indicating that it next expects the response
    for an API call. At this point, we interrupt the decoding process,
    call the appropriate API to get a response, and continue the decoding
    process after inserting both the response and the </API> token."
  - Trained, not architectural: "We use a self-supervised loss to
    determine which of these API calls actually help the model in
    predicting future tokens. Finally, we finetune the LM itself on the
    API calls that it considers useful."
  - Tools covered: calculator, a question-answering system, two search
    engines, a machine translation system, and a calendar lookup.
- Locators: Abstract; Section 2 (method: API call format, the "→"
  interruption mechanism, self-supervised filtering and fine-tuning);
  Table 3 (LAMA factual-lookup subsets); Table 4 (math word-problem
  benchmarks); Table 5 (question answering).

### 6. Model Context Protocol — "What is the Model Context Protocol (MCP)?"
- URL: https://modelcontextprotocol.io/introduction
- Classification: **Primary.** MCP's own specification site; owning
  source for what the protocol is and who its parties are.
- Establishes firsthand: the framing of MCP as a standard connecting "AI
  applications" (not models) to external tools, data, and workflows.
- Verbatim passage: "MCP (Model Context Protocol) is an open-source
  standard for connecting AI applications to external systems ... Using
  MCP, AI applications like Claude or ChatGPT can connect to data sources
  ..., tools ... and workflows ... enabling them to access key information
  and perform tasks."
- Locators: opening section, "What is the Model Context Protocol (MCP)?"

### 7. Model Context Protocol — "Architecture overview"
- URL: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture
- Classification: **Primary.** Same owning source as #6; distinct document
  (the architecture spec page) giving the concrete host/client/server
  split and worked JSON-RPC examples the commission asks for as evidence
  "the harness is external code."
- Establishes firsthand: the three-party architecture (MCP Host = the AI
  application; MCP Client = a connector object the host creates per
  server; MCP Server = the program that actually exposes tools); the
  JSON-RPC 2.0 request/response shape for `tools/list` and `tools/call`;
  and explicit pseudocode showing the host application, not the model,
  intercepting a tool call and dispatching it.
- Verbatim passages:
  - "MCP follows a client-server architecture where an MCP host — an AI
    application like Claude Code or Claude Desktop — establishes
    connections to one or more MCP servers. The MCP host accomplishes this
    by creating one MCP client for each MCP server."
  - Tool call request (`tools/call`), full JSON: `{"jsonrpc": "2.0", "id":
    3, "method": "tools/call", "params": {"name": "weather_current",
    "arguments": {"location": "San Francisco", "units": "imperial"}, ...}}`
    with response `{"jsonrpc": "2.0", "id": 3, "result": {"resultType":
    "complete", "content": [{"type": "text", "text": "Current weather in
    San Francisco: 68°F, partly cloudy ..."}]}}`.
  - The harness-is-external-code statement: "When the language model
    decides to use a tool during a conversation, the AI application
    intercepts the tool call, routes it to the appropriate MCP server,
    executes it, and returns the results back to the LLM as part of the
    conversation flow." — followed by pseudocode: `async def
    handle_tool_call(conversation, tool_name, arguments): client =
    app.find_mcp_client_for_tool(tool_name); result = await
    client.call_tool(tool_name, arguments); conversation.add_tool_result
    (result.content)`.
- Locators: sections "Concepts of MCP" → "Participants" (host/client/server
  definitions); "Example" → "Tool Execution (Primitives)" (the `tools/call`
  round trip and the "How This Works in AI Applications" pseudocode block).

### 8. Apideck / Saurabh Rai, "An introduction to function calling and tool use" (blog)
- URL: https://www.apideck.com/blog/llm-tool-use-and-function-calling
- Byline: Saurabh Rai, Developer Relations Engineer at Apideck; published
  January 28, 2025 (per the page).
- Classification: **Secondary.** Apideck is a third-party API-integration
  company writing about model providers' function-calling features it did
  not build; useful as an independent, plainly-written restatement of the
  request/decide/execute/respond loop for a lay reader, not as the owner
  of any claim about a specific model's API.
- Establishes: nothing not already established by the primary docs above;
  useful only to confirm the mechanism is described the same way outside
  the labs' own documentation, and as a possible plain-language framing
  device.
- Verbatim passage: "Function calling allows large language models (LLMs)
  to interact with external tools, APIs, and functions based on user
  input. Instead of generating text alone, the LLM can recognize that a
  specific action needs to happen and request that action from an
  external function."
- Locators: article body, opening explanation of function calling.

## Contradictions

- No source disagrees on the core mechanism: every primary source (Claude
  docs, OpenAI cookbook, MCP docs) independently states that a program
  outside the model — the client application, the MCP host, or (for
  Anthropic's server tools) Anthropic's own servers — performs execution,
  and that the model only emits and receives text. This is convergent, not
  contradictory, evidence and should be reported as such rather than
  padded into a false debate.
- The one place sources pull in different directions is whether execution
  ever happens "inside" the system in a way a reader could mistake for the
  model itself acting. Anthropic's server-executed tools (`web_search`,
  `code_execution`, etc.) run without the developer's application touching
  execution at all — "you enable the tool in your request and the server
  handles everything else" — which is the strongest case for something
  feeling "built into" the assistant. Anthropic's own "how tool use works"
  page forecloses that reading explicitly: those tools still run "on
  Anthropic's infrastructure," i.e., a server process outside the model's
  forward pass, and the model still only sees the result as inserted text
  (`server_tool_use` blocks). This is the honest answer to the
  commission's "seek contradiction" instruction: nothing in any source
  read describes execution happening inside the model weights themselves;
  the axis that varies is only which external program does the executing.
- Toolformer's own results complicate a naive "tool use = better
  performance" gloss, which the commission's angle does not make but a
  drafted paragraph might slip into: on WebQuestions and Natural Questions
  (Table 5), the 6.7B Toolformer trails plain GPT-3 (175B) — 26.3% vs.
  29.0%, and 17.7% vs. 22.6% — even though Toolformer had a search-engine
  tool available. Training a model to call tools does not guarantee the
  tool call is used well or that it beats a much larger model with no
  tools at all.

## Numbers

- **ALFWorld success rate (ReAct paper, Table 3):** ReAct best trial 71%
  vs. best Act-only trial 45% vs. BUTLER (imitation learning) 37%. ReAct's
  margin over BUTLER: 34 percentage points, absolute, on this benchmark's
  task-completion rate.
- **WebShop success rate (ReAct paper, Table 4):** ReAct 40.0% vs. an
  imitation+RL baseline of 28.7%, described in-paper as "an absolute 10%
  improvement over the previous best success rate."
- **Hallucination/false-positive rate in QA/fact-verification failure
  analysis (ReAct paper, Table 2 / Section 3.3):** Chain-of-thought
  prompting shows a 14% false-positive rate vs. ReAct's 6%; hallucination
  is 56% of CoT's failure modes vs. 0% of ReAct's, in the sampled failure
  set the authors analyzed. Denominator: a manually annotated sample of
  model failures on HotpotQA, not the full dataset — treat as a
  qualitative failure-mode comparison, not a population-wide rate.
- **Toolformer vs. GPT-3 on factual lookup, LAMA subsets (Toolformer
  paper, Table 3):** Toolformer (GPT-J, 6.7B parameters) vs. GPT-3 (175B,
  25x more parameters): SQuAD 33.8% vs. 26.8%; Google-RE 11.5% vs. 2.9%;
  T-REx 53.5% vs. 39.8%.
- **Toolformer vs. GPT-3 on math word problems (Toolformer paper, Table
  4):** ASDiv 40.4% vs. 14.0%; SVAMP 29.4% vs. 10.0%; MAWPS 44.0% vs.
  19.8%.
- **Toolformer vs. GPT-3 on open-domain QA, where tool use does not close
  the gap (Toolformer paper, Table 5):** WebQuestions 26.3% vs. 29.0%;
  Natural Questions 17.7% vs. 22.6%. Toolformer still smaller (6.7B vs.
  175B) and still behind here — the counter-case noted under
  Contradictions.
- **Anthropic tool-use system-prompt token overhead (Anthropic tool-use
  overview, "Pricing" table):** using tools adds a fixed system-prompt
  token cost on top of normal input/output tokens, e.g. Claude Sonnet 5:
  354 tokens at `tool_choice: auto`/`none`, 474 tokens at `tool_choice:
  any`/`tool`. Included for completeness; not load-bearing for the
  mechanism argument and likely not needed in the draft.

## Source assets

- **ReAct paper, Figure 1** (arXiv:2210.03629, full text at
  https://ar5iv.labs.arxiv.org/html/2210.03629): a two-panel comparison
  showing the same HotpotQA question answered by four prompting styles
  (Standard / Chain-of-Thought / Act-only / ReAct) and the same AlfWorld
  task solved by Act-only vs. ReAct. A reader can see, panel by panel,
  exactly where a "Thought" line appears, where an "Action" line appears,
  and where an "Observation" line is pasted back in — this is the single
  best visual proof of the interleaved loop the commission's angle
  describes step by step in prose. A crop must keep the Thought/Action/
  Observation labels legible and keep at least one full panel intact
  (cropping mid-panel would sever a Thought from its paired Action).
  Figure sits early in Section 1/2 of the HTML mirror.
- **MCP architecture page, participant diagram** (https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture,
  section "Participants"): a Mermaid diagram showing one "MCP Host (AI
  Application)" box containing multiple MCP Client sub-nodes, each with a
  dedicated connection out to a separate MCP Server (local filesystem,
  local database, remote Sentry). Useful to make concrete that "the
  harness" is a literal box with client objects inside it, separate from
  both the model and the tool. A crop must keep the host boundary box and
  at least two client-to-server connections; the host label ("MCP Host
  (AI Application)") must stay attached to its box.
- **Anthropic tool-use overview, the `get_weather` round trip**
  (https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview,
  section "How tool use works"): not a rendered image, but the JSON of
  the two requests and the intervening `tool_use`/`tool_result` blocks is
  clean enough to set as a labeled code figure/listing rather than prose,
  if the writer wants a second worked example alongside or instead of a
  bespoke one. None of it needs a screenshot; it is already text.
- Toolformer paper: **None found** beyond its results tables (already
  captured under Numbers); the paper's method figure is a schematic of the
  self-supervised filtering pipeline, not something that clarifies the
  "loop runs outside the model" argument better than the quoted sentences
  already do.

## Discarded

- https://platform.openai.com/docs/guides/function-calling — OpenAI's
  official function-calling guide; returned HTTP 503 on repeated fetch
  attempts (at least five, across two different request framings) with no
  content ever retrieved. Not used for any claim. Equivalent OpenAI-owned
  content (same JSON shapes, same execution-boundary statement) was
  recovered instead from OpenAI's official cookbook (Source 3).
- https://platform.openai.com/docs/api-reference/chat/create — same 503
  failure pattern as above; discarded for the same reason.
- https://web.archive.org/web/2026/https://platform.openai.com/docs/guides/function-calling —
  attempted as a fallback for the above; the fetch tool reported it cannot
  reach web.archive.org from this environment. Discarded, not "dead":
  this is an environment limitation, not evidence the page doesn't exist.
- arXiv PDF endpoints (https://arxiv.org/pdf/2210.03629 and
  https://arxiv.org/pdf/2302.04761) — fetched but returned as raw,
  undecoded PDF byte streams the fetch tool could not parse into text.
  Discarded in favor of the ar5iv.labs.arxiv.org HTML mirrors of the same
  two papers, which returned readable text and are cited as the full-text
  location for both papers above; the arxiv.org/abs/ landing pages were
  independently confirmed live and are cited as the canonical/abstract
  URLs.
