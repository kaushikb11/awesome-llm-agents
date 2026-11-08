# Awesome LLM Agent Frameworks [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of open-source frameworks, runtimes and tooling for building LLM
agents. Metrics refresh weekly. (Last updated: 2026-11-08)

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
| [OpenClaw](https://github.com/openclaw/openclaw) | 394,157 | TypeScript | MIT | 2026-11 | Personal AI assistant that runs on any platform |
| [LangChain](https://github.com/langchain-ai/langchain) | 149,183 | Python | MIT | 2026-11 | Compose LLM apps from modular pieces |
| [Smolagents](https://github.com/huggingface/smolagents) | 30,261 | Python | Apache-2.0 | 2026-11 | Minimal agents that write code to act |
| [Mastra](https://github.com/mastra-ai/mastra) | 29,400 | TypeScript | Other | 2026-11 | TypeScript agents with RAG and observability |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | 28,745 | C# | MIT | 2026-11 | Plugin-based AI integration for .NET and Python |
| [Google ADK](https://github.com/google/adk-python) | 22,137 | Python | Apache-2.0 | 2026-11 | Code-first agents that deploy to Vertex AI |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai) | 21,085 | Python | MIT | 2026-11 | Type-safe agents on Pydantic with structured output |
| [Tambo](https://github.com/tambo-ai/tambo) | 11,224 | TypeScript | MIT | 2026-11 | React components rendered by AI at runtime |
| [Hive](https://github.com/aden-hive/hive) | 11,145 | Python | Apache-2.0 | 2026-11 | Multi-agent harness aimed at production |
| [Openwork](https://github.com/accomplish-ai/coworker) | 10,807 | — | — | 2026-08 | Open-source AI coworker platform |
| [Upsonic](https://github.com/upsonic/upsonic) | 7,968 | Python | MIT | 2026-06 | Agents with MCP and isolated execution |
| [Atomic Agents](https://github.com/Eigenwise/atomic-agents) | 6,320 | Python | MIT | 2026-10 | Compose agents from small interchangeable parts |
| [OpenAgent](https://github.com/the-open-agent/openagent) | 5,730 | Go | Apache-2.0 | 2026-11 | Personal assistant built on LLM, RAG and agent loops |
| [Oh My Hermes](https://github.com/rlaope/oh-my-hermes) | 5,233 | Python | MIT | 2026-11 | Harness with optimized tools and memory |
| [AG2](https://github.com/ag2ai/ag2) | 5,052 | Python | Apache-2.0 | 2026-11 | Community fork of AutoGen, now an AgentOS |
| [AGiXT](https://github.com/Josh-XT/AGiXT) | 3,217 | Python | MIT | 2026-07 | Multi-provider agent platform with command chaining |
| [trpc-agent-go](https://github.com/trpc-group/trpc-agent-go) | 1,910 | Go | Apache-2.0 | 2026-11 | Go framework for agents with graph workflows |
| [Ouroboros](https://github.com/razzant/ouroboros) | 1,619 | Python | MIT | 2026-11 | Agent runtime with reviewed self-modification |
| [ConnectOnion](https://github.com/openonion/connectonion) | 1,507 | Python | Apache-2.0 | 2026-11 | Python framework focused on agent collaboration |
| [Agentlas OS](https://github.com/agentlas-ai/Agentlas-OS) | 1,467 | Python | Apache-2.0 | 2026-11 | Specialist agent hub with temporary orchestrators |
| [LightAgent](https://github.com/wanxingai/LightAgent) | 1,244 | Python | Apache-2.0 | 2026-10 | Lightweight Python agents with tools and memory |
| [ix](https://github.com/kreneskyp/ix) | 1,044 | Python | MIT | 2026-10 | Autonomous agents with a visual workflow builder |
| [Promptise Foundry](https://github.com/promptise-com/Foundry) | 894 | Python | Apache-2.0 | 2026-11 | Agentic framework with controllable reasoning |
| [Aeon](https://github.com/aeonfun/aeon) | 789 | JavaScript | MIT | 2026-11 | Runs unattended on GitHub Actions, self-healing |
| [Octomind](https://github.com/Muvon/octomind) | 607 | Rust | Apache-2.0 | 2026-11 | Model-agnostic runtime with specialist agents |
| [Octochains](https://github.com/ahmadvh/octochains) | 380 | Python | Other | 2026-10 | Parallel isolated reasoning with an aggregator |
| [Neurolink](https://github.com/juspay/neurolink) | 168 | TypeScript | MIT | 2026-11 | One interface across 12+ LLM providers |
| [Axar](https://github.com/axar-ai/axar) | 166 | TypeScript | Apache-2.0 | 2026-02 | Minimal TypeScript agents with Zod validation |
| [NarraNexus](https://github.com/NetMindAI-Open/NarraNexus) | 92 | Python | Apache-2.0 | 2026-11 | Builds nexuses where agent intelligence emerges |
| [ProtoLink](https://github.com/nMaroulis/protolink) | 85 | Python | MIT | 2026-11 | Python agents with native A2A communication |
| [ShaprAI](https://github.com/Scottcjn/shaprai) | 77 | Python | MIT | 2026-09 | Sharpens raw models into principled agents |
| [TrashClaw](https://github.com/Scottcjn/trashclaw) | 76 | Python | MIT | 2026-09 | Zero-dependency local agent for old hardware |
| [KodeAgent](https://github.com/barun-saha/kodeagent) | 45 | Python | Apache-2.0 | 2026-10 | Minimal agent engine, deliberately small |
| [OpenProgram](https://github.com/Fzkuji/OpenProgram) | — | — | — | — | Agents create and refine their own workflows |

## Multi-Agent Orchestration

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 71,215 | Python | MIT | 2026-01 | Agents role-play a software company |
| [AutoGen](https://github.com/microsoft/autogen) | 61,744 | Python | CC-BY-4.0 | 2026-10 | Conversational multi-agent systems |
| [CrewAI](https://github.com/crewAIInc/crewAI) | 60,628 | Python | MIT | 2026-11 | Orchestrate role-playing agent crews |
| [CAMEL](https://github.com/camel-ai/camel) | 18,019 | Python | Apache-2.0 | 2026-11 | Role-playing agents for studying agent society |
| [PraisonAI](https://github.com/MervinPraison/PraisonAI) | 9,327 | Python | MIT | 2026-11 | Multi-agent workflows with self-reflection |
| [OpenAgents](https://github.com/openagents-org/openagents) | 4,348 | TypeScript | Apache-2.0 | 2026-11 | Agent networks over WebSocket, gRPC, MCP and A2A |
| [hcom](https://github.com/aannoo/hcom) | 645 | Rust | MIT | 2026-10 | Agents message and spawn each other in terminals |
| [Markus](https://github.com/markus-global/markus) | 213 | TypeScript | Apache-2.0 | 2026-11 | Agents coordinate and review each other's work |
| [CommonGround Kernel](https://github.com/Intelligent-Internet/CommonGround) | 153 | Python | Apache-2.0 | 2026-05 | Postgres-backed shared substrate for agent teams |
| [Quorum](https://github.com/Detrol/quorum-cli) | 128 | Python | Other | 2026-09 | Structured multi-agent debate in the terminal |
| [Flock](https://github.com/whiteducksoftware/flock) | 126 | Python | MIT | 2026-11 | Declarative agents via blackboard architecture |
| [OpenAcme](https://github.com/sandydasari/openacme) | 89 | TypeScript | MIT | 2026-07 | Role-specialized agents that self-organize |
| [Hivekeep](https://github.com/MarlBurroW/hivekeep) | 79 | TypeScript | MIT | 2026-11 | Self-hosted team of persistent personal agents |
| [auto-co](https://github.com/NikitaDmitrieff/auto-co-meta) | 52 | TypeScript | MIT | 2026-06 | 14 agents run a company in a continuous loop |

## CLI Agent Harnesses

Tools that run, sandbox or coordinate command-line coding agents such as Claude Code,
Codex and Gemini CLI.

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Atomic Agent](https://github.com/AtomicBot-ai/atomic-agent) | 3,358 | TypeScript | MIT | 2026-11 | Local-first CLI agent for open-weight models |
| [Agent Teams](https://github.com/777genius/agent-teams-ai) | 2,439 | TypeScript | AGPL-3.0 | 2026-11 | Desktop app running coding-agent teams across CLIs |
| [Bernstein](https://github.com/sipyourdrink-ltd/bernstein) | 1,196 | Python | Apache-2.0 | 2026-11 | Deterministic orchestrator for 40+ CLI agents |
| [h5i](https://github.com/h5i-dev/h5i) | 899 | Rust | Apache-2.0 | 2026-11 | Runs agents in sandboxes, merges the verified result |
| [SwarmClaw](https://github.com/swarmclawai/swarmclaw) | 705 | TypeScript | MIT | 2026-06 | Self-hosted runtime for multi-agent CLI work |
| [Dorothy](https://github.com/Charlie85270/Dorothy) | 357 | TypeScript | MIT | 2026-10 | Desktop app to run several CLI agents at once |
| [ClawFleet](https://github.com/clawfleet/ClawFleet) | 179 | Go | MIT | 2026-04 | Deploys isolated agent instances via Docker |
| [OpenPaw](https://github.com/daxaur/openpaw) | 178 | TypeScript | MIT | 2026-05 | Turns Claude Code into an assistant with 38 skills |
| [ORCH](https://github.com/oxgeneral/ORCH) | 177 | TypeScript | MIT | 2026-08 | One CLI to manage a team of agents on tasks |
| [5dive](https://github.com/5dive-ai/5dive) | 111 | Shell | MIT | 2026-11 | Run a company of named agents on your own server |
| [OpenHermit](https://github.com/HCF-STUDIOS/openhermit) | 90 | TypeScript | MIT | 2026-11 | Deploys agent fleets as long-running services |
| [Agon](https://github.com/AutoResearch-Factory/Agon) | 55 | Python | MIT | 2026-10 | Claude Code plugin for autonomous research loops |
| [TeamHero](https://github.com/sagiyaacoby/TeamHero) | 38 | JavaScript | MIT | 2026-04 | Manage agents like a team, with structured roles |
| [OpenSepia](https://github.com/CelaenoIndustry/OpenSepia) | 35 | Python | MIT | 2026-03 | Nine Claude agents running as an agile team |

## Low-Code & Visual Builders

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Dify](https://github.com/langgenius/dify) | 160,639 | Python | Other | 2026-11 | Visual orchestration for LLM apps and agents |
| [Kiln AI](https://github.com/Kiln-AI/Kiln) | 5,261 | Python | Other | 2026-11 | Desktop app for evals, RAG and fine-tuning |
| [Heym](https://github.com/heymrun/heym) | 1,376 | Python | Other | 2026-11 | Visual builder for agentic workflow automation |

## Retrieval & Data

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [LlamaIndex](https://github.com/run-llama/llama_index) | 52,842 | Python | MIT | 2026-11 | Connects LLMs to 160+ data sources |
| [Haystack](https://github.com/deepset-ai/haystack) | 26,943 | Python | Apache-2.0 | 2026-11 | Composable pipelines for search and RAG |

## Memory & Context

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Hindsight](https://github.com/vectorize-io/hindsight) | 59,764 | Python | MIT | 2026-11 | Agent memory with retain, recall and reflect |
| [Caura](https://github.com/caura-ai/caura) | 551 | Python | Apache-2.0 | 2026-11 | Governed shared memory for fleets of agents |
| [AnimaWorks](https://github.com/xuiltul/animaworks) | 268 | Python | Apache-2.0 | 2026-11 | Organization-as-code with brain-inspired memory |
| [OMEGA](https://github.com/omega-memory/omega-memory) | 224 | Python | Apache-2.0 | 2026-10 | Persistent memory for coding agents over MCP |
| [Inite Brain](https://github.com/inite-ai/inite-brain-service) | 43 | TypeScript | AGPL-3.0 | 2026-11 | Bitemporal knowledge graph as agent memory |
| [Perseus](https://github.com/Perseus-Computing-LLC/perseus) | — | — | — | — | Resolves verified workspace state before a call |

## Agent Infrastructure

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Mem0](https://github.com/mem0ai/mem0) | 68,598 | Python | Apache-2.0 | 2026-11 | Memory layer that persists across agent sessions |
| [AgentField](https://github.com/Agent-Field/agentfield) | 2,647 | Go | Apache-2.0 | 2026-11 | Agent identity and RPC using W3C DIDs |
| [openma](https://github.com/openma-ai/open-managed-agents) | 348 | TypeScript | Apache-2.0 | 2026-11 | Self-hosted Managed Agents API implementation |

## Safety, Security & Evaluation

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Agentic Radar](https://github.com/splx-ai/agentic-radar) | 1,067 | Python | Apache-2.0 | 2025-11 | Scans agent workflows for CVE and OWASP issues |
| [Cordum](https://github.com/cordum-io/cordum) | 510 | Go | Other | 2026-11 | Evaluates policy before an agent action dispatches |
| [Kitaru](https://github.com/zenml-io/kitaru) | 317 | Python | Apache-2.0 | 2026-11 | Record, replay and improve agents in production |
| [Greywall](https://github.com/GreyhavenHQ/greywall) | 315 | Go | Apache-2.0 | 2026-10 | Deny-by-default sandbox for coding agents |
| [RapidFire AI](https://github.com/RapidFireAI/rapidfireai) | 176 | JavaScript | Apache-2.0 | 2026-10 | Experiment harness for RAG and fine-tuning runs |
| [APort Guardrails](https://github.com/aporthq/aport-agent-guardrails) | 30 | Shell | Other | 2026-11 | Pre-action authorization policy for agent calls |

## Domain-Specific Agents

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [DeepAnalyze](https://github.com/ruc-datalab/DeepAnalyze) | 4,793 | Python | MIT | 2026-11 | Autonomous data science without fixed workflows |
| [Darkmoon](https://github.com/ASCIT31/Dark-Moon) | 1,209 | Python | GPL-3.0 | 2026-10 | Autonomous pentesting across web, cloud and AD |
| [RAI](https://github.com/RobotecAI/rai) | 614 | Python | Apache-2.0 | 2026-11 | Agent framework for robotics, built on ROS 2 |
| [CleverBee](https://github.com/SureScaleAI/cleverbee) | 301 | Python | AGPL-3.0 | 2026-01 | Deep research agent that browses with Playwright |
| [text2sql-framework](https://github.com/Text2SqlAgent/text2sql-framework) | 163 | Python | MIT | 2026-08 | Text-to-SQL agent that explores schema, not RAG |
| [wechat-mac-rpa](https://github.com/wq19901103wq/wechat-mac-rpa) | 138 | Python | MIT | 2026-11 | Visual agent automating WeChat on macOS |
| [GenoMAS](https://github.com/Liu-Hy/GenoMAS) | 130 | Python | MIT | 2026-10 | Multi-agent pipeline for genomics data analysis |
| [Omni-Rewriter](https://github.com/WayneJin0918/Omni-Rewriter) | 90 | Python | Apache-2.0 | 2026-08 | Prompt expansion for image and video generation |
| [DNA Claude Analysis](https://github.com/shmlkv/dna-claude-analysis) | 60 | Python | MIT | 2026-03 | Explore your genome in natural language |
| [everyrow](https://github.com/futuresearch/futuresearch-python) | 57 | Python | MIT | 2026-11 | Run LLM agents over pandas DataFrames |
| [Inalpha](https://github.com/mirror29/inalpha) | 52 | Python | AGPL-3.0 | 2026-11 | Quant agents that pick factors that still work |

## Research & Experimental

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [EvoAgentX](https://github.com/EvoAgentX/EvoAgentX) | 3,424 | Python | Other | 2026-10 | Agent workflows that evolve and self-optimize |
| [AgentFlow](https://github.com/lupantech/AgentFlow) | 2,089 | Python | MIT | 2026-02 | Trainable multi-agent system using Flow-GRPO |
| [Cache-to-Cache](https://github.com/thu-nics/C2C) | 771 | Python | Apache-2.0 | 2026-10 | Agents exchange meaning directly via KV-cache |
| [AgentSquare](https://github.com/tsinghua-fib-lab/AgentSquare) | 235 | HTML | — | 2025-11 | Automatic search over modular agent designs |
| [GNAP](https://github.com/farol-team/gnap) | 87 | — | MIT | 2026-03 | Git-native protocol draft for agent coordination |
| [agent-opt](https://github.com/future-agi/agent-opt) | 75 | Python | Apache-2.0 | 2026-06 (archived) | Optimizes prompts and agent workflows |
| [AVP](https://github.com/VectorArc/avp-python) | 30 | Python | Apache-2.0 | 2026-04 | Transfers KV-cache between agents, not text |

## Autonomous Agents (2023 wave)

The 2023 autonomous-agent wave. Listed for their influence; several are no longer
actively developed.

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 187,933 | Python | Other | 2026-11 | The original autonomous GPT-4 agent loop |
| [OpenManus](https://github.com/FoundationAgents/OpenManus) | 58,923 | Python | MIT | 2026-11 | General-purpose agent, no invite code needed |
| [BabyAGI](https://github.com/yoheinakajima/babyagi) | 22,355 | Python | — | 2026-01 | Minimal task-driven autonomous agent loop |
| [XAgent](https://github.com/OpenBMB/XAgent) | 8,548 | Python | Apache-2.0 | 2026-07 | Autonomous agent with planning and tool learning |

## Inactive

Archived, or no push in over 12 months. Kept because they are widely referenced and
readers benefit from knowing their status.

| Project | Stars | Language | License | Updated | Description |
| --- | ---: | --- | --- | --- | --- |
| [Flowise](https://github.com/FlowiseAI/Flowise) | 55,562 | TypeScript | Other | 2026-08 (archived) | Drag-and-drop builder for LLM flows |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | 17,738 | Python | MIT | 2025-01 | Autonomous agent platform with a tool framework |
| [OpenAgents (XLang)](https://github.com/xlang-ai/OpenAgents) | 4,869 | Python | Apache-2.0 | 2026-10 | Platform for data, web and coding agents |
| [Agent Protocol](https://github.com/agi-inc/agent-protocol) | 1,460 | Python | MIT | 2025-04 | Standard interface for agent interoperability |
| [AI Legion](https://github.com/eumemic/ai-legion) | 1,439 | TypeScript | MIT | 2025-05 | TypeScript swarm of autonomous agents |

## License

[CC0 1.0 Universal](LICENSE) — to the extent possible under law, the contributors
have waived all copyright and related rights to this work.
