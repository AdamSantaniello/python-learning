# 01 · Functions & arguments

Python functions look like Ruby methods but differ in three ways that bite
early. **There is no implicit return** — a function that falls off the end
returns `None`, so you must write `return` everywhere you want a value (the
biggest habit to unlearn). **Argument passing is richer and more explicit**:
`def f(a, b=1)` gives defaults like Ruby, a bare `*` in the signature makes
every following parameter *keyword-only*, `*args` collects extra positionals
into a tuple, and `**kwargs` collects extra keyword arguments into a dict.
**"Multiple return values" isn't a real thing** — `return a, b` builds one
tuple, and the caller unpacks it with `lo, hi = f(...)`, exactly like Ruby's
`a, b = ...` on an array.

One gotcha not drilled here but worth knowing: a mutable default like
`def f(x=[])` is created *once* and shared across calls — use `x=None` and
build inside. (Ruby evaluates default expressions fresh each call, so this
surprises people coming from Ruby.)

Docs: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
