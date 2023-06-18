def sign(a, b):
    if (a > 0 and b > 0) or (a < 0 and b < 0):
        print(f"Numbers {a} and {b} have the same sign. ")
    elif a == 0 or b == 0:
        print("Numbers inserted equal to zero. ")
    else:
        print(f"Numbers {a} and {b} have different signs")


def minimum(a, b):
    if a < b:
        print(f"Number {a} is the smallest number. ")
    elif b < a:
        print(f"Number {b} is the smallest number. ")
    else:
        print("Numbers inserted are identical. ")


def maximum(a, b):
    if a > b:
        print(f"Number {a} is the biggest number. ")
    elif b > a:
        print(f"Number {b} is the biggest number. ")
    else:
        print("Numbers inserted are identical. ")
