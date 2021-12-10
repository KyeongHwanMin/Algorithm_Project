# https://www.codewars.com/kata/54edbc7200b811e956000556/train/python
def count_sheeps(sheep):
    count = 0
    for sheeps in sheep:
        if sheeps:
            count += 1
    return count


# # Best
# def count_sheeps(arrayOfSheeps):
#     return arrayOfSheeps.count(True)
