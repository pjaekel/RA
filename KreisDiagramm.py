import numpy as np
from bokeh.plotting import figure
from bokeh.io import show, output_file
from bokeh.models import HoverTool, ColumnDataSource
from math import pi
from bokeh.embed import file_html
from bokeh.resources import CDN

percents = [0, 13.5/100, 16.5/100, 39.4/100, 49.5/100, 59.9/100, 62.9/100, 65.9/100, 68.9/100, 97/100, 3/100, 1]
category = ['EXHA',	'EL49',	'Gold', 'ELFC', 'EXI5', 'EXW1', 'EXX7',	'EXS1', 'EXXT', 'EXV6']
counts = [13.5, 3, 23.4, 10, 10, 3, 3, 3, 28.1, 3]
starts = [1/2*pi-(p*2*pi) for p in percents[:-1]]
ends = [1/2*pi-(p*2*pi) for p in percents[1:]]
colors = ['#889dba', '#1f356f', '#1e92b8', '#33748a', '#a5d3e3', '#bbc2d4', 'lightcyan', 'midnightblue', 'darkyellow', 'goldenrot']
# create source
source = ColumnDataSource(
    data=dict(
        x=[0 for x in percents],
        y=[0 for x in percents],
        radius = [0.5 for x in percents],
        percents=percents,
        category= category,
        starts=starts,
        colors=colors,
        ends=ends,
        counts = counts
    )
)

TOOLS = "hover"

p = figure(plot_width = 500, plot_height = 500, x_axis_label = None, y_axis_label = None,
title = 'Portfolio Distribution', tools = TOOLS)

p.title.align = 'center'
p.title.text_font = 'arial narrow'

p.wedge(x='x', y='y',  radius = 'radius', direction="clock", legend_field='category',
                start_angle='starts', end_angle='ends', color='colors', source=source)

hover = p.select(dict(type=HoverTool))
hover.tooltips = [
    ('category', '@category'),
    ('percents','@counts %')
]

p.axis.visible = False
p.ygrid.visible = False
p.xgrid.visible = False

output_file('pie.html')
show(p)

html = file_html(p, CDN, "Kreisdiagramm")
print(html)