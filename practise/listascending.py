#Write a Python unit test program to check if a list is sorted in ascending order.
a=[]
n=int(input('Enter no of elements in list:'))
print('Enter Elements in list:')
for x in range(n):
    l=int(input())
    a.append(l)
print(a[0])
for i in range(n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            k=a[i]
            a[i]=a[j]
            a[j]=k
print(a)
    