def uppercase_dec(function):
    def wrapper():
        return function().upper()
    return wrapper
def somemsg():
    return "hello world"
result = uppercase_dec(somemsg)
print("the result is ",result())
        
