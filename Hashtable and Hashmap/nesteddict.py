#nested dictionaries are basically dictionaries that lie within other dictionaries
students={'srisanth':{'height':'6','weight':{60},'eye_color':'black'},'ram':{'height':'5','weight':{50},'eye_color':'brown'}}
print(students.get('ram'))
print(students.keys())
print(students['ram'])
print(students.values())
for x in students.values():
    print(x)
    for x,y in students.items():
        print(x,y)#prints both keys and values 
    
        