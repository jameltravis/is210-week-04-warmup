#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Creates a funny string.
    Args:
        wink (str): Arg to be multiplied by numwink and striped of spaces
        numwink (int, optional): Number of times wink and 'nude ' are repeated. Default is 2.

    Returns:
        str: 'Know what I mean <var1>, [<var2>]':

    Examples:

        >>> know_what_i_mean('toot')
        'Know what I mean? toottoot, nudge nudge'
        >>> know_what_i_mean('toot', 3)
        'Know what I mean? toottoottoot, nudge nudge nudge

    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
