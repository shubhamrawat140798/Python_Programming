"""
. Write a PYTHON program to produce following design
A
A B
A B C
A B C D 
A B C D E
If user enters n value as 5
"""
n =int(input("Enter a No. : "))
for i in range(0,n):
    val = 65
    for j in range(0,i+1):
        print(chr(val),end=" ")
        val+=1
    print("")
