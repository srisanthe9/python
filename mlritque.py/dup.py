#remove duplicate words

a=input("Enter text:").split()
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print(i,end=' ')