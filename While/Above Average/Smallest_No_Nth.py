lst = []
n = int(input("Enter how many number you want to input : "))
i=0

while(i<n):
    value = int(input(" Enter  No. : "))
    lst.append(value)
    i+=1
print("Maximum No. : ", min(lst))
    
