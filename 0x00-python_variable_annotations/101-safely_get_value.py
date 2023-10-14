#!/usr/bin/env python3
""" Type annotate function """
import typing
from typing import TypeVar


T = TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any,
                     default: typing.Union[T, None] = None) \
                     -> typing.Union[typing.Any, T]:
    """ Type annotation """
    if key in dct:
        return dct[key]
    else:
        return default
