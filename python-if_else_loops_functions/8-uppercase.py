#!/usr/bin/python3
def uppercase(str):
    str_upper = ""
    for char in str:
        if char >= 'a' and char <= 'z':
            str_upper += chr(ord(char) - 32)
        else:
            str_upper += char
    print("{}".format(str_upper))