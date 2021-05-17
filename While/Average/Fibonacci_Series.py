n = int(input(" Enter Nth term : "))
x=0
y=1
i=0
if(n<=0):
	print(" Provide No Greater than zero")
elif(n==1):
	print("This Fibonacci sequence has {} elements".format(n),":")
	print(x)
else:
	print("This Fibonacci sequence has {} elements".format(n),":")
	while(i<n):
		print(x,end=', ')
		z=x+y
		x=y
		y=z
		i+=1