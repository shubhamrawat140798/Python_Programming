''' WAP to remove duplicate from dictionary '''
d1 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':1}
d2 = {}
for key,value in d1.items():
    if value not in d2.values():
        d2[key]=value
print("Original dictionay: ",d1)
print("Alter dictionary: ",d2)
