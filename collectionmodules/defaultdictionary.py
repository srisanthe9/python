#defaultdict is a dictionary subclass which calls a factory function to supply missing values.
from collections import defaultdict
d=defaultdict(float)
d[1]='monday'
d[2]='tuesday'
d[3]='wednesday'
print(d[4])#prints 0
#let's try to access an element from ordinary dic
a={1:'monday',2:'sunday'}
#print(a[3])#you will get a key error


