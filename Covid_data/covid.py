import pandas
import plotly.express as px
b = pandas.read_csv("CovidData.csv")
a = px.scatter(b,x = "date", y = "cases",color = "country",title = "Covid Cases")
a.show()
