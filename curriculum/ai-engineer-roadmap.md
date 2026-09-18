# AI Engineer Roadmap — 0 to Hero (Nikita's personal path)

> Your path to **AI Application Engineer** — the person who builds real products *with* LLMs (RAG, agents, AI features), not the person who trains models from scratch or optimizes GPU inference.
> Built 2026-09-17, tuned to where you *actually* are, not a generic beginner plan.

Format per milestone: **Why → Concepts → Build → Checkpoint.** Same rhythm as `_index.md`.

---

## 📍 Where you already are (start here, not at zero)

You are **not** a blank-slate beginner. Honest map of your current position:

| Milestone | Status | Evidence |
|---|---|---|
| M1 · Python foundations | ✅ **Done** | OOP, APIs, CSV apps, Git, expense tracker |
| M2 · ML math | 🟡 **Gap** | know the ideas, not the underlying math |
| M3 · ML fundamentals | ✅ **Mostly done** | loan-default predictor (1.3M rows), threshold tuning, eval |
| M4 · Deep Learning / Transformers | ❌ Not yet | scikit-learn, not PyTorch |
| M5 · LLM app engineering | 🟡 **Partial** | shipped LLM apps (Gemini, Groq, explanation layers, AI chat) |
| M6 · RAG & vector DBs | ❌ Not yet | — |
| M7 · AI Agents | ❌ Not yet | — |

**Your real starting line: M2 (patch the math) → then the fun part, M5→M6→M7.**

> ⚡ **Reorder for YOUR situation:** the generic plan goes heavy on M4 (PyTorch/Transformers deep dive). You're job-hunting *now* as a full-stack/AI-app dev, and the JDs you're applying to (VenXR, Deloitte AI, CDM Smith) want **LLM apps + RAG + agents** — which is M5-M7. So we do a **light M4** (understand, don't master) and spend real time on M5-M7. The capstone carries most of it.

---

## Milestone 2 · ML Math (patch the gap)
- **Why:** you can build models with scikit-learn, but the math is *why* things work — and it's your one honest weak spot. Enough to reason, not to prove theorems.
- **Concepts:** vectors & matrices, dot product, matrix multiply; mean/variance/covariance, probability & distributions, conditional probability; derivatives, gradients, gradient descent; **cosine similarity** (the one that unlocks embeddings later).
- **Build:** implement Linear Regression + gradient descent in **NumPy only** (no scikit-learn); compute cosine similarity by hand in NumPy.
- **Checkpoint:** explain in plain words — *why does gradient descent work? what does a loss function measure? why do embeddings use vectors?*
- **Time:** ~2 weeks. Light, code-first. Don't rabbit-hole.

## Milestone 3 · ML Fundamentals (consolidate — mostly done)
- **Why:** you've done this via the loan predictor; just close the gaps so it's solid.
- **Concepts:** the full workflow (collect → clean → EDA → feature engineering → train → evaluate → deploy); supervised (Linear/Logistic Regression, Decision Trees, Random Forests, Gradient Boosting/XGBoost); unsupervised (K-Means, dimensionality reduction); **evaluation** (precision/recall/F1, why accuracy lies — you already know this one).
- **Build:** you have 2 of 3 already (loan default = churn-style prediction). Add one **customer-segmentation** (K-Means) mini-project to cover unsupervised.
- **Checkpoint:** pick the right algorithm for a scenario; explain precision vs recall with a real example (you can already do this).
- **Time:** ~1 week (mostly review + 1 new project).

## Milestone 4 · Deep Learning & Transformers (LIGHT — understand, don't master)
- **Why:** you need to *understand* what's under an LLM to build with it well — but you don't need to train neural nets from scratch for an AI-app role.
- **Concepts (light):** what a neural network is, activation/loss functions, backprop, optimizers — conceptually. Then the part that matters: **transformer architecture** — tokenization, embeddings, positional encoding, self-attention, multi-head attention. Learn these *five* properly.
- **Build:** run a pretrained transformer for text classification with **Hugging Face** (use it, don't build it). ~1 small notebook.
- **Checkpoint:** explain self-attention in plain English; explain what an embedding *is* and why cosine similarity matters (ties back to M2).
- **Time:** ~1-2 weeks. Resist going deep on PyTorch — you can return to it later if a role demands it.

## Milestone 5 · LLM Application Engineering (your lane — go deep)
- **Why:** this is the job you're applying for *right now*. You've done pieces (Gemini, Groq, explanation layers) — make it systematic.
- **Concepts:** prompts, system instructions, context windows, tokens, **structured outputs**, **function/tool calling**, streaming responses, model APIs (OpenAI, Anthropic/Claude, Gemini, open-source via Ollama/Hugging Face); prompt engineering (as *one part* of a system, not months of templates); cost/latency awareness.
- **Build:** an **AI document summarizer** + a **document-analysis app** with structured output. (These become the front half of your capstone.)
- **Checkpoint:** build an app that takes a document, calls an LLM with a good system prompt, streams the answer, and returns structured JSON.
- **Time:** ~2-3 weeks.

## Milestone 6 · RAG & Vector Databases (the money skill)
- **Why:** RAG is the single most in-demand AI-app skill — it's how you make an LLM answer from *your* data instead of making things up. Half the JDs you saw today want this.
- **Concepts:** the full RAG pipeline (documents → chunk → embed → store in vector DB → retrieve by query → pass to LLM as context); embeddings (Sentence Transformers); **vector DBs** (Qdrant, Chroma, or FAISS); then advanced: chunking strategies, metadata filtering, hybrid search, query rewriting, reranking, **RAG evaluation**.
- **Build:** an **end-to-end RAG system** that answers questions from multiple documents *with source citations*. → this is your **"Chat With Your Docs" capstone** (parked from Session #48).
- **Checkpoint:** when answers are bad, diagnose whether it's *retrieval* or the *LLM* (the pro insight: usually retrieval).
- **Time:** ~3-4 weeks. This is the centerpiece.

## Milestone 7 · AI Agents (the frontier — do it last)
- **Why:** the current hype, but it only makes sense *after* LLM apps + RAG. An agent is not "an LLM with a long prompt."
- **Concepts:** tool calling, agent state, memory, planning, multi-step workflows, human-in-the-loop, multi-agent systems; frameworks (LangGraph, CrewAI) — but build a simple agent loop *by hand first* so you understand what the framework hides.
- **Build:** a **research agent** (searches, synthesizes, cites) or a **self-correcting code assistant**. Bolt agent capabilities onto your capstone.
- **Checkpoint:** explain why an agent needs state/memory; trace a multi-step tool-calling flow.
- **Time:** ~3-4 weeks.

---

## 🏗️ The through-line: ONE capstone carries M5-M7

Instead of scattered demos, build **one flagship: "Chat With Your Docs" AI SaaS.** It grows with each milestone:
- **M5:** upload a doc → LLM summarizes/analyzes it, streamed, structured output.
- **M6:** embed docs into a vector DB → answers grounded in *your* files, with citations (RAG).
- **M7:** add an agent that can search, call tools, and self-check.
- **Ship it:** your stack already covers deployment (Docker, CI/CD, Vercel) — a huge edge most AI learners lack.

Result: **one portfolio project that proves LLM apps + RAG + agents** — exactly what the AI-app JDs ask for.

---

## 🎯 The order, one line
**M2 math (2wk) → M3 consolidate (1wk) → M4 light DL/transformers (1-2wk) → M5 LLM apps (2-3wk) → M6 RAG (3-4wk) → M7 agents (3-4wk).**
Roughly **3-4 months** at your pace, with a shippable capstone by the end of M6.

## 📌 What this path deliberately SKIPS (and why)
- **Deep PyTorch / training models from scratch** — not needed for AI-*app* roles; return only if a job demands it.
- **Inference engineering** (GPU/vLLM/quantization) — a *layer below* you; ~58 jobs worldwide, mostly US labs. Bookmark, don't study now. (See Session #49 notes.)
- **Months of prompt-template tutorials** — prompts are one part of a system, not the system.

## 🔑 Principles (from the mentors' plans + how you learn)
1. **In order.** Most people fail by doing LangChain before they're solid on Python classes / vector similarity. You won't.
2. **Build at every milestone.** No milestone is "done" without a shipped thing.
3. **Math tied to code.** Compute cosine similarity in NumPy; don't just read the formula.
4. **Understand systems, not tools.** When a RAG answer is bad, you'll know *why* — that's the skill that pays.
5. **Your unfair advantage:** you already ship (Docker, CI/CD, deploy, testing). Most AI learners can't. Lead with it.
