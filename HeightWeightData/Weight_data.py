import csv
with open("SOCR-HeightWeight.csv",newline="") as f:
    f_read = csv.reader(f)
    data = list(f_read)
"""print(data)
from collections import Counter
d = "Abhishek Singh"
r = Counter(d)
print(r)
n = r.items()
print(n)
v = r.values()
print(v)"""
data.pop(0)
#sorting data to fetch only weight
weight = []
for i in range(len(data)):
    n = data[i][2]
    weight.append(float(n))

a = len(weight)
total = 0
for i in weight:
    total+=i
mean = total/a
print("mean : "+str(mean))
weight.sort()
if a%2==0:
    #ceiling means to get get nearest larger whole number while roundin off
    #floor means to get nearest smaller whole number while rounding off
    m1  = float(weight[a//2])
    m2 = float(weight[a//2-1])
    median = (m1+m2)/2
else:
    median = weight[a//2]
print("median: "+str(median))

from collections import Counter
b = Counter(weight)
data_range = {
    "50-60":0,"60-70":0,"70-80":0
    }
for h,o in b.items():
    if 50 < float(h)<60:
        data_range["50-60"]+=o
    elif 60<float(h)<70:
        data_range["60-70"]+=o
    elif 70<float(h)<80:
        data_range["70-80"]+=o
mr,mo = 0,0
for r,occ in data_range.items():
    if occ>mo:
        mr,mo = [int(r.split("-")[0]),int(r.split("-")[1])],occ
mode = float((mr[0]+mr[1])/2)
print("mode: "+str(mode))


