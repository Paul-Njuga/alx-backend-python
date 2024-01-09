#!/usr/bin/env python3
"""
Unittest module
"""
from parameterized import parameterized
from utils import access_nested_map
from unittest import TestCase, mock
from unittest.mock import patch, Mock


class TestAccessNestedMap(TestCase):
    """Test class for nested map func"""
    # order of args: map, path, expected_output
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """Test method returns correct output"""
        output = access_nested_map(map, path)
        self.assertEqual(output, expected_output)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """Test method raises correct exception"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)
