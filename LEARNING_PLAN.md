# Python learning plan

One concept per exercise. When Adam says "let's do exercise NN" (or names the
topic), Claude scaffolds that exercise only:

- `exercises/NN_topic.py` — 3–5 tiny stub functions, each isolating one facet
- `tests/test_NN_topic.py` — written, all failing
- `notes/NN_topic.md` — short brief + the Ruby contrast + one doc link

Loop: read note → implement to green (`uv run pytest tests/test_NN_topic.py -v`)
→ `uv run ruff check` + `uv run mypy` on the file → paste to Claude for an
idiom review + one "going deeper" note → next.

## Progress

### Module A — syntax & values
- [ ] 01 · Functions & arguments — positional/keyword/default, `*args`/`**kwargs`, no implicit return
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

### Module D — structuring code
- [ ] 13 · Classes & `@dataclass` — `self`, `__init__`, `__repr__`
- [ ] 14 · Modules & imports — `import` forms, `if __name__ == "__main__"`, packages
- [ ] 15 · Exceptions — `try/except/else/finally`, EAFP vs LBYL
- [ ] 16 · Type hints in depth — `X | None`, `Sequence`, `TypeVar`, `Protocol`

### Module E — testing
- [ ] 17 · pytest properly — `parametrize`, fixtures, `pytest.raises`, structure
