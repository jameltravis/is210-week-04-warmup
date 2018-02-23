#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""compares two args and evaluates if they are equal or not"""

def defaults(my_required, my_optional=True):
    """Evaluates of two arguements are equal.

    If two arguments are given, then the two aregumetns are compared for equality.
    If only the required arguemnt is given, the argument is evaluated for boolean True.

    Args:
        my_required (bool)
        my_optional (bool, optional): True

    Returns:
        bool: my_optional is my_required

    Examples:
        >>> defaults(True)
        True
        >>> defaults(True, False)
        False
        >>> defaults(False, False)
        True
    """
    return my_optional is my_required
