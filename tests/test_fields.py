import unittest

from tabularjson.fields import collect_nested_paths


class FieldsTestCase(unittest.TestCase):
    def test_collect_nested_paths(self):
        self.assertEqual(collect_nested_paths([{}]), [])
        self.assertEqual(collect_nested_paths([{"": 1}]), [[""]])
        self.assertEqual(collect_nested_paths([{"a": 1}, {"b": 2}]), [["a"], ["b"]])
        self.assertEqual(
            collect_nested_paths([{"a": 1}, {"nested": {"b": 2}}]),
            [["a"], ["nested", "b"]],
        )
        self.assertEqual(
            collect_nested_paths([{"a": 1}, {"a": {"nested": 2}}]), [["a"]]
        )
        self.assertEqual(
            collect_nested_paths([{"a": {"nested": 2}}, {"a": 1}]), [["a"]]
        )
        self.assertEqual(collect_nested_paths([{"a": [1, 2, 3]}]), [["a"]])
        self.assertEqual(collect_nested_paths([{"a": [{"b": 2}]}]), [["a"]])
        self.assertEqual(collect_nested_paths([{"a": None}]), [["a"]])
        self.assertEqual(
            collect_nested_paths([{"a": None}, {"a": {"nested": 2}}]), [["a", "nested"]]
        )
