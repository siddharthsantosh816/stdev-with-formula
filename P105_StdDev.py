import csv
import pandas as pd
import plotly.express as px
import math

with open('C:/Users/w/Desktop/Python/csv/P105.csv') as f:
    reader=csv.reader(f)
    print(reader)
    data=list(reader)
    print(data)
    d_list=data[0]

print(d_list)
# MEAN
sum=0

for i in range(0,len(d_list)):
    print(d_list[i])
    sum=sum+float(d_list[i])
mean=sum/len(d_list)
#print(mean)
sum_sq=0

# Sum of the Squares of Mean Difference and its Mean

for k in range(0,len(d_list)):
    sum_sq=sum_sq+((float(d_list[k]))-mean)**2

mean_sq=sum_sq/len(d_list)
print(mean_sq)

# DEVIATION
deviation=math.sqrt(mean_sq)
print("Standard Deviation is : " + str(deviation))
