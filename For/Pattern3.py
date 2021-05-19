"""
Write a PYTHON program to produce following design
A B C D E
A B C D
A B C
A B
A
"""
n =int(input("Enter a No. : "))
for i in range(0,n):
    val = 65
    for j in range(0,n-i):
        print(chr(val),end=" ")
        val+=1
    print("")
