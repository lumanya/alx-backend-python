#!/usr/bin/env python3
"""
typed-annotated function to_kv that takes a  string k and an int  OR float
v as an argument and return tuple. the first element of the tuple is the string
the second element is the square of the int/float v  and should be annotated
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """ Return  tuple """
    return k, v ** 2
