#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not str or None:
        return 0

    num_rom = dict(I = "1", V = "5", X = "10", L = "50", C = "100", D = "500", M = "1000")

    for key, value in num_rom.items():
        if roman_string == num_rom[key]:
            return map(int, value)
