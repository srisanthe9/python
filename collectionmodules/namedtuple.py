#importing namedtuple
from collections import namedtuple
a=namedtuple('courses','name,technology')#here 'courses' is name of my tuple and 'name,technology 'are name of elements in my tuple  
s=a('datascience','python' )#datascience and python are elements in my tuple
print(s)