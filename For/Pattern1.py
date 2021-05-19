"""
Write a PYTHON program to produce following design
 A B C 
 A B C 
 A B C 

"""

for i in range(0,3):
    val = 65
    for i in range(0,3):
        print(chr(val),end=' ')
        val+=1
    print("")

