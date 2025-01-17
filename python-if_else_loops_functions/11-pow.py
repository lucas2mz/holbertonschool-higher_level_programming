#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1

    result = 1
    negative = b < 0
    b = abs(b)

    for i in range(0, b):
        result = (a * a)
        if negative:
            return 1 / result
    return result
