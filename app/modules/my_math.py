"""Module de calcul mathématiques."""

import pandas as pd


def add(a: int, b: int) -> int:
    """Add two integers.

    Args: a (int): First number.
        b (int): Second number.
    Returns: int: Sum of the numbers.
    """
    return a + b

def sub(a: int, b: int) -> int:
    """Subtract two integers.

    Args:   a (int): First number.
            b (int): Second number.
    Returns: int: Diference of the numbers.
    """
    return a - b

def square(a: float) -> float:
    """Return the square of a number.

    Args: a (float): Number to square.

    Returns: float: Square of the number.
    """
    return a * a

def print_data(df: pd.DataFrame) -> int:
    """Print dataframe and nomber of lines.

    Args: df (dataframe): Dataframe for printing

    Returns: int: Lenth of dataframe
    """
    print(df)
    return len(df)
