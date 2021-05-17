n = int(input(" Enter a No. : "))
temp=n
rev=0
while(n>0):
	dig=n%10
	rev=rev*10 + dig
	n=n//10

print(rev,temp)	
if(rev==temp):
	print(temp, " is Palindrome ")
else:
	print(temp," is not Palindrome")