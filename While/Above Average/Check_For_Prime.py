n = int(input(" Enter a No. : "))
i=1
flag=0
while(i<n+1):
	if(n%i==0):
		flag+=1
	i+=1
if((flag==2) or (flag==1)):
	print(" Prime No. ")
else:
	print(" Not a Prime No. ")