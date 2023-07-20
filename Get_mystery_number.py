# This program looks for a number under these conditions:
# 1- contains 3 numbers
# 2- Smaller than 1000
# 3- Bigger than 499
# 4- Impair number
# 5- At least 2 of the numbers are identical
# 6- total of the three numbers is 9

def identical_check(number):
    if number[0] == number[1] or number[0] == number[2] or number[1] == number[2]:
        return True
    else:
        return False


def sum_check(number):
    if int(number[0]) + int(number[1]) + int(number[2]) == 9:
        return True
    else:
        return False


numbers = list(range(501, 1000, 2))

for number in numbers:
    number = str(number)
    if identical_check(number) and sum_check(number):
        print("Mystery number is: ", number)
