"""Tests for exercise 01. All failing until you implement the stubs.

Run just these:  uv run pytest tests/test_01_functions.py -v
"""

from importlib import import_module

import pytest

# The exercise file is `exercises/01_functions.py`. Its name starts with a
# digit, so `from 01_functions import ...` is a syntax error — load it by
# string name instead. Your own code never needs this trick.
ex = import_module("01_functions")


class TestRectangleArea:
    def test_uses_both_arguments(self) -> None:
        assert ex.rectangle_area(3, 4) == 12

    def test_height_defaults_to_one(self) -> None:
        assert ex.rectangle_area(5) == 5.0

    def test_returns_a_value_not_none(self) -> None:
        # The Ruby-habit trap: forgetting `return` makes this None.
        assert ex.rectangle_area(2, 2) is not None


class TestGreet:
    def test_default_greeting(self) -> None:
        assert ex.greet("Sam") == "Hello, Sam!"

    def test_custom_greeting_by_keyword(self) -> None:
        assert ex.greet("Sam", greeting="Hi") == "Hi, Sam!"

    def test_greeting_is_keyword_only(self) -> None:
        with pytest.raises(TypeError):
            ex.greet("Sam", "Hi")


class TestTotal:
    @pytest.mark.parametrize(
        ("args", "expected"),
        [
            ((1, 2, 3), 6),
            ((), 0),
            ((10,), 10),
            ((-1, 1), 0),
        ],
    )
    def test_sums_any_number_of_args(
        self, args: tuple[float, ...], expected: float
    ) -> None:
        assert ex.total(*args) == expected


class TestBuildQuery:
    def test_no_params_returns_base(self) -> None:
        assert ex.build_query("/search") == "/search"

    def test_one_param(self) -> None:
        assert ex.build_query("/search", q="cats") == "/search?q=cats"

    def test_multiple_params_keep_order(self) -> None:
        assert ex.build_query("/search", q="cats", page="2") == "/search?q=cats&page=2"


class TestMinmax:
    def test_returns_low_high_tuple(self) -> None:
        assert ex.minmax([3, 1, 4, 1, 5]) == (1, 5)

    def test_result_unpacks(self) -> None:
        lo, hi = ex.minmax([7, 2, 9])
        assert (lo, hi) == (2, 9)

    def test_single_element(self) -> None:
        assert ex.minmax([42]) == (42, 42)
