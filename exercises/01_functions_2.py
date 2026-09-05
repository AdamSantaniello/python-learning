"""Exercise 01b · Functions & arguments — extra drills.

More reps on two things that tripped you up in 01: checking whether a
collection is empty (truthiness, not `len(x) == 0`) and iterating a dict
(`.items()`, not just the keys). Replace each `raise NotImplementedError`
with a real body.

Run: `uv run pytest tests/test_01_functions_2.py -v`
"""


def has_data(value: list[int] | dict[str, int] | str) -> bool:
    """Return whether `value` has anything in it.

    Works for a list, a dict, or a string — no `len(...)` allowed.

    >>> has_data([])
    False
    >>> has_data({"a": 1})
    True
    >>> has_data("")
    False

    Ruby you'd reach for: `value.empty?`. Python has no universal `.empty?`;
    instead every built-in collection (and string) is falsy when empty, so
    `if value:` / `if not value:` does the job directly — Python tools to
    look at: truthiness of `[]`, `{}`, `""`, `0`, `None`.
    """
    return bool(value)


def pick_first_nonempty(*groups: list[int]) -> list[int]:
    """Return the first non-empty list among `groups`, or `[]` if all are empty.

    >>> pick_first_nonempty([], [], [1, 2])
    [1, 2]
    >>> pick_first_nonempty([], [])
    []

    Ruby you'd reach for: `groups.find { |g| !g.empty? } || []`. Here `*groups`
    collects the arguments into a tuple you can loop over (Python tools to
    look at: plain `for`, truthiness again — no index or `len` needed).
    """
    result = []

    for group in groups:
        if group:
            result = group
            break

    return result


def describe_counts(counts: dict[str, int]) -> str:
    """Render a dict as `"key: value"` lines joined with `", "`.

    Empty dict -> the literal string `"no counts"`.

    >>> describe_counts({"cats": 2, "dogs": 1})
    'cats: 2, dogs: 1'
    >>> describe_counts({})
    'no counts'

    Ruby you'd reach for: `hash.map { |k, v| "#{k}: #{v}" }.join(", ")`.
    Iterating a Python dict directly (`for k in counts`) only gives you keys —
    Python tools to look at: `counts.items()` to get `(key, value)` pairs, and
    an empty-dict check via truthiness, not `len(counts) == 0`.
    """

    if not counts:
        return "no counts"

    results: list[str] = []
    for key, value in counts.items():
        results.append(f"{key}: {value}")

    return ", ".join(results)


def merge_totals(*dicts: dict[str, int]) -> dict[str, int]:
    """Merge any number of `{name: count}` dicts, summing shared keys.

    >>> merge_totals({"a": 1, "b": 2}, {"b": 3, "c": 4})
    {'a': 1, 'b': 5, 'c': 4}
    >>> merge_totals()
    {}

    Ruby you'd reach for: `dicts.reduce(Hash.new(0)) { |acc, h| h.each { |k, v|
    acc[k] += v }; acc }`. Combines two things from this exercise: `*dicts`
    collects however many dicts were passed, and each one needs `.items()` to
    walk its pairs (Python tools to look at: `dict.get(key, default)` to add
    into a running total without a `KeyError`).
    """
    result: dict[str, int] = {}
    for d in dicts:
        for key, value in d.items():
            result[key] = result.get(key, 0) + value

    return result
