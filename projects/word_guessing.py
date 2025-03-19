"""What is your name? Gautam
Good Luck!  Gautam
Guess the characters
_
_
_
_
_
guess a character:g
g
_
_
_
_
guess a character:e
g
e
e
_
_
guess a character:k
g
e
e
k
_
guess a character:s
g
e
e
k
s
You Win
The word is:  geeks """
a=''
x=(a.center(20))
print(x,'welcome to word guessing game')
name=input('What is your name? ')
print('Good Luck!',name)
my_words=['srisnth','sridhar','narmada','srividyan','vaishvik','dikshan']
#one method for importing a random word
import random
# num=random.randint(0,len(my_words)-1)
# word=my_words[num]
word=random.choice(my_words)
print("Guess the characters in word")
l1=len(word)
word1=word
for i in word1:
    word1=word1.replace(i,'_')
for i in word1:
    print(i)
guess=input('Guess the character:')
l2=len(guess)
for i in range(l1):
    for j in range(l2):
        
        if word[i] == guess[j]:
            word1[i]=word[i]
print(word1)
        



# guess=input('') 
# for char in word:
#     if char in guess:
#         word.replace(char,guess)
# print(word)



