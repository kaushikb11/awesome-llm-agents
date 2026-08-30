# Awesome LLM Agent Frameworks [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of open-source frameworks, runtimes and tooling for building LLM
agents. Metrics refresh weekly. (Last updated: 2026-08-30)

To suggest a project, see [CONTRIBUTING.md](CONTRIBUTING.md) — entries live in
`data/frameworks/`, and this file is generated from them.

## Contents

- [Core Frameworks](#core-frameworks) (34)
- [Multi-Agent Orchestration](#multi-agent-orchestration) (14)
- [CLI Agent Harnesses](#cli-agent-harnesses) (14)
- [Low-Code & Visual Builders](#low-code-visual-builders) (3)
- [Retrieval & Data](#retrieval-data) (2)
- [Memory & Context](#memory-context) (6)
- [Agent Infrastructure](#agent-infrastructure) (3)
- [Safety, Security & Evaluation](#safety-security-evaluation) (6)
- [Domain-Specific Agents](#domain-specific-agents) (11)
- [Research & Experimental](#research-experimental) (7)
- [Autonomous Agents (2023 wave)](#autonomous-agents-2023-wave) (4)
- [Inactive](#inactive) (5)

## Core Frameworks

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [OpenClaw](https://github.com/openclaw/openclaw) | 388,028 | TypeScript | Other | 2026-08 | Personal AI assistant that runs on any platform |
| [LangChain](https://github.com/langchain-ai/langchain) | 145,258 | Python | MIT | 2026-08 | Compose LLM apps from modular pieces |
| [Smolagents](https://github.com/huggingface/smolagents) | 29,045 | Python | Apache-2.0 | 2026-08 | Minimal agents that write code to act |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 28,518 | C# | MIT | 2026-08 | Plugin-based AI integration for .NET and Python |
| [Mastra](https://github.com/mastra-ai/mastra) | 27,563 | TypeScript | Other | 2026-08 | TypeScript agents with RAG and observability |
| [Google ADK](https://github.com/google/adk-python) | 21,327 | Python | Apache-2.0 | 2026-08 | Code-first agents that deploy to Vertex AI |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai) | 19,580 | Python | MIT | 2026-08 | Type-safe agents on Pydantic with structured output |
| [Tambo](https://github.com/tambo-ai/tambo) | 11,170 | TypeScript | MIT | 2026-08 | React components rendered by AI at runtime |
| [Hive](https://github.com/aden-hive/hive) | 10,987 | Python | Apache-2.0 | 2026-08 | Multi-agent harness aimed at production |
| [Openwork](https://github.com/accomplish-ai/coworker) | 10,925 | — | — | 2026-08 | Open-source AI coworker platform |
| [Upsonic](https://github.com/upsonic/upsonic) | 7,948 | Python | MIT | 2026-06 | Agents with MCP and isolated execution |
| [Atomic Agents](https://github.com/Eigenwise/atomic-agents) | 6,211 | Python | MIT | 2026-08 | Compose agents from small interchangeable parts |
| [OpenAgent](https://github.com/the-open-agent/openagent) | 5,584 | Go | Apache-2.0 | 2026-08 | Personal assistant built on LLM, RAG and agent loops |
| [AG2](https://github.com/ag2ai/ag2) | 4,893 | Python | Apache-2.0 | 2026-08 | Community fork of AutoGen, now an AgentOS |
| [AGiXT](https://github.com/Josh-XT/AGiXT) | 3,214 | Python | MIT | 2026-07 | Multi-provider agent platform with command chaining |
| [trpc-agent-go](https://github.com/trpc-group/trpc-agent-go) | 1,748 | Go | Apache-2.0 | 2026-08 | Go framework for agents with graph workflows |
| [ConnectOnion](https://github.com/openonion/connectonion) | 1,480 | Python | Apache-2.0 | 2026-08 | Python framework focused on agent collaboration |
| [Oh My Hermes](https://github.com/rlaope/oh-my-hermes) | 1,273 | Python | MIT | 2026-08 | Harness with optimized tools and memory |
| [Ouroboros](https://github.com/razzant/ouroboros) | 1,239 | Python | MIT | 2026-08 | Agent runtime with reviewed self-modification |
| [LightAgent](https://github.com/wanxingai/LightAgent) | 1,214 | Python | Apache-2.0 | 2026-08 | Lightweight Python agents with tools and memory |
| [Agentlas OS](https://github.com/agentlas-ai/Agentlas-OS) | 1,116 | Python | Apache-2.0 | 2026-08 | Specialist agent hub with temporary orchestrators |
| [ix](https://github.com/kreneskyp/ix) | 1,046 | Python | MIT | 2026-01 | Autonomous agents with a visual workflow builder |
| [Promptise Foundry](https://github.com/promptise-com/Foundry) | 869 | Python | Apache-2.0 | 2026-08 | Agentic framework with controllable reasoning |
| [Aeon](https://github.com/aeonfun/aeon) | 705 | TypeScript | MIT | 2026-08 | Runs unattended on GitHub Actions, self-healing |
| [Octochains](https://github.com/ahmadvh/octochains) | 369 | Python | Other | 2026-08 | Parallel isolated reasoning with an aggregator |
| [OpenProgram](https://github.com/Fzkuji/OpenProgram) | 323 | Python | AGPL-3.0 | 2026-08 | Agents create and refine their own workflows |
| [Axar](https://github.com/axar-ai/axar) | 163 | TypeScript | Apache-2.0 | 2026-02 | Minimal TypeScript agents with Zod validation |
| [Neurolink](https://github.com/juspay/neurolink) | 128 | TypeScript | MIT | 2026-08 | One interface across 12+ LLM providers |
| [Octomind](https://github.com/Muvon/octomind) | 116 | Rust | Apache-2.0 | 2026-08 | Model-agnostic runtime with specialist agents |
| [ProtoLink](https://github.com/nMaroulis/protolink) | 85 | Python | MIT | 2026-08 | Python agents with native A2A communication |
| [NarraNexus](https://github.com/NetMindAI-Open/NarraNexus) | 83 | Python | Apache-2.0 | 2026-08 | Builds nexuses where agent intelligence emerges |
| [ShaprAI](https://github.com/Scottcjn/shaprai) | 70 | Python | MIT | 2026-07 | Sharpens raw models into principled agents |
| [TrashClaw](https://github.com/Scottcjn/trashclaw) | 68 | Python | MIT | 2026-08 | Zero-dependency local agent for old hardware |
| [KodeAgent](https://github.com/barun-saha/kodeagent) | 40 | Python | Apache-2.0 | 2026-08 | Minimal agent engine, deliberately small |

## Multi-Agent Orchestration

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 70,095 | Python | MIT | 2026-01 | Agents role-play a software company |
| [AutoGen](https://github.com/microsoft/autogen) | 60,697 | Python | CC-BY-4.0 | 2026-04 | Conversational multi-agent systems |
| [CrewAI](https://github.com/crewAIInc/crewAI) | 57,807 | Python | MIT | 2026-08 | Orchestrate role-playing agent crews |
| [CAMEL](https://github.com/camel-ai/camel) | 17,651 | Python | Apache-2.0 | 2026-08 | Role-playing agents for studying agent society |
| [PraisonAI](https://github.com/MervinPraison/PraisonAI) | 8,987 | Python | MIT | 2026-08 | Multi-agent workflows with self-reflection |
| [OpenAgents](https://github.com/openagents-org/openagents) | 4,018 | TypeScript | Apache-2.0 | 2026-08 | Agent networks over WebSocket, gRPC, MCP and A2A |
| [hcom](https://github.com/aannoo/hcom) | 468 | Rust | MIT | 2026-08 | Agents message and spawn each other in terminals |
| [Markus](https://github.com/markus-global/markus) | 157 | TypeScript | Apache-2.0 | 2026-08 | Agents coordinate and review each other's work |
| [CommonGround Kernel](https://github.com/Intelligent-Internet/CommonGround) | 149 | Python | Apache-2.0 | 2026-05 | Postgres-backed shared substrate for agent teams |
| [Flock](https://github.com/whiteducksoftware/flock) | 117 | Python | MIT | 2026-08 | Declarative agents via blackboard architecture |
| [Quorum](https://github.com/Detrol/quorum-cli) | 115 | Python | Other | 2026-01 | Structured multi-agent debate in the terminal |
| [OpenAcme](https://github.com/sandydasari/openacme) | 86 | TypeScript | MIT | 2026-07 | Role-specialized agents that self-organize |
| [Hivekeep](https://github.com/MarlBurroW/hivekeep) | 51 | TypeScript | MIT | 2026-08 | Self-hosted team of persistent personal agents |
| [auto-co](https://github.com/NikitaDmitrieff/auto-co-meta) | 42 | TypeScript | MIT | 2026-06 | 14 agents run a company in a continuous loop |

## CLI Agent Harnesses

Tools that run, sandbox or coordinate command-line coding agents such as Claude Code,
Codex and Gemini CLI.

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Atomic Agent](https://github.com/AtomicBot-ai/atomic-agent) | 2,458 | TypeScript | MIT | 2026-08 | Local-first CLI agent for open-weight models |
| [Agent Teams](https://github.com/777genius/agent-teams-ai) | 2,000 | TypeScript | AGPL-3.0 | 2026-08 | Desktop app running coding-agent teams across CLIs |
| [Bernstein](https://github.com/sipyourdrink-ltd/bernstein) | 1,035 | Python | Apache-2.0 | 2026-08 | Deterministic orchestrator for 40+ CLI agents |
| [SwarmClaw](https://github.com/swarmclawai/swarmclaw) | 654 | TypeScript | MIT | 2026-06 | Self-hosted runtime for multi-agent CLI work |
| [h5i](https://github.com/h5i-dev/h5i) | 584 | Rust | Apache-2.0 | 2026-08 | Runs agents in sandboxes, merges the verified result |
| [Dorothy](https://github.com/Charlie85270/Dorothy) | 341 | TypeScript | MIT | 2026-07 | Desktop app to run several CLI agents at once |
| [ClawFleet](https://github.com/clawfleet/ClawFleet) | 172 | Go | MIT | 2026-04 | Deploys isolated agent instances via Docker |
| [OpenPaw](https://github.com/daxaur/openpaw) | 165 | TypeScript | MIT | 2026-05 | Turns Claude Code into an assistant with 38 skills |
| [ORCH](https://github.com/oxgeneral/ORCH) | 153 | TypeScript | MIT | 2026-08 | One CLI to manage a team of agents on tasks |
| [5dive](https://github.com/5dive-ai/5dive) | 55 | Shell | MIT | 2026-08 | Run a company of named agents on your own server |
| [OpenHermit](https://github.com/HCF-STUDIOS/openhermit) | 53 | TypeScript | MIT | 2026-08 | Deploys agent fleets as long-running services |
| [Agon](https://github.com/AutoResearch-Factory/Agon) | 44 | Python | MIT | 2026-08 | Claude Code plugin for autonomous research loops |
| [TeamHero](https://github.com/sagiyaacoby/TeamHero) | 35 | JavaScript | MIT | 2026-04 | Manage agents like a team, with structured roles |
| [OpenSepia](https://github.com/CelaenoIndustry/OpenSepia) | 34 | Python | MIT | 2026-03 | Nine Claude agents running as an agile team |

## Low-Code & Visual Builders

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Dify](https://github.com/langgenius/dify) | 153,857 | TypeScript | Other | 2026-08 | Visual orchestration for LLM apps and agents |
| [Kiln AI](https://github.com/Kiln-AI/Kiln) | 5,038 | Python | Other | 2026-08 | Desktop app for evals, RAG and fine-tuning |
| [Heym](https://github.com/heymrun/heym) | 1,056 | Python | Other | 2026-08 | Visual builder for agentic workflow automation |

## Retrieval & Data

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [LlamaIndex](https://github.com/run-llama/llama_index) | 51,917 | Python | MIT | 2026-08 | Connects LLMs to 160+ data sources |
| [Haystack](https://github.com/deepset-ai/haystack) | 26,362 | Python | Apache-2.0 | 2026-08 | Composable pipelines for search and RAG |

## Memory & Context

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Hindsight](https://github.com/vectorize-io/hindsight) | 21,673 | Python | MIT | 2026-08 | Agent memory with retain, recall and reflect |
| [Caura](https://github.com/caura-ai/caura) | 469 | Python | Apache-2.0 | 2026-08 | Governed shared memory for fleets of agents |
| [AnimaWorks](https://github.com/xuiltul/animaworks) | 254 | Python | Apache-2.0 | 2026-08 | Organization-as-code with brain-inspired memory |
| [OMEGA](https://github.com/omega-memory/omega-memory) | 210 | Python | Apache-2.0 | 2026-08 | Persistent memory for coding agents over MCP |
| [Perseus](https://github.com/Perseus-Computing-LLC/perseus) | 42 | Python | MIT | 2026-08 | Resolves verified workspace state before a call |
| [Inite Brain](https://github.com/inite-ai/inite-brain-service) | 33 | TypeScript | AGPL-3.0 | 2026-08 | Bitemporal knowledge graph as agent memory |

## Agent Infrastructure

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Mem0](https://github.com/mem0ai/mem0) | 64,334 | Python | Apache-2.0 | 2026-08 | Memory layer that persists across agent sessions |
| [AgentField](https://github.com/Agent-Field/agentfield) | 2,539 | Go | Apache-2.0 | 2026-08 | Agent identity and RPC using W3C DIDs |
| [openma](https://github.com/openma-ai/open-managed-agents) | 250 | TypeScript | Apache-2.0 | 2026-08 | Self-hosted Managed Agents API implementation |

## Safety, Security & Evaluation

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Agentic Radar](https://github.com/splx-ai/agentic-radar) | 1,043 | Python | Apache-2.0 | 2025-11 | Scans agent workflows for CVE and OWASP issues |
| [Cordum](https://github.com/cordum-io/cordum) | 498 | Go | Other | 2026-08 | Evaluates policy before an agent action dispatches |
| [Greywall](https://github.com/GreyhavenHQ/greywall) | 289 | Go | Apache-2.0 | 2026-08 | Deny-by-default sandbox for coding agents |
| [Kitaru](https://github.com/zenml-io/kitaru) | 270 | Python | Apache-2.0 | 2026-08 | Record, replay and improve agents in production |
| [RapidFire AI](https://github.com/RapidFireAI/rapidfireai) | 167 | JavaScript | Apache-2.0 | 2026-08 | Experiment harness for RAG and fine-tuning runs |
| [APort Guardrails](https://github.com/aporthq/aport-agent-guardrails) | 25 | Shell | Other | 2026-08 | Pre-action authorization policy for agent calls |

## Domain-Specific Agents

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [DeepAnalyze](https://github.com/ruc-datalab/DeepAnalyze) | 4,573 | Python | MIT | 2026-08 | Autonomous data science without fixed workflows |
| [Darkmoon](https://github.com/ASCIT31/Dark-Moon) | 878 | Python | GPL-3.0 | 2026-08 | Autonomous pentesting across web, cloud and AD |
| [RAI](https://github.com/RobotecAI/rai) | 575 | Python | Apache-2.0 | 2026-08 | Agent framework for robotics, built on ROS 2 |
| [CleverBee](https://github.com/SureScaleAI/cleverbee) | 302 | Python | AGPL-3.0 | 2026-01 | Deep research agent that browses with Playwright |
| [text2sql-framework](https://github.com/Text2SqlAgent/text2sql-framework) | 155 | Python | MIT | 2026-08 | Text-to-SQL agent that explores schema, not RAG |
| [GenoMAS](https://github.com/Liu-Hy/GenoMAS) | 134 | Python | MIT | 2026-04 | Multi-agent pipeline for genomics data analysis |
| [wechat-mac-rpa](https://github.com/wq19901103wq/wechat-mac-rpa) | 88 | Python | MIT | 2026-08 | Visual agent automating WeChat on macOS |
| [Omni-Rewriter](https://github.com/WayneJin0918/Omni-Rewriter) | 82 | Python | Apache-2.0 | 2026-08 | Prompt expansion for image and video generation |
| [DNA Claude Analysis](https://github.com/shmlkv/dna-claude-analysis) | 57 | Python | MIT | 2026-03 | Explore your genome in natural language |
| [everyrow](https://github.com/futuresearch/futuresearch-python) | 54 | Python | MIT | 2026-08 | Run LLM agents over pandas DataFrames |
| [Inalpha](https://github.com/mirror29/inalpha) | 32 | Python | AGPL-3.0 | 2026-08 | Quant agents that pick factors that still work |

## Research & Experimental

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [EvoAgentX](https://github.com/EvoAgentX/EvoAgentX) | 3,274 | Python | Other | 2026-08 | Agent workflows that evolve and self-optimize |
| [AgentFlow](https://github.com/lupantech/AgentFlow) | 2,021 | Python | MIT | 2026-02 | Trainable multi-agent system using Flow-GRPO |
| [Cache-to-Cache](https://github.com/thu-nics/C2C) | 435 | Python | Apache-2.0 | 2026-03 | Agents exchange meaning directly via KV-cache |
| [AgentSquare](https://github.com/tsinghua-fib-lab/AgentSquare) | 230 | HTML | — | 2025-11 | Automatic search over modular agent designs |
| [GNAP](https://github.com/farol-team/gnap) | 83 | — | MIT | 2026-03 | Git-native protocol draft for agent coordination |
| [agent-opt](https://github.com/future-agi/agent-opt) | 73 | Python | Apache-2.0 | 2026-06 | Optimizes prompts and agent workflows |
| [AVP](https://github.com/VectorArc/avp-python) | 26 | Python | Apache-2.0 | 2026-04 | Transfers KV-cache between agents, not text |

## Autonomous Agents (2023 wave)

The 2023 autonomous-agent wave. Listed for their influence; several are no longer
actively developed.

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 186,994 | Python | Other | 2026-08 | The original autonomous GPT-4 agent loop |
| [OpenManus](https://github.com/FoundationAgents/OpenManus) | 58,114 | Python | MIT | 2026-08 | General-purpose agent, no invite code needed |
| [BabyAGI](https://github.com/yoheinakajima/babyagi) | 22,358 | Python | — | 2026-01 | Minimal task-driven autonomous agent loop |
| [XAgent](https://github.com/OpenBMB/XAgent) | 8,544 | Python | Apache-2.0 | 2026-07 | Autonomous agent with planning and tool learning |

## Inactive

Archived, or no push in over 12 months. Kept because they are widely referenced and
readers benefit from knowing their status.

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Flowise](https://github.com/FlowiseAI/Flowise) | 55,399 | TypeScript | Other | 2026-08 (archived) | Drag-and-drop builder for LLM flows |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | 17,670 | Python | MIT | 2025-01 | Autonomous agent platform with a tool framework |
| [OpenAgents (XLang)](https://github.com/xlang-ai/OpenAgents) | 4,859 | Python | Apache-2.0 | 2024-11 | Platform for data, web and coding agents |
| [Agent Protocol](https://github.com/agi-inc/agent-protocol) | 1,455 | Python | MIT | 2025-04 | Standard interface for agent interoperability |
| [AI Legion](https://github.com/eumemic/ai-legion) | 1,435 | TypeScript | MIT | 2025-05 | TypeScript swarm of autonomous agents |

## License

[CC0 1.0 Universal](LICENSE) — to the extent possible under law, the contributors
have waived all copyright and related rights to this work.
