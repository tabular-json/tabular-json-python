import json
import math
import unittest
from os import path

from tabularjson import stringify, StringifyOptions
from tabularjson.table_properties import no_nested_arrays, no_nested_tables


class StringifyTestCase(unittest.TestCase):
    def test_suite(self):
        """Run the official stringify test-suite"""
        test_suite_file = (
            path.dirname(path.realpath(__file__)) + "/test-suite/stringify.test.json"
        )

        with open(test_suite_file, "r", encoding="utf-8") as read_file:
            suite = json.load(read_file)

            for group in suite["groups"]:
                options = (
                    to_stringify_options(group["options"])
                    if "options" in group
                    else None
                )

                for test in group["tests"]:
                    if "input_enum" in test:
                        message = f"[{group['category']}] {group['description']} (input_enum: {test['input_enum']})"
                        with self.subTest(message=message):
                            match test["input_enum"]:
                                case "negative_zero":
                                    self.assertEqual(
                                        stringify(-0, options), test["output"]
                                    )
                                case "positive_infinity":
                                    self.assertEqual(
                                        stringify(math.inf, options),
                                        test["output"],
                                    )
                                case "negative_infinity":
                                    self.assertEqual(
                                        stringify(-math.inf, options),
                                        test["output"],
                                    )
                                case "not_a_number":
                                    nan = math.inf - math.inf
                                    self.assertEqual(
                                        stringify(nan, options), test["output"]
                                    )
                                case _:
                                    raise SyntaxError(
                                        'Unknown input_enum value "'
                                        + test["input_enum"]
                                        + '"'
                                    )
                    else:
                        message = f"[{group['category']}] {group['description']} (input: {test['input']})"
                        with self.subTest(message=message):
                            self.assertEqual(
                                stringify(test["input"], options), test["output"]
                            )

    data = {
        "scores": [{"values": [1, 2, 3]}, {"values": [5, 6, 7]}],
        "data": [{"measurements": [{"x": 1, "y": 3}, {"x": 2, "y": 4}]}],
    }

    def test_output_as_table(self):
        self.assertEqual(
            stringify(self.data),
            '{"scores":(\n'
            + '"values"\n'
            + "[1,2,3]\n"
            + "[5,6,7]\n"
            + '),"data":(\n'
            + '"measurements"\n'
            + "(\n"
            + '"x","y"\n'
            + "1,3\n"
            + "2,4\n"
            + ")\n"
            + ")}",
        )

        self.assertEqual(
            stringify(self.data, {"output_as_table": no_nested_tables}),
            '{"scores":(\n'
            + '"values"\n'
            + "[1,2,3]\n"
            + "[5,6,7]\n"
            + '),"data":[{"measurements":(\n'
            + '"x","y"\n'
            + "1,3\n"
            + "2,4\n"
            + ")}]}",
        )

        self.assertEqual(
            stringify(self.data, {"output_as_table": no_nested_arrays}),
            '{"scores":[{"values":[1,2,3]},{"values":[5,6,7]}],"data":[{"measurements":(\n'
            + '"x","y"\n'
            + "1,3\n"
            + "2,4\n"
            + ")}]}",
        )

    def test_output_as_table_path(self):
        def log_paths(data):
            paths = []

            def output_as_table(_table, path):
                nonlocal paths

                paths.append(path)
                return True

            stringify(data, {"output_as_table": output_as_table})

            return paths

        self.assertEqual(log_paths([{"id": 1}]), [[]])
        self.assertEqual(log_paths([[{"id": 1}]]), [[0]])
        self.assertEqual(log_paths([[{"id": 1}], [{"id": 1}]]), [[0], [1]])
        self.assertEqual(log_paths({"table": [{"id": 1}]}), [["table"]])
        self.assertEqual(log_paths([{"table": [{"id": 1}]}]), [[], [0, "table"]])
        self.assertEqual(log_paths([[{"table": [{"id": 1}]}]]), [[0], [0, 0, "table"]])
        self.assertEqual(
            log_paths([{"table": [{"id": 1}]}, {"table": [{"id": 1}]}]),
            [[], [0, "table"], [1, "table"]],
        )
        self.assertEqual(
            log_paths(self.data), [["scores"], ["data"], ["data", 0, "measurements"]]
        )


if __name__ == "__main__":
    unittest.main()


def to_stringify_options(javascript_options) -> StringifyOptions:
    return {
        "indentation": javascript_options.get("indentation", None),
        "trailing_commas": javascript_options.get("trailingCommas", None),
    }
