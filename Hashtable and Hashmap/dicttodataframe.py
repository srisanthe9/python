#converting a dictionary into a pandas dataframe
student_details={'student':{'srisanth':{'height':'6','weight':'60','eye_color':'black'},'ram':{'height':'5','weight':'50','eye_color':'brown'}}}
import  pandas as pd 
#if pandas module is not present the run >>pip install pandas
b=pd.DataFrame(student_details['student'])
print(b)

