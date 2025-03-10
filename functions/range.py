#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument
def test_range(x):
    if x in range(1,7):
        print("ture")
    else:
        print('false')
    
n=int(input('Enter number:'))
test_range(n)