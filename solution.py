import re
import pandas as pd

# Column labels may contain only letters and underscores (no digits, spaces, dashes, etc.)
_LABEL_RE = re.compile(r"^[A-Za-z_]+$")

# Rule format: <label><op><label>, with optional whitespace and op = + or - or *
_ROLE_ALLOWED_FORMAT_RE = re.compile(r"\s*([A-Za-z_]+)\s*([\+\-\*])\s*([A-Za-z_]+)\s*")

# Quick reject for any character outside the allowed set (catches &, \, digits, etc.)
_ROLE_ALLOWED_CHARS_RE = re.compile(r"^[A-Za-z_\s\+\-\*]*$")


def _is_valid_label(name: str) -> bool:
    """Return True if `name` contains only letters and underscores and is non-empty."""
    return isinstance(name, str) and bool(_LABEL_RE.fullmatch(name))


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    """
    Add a computed virtual column to `df` based on a simple expression in `role`.

    `role` must have the form: <column> <op> <column>, where op is one of: +, -, *.
    Whitespace is optional (e.g., "a+b" and "a + b" are both valid).

    Validation rules:
    - All existing df column names must contain only letters and underscores.
    - `new_column` must contain only letters and underscores.
    - `role` must reference exactly two valid column labels and exactly one operator (+, -, *).
    - If any validation fails, return an empty DataFrame.
    """
    if not isinstance(df, pd.DataFrame) or not isinstance(role, str) or not isinstance(new_column, str):
        return pd.DataFrame([])

    if not all(_is_valid_label(c) for c in df.columns):
        return pd.DataFrame([])

    if not _is_valid_label(new_column):
        return pd.DataFrame([])

    role_stripped = role.strip()

    if not _ROLE_ALLOWED_CHARS_RE.fullmatch(role_stripped):
        return pd.DataFrame([])

    m = _ROLE_ALLOWED_FORMAT_RE.fullmatch(role_stripped)
    if not m:
        return pd.DataFrame([])

    left, op, right = m.group(1), m.group(2), m.group(3)

    if not (_is_valid_label(left) and _is_valid_label(right)):
        return pd.DataFrame([])

    if left not in df.columns or right not in df.columns:
        return pd.DataFrame([])

    out = df.copy()
    if op == "+":
        out[new_column] = out[left] + out[right]
    elif op == "-":
        out[new_column] = out[left] - out[right]
    else:
        out[new_column] = out[left] * out[right]

    return out
