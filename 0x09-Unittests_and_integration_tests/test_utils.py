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
    def test_access_nested_map(self, map, path, output):
        """Testing correct output."""
        self.assertEqual(access_nested_map(map, path), output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, output):
        """Testing correct exception."""
        with self.assertRaises(KeyError) as error:
            access_nested_map(map, path)
            self.assertEqual(output, error.exception)
        error = error.exception
        self.assertEqual(error.args[0], output)
