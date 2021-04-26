#!/usr/bin/env python3
"""Testing-Utilities."""

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """Testing that the method returns what it is supposed to."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """Testing correct output."""
        self.assertEqual(access_nested_map(map, path), expected_output)
