import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('/Users/darthlourd/Documents/dash/Plotly-Dashboards-with-Dash/data/mpg.csv')


data = [go.Scatter(x = df['horsepower'],
                   y = df['mpg'],
                   text = df['name'],
                   mode = 'markers',
                   marker = dict(size = df['weight']/100, color = df['cylinders'], showscale=True)
 
        )]

layout = go.Layout(title = 'Bubbles Chart', hovermode='closest')
fig = go.Figure(data = data, layout = layout)
pyo.plot(fig)