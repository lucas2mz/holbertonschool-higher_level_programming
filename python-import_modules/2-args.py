#!/usr/bin/python3
import sys

def main():
    arguments = sys.argv[1:]
    argc = len(arguments)

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print("1: {}".format(arguments[0]))
    else:
        print("{} arguments:".format(argc))
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg))
if __name__ == "__main__":
    main()
