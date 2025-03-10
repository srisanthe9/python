import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
print(Style.BRIGHT + '                 Millions of songs.')
print(Style.BRIGHT + '                  Free on Spotify.')
print(Back.GREEN+Fore.BLACK+Style.BRIGHT+'sign up for free(1)')
print(Back.GREEN+Fore.BLACK+Style.BRIGHT+'Log in (2)')
print('enter 1 for sign up and 2 if u want to login')
user=input()
if user==1:
    print('Enter Username:')
    print('Password:')
    
if user==2:
    print('')
    
else:
    print('Thanks for visting Website')

