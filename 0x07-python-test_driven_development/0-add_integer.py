#!/usr/bin/python3
"""writing an integer addition function."""


def add_integer(a, b=98):
    """Returning the integer addition of a and b.

    Float arg are typecasted to ints before addition is done or executed.

    Raises:
        TypeError: If a or b is a non-integer or  non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
