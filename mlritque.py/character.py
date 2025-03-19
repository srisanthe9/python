str=input('Enter string:')
str=str.lower()
vowels=['a','e','i','o','u']
v=0
d=0
c=0
s=0
for i in str:
    if i in vowels:
        v+=1
    char=ord(i)
    if char in range(48,58):
         d+=1
    elif char in range(97,123):
        c+=1
    else:
        s+=1
c=c-v
print('vowels:',v)
print('digits:',d)
print('consonants:',c)
print('special character:',s)