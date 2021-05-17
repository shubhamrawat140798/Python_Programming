n = int(input(" Enter Nth term : "))
i=1
sum=0
while(i<n+1):
	if(i%2!=0):
		sum+=i
	i+=1
print("Sum of odd Numbers : ",sum)