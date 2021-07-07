def mul(num):
    return num**2
try:
    mul("abc")
except TypeError as tp:
    print("excerption caught",tp.args)
