# identity operators are used to compare objects
# 'IS' and 'ISNOT'
#is returns true if the variables are same object
a=[10,20,30]
b=[10,20,30]
print(a is b)#prints false because objects are different
c=a
print(c is a)#prints true
#is not returns true if both variables are not same object
print(a is not b)#prints true