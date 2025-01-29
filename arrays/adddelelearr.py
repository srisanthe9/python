#adding elements to array using append(),extend(),insert()
import array as arr 
a=arr.array('d',[1.2,1.4,2.3])
a.append(5.2)
print(a)
a.extend([4.2,3.5,6.1])
print(a)
a.insert(0,1.1)#inserts 1.1 at index 0 in array a 
print(a)
#removing element in array using pop function
a.pop()#remove last element in array
print(a)
a.pop(0)#removes element of index 0
print(a)
a.remove(1.4)
print(a)