
my_list=[]
m=int(input('Enter no of rows in list:'))
n=int(input('Enter no of coloumns in list:'))
for i in range(m):
    a=[]
    for j in range(n):
        a.append(int(input()))
        my_list.append(a)
for i in range(m):
    for j in range(n):
        print(my_list[i][j],end=' ')
    print()