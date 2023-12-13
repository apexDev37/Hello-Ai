# II. Memory

> This module includes demos that leverage Langchain [memory] components.

#### Core Components covered

- [ConversationBufferMemory]
- [ConversationBufferWindowMemory]
- [ConversationTokenBufferMemory]
- [ConversationSummaryMemory]

## Introduction

LLMs are inherently stateless. This means they are unable to recall previous inputs or interactions. LLMs are not intended to store any state; each transaction (API request) or prompt is considered a completely new, independent input. This can be difficult in many cases, such as end-user chatbots, where the user wants the chatbot to remember past conversations.

This presents new problems for developers to tackle. The responsibility is then tasked to developers to pragmatically create the "illusion" of memory at the application layer for end-users. One simple approach to this would be to pass all prior conversations as context for each subsequent request or input. This gives the LLM contextual info to respond to earlier conversations. This might seem straightforward, but it introduces new issues to take into account:

- Token-based Price Model  
  Most models use a token-based pricing model for their API end users. As contextual data grows over time, sustaining the illusion of "memory" can become costly. Additional tokens will be used to pass contextual data to the LLM which increases linearly for each subsequent request.

- Performance Implications  
  Given each input requires the inclusion of a complete history of all preceding transactions (input/output). This leads to a continuous increase in the payloads transmitted, consequently impacting throughput, response times, and application latency. Moreover, this influx of data can contribute to the degradation of overall LLM output quality and performance.

Langchain provides simple interfaces to approach handling `memory` in our applications for contexts where it's crucial. These interfaces coupled with efficient retrieval strategies such as caching, retrieval algorithms/data structures (trie, binary search, etc), hashing/indexing, or parallel processing, can provide highly responsive user experiences and robust applications while keeping token-usage costs to a minimum.

## Demos

> Relevant, contextual demos to demonstrate adding memory to applications with Langchain memory utils.

- [ConversationBufferMemory]

| Name              | Script       | Description                                                                                                                  |
| ----------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| Reviving-Memories | `demo-01.py` | Loads and writes a past conversation into the LLM's `memory` context and interactively queries the LLM on the provided data. |

[//]: # "These are reference links used in the body of this note and get stripped out when the markdown processor does 
its job. There is no need to format nicely because it shouldn't be seen. 
Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax"
[memory]: https://python.langchain.com/docs/modules/memory/
[ConversationBufferMemory]: https://python.langchain.com/docs/modules/memory/types/buffer
[ConversationBufferWindowMemory]: https://python.langchain.com/docs/modules/memory/types/buffer_window
[ConversationTokenBufferMemory]: https://python.langchain.com/docs/modules/memory/types/token_buffer
[ConversationSummaryMemory]: https://python.langchain.com/docs/modules/memory/types/summary
