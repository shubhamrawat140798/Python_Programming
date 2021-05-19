"""
 Write a PYTHON program to produce following design 
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
If user enters n value as 5
"""
n = int(input("Enter a No. : "))
for i in range(0,n):
    for j in range(0,i+1):
        print(i+1,end=" ")
    print("") 
