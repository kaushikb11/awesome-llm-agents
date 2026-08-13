# Contributing

Thanks for suggesting a project. This list aims to cover the open-source LLM agent
ecosystem broadly, so most serious projects have a place here — but every entry has
to earn its row, and the rules below are applied mechanically so that acceptance is
a policy decision rather than a matter of taste.

## Scope

The list covers the **open-source ecosystem for building and running LLM agents**.
That is deliberately broad: frameworks, SDKs, runtimes, orchestration layers,
low-code builders, safety and evaluation tooling, domain-specific agents, and
research implementations all belong. What matters is that each entry lands in a
named section, so readers know what kind of thing they are looking at.

Every entry belongs to exactly one section:

| Section | What goes here |
| --- | --- |
| Core Frameworks | General-purpose libraries for building agents |
| Multi-Agent Orchestration | Coordinating several agents: roles, handoffs, topologies |
| Low-Code & Visual Builders | Build agents primarily through a UI |
| Retrieval & Data | RAG stacks and data frameworks agents are built on |
| Agent Infrastructure | Runtimes, gateways, identity, messaging, deployment |
| Safety, Security & Evaluation | Policy enforcement, scanning, evals, observability |
| Domain-Specific Agents | Agents built for one field: robotics, science, data, ops |
| Research & Experimental | Paper implementations and experimental architectures |
| Autonomous Agents (2023 wave) | Historically important autonomous agents, many now idle |
| Inactive | Archived or unmaintained, kept because they are widely referenced |

If a project does not fit any section, open an issue before the pull request.

## Retirement

Entries are re-checked weekly. When a project is archived, or goes 12 months
without a push, one of two things happens:

- **1,000 stars or more** — it moves to **Inactive**, with its archived status and
  last-updated date shown. A reader looking for a project they have heard of
  should find it here and learn that it wound down, rather than find nothing.
- **Under 1,000 stars** — the entry is removed.

A repository that stops resolving is removed regardless of size, since there is
nothing left to link to.

## Requirements

An entry is accepted when all of the following hold. These are checked in CI.

1. **The repository resolves.** A URL returning 404 is rejected. This is the single
   most common reason submissions fail.
2. **Not archived.**
3. **Pushed within the last 12 months.** Entries that go 12 months without a push
   are retired, so new entries are held to the same standard.
4. **At least 25 stars**, or published by a recognized organization or research lab.
5. **Has a license.** A repository with no license is not usable by the people
   reading this list.
6. **Not a duplicate.** Including renames and redirects of a project already listed.
7. **Description is 60 characters or fewer.**

## Writing the description

The description is one table cell. It should say what makes the project
**different**, not what category it is in. Length is the easy part; being
informative is the actual bar.

```
✗  Multi-provider AI agent framework with workflow orchestration
   capabilities, unifying 12+ providers (OpenAI, Google, Anthropic, …)
       Too long, and it is a feature list rather than a description.

✗  Autonomous agent framework
       Short, but says nothing. Every project here is one of those.

✓  Type-safe agents on Pydantic with structured output
✓  Visual drag-and-drop builder for LLM flows
✓  Agent framework for robotics, built on ROS 2
```

No marketing adjectives — *production-ready*, *powerful*, *seamless*, *revolutionary*
say nothing and will be edited out. Provider lists, benchmark numbers and feature
enumerations belong in your README, not in the row.

## Adding an entry

Each project is one file in `data/frameworks/`, named after its slug. Add one file;
do not edit `README.md` directly — it is generated, and edits to it are overwritten
by the weekly metrics job.

```yaml
# data/frameworks/pydantic-ai.yml
name: Pydantic AI
repo: https://github.com/pydantic/pydantic-ai
section: Core Frameworks
description: Type-safe agents on Pydantic with structured output
```

Stars, forks, language, license and last-updated are filled in automatically. Do not
include them.

Because every project is its own file, two pull requests adding different projects
never conflict with each other.

## Self-submissions

Submitting your own project is fine and common. It is held to exactly the same
requirements — most self-submissions that get rejected fail on the star count or
the missing license, not on being a self-submission.
