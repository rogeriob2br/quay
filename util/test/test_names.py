# -*- coding: utf-8 -*-

import pytest
import re

from util.names import escape_tag, REPOSITORY_NAME_REGEX


@pytest.mark.parametrize(
    "input_tag, expected",
    [
        ("latest", "latest"),
        ("latest124", "latest124"),
        ("5de1e98d", "5de1e98d"),
        ("detailed_view#61", "detailed_view_61"),
        ("-detailed_view#61", "_detailed_view_61"),
    ],
)
def test_escape_tag(input_tag, expected):
    assert escape_tag(input_tag) == expected


@pytest.mark.parametrize(
    "name, should_match",
    [
        ("devtable", True),  # Lowercase allowed
        ("DevTable", False),  # Uppercase NOT allowed
        ("dev-table", True),  # Hyphens allowed
        ("dev_table", True),  # Underscores allowed
        ("devtable123", True),  # Numbers allowed
        (u"🌸", False),  # Non-ASCII NOT allowed
    ],
)
def test_repository_names_regex(name, should_match):
    """
    Verify that repository names conform to the standards/specifications.
    """
    result = re.match(REPOSITORY_NAME_REGEX, name)
    assert bool(result) == should_match
