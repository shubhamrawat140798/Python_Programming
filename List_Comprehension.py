''' WAP to remove an empty tuples from a list of tuples'''
print("Using List Comprehension:")
tuples =[(),('ram','15','8'),(),('laxman','sita'),('krishna','akbar','45'),('',''),()]
print(tuples)
tuples =[t for t in tuples if t] # if t is ture means t hold value
print(tuples)

print("Using filter():")
tuples =[(),('ram','15','8'),(),('laxman','sita'),('krishna','akbar','45'),('',''),()]
print(tuples)
tuples= list(filter(None,tuples))
print(tuples)
