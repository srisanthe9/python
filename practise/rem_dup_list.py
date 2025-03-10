#write a program to remove the duplicates from the list
l=[]
c=[]
b=[]
n=int(input('Enter no of elements in list:'))
for i  in range(n):
    a=int(input())
    l.append(a)
for i in l:
    if i not in c:
        c.append(i)
        b.append(i)
print(b)
