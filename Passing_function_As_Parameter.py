def add_two(num):
    return num + 2

def callingfun(func):
    a = int(input("Enter a No. : "))
    print(type(func))
    return func(a)
print(callingfun(add_two))  # passing function as passing argument.
