"""Tests for exercise 01b. All failing until you implement the stubs.

Run just these:  uv run pytest tests/test_01_functions_2.py -v
"""

from importlib import import_module

import pytest

ex = import_module("01_functions_2")


class TestHasData:
    @pytest.mark.parametrize(
        ("value", "expected"),
        [
            ([], False),
            ([0], True),
            ({}, False),
            ({"a": 1}, True),
            ("", False),
            ("hi", True),
        ],
    )
    def test_reports_emptiness_by_truthiness(
        self, value: list[int] | dict[str, int] | str, expected: bool
    ) -> None:
        assert ex.has_data(value) is expected


class TestPickFirstNonempty:
    def test_skips_leading_empty_lists(self) -> None:
        assert ex.pick_first_nonempty([], [], [1, 2]) == [1, 2]

    def test_returns_first_match_not_last(self) -> None:
        assert ex.pick_first_nonempty([], [1], [2]) == [1]

    def test_all_empty_returns_empty_list(self) -> None:
        assert ex.pick_first_nonempty([], []) == []

    def test_no_args_returns_empty_list(self) -> None:
        assert ex.pick_first_nonempty() == []


class TestDescribeCounts:
    def test_multiple_entries_join_with_comma(self) -> None:
        assert ex.describe_counts({"cats": 2, "dogs": 1}) == "cats: 2, dogs: 1"

    def test_single_entry_no_trailing_comma(self) -> None:
        assert ex.describe_counts({"cats": 2}) == "cats: 2"

    def test_empty_dict(self) -> None:
        assert ex.describe_counts({}) == "no counts"


class TestMergeTotals:
    def test_sums_shared_keys(self) -> None:
        assert ex.merge_totals({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {
            "a": 1,
            "b": 5,
            "c": 4,
        }

    def test_no_dicts_returns_empty_dict(self) -> None:
        assert ex.merge_totals() == {}

    def test_single_dict_returned_unchanged(self) -> None:
        assert ex.merge_totals({"x": 5}) == {"x": 5}

    def test_three_dicts(self) -> None:
        assert ex.merge_totals({"a": 1}, {"a": 1}, {"a": 1}) == {"a": 3}
