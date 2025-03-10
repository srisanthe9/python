# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
#Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself
def prime(x):
    c1=0
    c2=0
    if x == 1:
        print(f'{x} is neither prime nor composite')
    else:
        for i in range(2,x):
            if x%i==0:
                c1+=1
            else:
                c2+=1
        if c1>0:
            print(f'{x} is not a prime')
        if c2==x-2:
            print(f'{x} is prime')
        
        
n=int(input('Enter number:'))
prime(n)