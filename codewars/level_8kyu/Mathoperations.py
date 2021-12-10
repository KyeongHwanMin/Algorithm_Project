# https://www.codewars.com/kata/59c287b16bddd291c700009a/train/python
# Best
# def ice_brick_volume(radius, bottle_length, rim_length):
#     return (bottle_length - rim_length) * 2 * radius ** 2


def ice_brick_volume(radius, bottle_length, rim_length):
    return radius * (2 * radius) * (bottle_length - rim_length)
