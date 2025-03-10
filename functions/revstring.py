# Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"
def rev(x):
    l=len(x)
    l=l-1
    print('reverse of string is:',end=' ')
    while l>=0:
        print(x[l],end='')
        l-=1  
    
n=input('input:')
rev(n)