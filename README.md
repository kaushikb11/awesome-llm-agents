# Awesome LLM Agent Frameworks [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of open-source frameworks, runtimes and tooling for building LLM
agents. Metrics refresh weekly. (Last updated: 2026-08-14)

To suggest a project, see [CONTRIBUTING.md](CONTRIBUTING.md) — entries live in
`data/frameworks/`, and this file is generated from them.

## Contents

- [Core Frameworks](#core-frameworks) (12)
- [Multi-Agent Orchestration](#multi-agent-orchestration) (10)
- [Low-Code & Visual Builders](#low-code-visual-builders) (2)
- [Retrieval & Data](#retrieval-data) (2)
- [Agent Infrastructure](#agent-infrastructure) (2)
- [Safety, Security & Evaluation](#safety-security-evaluation) (2)
- [Domain-Specific Agents](#domain-specific-agents) (5)
- [Research & Experimental](#research-experimental) (5)
- [Autonomous Agents (2023 wave)](#autonomous-agents-2023-wave) (4)
- [Inactive](#inactive) (5)

## Core Frameworks

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [LangChain](https://github.com/langchain-ai/langchain) | 144,183 | Python | MIT | 2026-08 | Compose LLM apps from modular pieces |
| [Smolagents](https://github.com/huggingface/smolagents) | 28,795 | Python | Apache-2.0 | 2026-07 | Minimal agents that write code to act |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 28,447 | C# | MIT | 2026-08 | Plugin-based AI integration for .NET and Python |
| [Mastra](https://github.com/mastra-ai/mastra) | 27,182 | TypeScript | Other | 2026-08 | TypeScript agents with RAG and observability |
| [Google ADK](https://github.com/google/adk-python) | 21,098 | Python | Apache-2.0 | 2026-08 | Code-first agents that deploy to Vertex AI |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai) | 19,273 | Python | MIT | 2026-08 | Type-safe agents on Pydantic with structured output |
| [Tambo](https://github.com/tambo-ai/tambo) | 11,163 | TypeScript | MIT | 2026-08 | React components rendered by AI at runtime |
| [Upsonic](https://github.com/upsonic/upsonic) | 7,938 | Python | MIT | 2026-06 | Agents with MCP and isolated execution |
| [AGiXT](https://github.com/Josh-XT/AGiXT) | 3,209 | Python | MIT | 2026-07 | Multi-provider agent platform with command chaining |
| [ix](https://github.com/kreneskyp/ix) | 1,044 | Python | MIT | 2026-01 | Autonomous agents with a visual workflow builder |
| [Axar](https://github.com/axar-ai/axar) | 163 | TypeScript | Apache-2.0 | 2026-02 | Minimal TypeScript agents with Zod validation |
| [Neurolink](https://github.com/juspay/neurolink) | 121 | TypeScript | MIT | 2026-08 | One interface across 12+ LLM providers |

## Multi-Agent Orchestration

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 69,806 | Python | MIT | 2026-01 | Agents role-play a software company |
| [AutoGen](https://github.com/microsoft/autogen) | 60,407 | Python | CC-BY-4.0 | 2026-04 | Conversational multi-agent systems |
| [CrewAI](https://github.com/crewAIInc/crewAI) | 57,049 | Python | MIT | 2026-08 | Orchestrate role-playing agent crews |
| [CAMEL](https://github.com/camel-ai/camel) | 17,581 | Python | Apache-2.0 | 2026-08 | Role-playing agents for studying agent society |
| [PraisonAI](https://github.com/MervinPraison/PraisonAI) | 8,839 | Python | MIT | 2026-08 | Multi-agent workflows with self-reflection |
| [OpenAgents](https://github.com/openagents-org/openagents) | 3,986 | TypeScript | Apache-2.0 | 2026-08 | Agent networks over WebSocket, gRPC, MCP and A2A |
| [hcom](https://github.com/aannoo/hcom) | 446 | Rust | MIT | 2026-08 | Agents message and spawn each other in terminals |
| [Flock](https://github.com/whiteducksoftware/flock) | 117 | Python | MIT | 2026-08 | Declarative agents via blackboard architecture |
| [Quorum](https://github.com/Detrol/quorum-cli) | 114 | Python | Other | 2026-01 | Structured multi-agent debate in the terminal |
| [auto-co](https://github.com/NikitaDmitrieff/auto-co-meta) | 41 | TypeScript | MIT | 2026-06 | 14 agents run a company in a continuous loop |

## Low-Code & Visual Builders

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Dify](https://github.com/langgenius/dify) | 152,362 | TypeScript | Other | 2026-08 | Visual orchestration for LLM apps and agents |
| [Kiln AI](https://github.com/Kiln-AI/Kiln) | 5,022 | Python | Other | 2026-08 | Desktop app for evals, RAG and fine-tuning |

## Retrieval & Data

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [LlamaIndex](https://github.com/run-llama/llama_index) | 51,625 | Python | MIT | 2026-08 | Connects LLMs to 160+ data sources |
| [Haystack](https://github.com/deepset-ai/haystack) | 26,201 | Python | Apache-2.0 | 2026-08 | Composable pipelines for search and RAG |

## Agent Infrastructure

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Mem0](https://github.com/mem0ai/mem0) | 63,208 | Python | Apache-2.0 | 2026-08 | Memory layer that persists across agent sessions |
| [AgentField](https://github.com/Agent-Field/agentfield) | 2,509 | Go | Apache-2.0 | 2026-08 | Agent identity and RPC using W3C DIDs |

## Safety, Security & Evaluation

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Agentic Radar](https://github.com/splx-ai/agentic-radar) | 1,030 | Python | Apache-2.0 | 2025-11 | Scans agent workflows for CVE and OWASP issues |
| [Cordum](https://github.com/cordum-io/cordum) | 495 | Go | Other | 2026-08 | Evaluates policy before an agent action dispatches |

## Domain-Specific Agents

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [DeepAnalyze](https://github.com/ruc-datalab/DeepAnalyze) | 4,523 | Python | MIT | 2026-07 | Autonomous data science without fixed workflows |
| [RAI](https://github.com/RobotecAI/rai) | 569 | Python | Apache-2.0 | 2026-08 | Agent framework for robotics, built on ROS 2 |
| [CleverBee](https://github.com/SureScaleAI/cleverbee) | 302 | Python | AGPL-3.0 | 2026-01 | Deep research agent that browses with Playwright |
| [GenoMAS](https://github.com/Liu-Hy/GenoMAS) | 135 | Python | MIT | 2026-04 | Multi-agent pipeline for genomics data analysis |
| [everyrow](https://github.com/futuresearch/futuresearch-python) | 51 | Python | MIT | 2026-08 | Run LLM agents over pandas DataFrames |

## Research & Experimental

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [EvoAgentX](https://github.com/EvoAgentX/EvoAgentX) | 3,228 | Python | Other | 2026-07 | Agent workflows that evolve and self-optimize |
| [AgentFlow](https://github.com/lupantech/AgentFlow) | 2,002 | Python | MIT | 2026-02 | Trainable multi-agent system using Flow-GRPO |
| [Cache-to-Cache](https://github.com/thu-nics/C2C) | 428 | Python | Apache-2.0 | 2026-03 | Agents exchange meaning directly via KV-cache |
| [AgentSquare](https://github.com/tsinghua-fib-lab/AgentSquare) | 229 | HTML | — | 2025-11 | Automatic search over modular agent designs |
| [agent-opt](https://github.com/future-agi/agent-opt) | 73 | Python | Apache-2.0 | 2026-06 | Optimizes prompts and agent workflows |

## Autonomous Agents (2023 wave)

The 2023 autonomous-agent wave. Listed for their influence; several are no longer
actively developed.

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 186,591 | Python | Other | 2026-08 | The original autonomous GPT-4 agent loop |
| [OpenManus](https://github.com/FoundationAgents/OpenManus) | 57,960 | Python | MIT | 2026-02 | General-purpose agent, no invite code needed |
| [BabyAGI](https://github.com/yoheinakajima/babyagi) | 22,348 | Python | — | 2026-01 | Minimal task-driven autonomous agent loop |
| [XAgent](https://github.com/OpenBMB/XAgent) | 8,531 | Python | Apache-2.0 | 2026-07 | Autonomous agent with planning and tool learning |

## Inactive

Archived, or no push in over 12 months. Kept because they are widely referenced and
readers benefit from knowing their status.

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Flowise](https://github.com/FlowiseAI/Flowise) | 55,362 | TypeScript | Other | 2026-08 (archived) | Drag-and-drop builder for LLM flows |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | 17,653 | Python | MIT | 2025-01 | Autonomous agent platform with a tool framework |
| [OpenAgents (XLang)](https://github.com/xlang-ai/OpenAgents) | 4,854 | Python | Apache-2.0 | 2024-11 | Platform for data, web and coding agents |
| [Agent Protocol](https://github.com/agi-inc/agent-protocol) | 1,457 | Python | MIT | 2025-04 | Standard interface for agent interoperability |
| [AI Legion](https://github.com/eumemic/ai-legion) | 1,433 | TypeScript | MIT | 2025-05 | TypeScript swarm of autonomous agents |

## License

[CC0 1.0 Universal](LICENSE) — to the extent possible under law, the contributors
have waived all copyright and related rights to this work.
