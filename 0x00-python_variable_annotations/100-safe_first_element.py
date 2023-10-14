#!/usr/bin/env python3
""" Augment the code """
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) \
     -> typing.Union[typing.Any, None]:
    """ ruturn any data or none """
    if lst:
        return lst[0]
    else:
        return None
