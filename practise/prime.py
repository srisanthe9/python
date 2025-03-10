#Write a Python unit test program to check if a given number is prime or not.
n=int(input())
c=0
for i in range(2,n):
    if(n%i==0):
        c=c+1
if(c>0):
    print(n,'not prime')
else:
    print(n,'is prime')