#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Do you have enough cats?"""

def too_many_kittens(kittens, litterboxes, catfood):
    """Checks to see if you have too many kittens.

    if you have:
        (a) more kittens than litterboxes and/or
        (b) no catfood.
    Then you have too many cats.

    Args:
        kittens (int): number of kittens
        litterboxes (int): number of available litterboxes
        catfood (mixed): whether or not catfood exists

    Returns:
        bool: not (litterboxes >= kittens and catfood)

    Examples:

        >>> too_many_kittens(12, 12, False)
        True
        >>> too_many_kittens(13, 12, True)
        True
        >>> too_many_kittens(12, 13, True)
        False

    """
    return not (litterboxes >= kittens and catfood)
