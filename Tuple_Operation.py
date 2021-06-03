print("\n Tuple Concatination \n ")
t1=(1,2,3,4)    # tuple are immutable
t2=(1,2,6,7)
t1=t1+t2
print(t1)

print(t1.index(6))#return the index value search value
t3="good"               #concatination (t3 + t3 + t3)
print(t3*3,"\n",t1*3)

print("\n Index \n")
print(" t1[3]: ",t1[3])

print("\n Slice Operation  \n")
print("t1[2:6]: ",t1[2:6])  #Slice operation
print("t1[::]",t1[::])

print(t1<t2)    # compare operator return Boolean value
# t2 is greater because on index 2 is 6 and on t1 it is 3

print(t1)
print(t2)

list1=[1,2,3]
print(list1,type(list1))
print(type(tuple(list1))) # list to tuple constructor

# tuple Assignment
print("\n\n tuple Assignment")
(val1,val2,val3)=(12,13,14) #Unnamed tuple
print("\n val1 : ",val1,"\n",type(val1))
print("\n val1 : ",val2,"\n",type(val2))
print("\n val1 : ",val3,"\n",type(val3))
