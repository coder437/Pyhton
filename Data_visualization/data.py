import pandas
import csv
import plotly.express as plotly
import statistics
data_frame = pandas.read_csv("data.csv")
data = statistics.mean(data_frame[1])
fig = plotly.scatter(mean, x="student_id", y="level", size="attempt", color="attempt")
fig.show()