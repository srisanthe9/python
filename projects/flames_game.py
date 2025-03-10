#creating a flames game using py
a=''
x=(a.center(20))
print(x,'Welcome to flames game')
name1=input('Enter name of person1:')
name2=input('Enter name of person2:')
l=[]
c=0
for char1 in name1:
    for char2 in name2:
        if char1 is char2:
            if char1 not in l:
                l.append(char1)
                c+=1
c1=len(name1)
c2=len(name2)
n=c1+c2-c-1
temp=n
s='flames'
l1=6
while l1>=2:
    n=n%l1
    s=s.replace(s[n],'')
    l1-=1
    n=temp
print('Relationship status:',end='')
if s[0]=='f':
    print('friendship')
elif s[0]=='l':
    print('love')
elif s[0]=='a':
    print('affection')
elif s[0]=='m':
    print('marraige')
elif s[0]=='e':
    print('enemies')
else:
    print('siblings')