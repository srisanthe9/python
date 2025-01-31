#Membership operators are used to check if a sequence is present in an object
#in and not in
#'in' returns true if a sequence with the specified value is present in the object
#'not in' returns true if a sequence with the specified value is not present in the object
a=[10,20,30]
b=[10,20,30]
print(10 in a)#prints true
print(10 not in a)#prints false
print(a in b)#prints false
print([10,20,30] in a)#prints false
print(20,10 in a)