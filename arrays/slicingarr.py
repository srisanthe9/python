##slicing an array
#an array can be sliced using the : symbol.This returns a range of elements that we have specified by the index numbers.
import array as arr 
a=arr.array('d',[1.2,1.3,2.1,2.3])
print(a[0:3])#prints 1.2, 1.3,2.1
print(a[::-1])
print(a)