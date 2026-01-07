import unittest

from tabularjson.table_properties import (
    always,
    is_homogeneous,
    no_long_strings,
    no_nested_arrays,
    no_nested_tables,
)


class TablePropertiesTestCase(unittest.TestCase):
    def test_no_nested_arrays(self):
        self.assertEqual(no_nested_arrays([{}]), True)
        self.assertEqual(no_nested_arrays([{"x": 3}]), True)
        self.assertEqual(no_nested_arrays([{"nested": {"x": 3}}]), True)
        self.assertEqual(no_nested_arrays([{}, {"x": 3}]), True)
        self.assertEqual(no_nested_arrays([{}, {"scores": [4, 5]}]), False)
        self.assertEqual(no_nested_arrays([{"scores": [{"value": 2}]}]), False)
        self.assertEqual(no_nested_arrays([{}, {"scores": [{"value": 2}]}]), False)
        self.assertEqual(
            no_nested_arrays([{}, {"nested": {"scores": [{"value": 2}]}}]), False
        )
        self.assertEqual(no_nested_arrays([{}, {"nested": {"scores": [2, 3]}}]), False)

    def test_no_nested_tables(self):
        self.assertEqual(no_nested_tables([{}]), True)
        self.assertEqual(no_nested_tables([{"x": 3}]), True)
        self.assertEqual(no_nested_tables([{"nested": {"x": 3}}]), True)
        self.assertEqual(no_nested_tables([{}, {"x": 3}]), True)
        self.assertEqual(no_nested_tables([{}, {"scores": [4, 5]}]), True)
        self.assertEqual(no_nested_tables([{"scores": [{"value": 2}]}]), False)
        self.assertEqual(no_nested_tables([{}, {"scores": [{"value": 2}]}]), False)
        self.assertEqual(
            no_nested_tables([{}, {"nested": {"scores": [{"value": 2}]}}]), False
        )
        self.assertEqual(no_nested_tables([{}, {"nested": {"scores": [2, 3]}}]), True)

    def test_is_homogeneous(self):
        self.assertEqual(is_homogeneous([{}, {}, {}]), True)
        self.assertEqual(is_homogeneous([{"a": 2}, {"a": 3}, {"a": 4}]), True)
        self.assertEqual(is_homogeneous([{"a": 2}, {"b": 3}]), False)
        self.assertEqual(is_homogeneous([{"a": 2}, {"a": 3}, {"b": 4}]), False)
        self.assertEqual(is_homogeneous([{"a": 2}, {"b": None}]), False)
        self.assertEqual(
            is_homogeneous([{"nested": {"a": 2}}, {"nested": {"a": 2}}]), True
        )
        self.assertEqual(is_homogeneous([{"nested": {"a": 2}}, {"nested": {}}]), False)
        self.assertEqual(is_homogeneous([{"nested": {}}, {"nested": {"a": 2}}]), False)
        self.assertEqual(is_homogeneous([{}, {"nested": {"a": 2}}]), False)
        self.assertEqual(is_homogeneous([{"nested": {"a": 2}}, {}]), False)
        self.assertEqual(
            is_homogeneous([{"nested": {"a": 2}}, {"nested": True}]), False
        )
        self.assertEqual(
            is_homogeneous([{"arr": [{"a": 2}]}, {"arr": [{"a": 3}]}]), True
        )
        self.assertEqual(is_homogeneous([{"arr": [1, 2]}, {"arr": [3, 4]}]), True)
        self.assertEqual(is_homogeneous([{"arr": [1, 2]}, {"arr": [3, 4, 5]}]), False)
        self.assertEqual(
            is_homogeneous([{"arr": [{"a": 2}]}, {"arr": [{"b": 3}]}]), False
        )
        self.assertEqual(
            is_homogeneous([{"arr": [{"b": 2}]}, {"arr": [{"a": 0, "b": 3}]}]), False
        )

    def test_no_long_strings(self):
        # with the default max_length
        self.assertEqual(no_long_strings([{}, {}]), True)
        self.assertEqual(no_long_strings([{"value": 2}, {"value": 3}]), True)
        self.assertEqual(no_long_strings([{"comment": "bla"}]), True)
        self.assertEqual(
            no_long_strings([{"comment": "123456789012345678901234567890"}]), False
        )
        self.assertEqual(
            no_long_strings([{}, {}, {"comment": "123456789012345678901234567890"}]),
            False,
        )
        self.assertEqual(
            no_long_strings(
                [{"nested": {"comment": "123456789012345678901234567890"}}]
            ),
            False,
        )

        # with a custom max_length
        self.assertEqual(no_long_strings([{"comment": "hello world"}]), True)
        self.assertEqual(no_long_strings([{"comment": "hello world"}], 4), False)
        self.assertEqual(no_long_strings([{"comment": "1234"}], 4), True)
        self.assertEqual(no_long_strings([{"comment": "12345"}], 4), False)

    def test_always(self):
        self.assertEqual(always([]), True)
