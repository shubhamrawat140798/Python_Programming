""" PYTHON program that prints       1 2 4 8 16 32 ... n2 """
n = int(input("Enter N th term : "))
num=1
for i in range(1,n+1):
        print(num,end=", ")
        num*=2
