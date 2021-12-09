def count_sheeps(sheep):
    count = 0
    for sheeps in sheep:
        if sheeps:
            count += 1
    return count


# # Best
# def count_sheeps(arrayOfSheeps):
#     return arrayOfSheeps.count(True)
