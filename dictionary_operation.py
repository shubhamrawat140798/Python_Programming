def dict_op():
    dict1={"name":"Shubham","rno":27}
    dict2=dict.fromkeys(dict1)      #copy the key value only
    dict3=dict.fromkeys(dict1,-1)   #copy the key value and assign value with default
    dict4=dict1.copy()              #copy the dictionary    
    print("dict1: ",dict1)
    print("dict2: ",dict2)
    print("dict3: ",dict3)
    print("dict4: ",dict4)

    # in operation
    print("dict4.get(): ",dict4.get("name"))
    print("name is present in dict4: ","name" in dict4)

    #update method
    dict5={"address":"shalimar Bagh"}
    dict4.update(dict5)
    print("dict4",dict4)

    # not in operation
    print("address is not present in dict1:","address" not in dict1)

    #format
    for k,v in dict4.items():
        print("%s : %s"%(k,str(v)))
print("choices:","1. Dictionary Opperation",sep="\n")
n = int(input("Enter your choice: "))
if(n==1):
    dict_op()
    
