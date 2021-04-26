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


class TestGetJson(TestCase):
    """Mock HTTP calls."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Mock HTTP calls."""
        mock = Mock()
        mock.json.return_value = test_payload
        with patch('requests.get', return_value=mock):
            self.assertEqual(get_json(test_url), test_payload)
            mock.json.assert_called_once()


class TestMemoize(TestCase):
    """Parameterize and patch."""

    def test_memoize(self):
        """Correct result is returned."""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as test:
            test_class = TestClass()
            method = test_class.a_property
            method = test_class.a_property
            self.assertEqual(method, 42)
            test.a_method.assert_called_with()
