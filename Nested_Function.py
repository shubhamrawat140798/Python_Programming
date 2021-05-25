def inner(number):
    def outter(number):
        return number+2
    res = outter(number)
    return res
print(inner(5))
