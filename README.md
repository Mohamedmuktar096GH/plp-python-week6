# Week 6 Assignment: Safe Functions & Error Handling

* **safe_tools.py**: Implements three error-handling functions (`safe_divide`, `safe_number`, and `get_field`) using `try` and `except` blocks to prevent crashes on invalid inputs.

**Reflection:** An `if` check alone cannot catch `"abc"` before calling `int()` because converting a non-numeric string immediately raises a `ValueError` and crashes the program unless it is wrapped inside a `try` / `except` block (and standard `if` checks like `.isdigit()` fail on negative numbers like `"-5"`).
