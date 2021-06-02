def uppercase_dec(function):
    def wrapper():
        return function().upper().split()
    return wrapper
@uppercase_dec
def somemsg():
    return "hello world"
print("the result is ",somemsg())
        
