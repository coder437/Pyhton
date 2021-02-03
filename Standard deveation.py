"""standard deviation is a measure of how spread out a data set is. without calculating
this we cannot understand whether the data is close to average or spread out over a wide
range
STEPS:
1- calculate mean of numbers
2- subtract mean from every number
3- square every  number (diffrence)
4- add results(sum of all squares) 
5- divide sum of square by the total (number of data values - 1 )
6- take square root to get final result
EXAMPLE:
RNO,Marks
1,12  8  4   16
2,3   8  -5  25
3,9   8   1  1
16+25+1 = 42
42/2
21 sqrt=4.58
"""
import csv
import math
import statistics
with open("class1.csv",newline="") as file:
    r = csv.reader(file) 
    data1 = list(r)


data = data1[0]

#l = le
#sum = 
#for i in data:
#   sum+=float(i[1])
#mean = sum/l
#print("mean: "+str(mean))
subsq = []
for n in data:
    a = int(n[1])-statistics.mean(data)
    a = a**2
    subsq.append(a)
sum = 0
for i in subsq:
    sum=sum+i
result = sum/(len(data)-1)
sd = math.sqrt(result)
print(sd)
    
