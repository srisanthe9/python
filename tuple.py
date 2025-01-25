#tuple is ordered cannot be changed.duplicate entries are present
animals=(10,10,20,'tiger','lion','tiger')
print(animals[2])#prints 20
print(animals.count('tiger'))#prints 2
animals[2]='wolf'#error because tuple cannot be changed
print(animals)