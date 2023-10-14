#!/usr/bin/env python3
""" Annotate the function """
import typing


def element_length(list: typing.Iterable[typing.Sequence]) \
     -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """ annotated function that return list which contains tuple"""
    return [(i, len(i)) for i in lst]
