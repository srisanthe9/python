""" 5
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 

    """
n=int(input())
for i in range(1,n+1):
    for j in reversed(range(1,n-i+2)):
        print(j,end=' ')
    print()
        