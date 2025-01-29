#chainmap is a dictionary like class for creting a single view of multiple mappings
#suppose we have two dictonaries chainmap creates a single list from these two lists
a={1:'srisanth',2:'ram','dad':'sridhar'}
b={'mom':'narmada','bro':'vaishu'}
from collections import ChainMap
c=ChainMap(a,b)
print(c)