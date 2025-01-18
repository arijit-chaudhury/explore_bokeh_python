from bokeh.plotting import figure
from bokeh.io import show, output_file
import pandas as pd

df = pd.read_csv("../../mpg.csv")

output_file("__init__.html")
fig = figure()
fig.line(df['horsepower'], df['model_year'])

show(fig)
