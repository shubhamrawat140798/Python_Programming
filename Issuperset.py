"""
Write a Python program to check if a given set is superset of itself and superset of another given set. 
"""

Set1= set([1,2,3,4,5])
Set2= set([1,4,2])
print(" Original : ",Set1)
print(" Set is super set of itself: ",Set1.issuperset(Set1))
print("\n Set1:\n",Set1," \n is Super set of Set2:\n",Set2,"\n= ",Set1>Set2)
