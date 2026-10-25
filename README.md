# Awesome LLM Agent Frameworks [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of open-source frameworks, runtimes and tooling for building LLM
agents. Metrics refresh weekly. (Last updated: 2026-10-25)

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
| [OpenClaw](https://github.com/openclaw/openclaw) | 392,972 | TypeScript | MIT | 2026-10 | Personal AI assistant that runs on any platform |
| [LangChain](https://github.com/langchain-ai/langchain) | 148,400 | Python | MIT | 2026-10 | Compose LLM apps from modular pieces |
| [Smolagents](https://github.com/huggingface/smolagents) | 30,032 | Python | Apache-2.0 | 2026-10 | Minimal agents that write code to act |
| [Mastra](https://github.com/mastra-ai/mastra) | 29,057 | TypeScript | Other | 2026-10 | TypeScript agents with RAG and observability |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 28,695 | C# | MIT | 2026-10 | Plugin-based AI integration for .NET and Python |
| [Google ADK](https://github.com/google/adk-python) | 21,993 | Python | Apache-2.0 | 2026-10 | Code-first agents that deploy to Vertex AI |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai) | 20,845 | Python | MIT | 2026-10 | Type-safe agents on Pydantic with structured output |
| [Tambo](https://github.com/tambo-ai/tambo) | 11,203 | TypeScript | MIT | 2026-10 | React components rendered by AI at runtime |
| [Hive](https://github.com/aden-hive/hive) | 11,123 | Python | Apache-2.0 | 2026-10 | Multi-agent harness aimed at production |
| [Openwork](https://github.com/accomplish-ai/coworker) | 10,832 | — | — | 2026-08 | Open-source AI coworker platform |
| [Upsonic](https://github.com/upsonic/upsonic) | 7,963 | Python | MIT | 2026-06 | Agents with MCP and isolated execution |
| [Atomic Agents](https://github.com/Eigenwise/atomic-agents) | 6,304 | Python | MIT | 2026-10 | Compose agents from small interchangeable parts |
| [OpenAgent](https://github.com/the-open-agent/openagent) | 5,709 | Go | Apache-2.0 | 2026-10 | Personal assistant built on LLM, RAG and agent loops |
| [AG2](https://github.com/ag2ai/ag2) | 5,016 | Python | Apache-2.0 | 2026-10 | Community fork of AutoGen, now an AgentOS |
| [Oh My Hermes](https://github.com/rlaope/oh-my-hermes) | 3,972 | Python | MIT | 2026-10 | Harness with optimized tools and memory |
| [AGiXT](https://github.com/Josh-XT/AGiXT) | 3,216 | Python | MIT | 2026-07 | Multi-provider agent platform with command chaining |
| [trpc-agent-go](https://github.com/trpc-group/trpc-agent-go) | 1,876 | Go | Apache-2.0 | 2026-10 | Go framework for agents with graph workflows |
| [Agentlas OS](https://github.com/agentlas-ai/Agentlas-OS) | 1,583 | Python | Apache-2.0 | 2026-10 | Specialist agent hub with temporary orchestrators |
| [Ouroboros](https://github.com/razzant/ouroboros) | 1,583 | Python | MIT | 2026-10 | Agent runtime with reviewed self-modification |
| [ConnectOnion](https://github.com/openonion/connectonion) | 1,501 | Python | Apache-2.0 | 2026-10 | Python framework focused on agent collaboration |
| [LightAgent](https://github.com/wanxingai/LightAgent) | 1,237 | Python | Apache-2.0 | 2026-09 | Lightweight Python agents with tools and memory |
| [ix](https://github.com/kreneskyp/ix) | 1,045 | Python | MIT | 2026-10 | Autonomous agents with a visual workflow builder |
| [Promptise Foundry](https://github.com/promptise-com/Foundry) | 892 | Python | Apache-2.0 | 2026-10 | Agentic framework with controllable reasoning |
| [Aeon](https://github.com/aeonfun/aeon) | 782 | JavaScript | MIT | 2026-10 | Runs unattended on GitHub Actions, self-healing |
| [Octochains](https://github.com/ahmadvh/octochains) | 377 | Python | Other | 2026-10 | Parallel isolated reasoning with an aggregator |
| [Octomind](https://github.com/Muvon/octomind) | 179 | Rust | Apache-2.0 | 2026-10 | Model-agnostic runtime with specialist agents |
| [Axar](https://github.com/axar-ai/axar) | 166 | TypeScript | Apache-2.0 | 2026-02 | Minimal TypeScript agents with Zod validation |
| [Neurolink](https://github.com/juspay/neurolink) | 157 | TypeScript | MIT | 2026-10 | One interface across 12+ LLM providers |
| [NarraNexus](https://github.com/NetMindAI-Open/NarraNexus) | 92 | Python | Apache-2.0 | 2026-10 | Builds nexuses where agent intelligence emerges |
| [ProtoLink](https://github.com/nMaroulis/protolink) | 87 | Python | MIT | 2026-10 | Python agents with native A2A communication |
| [KodeAgent](https://github.com/barun-saha/kodeagent) | 44 | Python | Apache-2.0 | 2026-10 | Minimal agent engine, deliberately small |
| [OpenProgram](https://github.com/Fzkuji/OpenProgram) | — | — | — | — | Agents create and refine their own workflows |
| [ShaprAI](https://github.com/Scottcjn/shaprai) | — | — | — | — | Sharpens raw models into principled agents |
| [TrashClaw](https://github.com/Scottcjn/trashclaw) | — | — | — | — | Zero-dependency local agent for old hardware |

## Multi-Agent Orchestration

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 71,010 | Python | MIT | 2026-01 | Agents role-play a software company |
| [AutoGen](https://github.com/microsoft/autogen) | 61,550 | Python | CC-BY-4.0 | 2026-10 | Conversational multi-agent systems |
| [CrewAI](https://github.com/crewAIInc/crewAI) | 60,074 | Python | MIT | 2026-10 | Orchestrate role-playing agent crews |
| [CAMEL](https://github.com/camel-ai/camel) | 17,964 | Python | Apache-2.0 | 2026-10 | Role-playing agents for studying agent society |
| [PraisonAI](https://github.com/MervinPraison/PraisonAI) | 9,290 | Python | MIT | 2026-10 | Multi-agent workflows with self-reflection |
| [OpenAgents](https://github.com/openagents-org/openagents) | 4,253 | TypeScript | Apache-2.0 | 2026-10 | Agent networks over WebSocket, gRPC, MCP and A2A |
| [hcom](https://github.com/aannoo/hcom) | 602 | Rust | MIT | 2026-10 | Agents message and spawn each other in terminals |
| [Markus](https://github.com/markus-global/markus) | 208 | TypeScript | Apache-2.0 | 2026-10 | Agents coordinate and review each other's work |
| [CommonGround Kernel](https://github.com/Intelligent-Internet/CommonGround) | 153 | Python | Apache-2.0 | 2026-05 | Postgres-backed shared substrate for agent teams |
| [Quorum](https://github.com/Detrol/quorum-cli) | 123 | Python | Other | 2026-09 | Structured multi-agent debate in the terminal |
| [Flock](https://github.com/whiteducksoftware/flock) | 122 | Python | MIT | 2026-10 | Declarative agents via blackboard architecture |
| [OpenAcme](https://github.com/sandydasari/openacme) | 89 | TypeScript | MIT | 2026-07 | Role-specialized agents that self-organize |
| [Hivekeep](https://github.com/MarlBurroW/hivekeep) | 73 | TypeScript | MIT | 2026-10 | Self-hosted team of persistent personal agents |
| [auto-co](https://github.com/NikitaDmitrieff/auto-co-meta) | 51 | TypeScript | MIT | 2026-06 | 14 agents run a company in a continuous loop |

## CLI Agent Harnesses

Tools that run, sandbox or coordinate command-line coding agents such as Claude Code,
Codex and Gemini CLI.

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Atomic Agent](https://github.com/AtomicBot-ai/atomic-agent) | 3,426 | TypeScript | MIT | 2026-10 | Local-first CLI agent for open-weight models |
| [Agent Teams](https://github.com/777genius/agent-teams-ai) | 2,314 | TypeScript | AGPL-3.0 | 2026-10 | Desktop app running coding-agent teams across CLIs |
| [Bernstein](https://github.com/sipyourdrink-ltd/bernstein) | 1,330 | Python | Apache-2.0 | 2026-10 | Deterministic orchestrator for 40+ CLI agents |
| [h5i](https://github.com/h5i-dev/h5i) | 806 | Rust | Apache-2.0 | 2026-10 | Runs agents in sandboxes, merges the verified result |
| [SwarmClaw](https://github.com/swarmclawai/swarmclaw) | 697 | TypeScript | MIT | 2026-06 | Self-hosted runtime for multi-agent CLI work |
| [Dorothy](https://github.com/Charlie85270/Dorothy) | 353 | TypeScript | MIT | 2026-10 | Desktop app to run several CLI agents at once |
| [ClawFleet](https://github.com/clawfleet/ClawFleet) | 178 | Go | MIT | 2026-04 | Deploys isolated agent instances via Docker |
| [ORCH](https://github.com/oxgeneral/ORCH) | 174 | TypeScript | MIT | 2026-08 | One CLI to manage a team of agents on tasks |
| [OpenPaw](https://github.com/daxaur/openpaw) | 173 | TypeScript | MIT | 2026-05 | Turns Claude Code into an assistant with 38 skills |
| [OpenHermit](https://github.com/HCF-STUDIOS/openhermit) | 88 | TypeScript | MIT | 2026-10 | Deploys agent fleets as long-running services |
| [5dive](https://github.com/5dive-ai/5dive) | 73 | Shell | MIT | 2026-10 | Run a company of named agents on your own server |
| [Agon](https://github.com/AutoResearch-Factory/Agon) | 54 | Python | MIT | 2026-10 | Claude Code plugin for autonomous research loops |
| [TeamHero](https://github.com/sagiyaacoby/TeamHero) | 38 | JavaScript | MIT | 2026-04 | Manage agents like a team, with structured roles |
| [OpenSepia](https://github.com/CelaenoIndustry/OpenSepia) | 35 | Python | MIT | 2026-03 | Nine Claude agents running as an agile team |

## Low-Code & Visual Builders

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Dify](https://github.com/langgenius/dify) | 159,450 | Python | Other | 2026-10 | Visual orchestration for LLM apps and agents |
| [Kiln AI](https://github.com/Kiln-AI/Kiln) | 5,230 | Python | Other | 2026-10 | Desktop app for evals, RAG and fine-tuning |
| [Heym](https://github.com/heymrun/heym) | 1,262 | Python | Other | 2026-10 | Visual builder for agentic workflow automation |

## Retrieval & Data

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [LlamaIndex](https://github.com/run-llama/llama_index) | 52,647 | Python | MIT | 2026-10 | Connects LLMs to 160+ data sources |
| [Haystack](https://github.com/deepset-ai/haystack) | 26,831 | Python | Apache-2.0 | 2026-10 | Composable pipelines for search and RAG |

## Memory & Context

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Hindsight](https://github.com/vectorize-io/hindsight) | 53,485 | Python | MIT | 2026-10 | Agent memory with retain, recall and reflect |
| [Caura](https://github.com/caura-ai/caura) | 504 | Python | Apache-2.0 | 2026-10 | Governed shared memory for fleets of agents |
| [AnimaWorks](https://github.com/xuiltul/animaworks) | 268 | Python | Apache-2.0 | 2026-10 | Organization-as-code with brain-inspired memory |
| [OMEGA](https://github.com/omega-memory/omega-memory) | 224 | Python | Apache-2.0 | 2026-10 | Persistent memory for coding agents over MCP |
| [Inite Brain](https://github.com/inite-ai/inite-brain-service) | 42 | TypeScript | AGPL-3.0 | 2026-10 | Bitemporal knowledge graph as agent memory |
| [Perseus](https://github.com/Perseus-Computing-LLC/perseus) | — | — | — | — | Resolves verified workspace state before a call |

## Agent Infrastructure

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Mem0](https://github.com/mem0ai/mem0) | 67,757 | Python | Apache-2.0 | 2026-10 | Memory layer that persists across agent sessions |
| [AgentField](https://github.com/Agent-Field/agentfield) | 2,619 | Go | Apache-2.0 | 2026-10 | Agent identity and RPC using W3C DIDs |
| [openma](https://github.com/openma-ai/open-managed-agents) | 334 | TypeScript | Apache-2.0 | 2026-10 | Self-hosted Managed Agents API implementation |

## Safety, Security & Evaluation

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Agentic Radar](https://github.com/splx-ai/agentic-radar) | 1,058 | Python | Apache-2.0 | 2025-11 | Scans agent workflows for CVE and OWASP issues |
| [Cordum](https://github.com/cordum-io/cordum) | 511 | Go | Other | 2026-10 | Evaluates policy before an agent action dispatches |
| [Kitaru](https://github.com/zenml-io/kitaru) | 314 | Python | Apache-2.0 | 2026-10 | Record, replay and improve agents in production |
| [Greywall](https://github.com/GreyhavenHQ/greywall) | 311 | Go | Apache-2.0 | 2026-10 | Deny-by-default sandbox for coding agents |
| [RapidFire AI](https://github.com/RapidFireAI/rapidfireai) | 173 | JavaScript | Apache-2.0 | 2026-10 | Experiment harness for RAG and fine-tuning runs |
| [APort Guardrails](https://github.com/aporthq/aport-agent-guardrails) | 30 | Shell | Other | 2026-10 | Pre-action authorization policy for agent calls |

## Domain-Specific Agents

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [DeepAnalyze](https://github.com/ruc-datalab/DeepAnalyze) | 4,749 | Python | MIT | 2026-10 | Autonomous data science without fixed workflows |
| [Darkmoon](https://github.com/ASCIT31/Dark-Moon) | 1,140 | Python | GPL-3.0 | 2026-10 | Autonomous pentesting across web, cloud and AD |
| [RAI](https://github.com/RobotecAI/rai) | 609 | Python | Apache-2.0 | 2026-10 | Agent framework for robotics, built on ROS 2 |
| [CleverBee](https://github.com/SureScaleAI/cleverbee) | 301 | Python | AGPL-3.0 | 2026-01 | Deep research agent that browses with Playwright |
| [text2sql-framework](https://github.com/Text2SqlAgent/text2sql-framework) | 162 | Python | MIT | 2026-08 | Text-to-SQL agent that explores schema, not RAG |
| [GenoMAS](https://github.com/Liu-Hy/GenoMAS) | 134 | Python | MIT | 2026-10 | Multi-agent pipeline for genomics data analysis |
| [wechat-mac-rpa](https://github.com/wq19901103wq/wechat-mac-rpa) | 126 | Python | MIT | 2026-10 | Visual agent automating WeChat on macOS |
| [DNA Claude Analysis](https://github.com/shmlkv/dna-claude-analysis) | 59 | Python | MIT | 2026-03 | Explore your genome in natural language |
| [everyrow](https://github.com/futuresearch/futuresearch-python) | 57 | Python | MIT | 2026-10 | Run LLM agents over pandas DataFrames |
| [Inalpha](https://github.com/mirror29/inalpha) | 48 | Python | AGPL-3.0 | 2026-10 | Quant agents that pick factors that still work |
| [Omni-Rewriter](https://github.com/WayneJin0918/Omni-Rewriter) | — | — | — | — | Prompt expansion for image and video generation |

## Research & Experimental

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [EvoAgentX](https://github.com/EvoAgentX/EvoAgentX) | 3,402 | Python | Other | 2026-10 | Agent workflows that evolve and self-optimize |
| [AgentFlow](https://github.com/lupantech/AgentFlow) | 2,067 | Python | MIT | 2026-02 | Trainable multi-agent system using Flow-GRPO |
| [Cache-to-Cache](https://github.com/thu-nics/C2C) | 732 | Python | Apache-2.0 | 2026-10 | Agents exchange meaning directly via KV-cache |
| [AgentSquare](https://github.com/tsinghua-fib-lab/AgentSquare) | 234 | HTML | — | 2025-11 | Automatic search over modular agent designs |
| [GNAP](https://github.com/farol-team/gnap) | 87 | — | MIT | 2026-03 | Git-native protocol draft for agent coordination |
| [agent-opt](https://github.com/future-agi/agent-opt) | 75 | Python | Apache-2.0 | 2026-06 (archived) | Optimizes prompts and agent workflows |
| [AVP](https://github.com/VectorArc/avp-python) | 29 | Python | Apache-2.0 | 2026-04 | Transfers KV-cache between agents, not text |

## Autonomous Agents (2023 wave)

The 2023 autonomous-agent wave. Listed for their influence; several are no longer
actively developed.

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 187,731 | Python | Other | 2026-10 | The original autonomous GPT-4 agent loop |
| [OpenManus](https://github.com/FoundationAgents/OpenManus) | 58,770 | Python | MIT | 2026-09 | General-purpose agent, no invite code needed |
| [BabyAGI](https://github.com/yoheinakajima/babyagi) | 22,356 | Python | — | 2026-01 | Minimal task-driven autonomous agent loop |
| [XAgent](https://github.com/OpenBMB/XAgent) | 8,549 | Python | Apache-2.0 | 2026-07 | Autonomous agent with planning and tool learning |

## Inactive

Archived, or no push in over 12 months. Kept because they are widely referenced and
readers benefit from knowing their status.

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Flowise](https://github.com/FlowiseAI/Flowise) | 55,527 | TypeScript | Other | 2026-08 (archived) | Drag-and-drop builder for LLM flows |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | 17,713 | Python | MIT | 2025-01 | Autonomous agent platform with a tool framework |
| [OpenAgents (XLang)](https://github.com/xlang-ai/OpenAgents) | 4,864 | Python | Apache-2.0 | 2024-11 | Platform for data, web and coding agents |
| [Agent Protocol](https://github.com/agi-inc/agent-protocol) | 1,460 | Python | MIT | 2025-04 | Standard interface for agent interoperability |
| [AI Legion](https://github.com/eumemic/ai-legion) | 1,439 | TypeScript | MIT | 2025-05 | TypeScript swarm of autonomous agents |

## License

[CC0 1.0 Universal](LICENSE) — to the extent possible under law, the contributors
have waived all copyright and related rights to this work.

- [DoomPay](https://github.com/doomsday-network/doom-pay) - Non-custodial 3-line Web3 checkout widget, REST API, and remote MCP payment receipt verifier (`wDOOM` on Base Mainnet & `DOOM` Layer-1).
