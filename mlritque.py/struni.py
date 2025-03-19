a=input('Enter string:')
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(len(b))
for i in b:
    print(i,end='')
