def adder(number):
    print("adder")
    print(type(number))
    return number +1
def fun1(function):
    print("fun1")
    print(type(function))
    return function(12)
print(fun1(adder))

