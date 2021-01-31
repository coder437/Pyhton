import csv
with open("SOCR-weightWeight.csv",newline="") as f:
    f_read = csv.reader(f)
    data = list(f_read)
 height = []
for i in range(len(data)):
    n = data[i][1]
    height.append(float(n))

a = len(height)
total = 0
for i in height:
    total+=i
mean = total/a
print("mean : "+str(mean))
height.sort()
if a%2==0:
    m1  = float(height[a//2])
    m2 = float(height[a//2-1])
    median = (m1+m2)/2
else:
    median = height[a//2]
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


