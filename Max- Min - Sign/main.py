import functions as f

a = input("Number A: ")
b = input("Number B: ")

try:
    a = int(a)
    b = int(b)

    f.sign(a, b)
    f.minimum(a, b)
    f.maximum(a, b)

except ValueError:
    print("Invalid input! ")

