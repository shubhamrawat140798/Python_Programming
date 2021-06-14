''' Write a Python script to generate and print a dictionary with output
{1:1,2:4,3:9} that contain Number(Between 1 to n)in form of (x,x*x)'''
n = int(input(" Enter a n th : "))
d = dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)
