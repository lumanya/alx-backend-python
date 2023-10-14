#!/usr/bin/env python3
""" Type annotation of complex types - list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of float as input and return their sum


    Args:
    input_list (List[float] = list of floats
    Returns:
    float: sum of the input list
    """
    return sum(input_list)
