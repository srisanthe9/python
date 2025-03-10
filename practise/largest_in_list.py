#find the largest number in list
l=[]
n=int(input('Enter no of elements in list:'))
for i  in range(n):
    a=int(input())
    l.append(a)
max=l[i]
for i in range(n):
    if max<l[i]:
        max=l[i]
print('largest number from list is:',max)
        
        