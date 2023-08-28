#!/usr/bin/env python3
"""
Parameterized a unit test
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    test access class
    """
    @parameterized.expand(
            [
                ({"a": 1}, ["a", ], 1),
                ({"a": {"b": 2}}, ["a", ], 2),
                ({"a": {"b": 2}}, ["a", "b"], 2)
            ]
    )
    def test_access_nested_map(self, nest_map, path, expected_result):
        result = access_nested_map(nest_map, path)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
