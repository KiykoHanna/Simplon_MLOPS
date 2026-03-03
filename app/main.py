"""app.main.py."""

import pandas as pd

from app.modules.my_math import add, print_data, square, sub

__all__ = ["add", "print_data", "square", "sub"]

def main():
    """Read the csv-ffile and Execute all function."""
    df = pd.read_csv(r"moncsv.csv")
    print_data(df)
    print(add(5, 5))
    print(sub(5, 5))
    print(square(5))


if __name__ == "__main__":
    main()
