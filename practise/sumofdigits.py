#printing sum of digits
n=int(input('Enter number:'))
sum=0
import array as arr
a=arr.array('i')
c=0
while(n>0):
    rem=n%10
    a.append(rem)
    sum=sum+rem
    c=c+1
    n=n//10
print('sum: ',end='')
for i in reversed(range(c)):
    if (i==0):
        print(a[i],'=',sum,end='')
        break
    print(a[i],'+',end='')
        