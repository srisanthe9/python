#Unordered,can be changed.No duplicate entries are present
course={1:'ram',2:'srisanth','third':"machine"}
print(course)
print(course[1])#prints ram
print(course.get(2))#prints srisanth
course[1]='abhi'#updating key
print(course[1])#prints abhi
print(course['third'])#prints machine
course={1:'ram',2:'srisanth','third':"machine",1:'raj'}
print(course)#