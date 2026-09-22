# Automa AI

Personal single-user project automation system — a working, end-to-end agentic pipeline that turns a plain-English prompt into a pushed GitHub repo and a published LinkedIn post.

## What it does

Give it a task like:
> "Build a modern LMS using React.js, Java Spring Boot, and MySQL with role-based auth, course creation, enrollment, quizzes, and dashboards..."

And the agent handles the rest, autonomously:

1. **Project Generation** — generates a complete, working codebase (backend, config, schema, README) from the prompt
2. **GitHub Repo & Push** — creates a repo and pushes the code with proper commit messages
3. **Repository Analysis** — analyzes its own generated repo to understand what it built
4. **LinkedIn Post Gen** — drafts a polished, structured post about the project (problem, features, tech stack)
5. **LinkedIn Published** — publishes the post via the LinkedIn REST API, after a human review/approval step

## Architecture

- **Entry Points:** `run.py`, `agent.py`, Web Dashboard (Flask app)
- **Orchestration:** Workflow Orchestrator + Workflow Store (`workflows.db`)
- **AI Services Layer:** `ai_client.py` — routes requests across multiple AI providers
- **Integrations:** GitHub Service, LinkedIn Publisher, Config Manager

## Resilience: Multi-Provider AI Fallback

Never depends on a single AI vendor — tries each provider in order until one succeeds:

1. **Ollama (Local)** — free, private, first attempt (qwen3:4b)
2. **Groq Cloud** — fast hosted inference fallback
3. **Google Gemini** — cloud fallback with JSON mode
4. **OpenAI** — final fallback for maximum coverage

## Features

- Generates full HTML/CSS/JS or full-stack codebases from natural-language prompts
- Auto add, commit (conventional commit messages), and push to GitHub
- Drafts and publishes LinkedIn posts via the LinkedIn REST API
- OAuth-based LinkedIn authentication
- Resilient JSON parsing with regex fallback extraction for inconsistent AI output
- Every action logged and auditable (`agent.log`, `automation.log`)
- Web dashboard for reviewing/editing generated posts before publishing

## Tech Stack

- **Backend:** Flask (Python)
- **AI:** Ollama, Groq, Gemini, OpenAI (multi-provider fallback)
- **Integrations:** GitHub API, LinkedIn REST API
- **Storage:** SQLite (`workflows.db`)

## Setup

```bash
git clone <repo-url>
cd automa-ai
pip install -r requirements.txt
cp .env.example .env   # add your API keys (GitHub, LinkedIn, AI providers)
python run.py
```

## Lessons Learned

- Redundancy across AI providers turns a fragile demo into a dependable system
- Automation is only trustworthy when every action is logged and auditable
- Real-world engineering means designing for failure, not just the happy path

---
Built as part of a 45-Day Agentic AI & Automation training program.
