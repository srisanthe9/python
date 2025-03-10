#Write a Python function to find the maximum of three numbers.
def maximum(x,y,z):
    a=max(x,y,z)
    return a
    
a=int(input('Enter fisrt no:'))
b=int(input('Enter second number:'))
c=int(input('Enter third number:'))
z=maximum(a,b,c)
print(z)
