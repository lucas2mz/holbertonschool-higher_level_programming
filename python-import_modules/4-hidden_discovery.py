#!/usr/bin/python3
import sys
import importlib.util


sys.path.append("/tmp")


import hidden_4


def main():
    names = dir(hidden_4)

    correct_names = [name for name in names if not name.startswith("__")]

    for name in sorted(correct_names):
        print(name)    


if __name__ == "__main__":
    main()
