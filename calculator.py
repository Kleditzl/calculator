def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x,y):
    if x != 0 and y != 0:
        return (x/y)
    else:
        return 0

print(addition(2, 4))
print(subtraction(2, 4))
print(multiplication(2, 4))
print(division(2, 4))