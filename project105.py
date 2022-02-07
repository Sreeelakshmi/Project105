import math
import csv
with open("C:/Users/dell/Desktop/Python/folderA/txt/data(pro 105).csv")as f:
    reader=csv.reader(f)
    fileData=list(reader)
data=fileData[0]
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean
squaredList=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squaredList.append(a)
sum=0
for i in squaredList:
    sum=sum+i
result=sum/(len(data)-1)
standardDeviation=math.sqrt(result)
print(standardDeviation)
