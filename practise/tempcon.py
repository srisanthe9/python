'''Write a Python  program to convert temperatures 
to and from Celsius and Fahrenheit.
[ Formula : c/5 = f-32/9 
[ where c = temperature in celsius and 
f = temperature in Fahrenheit ]
input=60
45
output=60°C is 140°F in Fahrenheit
45°F is 7°C in Celsius
'''
c=int(input())
f=int(input())
fc=5*(f-32)//9
cf=9*c//5+32
print(c,'°C is ',cf,'°F in Fahrenheit')
print(f,'°F is ',fc,'°C in Celsius')