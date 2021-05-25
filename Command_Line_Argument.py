import sys  # Import library for to use Command Line argument passing
args0 =sys.argv[0]
args1 =sys.argv[1]
args2 =sys.argv[2]
for i in sys.argv:
    print(i)
print(args1," : ",args2," : ",args0)
print(len(sys.argv))
print(type(sys.argv))
