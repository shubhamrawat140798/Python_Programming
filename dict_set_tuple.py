# Zip operation
def Zip_Op():
    print("\nZip Operation\n")
    list1=[1,2,3,4,5]
    list2=["shubham","deepak","saksham"]
    print(list1,"\n",list2)
    print(list(zip(list1,list2)))
    t1 =(12.34,14.23,45,56)
    print(list(zip(list1,t1)))
    print(list(zip(list1,list2,t1)))
def Set_Op():
    print("\nSet Operation\n")
    set1={1,2,3,4,5,6}
    print(set1)
    set2={9,10}
    print(set1)
    set1.update(set2)               # update
    print(set1)
    set1.add(12)                    # add()
    print(set1)
    set1.remove(12)                 # remove()
    print(set1)
    set1.discard(3)                 # discard()
    print(set1)
    set1.pop()                      # pop()
    print(set1)
    print(len(set1))
    if (4 in set1):                 # if operation on set
        print("It is present! ")
    else:
        print("Not present !")
    if (3 not in set1):
        print("It is not present! ")
    else:
        print("It is  present !")
    set1={1,2,3,4,5,6,7}
    set2={7,8,9}
    print("set 1 is subset of set2: ",set1.issubset(set2))      #Check for subset
    print("set1>=set2 : ",set1>=set2)
    print("set1<set2: ",set1<set2)
    print("set 1 is supperset of set2",set1.issuperset(set2))
    print("set1.union(set3): ",set1.union(set2))
    print("set1|set2: ",set1|set2)
    print("set1&set2: ",set1&set2)
    print("set1.intersection(set2): ",set1.intersection(set2))
    print("set1.intersection_update(set2)",set1.intersection_update(set2))
    print("set1: ",set1)
    print("set1-set2: ",set1-set2)
    print(set1.difference(set2))
    print("set1^set2: ",set1^set2)
    print(set1.symmetric_difference(set2))
    set4= set1.copy()
    print("set1: ",set1)
    print("set4: ",set4)
    print("id of set1: ",id(set1))
    print("id of set4: ",id(set4))
    print("set1.isdisjoint(set4): ",set1.isdisjoint(set4))
def dict_Op():
    print("\nDictionay Operation\n")
    dict1={"name":"shubham","age":23,"marks":60}
    print("dict1: ",dict1)                 # keys in dictionary is immutable
    print("value at key age: ",dict1['age'])
    dict1['class']="1st year"
    print("dict1: ",dict1)
    print("sorted(dict1): ",sorted(dict1))
    print("\nfor i in dict1: ")
    for i in dict1:
        print(i)
    print("\nfor i in dict1.values(): ")
    for i in dict1.values():
        print(i)
    print("\nfor i in dict1.items(): ")
    for i in dict1.items():
        print(i)
    
print("Choice: ")
print("1.zip","2.set","3.Dict",sep="\n")
n=int(input("Enter your choice: "))
if(n==1):
    Zip_Op()
elif(n==2):
    Set_Op()
elif(n==3):
    dict_Op()
else:
    print("Wrong Input")
