# Applying this yourself — setup in 10 minutes

This repo turns **Claude Code** into a Python mentor with memory. Here's how to get running from a clean machine.

## What you need

1. **Python 3** — check with `python3 --version` (Windows: `python --version`). If missing, install from [python.org](https://www.python.org/downloads/) and tick "Add to PATH".
2. **VS Code** — [code.visualstudio.com](https://code.visualstudio.com/). Install the **Python** extension (by Microsoft) from the Extensions panel.
3. **Claude Code** — Anthropic's CLI/agent. Install per [the official docs](https://docs.claude.com/en/docs/claude-code). It runs inside VS Code's terminal or as an extension.
4. **An Anthropic API key** — set it so Claude Code can authenticate.

## Setup steps

```bash
# 1. Clone this repo
git clone https://github.com/nikita1-pixel/python_Claude.git
cd python_Claude

# 2. Open it in VS Code
code .

# 3. Provide your Anthropic API key (one option below)
export ANTHROPIC_API_KEY="sk-ant-..."     # macOS/Linux, current shell
# Windows PowerShell:  $env:ANTHROPIC_API_KEY="sk-ant-..."
# (or run `claude` and follow its login/auth prompt)

# 4. Launch Claude Code in this folder
claude
```

When Claude starts inside this folder it **auto-reads `CLAUDE.md`** (the coaching brain) and `memory/study-state.md` (your progress). It'll greet you and offer the next step.

## How to use it day to day

- Say **"start session"** → it begins Phase 0+1, creates a dated log in `sessions/`, and teaches click-by-click.
- Say **"test me"** → a checkpoint quiz on the current phase.
- Say **"I built X"** → logged to your Wins list.
- Say **"wrap up"** → saves your resume point so tomorrow is a warm start.
- Type **`/python`** as a shortcut to (re)enter mentor mode.

## Save your progress

Your learning is recorded in `memory/study-state.md` and `sessions/`. Commit it so it's never lost and you can resume on any machine:

```bash
git add memory sessions projects exercises
git commit -m "study: progress through phase N"
git push
```

> Tip: a separate practice repo of just your `projects/` makes a tidy portfolio for interviews.

## Notes on the API key

- Using someone else's API key means **they pay for the tokens** your sessions consume. Be considerate — wrap up sessions you're done with, and don't leave it running idle.
- Treat the key like a password: never commit it, never paste it into a file in the repo. Set it as an environment variable as shown above.

## Troubleshooting

| Problem | Fix |
|---|---|
| `python3: command not found` | Use `python` (Windows), or reinstall Python with "Add to PATH". |
| Claude doesn't greet / ignores the plan | Make sure you launched it **inside** the `python_Claude` folder so it loads `CLAUDE.md`. |
| Run button missing in VS Code | Install the Microsoft **Python** extension. |
| Auth errors | Re-check `ANTHROPIC_API_KEY`, or run `claude` and complete the login prompt. |
