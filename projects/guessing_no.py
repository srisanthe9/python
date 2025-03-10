#Number guessing game in Python 3 and C
import random
num=random.randint(1,20)
c=5
while c>0:
    print('Guess a number:',end='')
    key=int(input())
    if key==num:
        print('Congratulations! ')
        break
    if key>num:
        print('Try Again! You guessed too high')
    if key<num:
        print('Try Again! You guessed too small')
    if num>20 or num<1:
        print('Enter number between 1 and 20!')
    c=c-1
    if(c==0):
        print('Better Luck Next Time!')
    