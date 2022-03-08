# https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/python
# from math import prod
#
#
# def find_difference(a, b):
#     return abs(prod(a) - prod(b))

def find_difference(a, b):
    return abs((a[1]*a[2]*a[0])-b[1]*b[2]*b[0])
