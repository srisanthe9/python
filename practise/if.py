#Write a Python program that accepts an integer and determines whether it is greater than 4^4 and which is 4 mod 34.
n=int(input('Enter no:'))
a=n%34
if(n>256 and a==4):
    print('True')
else:
    print('False')