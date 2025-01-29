#counter is a dictionary subclass for counting hashable objects..
from collections import Counter
a=[1,1,2,3,4,2,3,5,4,6,4,5]
b=Counter(a)
print(b)#prints a dictionary the no of times a element present in a list
print(list(b.elements()))#prints all elements in my list in ascending order
print(b.most_common())
sub={4:2,2:1}
print(b.subtract(sub))
print(b.most_common())