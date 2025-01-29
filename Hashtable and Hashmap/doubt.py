student_details = {
    'student': {
        'srisanth': {'height': '6', 'weight': '60', 'eye_color': 'black'},
        'ram': {'height': '5', 'weight': '50', 'eye_color': 'brown'}
    }
}

# Accessing and printing values for srisanth
srisanth_details = student_details['student']['srisanth']
print("Details for Srisanth:")
for x,y in srisanth_details.items():
    print(x,y)
