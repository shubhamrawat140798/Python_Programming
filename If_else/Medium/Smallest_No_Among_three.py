i = int(input("Enter first no."))
j = int(input("Enter second no."))
k = int(input("Enter thrid no."))

if(i<j):
	if(i<k):
		print(i," is smallest among ",i,",",j," and ",k)
	else:
		print(k," is smallest among ",i,",",j," and ",k)
else:
	if(j<k):
		print(j," is smallest among ",i,",",j," and ",k)
	else:
		print(k," is smallest among ",i,",",j," and ",k)