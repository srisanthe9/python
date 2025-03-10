## """Winning rules of the game ROCK PAPER SCISSORS are:
"""Rock vs Paper -> Paper wins 
Rock vs Scissors -> Rock wins 
Paper vs Scissors -> Scissors wins 

Enter your choice 
 1 - Rock 
 2 - Paper 
 3 - Scissors 

Enter your choice: 1
User choice is: Rock
Now it's Computer's Turn...
Computer choice is: Paper
Rock vs Paper
<== Computer wins! ==>
Do you want to play again? (Y/N)
y
Enter your choice 
 1 - Rock 
 2 - Paper 
 3 - Scissors 

Enter your choice: 2
User choice is: Paper
Now it's Computer's Turn...
Computer choice is: Paper
Paper vs Paper
<== It's a tie! ==>
Do you want to play again? (Y/N)
n
Thanks for playing!"""
print('Winning rules of the game ROCK PAPER SCISSORS are:')
print('Rock vs Paper -> Paper wins ')
print('Rock vs Scissors -> Rock wins')
print('Paper vs Scissors -> Scissors wins ')
print('Enter your choice ')
print(' 1 - Rock ')
print(' 2 - Paper ')
print(' 3 - Scissors ')
my_list=['Rock','Paper','Scissors']
count=0
while count<1:
    n=int(input('Enter your choice:'))
    if(n>3):
        print('Enter 1 or 2 or 3!!!')
    print('User choice is:',my_list[n-1])
    my_choice=my_list[n-1]
    import random
    num=random.randint(0,2)
    print("Now it's Computer's Turn...")
    print('Computer choice is:',my_list[num])
    com_choice=my_list[num]
    print(my_choice ,'vs', com_choice)
    if (my_choice == com_choice):
        print("<== It's a tie! ==>")
    if (my_choice=='Rock' and com_choice=='Paper'):
        print("<== Computer wins! ==>")
    if (my_choice=='Rock' and com_choice=='Scissors'):
        print("<== Congratulations you won! ==>")
    if (my_choice=='Paper' and com_choice=='Scissors'):
        print("<== Computer wins! ==>")
    if (my_choice=='Paper' and com_choice=='Rock'):
        print('<== Congratulations you won! ==>')
    if (my_choice=='Scissors' and com_choice=='Rock'):
        print("<== Computer wins! ==>")
    if (my_choice=='Scissors' and com_choice=='Paper'):
        print('<== Congratulations you won! ==>')
    playagain=input('Do you want to play again? (Y/N):')
    if (playagain=='y'):
       count=0
    if (playagain=='n'):
       print("Thanks for playing!")
       count=1
    if (playagain!='y' and playagain!='n'):
        count=1
        print("enter either y/n!!")

