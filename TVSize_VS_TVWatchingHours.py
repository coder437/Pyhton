import csv 
import numpy
import plotly.express as plotly

def open_file(data):
    column1 = []
    column2 = []
    with open(data) as file:
        csv_reader = csv.DictReader(file)
        #chart = plotly.scatter(csv_reader, x = "SizeofTV", y = "Averagetime",color="SizeofTV")
        #chart.show()
        for row in csv_reader:
            column1.append(float(row["SizeofTV"]))
            column2.append(float(row["Averagetime"]))
    return {"x":column1,"y":column2}

def find_Correlation(data):
    correlation = numpy.corrcoef(data["x"],data["y"])
    print(correlation[0,1])

def main():
    path = "TVSize_VS_TVWatchingHours.csv"
    data_source = open_file(path)
    find_Correlation(data_source)



main()