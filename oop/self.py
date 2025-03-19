#self refers to the instance of the class.It is automatically passed with a function call from an object
class student:
    name='srisanth'
    age=18
    def fun(self):
        print(f'Hi this is {self.name}.I am {self.age} ears old.')
s1=student()
s1.fun()   
# student.fun() takes 0 positional arguments but 1 was given
# u get this error because python assumes
# s1.fun() as student.fun(s1)

    