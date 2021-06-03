print("\n list Comprehension \n")
t1=(1,2,3,4)
print([i*3 for i in t1])

print("\n variable length argument \n")
def f1(*args):
    print(args)

t1=(1,2,3,4,5)
f1(t1)
