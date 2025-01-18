from bokeh.plotting import figure
from bokeh.io import show, output_file
import pandas as pd

df = pd.read_csv("../../organizations-1000.csv")

output_file("__init__.html")
fig = figure()
fig.line(df['Founded'], df['Number of employees'])

show(fig)
