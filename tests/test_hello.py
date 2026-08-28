from hello import greeting


def test_greeting_uses_the_name() -> None:
    # pytest just needs functions named test_*; assertions are plain `assert`.
    # It rewrites `assert` under the hood to give rich failure output,
    # so you don't need RSpec-style matchers for most things.
    assert greeting("Adam") == "Hello, Adam!"


def test_greeting_is_a_string() -> None:
    assert isinstance(greeting("x"), str)
