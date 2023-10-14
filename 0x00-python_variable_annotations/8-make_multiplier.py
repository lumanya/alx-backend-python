#!/usr/bin/env python3
"""
Type-annotated function that takes a float multiplier as argument and returns
function that mutiplies a float by multipilier
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """ return a float by multiplier """
    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func
