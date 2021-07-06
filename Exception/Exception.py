try:
    raise Exception("hello","pooja")
except Exception as errorobj:
    print(errorobj)
    print(type(errorobj))
    print(errorobj.args)
    arg1,arg2=errorobj.args
    print("the first arg is ",arg1)
    print("the first arg is ",arg2)
