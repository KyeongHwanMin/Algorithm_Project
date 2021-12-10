# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python

def even_or_odd(number):
    if number % 2 == 0:
        number = 'Even'
    else:
        number = 'Odd'
    return number

# Best
# def even_or_odd(number):
#     return 'Odd' if number % 2 else 'Even'