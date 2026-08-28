# Python learning plan

## How this works

This is a **menu, not a track.** Work through what's useful, skip what's
already obvious, do topics out of order if you feel like it. It's "done" when
you're comfortable enough to build things — **not** when every box is ticked.
You're an experienced programmer; some of these you'll finish in five minutes
or skip outright. That's the plan working, not cheating.

Two modes, switch freely:

- **Drill mode** — "let's do exercise 07". Claude scaffolds *that one only*:
  - `exercises/NN_topic.py` — 3–5 tiny stubs, each isolating one facet
  - `tests/test_NN_topic.py` — written, all failing
  - `notes/NN_topic.md` — short brief + the Ruby contrast + one doc link

  Loop: read note → implement to green
  (`uv run pytest tests/test_NN_topic.py -v`) → `ruff` + `mypy` on the file →
  paste to Claude for an idiom review + one "going deeper" note.

- **Project mode** — "I want to build X". Claude helps scaffold it; you write
  it; Claude reviews idioms *in context* as you go. Small experiments live in
  `projects/<name>/`. Anything that could become real graduates to its own repo.

You can also ask for **more / harder / mixed drills** on any topic at any time —
see "Extra drills" below.

## Drill sequence (worth doing as isolated exercises)

These are pure Python muscle — small, mechanical, benefit from reps. This is
the part that rebuilds hands-on-keyboard dexterity.

### Module A — syntax & values
- [x] 01 · Functions & arguments — positional/keyword/default, `*args`/`**kwargs`, no implicit return
- [ ] 02 · Strings — f-strings, methods, slicing, immutability, `"sep".join(...)`
- [ ] 03 · Numbers & booleans — `/` vs `//`, truthiness, `None` vs `nil`, `is` vs `==`
- [ ] 04 · Conditionals — `if/elif/else`, ternary expression, `and`/`or` short-circuit, `match`

### Module B — collections
- [ ] 05 · Lists — methods, slicing, in-place mutation, `.append` returns `None`
- [ ] 06 · Tuples & unpacking — multiple assignment, `a, *rest = ...`, swap, tuple vs list
- [ ] 07 · Dicts — `.get`, `.items()`, `setdefault`, `defaultdict`, `Counter`
- [ ] 08 · Sets — membership, dedup, `| & - ^`
- [ ] 09 · Iteration — `for x in`, `enumerate`, `zip`, `range`, no `for i in range(len())`
- [ ] B-checkpoint · rebuild of the old capstone (`initials`, `tally`, `first_duplicate`, `chunk`)

### Module C — Pythonic transformation
- [ ] 10 · Comprehensions — list / set / dict / generator
- [ ] 11 · Generators & laziness — `yield`, generator expressions, one-shot iterators
- [ ] 12 · Key built-ins — `sorted`/`min`/`max` with `key=`, `any`/`all`, `sum`

## Learn in context (not as isolated drills)

These barely make sense in a vacuum — pick them up when a project forces the
topic, and write a `notes/` file then. Ask Claude for a focused exercise only
if a project isn't giving you enough reps.

- [ ] Classes & `@dataclass` — `self`, `__init__`, `__repr__`
- [ ] Modules & imports — `import` forms, `if __name__ == "__main__"`, packages
- [ ] Exceptions — `try/except/else/finally`, EAFP vs LBYL
- [ ] Type hints in depth — `X | None`, `Sequence`, `TypeVar`, `Protocol`
- [ ] pytest properly — `parametrize`, fixtures, `pytest.raises`, structure

## Friction log

Claude appends a row after each idiom review — this is the memory across
sessions. Confidence is Claude's read at the end of the review (`shaky` / `ok`
/ `solid`); Adam can overrule it. Used to decide what needs another pass and to
answer "what should I work on?".

| Date | Topic | Confidence | What tripped me up | Follow-up |
|------|-------|-----------|--------------------|-----------|
| 2026-08-28 | 01 · Functions & arguments | ok | Dict iteration yields keys, not pairs (needed `.items()`); `if not params:` for empty-dict check instead of `len(...) == 0`; "multiple return values" = one tuple | Watch for `len(x) == 0` / explicit empty checks in future exercises — the falsy-collection idiom |

## Extra drills

More reps on a topic you've already done. Ask for "more list drills", "harder
dict drills", "edge-case heavy", "speed round", or "mixed review of everything
so far". Files land flat: `exercises/05_lists_2.py`, `exercises/review_01.py`, etc.

Log them here so you can see what you've hammered:

| Date | File | Topic | Notes |
|------|------|-------|-------|
|      |      |       |       |

## Idea stash

Small things worth building. Add a row whenever an idea strikes so it's not
lost — scope and idiom coverage get figured out when you pick one. Ask Claude
"what should I work on?" any time and it'll pull from here plus the drill list.

Seeds:

| Idea | Flavour |
|------|---------|
| `wc` clone — count lines / words / chars in a file | CLI, strings, file IO |
| Batch file renamer — rename files in a dir by pattern | CLI, `pathlib`, strings |
| CSV summary stats — min/max/mean/count per column (stdlib `csv`, no pandas) | parsing, dicts, numbers |
| RPN calculator — evaluate `3 4 + 2 *` | parsing, stack/list, `match` |
| `grep` clone — print lines matching a pattern, with `-n`, `-i` | CLI, regex, iteration |
| Terminal tic-tac-toe — 2-player, detect wins | state, loops, `match` |
| Mini `jq` — pull a key path out of a JSON file | `json`, recursion, CLI |
| Log analyzer — top IPs / status codes from an nginx or Apache log | regex, `Counter`, sorting |

Your additions:

| Date | Idea | Notes |
|------|------|-------|
|      |      |       |

## Projects

Things built in project mode. Add a row when you start one.

| Date | Location | What it is | Status |
|------|----------|------------|--------|
|      |          |            |        |
