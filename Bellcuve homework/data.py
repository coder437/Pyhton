import pandas
import plotly.figure_factory as plotly
import csv

file = pandas.read_csv("data.csv")
result = plotly.create_distplot([file["AvgRating"].tolist()],["AvgRating"],show_hist=False)
result.show()
