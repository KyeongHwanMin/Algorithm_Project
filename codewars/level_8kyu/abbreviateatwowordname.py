# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

# def abbrev_name(name):
#     name = name.upper()
#     name = name.replace("", ".")
#     return name

def abbrev_name(name):
    return '.'.join(w[0] for w in name.split()).upper()