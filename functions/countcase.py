#Write a Python function that accepts a string and counts the number of upper and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12
def string(x):
    c1=0
    c2=0
    for i in x:
        convert=ord(i)
        if convert in range(65,91):
            c1+=1
        if convert in range(96,123):
            c2+=1
    print('No. of Upper case characters :',c1)
    print('No. of Lower case Characters :',c2)
            
    
    
n=input('Enter string:')
string(n)