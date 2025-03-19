a=input('Enter string:')
l=len(a)
c=0
for i in a:
    if a.count(i)>1:
        break
    else:
        c+=1
if c==l:
    print('Heterogram')
else:
    print('Not a Heterogram')