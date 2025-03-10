#Write a Python function to multiply all the numbers in a list
my_list=[]
def mul(numbers):
    t=1
    for i in numbers:
        t*=i
    print('Multiplying all numbers in a list:',t)

        
    
n=int(input('Enter no of elements in list:'))
for i in range(n):
    a=int(input())
    my_list.append(a)
mul(my_list)
