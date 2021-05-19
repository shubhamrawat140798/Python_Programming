""" PYTHON program to print odd numbers up to n """
n = int(input("Enter N th term : "))
for i in range(1,n+1):
    if(i%2!=0):
        print(i,end=", ")
