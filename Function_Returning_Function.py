def hello_function():
    def say_hi():       #inner function
        str="hello"
        return str
    return say_hi       #call to say_hi function
hello = hello_function()
print(hello)
print(hello())
print(type(hello))
