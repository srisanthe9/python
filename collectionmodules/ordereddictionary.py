#OrderedDict is dictionary subclass which remembers the order in which the entries were done
from collections import OrderedDict
a=OrderedDict()
a[1]='s'
a[2]='r'
a[3]='i'
a[4]='s'
a[5]='a'
a[6]='n'
a[7]='t'
a[8]='h'
print(a)

print(a.keys())
print(a.get(3))
print(a.popitem())
print(a.clear)
print(a)