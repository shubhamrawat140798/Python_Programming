""" Write a short PYTHON program to check weather the square root of number is prime or not. """
import math
n = int(input(" Enter No. : "))
a = int(math.sqrt(n))
count = 0

for i in range(2,a):
    if (a % i == 0):
        count = count + 1
if (count == 0):
    print(a, "is a prime No.")
else:
    print(a, "is  not a prime No.")
    
    
