my_list=[]
def sumoflist(numbers):
    t=0
    for i in numbers:
        t+=i
    print('sum of elements in list:',t)
    
n=int(input('Enter no of elements in list:'))
for i in range(n):
    a=int(input())
    my_list.append(a)
sumoflist(my_list)
