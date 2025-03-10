#Write a Python program that accepts list and return true if the fifth element occurs thrice in the said list.
"""Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
False
Input:
[11, 12, 14, 13, 14, 13, 15, 14]
Output:
True
Input:
[19, 15, 11, 7, 5, 6, 2]
Output:
False"""
l=[]
c=0
n=int(input('Enter no of elements in list:'))
print('Enter elements:')
for i in range(n):
    a=int(input())
    l.append(a)
for i in range(n):
    if(l[i]==l[4]):
        c=c+1
if(c==3):
    print('True')
else:
    print('False')