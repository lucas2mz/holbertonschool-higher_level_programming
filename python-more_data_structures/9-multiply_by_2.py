#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dic = dict(a_dictionary)
    for key, value in b_dic.items():
        b_dic[key] = value * 2
    return b_dic