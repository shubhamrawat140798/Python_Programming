try:
    print("raising exception")
    raise ValueError
except:
    print("Exception caught")
finally:
    print("finally done")
print("bye")

