# Awesome-LLM-Agents: Recent Trends and Advancement in Agentic AI
![image](https://github.com/user-attachments/assets/c32b1f99-e434-473b-8916-59cb5d6e8bab)
This Awesome-LLM-Agents contains A hand-picked and carefully categorised reading list. Furthermore, I will conduct review on each paper and project, and (hopefully) put them in anto a survey paper.
The detailed thought process of forming this project is documented at this [Medium Post](https://ai.gopubby.com/awesome-llm-agents-recent-trends-and-advancement-in-agentic-ai-90bac6249060). It's put behind a paywall to prevent the evil LLMs' crawling. [The full category breakdown](https://github.com/junhua/awesome-llm-agents/blob/main/Categories.md).

## LLM Core — Foundation Models
- Scaling laws for neural language models (OpenAI, 2020, [arXiv](https://arxiv.org/pdf/2001.08361))
- LLaMA: Open and Efficient Foundation Language Models (Meta, Feb 2023, [arXiv](https://arxiv.org/pdf/2302.13971))
- The Llama 3 Herd of Models (Meta, July 2024, [arXiv](https://arxiv.org/pdf/2407.21783))
- Sparks of Artificial General Intelligence: Early experiments with GPT-4 (Microsoft, Apr 2023, [arXiv](https://arxiv.org/pdf/2303.12712))
- Apple Intelligence Foundation Language Models (Apple, [Doc](https://machinelearning.apple.com/papers/apple_intelligence_foundation_language_models.pdf))
- StarCoder (Dec 2023, [arXiv](https://arxiv.org/pdf/2305.06161))
- Gemma 2B: Improving Open Language Models at a Practical Size (Jul, 2024, [arXiv](https://arxiv.org/pdf/2408.00118))

## LLM Core — Prompt Engineering
- Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (Google Brain, 2022, [NeurIPS](https://arxiv.org/pdf/2201.11903))
- Tree of Thoughts: Deliberate Problem Solving with Large Language Models (Princeton & DeepMind, 2023, [NeurIPS](https://arxiv.org/pdf/2305.10601), [Benchmark](https://github.com/holarissun/PanelGPT))
- Self-Consistency Improves Chain of Thought Reasoning in Language Models (Google Brain, 2023, [ICLR](https://arxiv.org/pdf/2203.11171))
- ReAct: Synergizing Reasoning and Action in Language Models (Princeton & Google Brain, Mar 2023 [ICLR](https://react-lm.github.io/))
- Reflexion: Language agents with verbal reinforcement learning (Northeastern, MIT & Princeton, 2023, [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf))
- ART: Automatic multi-step reasoning and tool-use for large language models (UW, UCI, Microsoft, Allen AI & Meta, 2023, [arXiv](https://arxiv.org/pdf/2303.09014))
- Directional Stimulus Prompting (UCSB & Microsoft, 2023, [NeurIPS](https://arxiv.org/pdf/2302.11520))
- Active Prompting with Chain-of-Thought for Large Language Models (HKUST etc., Jul 2024, [arXiv](https://arxiv.org/pdf/2302.12246))
- Step-Back Prompting Enables Reasoning Via Abstraction in Large Language Models (DeepMind, Mar 2024, [arXiv](https://arxiv.org/pdf/2310.06117))

## LLM Core — Retrieval-Augmented Generation
- Retrieval Augmented Generation or Long-Context LLMs? A Comprehensive Study and Hybrid Approach (DeepMind, Jul 2024, [arXiv](https://www.arxiv.org/pdf/2407.16833))
- Retrieval-Augmented Generation for Large Language Models: A Survey (Tongji & Fudan, Mar 2024, [arXiv](https://arxiv.org/pdf/2312.10997))
- Improving Retrieval Augmented Language Model with Self-Reasoning (Baidu, Jul 2024, [arXiv](https://arxiv.org/pdf/2407.19813))

## LLM Core — Finetuning / PEFT
- Lora: Low-rank adaptation of large language models (Microsoft & CMU, Oct 2021, [arXiv](https://arxiv.org/pdf/2106.09685))
- QLoRA: Efficient Finetuning of Quantized LLMs (UW, 2023, [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2023/file/1feb87871436031bdc0f2beaa62a049b-Paper-Conference.pdf))
- A Survey on LoRA of Large Language Models (ZJU, Jul 2024, [arXiv](https://arxiv.org/pdf/2407.11046))
- Distilling System 2 into System 1 (Meta, Jul 2024, [arXiv](https://arxiv.org/pdf/2407.06023))
- Mixture of LoRA Experts (Microsoft & Tsinghua, 2024, [ICLR](https://openreview.net/pdf?id=uWvKBCYh4S))

## LLM Core — Alignments and Safety
- Rule Based Rewards for Language Model Safety (OpenAI, Jul 2024, [Preprint](https://cdn.openai.com/rule-based-rewards-for-language-model-safety.pdf))
- A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More (Salesforce, Jul 2024, [arXiv](https://arxiv.org/pdf/2407.16216))
- Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study (Tsinghua, Apr 2024, [arXiv](https://arxiv.org/pdf/2404.10719))
- PERL: Parameter Efficient Reinforcement Learning from Human Feedback (Google, Mar 2024, [arXiv](https://arxiv.org/pdf/2403.10704))
- RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback (Google, Dec 2023, [arXiv](https://arxiv.org/pdf/2309.00267))
- Training language models to follow instructions with human feedback (OpenAI, Mar 2022, [arXiv](https://arxiv.org/pdf/2203.02155))
- Constitutional AI: Harmlessness from AI Feedback (Anthropic, Dec 2022, [arXiv](https://arxiv.org/pdf/2212.08073)) ⭐
- Self-instruct: Aligning language models with self-generated instructions (Allen AI, May 2023, [ACL](https://arxiv.org/pdf/2212.10560)) ⭐
- Direct preference optimization: Your language model is secretly a reward model (Stanford, 2023, [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2023/file/a85b405ed65c6477a4fe8302b5e06ce7-Paper-Conference.pdf))⭐
- ULTRAFEEDBACK: Boosting Language Models with Scaled AI Feedback (Tsinghua, UIUC, Tencent, RUC etc., 2024, [ICML](https://openreview.net/pdf?id=BOorDpKHiJ)) ⭐
- Camels in a changing climate: Enhancing lm adaptation with tulu 2 (Allen AI & UW, Nov 2023, [arXiv](https://arxiv.org/pdf/2311.10702))
- Steerlm: Attribute conditioned sft as an (user-steerable) alternative to rlhf (Nvidia, Oct 2023, [arXiv](https://arxiv.org/pdf/2310.05344))
- 


## LLM Core — Datasets, benchmarks, Metrics
- GAIA: a benchmark for general AI assistants (Meta, Nov 2023, [ICLR](https://arxiv.org/pdf/2311.12983))
- Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators (Stanford, Apr 2024, [arXiv](https://arxiv.org/pdf/2404.04475))
- Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena (UCB, UCSD, CMU & Stanford, Dec 2023, [NeurIPS](https://arxiv.org/pdf/2306.05685))
- FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets (KAIST, Apr 2024, [ICLR](https://arxiv.org/pdf/2307.10928))
- Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference (UCB, Stanford & UCSD, Mar 2024, [arXiv](https://arxiv.org/pdf/2403.04132))
- Starling-7B: Improving LLM Helpfulness & Harmlessness with RLAIF (UCB, 2023, [HF](https://huggingface.co/berkeley-nest/Starling-LM-7B-alpha))
- Lmsys-chat-1m: A large-scale real-world llm conversation dataset (UCB, UCSD, CMU & Stanford, Mar 2024, [ICLR](https://arxiv.org/pdf/2309.11998))

## Agent Core — Planning / Reasoning Describe
- Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents (PKU, 2024, [NIPS](https://proceedings.neurips.cc/paper_files/paper/2023/file/6b8dfb8c0c12e6fafc6c256cb08a5ca7-Paper-Conference.pdf))
- Large Language Models as Commonsense Knowledge for Large-Scale Task Planning (NUS, 2023 , [NIPS](https://proceedings.neurips.cc/paper_files/paper/2023/file/65a39213d7d0e1eb5d192aa77e77eeb7-Paper-Conference.pdf))

## Agent Core — Memory
- A Survey on the Memory Mechanism of Large Language Model based Agents (RUC &Huawei, Apr 2024, [arXiv](https://arxiv.org/pdf/2404.13501))

## Agent Core — Tools
- Offline Training of Language Model Agents with Functions as Learnable Weights (PSU, UW, USC & Microsoft, 2024, [ICML](https://openreview.net/pdf?id=2xbkWiEuR1))
- Tool Learning with Foundation Models (Tsinghua, UIUC, CMU, etc., 2023, [arXiv](https://arxiv.org/pdf/2304.08354))
- Toolformer: Language models can teach themselves to use tools (Meta, 2023, [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2023/file/d842425e4bf79ba039352da0f658a906-Paper-Conference.pdf))

## Agentic Workflow — Paradigms
- Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View (ZJU & Deepmind, Oct 2023, [arXiv](https://arxiv.org/pdf/2310.02124))
- Rethinking the Bounds of LLM Reasoning: Are Multi-Agent Discussions the Key? (ZJU, HKUST & UIUC, May 2024, [arXiv](https://arxiv.org/pdf/2402.18272))
- 360◦REA: Towards A Reusable Experience Accumulation with 360◦Assessment for Multi-Agent System (Apr 2024, [arXiv](https://arxiv.org/abs/2404.05569))
- CAMEL: Communicative Agents for “Mind” Exploration of Large Language Model Society (KAUST, 2023, [NIPS](https://proceedings.neurips.cc/paper_files/paper/2023/file/a3621ee907def47c1b952ade25c67698-Paper-Conference.pdf))
- A Survey on Large Language Model based Autonomous Agents (2023, [arXiv](https://arxiv.org/pdf/2308.11432))
- Mixture-of-Agents Enhances Large Language Model Capabilities (Together AI, Jun 2024, [arXiv](https://arxiv.org/pdf/2406.04692))

## Agentic Applications — Simulation
- Generative Agents: Interactive Simulacra of Human Behavior (Stanford/Google, Apr 2023, [arXiv](https://arxiv.org/pdf/2304.03442), [Demo](https://reverie.herokuapp.com/arXiv_Demo/))
- Deciphering digital detectives: Understanding llm behaviors and capabilities in multi-agent mystery games (Umontreal, Dec 2023, [arXiv](https://arxiv.org/pdf/2312.00746))
- VillagerAgent: A Graph-Based Multi-Agent Framework for Coordinating Complex Task Dependencies in Minecraft (ZJU, Jun 2024, [arXiv](https://arxiv.org/pdf/2406.05720))

## Agentic Applications — Finance
- Complete list: [Awesome-Finance-AI-Papers](https://github.com/junhua/awesome-finance-ai-papers)

## Multi-agent frameworks
- LangGraph ([GitHub](https://github.com/langchain-ai/langgraph))
- AutoGen by Microsoft ([GitHub](https://github.com/microsoft/autogen), [Paper](https://arxiv.org/pdf/2308.08155))
- AgentScope by Alibaba Group([GitHub](https://github.com/modelscope/agentscope), [System Paper](https://arxiv.org/pdf/2402.14034), [Projects paper](https://arxiv.org/pdf/2407.17789))
- Translation-agent by Andrew Ng ([GitHub](https://github.com/andrewyng/translation-agent))
- [Ivy Tendril](https://github.com/Ivy-Interactive/Ivy-Tendril) - Open-source agentic software factory with an amazing UI that handles parallel Git worktrees for you, complete with programmatic verifications and fast review loops
  
## TODO:
- Agentic Workflow — Human-Agent Interactions
- Agentic Applications — Dev Tools
- Agentic Applications — Content Creation (AIGC)
- Agentic Applications — Social Network
- Agentic Applications — Education
- Production Operations — LLMOps
- Production Operations — AI Cloud
- Production Operations — Monitoring

## Citation

Please cite the repo if you refer to the content of the this repository for your work.

```
@misc{awesome-llm-agents-jl,
  author = {Junhua Liu},
  title = {Awesome-LLM-Agents: recent trends and advancement in Agentic AI},
  year = {2024},
  month = {August},
  publisher = {Medium},
  journal = {AI Advances},
  doi = {10.5281/zenodo.14021180},
  url = {https://medium.com/junhua/awesome-llm-agents-recent-trends-and-advancement-in-agentic-ai-90bac6249060},
}
```
