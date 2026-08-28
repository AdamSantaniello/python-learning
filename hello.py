def greeting(name: str) -> str:
    """Return a greeting for `name`.

    The `-> str` and `name: str` are type hints. They don't affect how the
    code runs (Python ignores them at runtime), but mypy checks them, and
    your editor uses them for autocomplete and error highlighting. This is
    the "type system Ruby doesn't have" that you asked about.
    """
    return f"Hello, {name}!"


def main() -> None:
    print(greeting("world"))


if __name__ == "__main__":
    # This block runs only when the file is executed directly
    # (`python hello.py`), not when it's imported by another file
    # (like the test does). Rough analogy: Ruby's `if __FILE__ == $0`.
    main()
