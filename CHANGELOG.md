# Changelog

## 2.0.0 (2026-02-25)

Breaking changes:

- Feat: changes the table syntax from `---...---` to `(...)`. The change is implemented in a backward compatible way. You can parse tables in both the old and new format, but stringifying data will now output tables with the new syntax.
- Feat: the current `path` is now passed too via the `output_as_table` callback of function `stringify`. The callback function now requires two arguments: `output_as_table(tabular_data, path)` (#17).

## 1.1.3 (2026-01-27)

- Fix: improve parsing of tables inside tables.

## 1.1.2 (2026-01-24)

- Fix: correctly identify table start and end in nested tables.

## 1.1.1 (2025-11-24)

- Fix: improve field alignment of nested tables inside a table.

## 1.1.0 (2025-11-22)

- Feat: function `stringify` has a new option `output_as_table` and helper functions `no_nested_arrays`, `no_nested_tables`, `is_homogeneous`, `no_long_strings`, and `always`.
- Fix: improved formatting of tables inside tables.
- Fix: renamed `stringify` option `trailingCommas` to `trailing_commas`.

## 1.0.2 (2025-10-20)

- Fix: refine empty input error message.
- Fix: added more unit tests to the test suite.

## 1.0.1 (2025-09-30)

- Fix: added more unit tests to the test suite.

## 1.0.0 (2025-09-30)

- First version published.
