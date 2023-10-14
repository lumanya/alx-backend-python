#!/usr/bin/env python3
""" Type-annotated function which takes a list of mixed integer and float
and retunr sum as float
"""
import typing
from typing import List


def sum_mixed_list(mxd_lst: List[typing.Union[int, float]]) -> float:
    """ ruturn sum of the list as float """
    return sum(mxd_lst)
