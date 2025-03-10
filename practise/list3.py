"""Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings.
Input:
['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
Output:
True
Input:
['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
Output:False"""
l=[]
n=int(input('Enter no. of strings in list:'))
for i in range(n):
    a=input()
    l.append(a)
print(l[n-2] in l[n-1])