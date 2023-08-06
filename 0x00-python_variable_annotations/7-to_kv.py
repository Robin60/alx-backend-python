#!/usr/bin/env python3
"""Complex types - string and int/float to tuple
function to_kv that takes a string k and an int OR float v as arguments
and returns a tuple"""


from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, Union[int, float]) -> tuple[str, float]:
    """Takes a string k and an int OR float v as arguments and
    returns a tuple """

    return (k, v**2)