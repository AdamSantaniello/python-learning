# CLAUDE.md

Context for Claude Code sessions working in this repo.

## What this is

Adam's Python learning repo. **Adam is an experienced Ruby developer** (knows
Bundler, gem, rbenv, RSpec well) learning Python from scratch, starting
August 2026. He wants to *understand* his tools and idioms, not just get
working code. **Draw explicit Ruby comparisons** when explaining anything.

This is not a product. The goal is learning, so favour clarity and teaching
over cleverness.

## How the learning works

`LEARNING_PLAN.md` holds a sequence of ~17 exercises, one concept each.

When Adam says "let's do exercise NN" (or names a topic), scaffold **only that
one**:

- `exercises/NN_topic.py` — 3–5 tiny stub functions, each isolating one facet
  of the concept. Each raises `NotImplementedError`. Full type hints.
  Docstrings with examples + a "Ruby you'd reach for / Python tools to look
  at" hint.
- `tests/test_NN_topic.py` — complete, all failing. Uses `pytest.mark.parametrize`
  where it helps. Do not make Adam edit these.
- `notes/NN_topic.md` — ~5 sentences: the concept, how it differs from Ruby,
  one link to the official docs.

Then Adam: reads the note → implements to green → runs `ruff` + `mypy` on the
file → pastes it back for an **idiom review** (is this Python or transliterated
Ruby?) plus one "going deeper" note. Then he ticks the box in `LEARNING_PLAN.md`.

**Do not scaffold exercises ahead of the one requested.** Do not hand him the
solution when he's stuck — explain the missing *concept* and let him write it.

## Toolchain

- **uv** — Python version + environment + dependency manager. Python pinned in
  `.python-version` (3.13). No pip, no manual venv.
- **ruff** — lint + format (config in `pyproject.toml`, `[tool.ruff]`).
- **mypy** — type checker, `strict = true`. Every function gets type hints.
- **pytest** — tests live in `tests/`, `pythonpath` is set so top-level modules
  import directly.
- Runtimes for Ruby/Node on this machine are managed by **mise**, not asdf.

### Commands

```bash
uv sync                       # match env to uv.lock (after clone or pull)
uv add <pkg>                   # add a runtime dependency
uv add --dev <pkg>             # add a dev dependency
uv run python <file>           # run a script in the venv
uv run pytest                  # all tests
uv run pytest tests/test_05_lists.py -v
uv run pytest -k <name>        # one function's tests
uv run ruff check .            # lint
uv run ruff format .           # format
uv run mypy .                  # type check
```

## Layout

```
hello.py                 first sanity script
exercises/NN_topic.py    one per concept, built on demand
tests/                   pytest tests
notes/NN_topic.md        short concept briefs
LEARNING_PLAN.md         the sequence + progress checkboxes
pyproject.toml           project + all tool config
.github/workflows/ci.yml runs ruff + mypy + pytest on every push
```

## Conventions

- Flat layout, no `src/`, no build system — this is not a package.
- Full type hints on everything; keep mypy strict passing.
- Keep `ruff check`, `ruff format --check`, and `mypy` clean before committing.
- Adam pushes directly to `main`. No PR workflow.
