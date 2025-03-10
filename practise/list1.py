#Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
"""Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:Puzzle booksScripting language courses
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:true"""
my_list=[]
c1=0
c2=0
n=int(input('Enter no of elements in list:'))
print('Enter elements in list:')
for i in range(n):
    a=int(input())
    my_list.append(a)
print(my_list)
for i in range(n):
    if(my_list[i]==19):
        c1=c1+1
    if(my_list[i]==5):
        c2=c2+1
if(c1==2 and c2>=3):
    print('True')
else:
    print('False')
    