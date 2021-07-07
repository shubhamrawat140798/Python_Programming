class myError(Exception):
    def message(self):
        raise NothingimplementError()
class InputError(myError):
    def __init__(self,e,msg):
        self.e=e
        self.msg=msg
    def message(self):
        print("Input error",self.e," ",self.msg)
try:
    raise InputError("enter value of a= 10","wrong Input") 
except InputError as e:
    e.message()
