# Mysolution
def remainder(num1, num2):
    if num1 < num2:
        small, large = num1, num2

    else:
        small, large = num2, num1

    if small == 0:
        return None
    return large % small

# Best
# def remainder(num1, num2):
#     if min(num1, num2) == 0:
#         return None
#     elif num1 > num2:
#         return num1 % num2
#     else:
#         return num2 % num1
# Clever
# def remainder(num1, num2):
#     if min(num1, num2) != 0:
#         return max(num1, num2) % min(num1, num2)
