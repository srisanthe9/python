a=input('Enter string1:')
b=input('Enter string2:')
l=len(a)
c=0
for i in a:
    if i in b:
        c+=1
if c==l:
    print("anagram")
else:
    print('not anagram')