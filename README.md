# python-learning

A scratch repo for learning Python — coming from Ruby. Small, test-driven
exercises, one language concept at a time.

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone git@github.com:<you>/python-learning.git
cd python-learning
uv sync          # installs the pinned Python (3.13) + dev tools into .venv
```

## Working an exercise

Exercises live in `exercises/`, each isolating one concept. Tests are written
ahead of time and start red.

```bash
uv run pytest tests/test_01_functions.py -v   # watch it fail
# ...implement exercises/01_functions.py...
uv run pytest tests/test_01_functions.py -v   # get to green
uv run ruff check exercises/01_functions.py
uv run mypy exercises/01_functions.py
```

See [`LEARNING_PLAN.md`](LEARNING_PLAN.md) for the full sequence and progress.

## Toolchain

| Tool | Role |
|------|------|
| [uv](https://docs.astral.sh/uv/) | Python version, virtualenv, dependencies, lockfile |
| [ruff](https://docs.astral.sh/ruff/) | linter + formatter |
| [mypy](https://mypy.readthedocs.io/) | static type checker (strict) |
| [pytest](https://docs.pytest.org/) | test runner |

All four are configured in [`pyproject.toml`](pyproject.toml). CI
(`.github/workflows/ci.yml`) runs ruff, mypy, and pytest on every push.
