# 102V_flask

Minimal Flask app — single route at `/` rendering `templates/index.html`.

## Commands

| Action | Command |
|--------|---------|
| Install deps | `uv sync` |
| Add a package | `uv add <package>` |
| Run dev server | `uv run flask run` |
| Run directly | `uv run python main.py` |

The Flask app object is `main:app` (module `main`, variable `app`).

## Python & tooling

- Python 3.14 required (`.python-version`)
- Package manager: `uv` (not pip/poetry/virtualenv)
- No tests, no CI, no linting/formatting config
- Templates live in `templates/` (Flask default)
