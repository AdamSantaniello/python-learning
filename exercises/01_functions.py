"""Exercise 01 · Functions & arguments.

Five tiny functions, each isolating one facet of how Python does parameters
and return values. Replace each `raise NotImplementedError` with a real body.
Run: `uv run pytest tests/test_01_functions.py -v`
"""


def rectangle_area(width: float, height: float = 1.0) -> float:
    """Return the area of a rectangle.

    `height` defaults to 1.0, so `rectangle_area(5)` treats it as a 5x1 strip.

    >>> rectangle_area(3, 4)
    12
    >>> rectangle_area(5)
    5.0

    Ruby you'd reach for: `def rectangle_area(width, height = 1)` — and Ruby
    would return the last expression automatically. Python does NOT: a function
    with no `return` hands back `None`. You must write `return`.
    """
    return width * height


def greet(name: str, *, greeting: str = "Hello") -> str:
    """Return "<greeting>, <name>!".

    The bare `*` means everything after it is *keyword-only*: callers must
    write `greet("Sam", greeting="Hi")`, never `greet("Sam", "Hi")`.

    >>> greet("Sam")
    'Hello, Sam!'
    >>> greet("Sam", greeting="Hi")
    'Hi, Sam!'

    Ruby you'd reach for: real keyword arguments — `def greet(name, greeting:
    "Hello")`. Python's twist is the `*` separator that forces the keyword form.
    """
    return f"{greeting}, {name}!"


def total(*numbers: float) -> float:
    """Sum any number of positional arguments. No arguments -> 0.

    >>> total(1, 2, 3)
    6
    >>> total()
    0

    Ruby you'd reach for: the splat — `def total(*numbers)`. Nearly identical.
    Inside the function `numbers` is a tuple (Python tools to look at: the
    built-in `sum`).
    """
    return sum(numbers)


def build_query(base: str, **params: str) -> str:
    """Append `key=value` pairs to `base` as a query string.

    With no params, return `base` unchanged. Otherwise join pairs with `&`
    and attach with `?`. Insertion order is preserved (dicts are ordered).

    >>> build_query("/search")
    '/search'
    >>> build_query("/search", q="cats", page="2")
    '/search?q=cats&page=2'

    Ruby you'd reach for: `**opts` or a trailing options hash. In Python
    `**params` collects leftover keyword arguments into a dict (Python tools to
    look at: `dict.items`, `str.join`).
    """
    if not params:
        return base

    return f"{base}?{'&'.join([f'{key}={value}' for key, value in params.items()])}"


def minmax(numbers: list[int]) -> tuple[int, int]:
    """Return `(smallest, largest)` from a non-empty list.

    >>> minmax([3, 1, 4, 1, 5])
    (1, 5)

    Ruby you'd reach for: returning `[numbers.min, numbers.max]` — an array.
    Python returns a tuple, and the caller can unpack it: `lo, hi = minmax(xs)`.
    A "multiple return values" function is really just one tuple.
    """
    return min(numbers), max(numbers)
