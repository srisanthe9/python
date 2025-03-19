a=input('Enter string:')
l=len(a)
i=0
j=l-1
while(i<j):
    if a[i]==a[j]:
        i+=1
        j-=1
    else:
        break
if i==l//2:
    print('palindrome')
else:
    print('not palindrome')