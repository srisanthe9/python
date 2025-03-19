#instance attributes,take prefrence over class attributes during assignment and retrival
class student:
    name='srisanth'#this is a class attribute
    age=18
obj=student()
obj.name='srividyan'#this is a instance attribute
print(obj.name)