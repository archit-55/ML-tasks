
Q.  data_visualization: 1

visualize data graphs  
i)  take input from  a file where you have 4 rows and 5 columns
ii)  columns having - student_name , marks , age , contact , study_hours
iii)  visualize this data as pie chart
iv)  file name must  student.csv with all column separated by ','






#!/usr/bin/python3


import pandas as pd
import matplotlib.pyplot as plt

#  entering data in file(dictionary)

data={"Student_Name":["Archit","MSD","Jack","Kane"],"Marks":[89,99,67,79],
      "Age":[21,37,25,16],"Contact":[7611425575,7777777777,4563214569,7852365894],"Study_hours":[5,8,10,2]}
print(data)

exp=[0.1,0.1,0,0]


#   columns
student=pd.DataFrame(data,columns=["Student_Name","Marks","Age","Contact","Study_hours"])
print(student)

#  creating pie graph
plt.pie(student["Marks"],labels=student["Student_Name"],explode=exp,shadow="True",autopct="%1.1f%%")
plt.legend()
plt.show()

