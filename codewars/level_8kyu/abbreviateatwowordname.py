# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

def abbrev_name(name):
    name = name.upper()
    name = name.replace("", ".")
    return