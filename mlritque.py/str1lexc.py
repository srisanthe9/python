n=input('Enter string:')
f=n[0]
l=n[-1]
n=l+n[1:-1]+f
print(n)
# l=list(n)
# temp=l[0]
# l[0]=l[-1]
# l[-1]=temp
# for i in l:
#     print(i,end='')