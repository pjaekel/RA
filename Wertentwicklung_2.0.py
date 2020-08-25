import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

import numpy.random as npr
import scipy.stats as scs
import pandas_datareader as data
import numpy as np
import scipy.optimize as sco
import matplotlib.pyplot as plt
from pandas.util.testing import assert_frame_equal
import warnings
from statistics import mean
import numpy.random as npr
import scipy.stats as scs

#Code
initial_value = 20000
log_return = 0.06367934
t = 30
sigma = 0.10540465
c_company = 0.003 #Kosten Tradvestgo
c_etf = 0.0019 #Tradingkosten
log_return_net = log_return - c_company - c_etf
alpha_95 = 1.64
alpha_50 = 0.00
alpha_05 = -1.64

final_value_95 = np.exp(np.log(initial_value) + t * log_return_net + (np.sqrt(t) * sigma * alpha_95))
print('Gute Entwicklung =', final_value_95)

final_value_50 = np.exp(np.log(initial_value) + t * log_return_net + (np.sqrt(t) * sigma * alpha_50))
print('Mittlere Entwicklung =', final_value_50)

final_value_05 = np.exp(np.log(initial_value) + t * log_return_net + (np.sqrt(t) * sigma * alpha_05))
print('Schlechte Entwicklung =', final_value_05)

gute = []
for t in range(31):
    gute.append(np.exp(np.log(initial_value) + t * log_return_net + (np.sqrt(t) * sigma * alpha_95)))

mittlere = []
for t in range(31):
    mittlere.append(np.exp(np.log(initial_value) + t * log_return_net + (np.sqrt(t) * sigma * alpha_50)))

schlechte = []
for t in range(31):
    schlechte.append(np.exp(np.log(initial_value) + t * log_return_net + (np.sqrt(t) * sigma * alpha_05)))

class dashboard(object):

    def _init_(self, initial_value, log_return, sigma, t, alpha_95, c_company, c_etf):
        self.initial_value = initial_value
        self.log_return = log_return
        self.sigma = sigma
        self.alpha_95 = alpha_95
        self.alpha_50 = alpha_50
        self.alpha_05 = alpha_05
        self.t = t
        self.c_company = c_company
        self.c_etf = c_etf

    def net_return(self):
        self.log_return = log_return
        self.c_company = c_company
        self.c_etf = c_etf

        return self.log_return - (self.c_company + c_etf)

    def good_development(self):
        net_return = self.net_return()
        self.initial_value = initial_value
        self.sigma = sigma
        self.alpha_95 = alpha_95
        good = []
        for t in range(31):
            good.append(np.exp(np.log(initial_value) + t * net_return + (np.sqrt(t) * sigma * alpha_95)))

        return good

    def middle_development(self):
        net_return = self.net_return()
        self.initial_value = initial_value
        self.sigma = sigma
        self.alpha_50 = alpha_50
        middle = []
        for t in range(31):
            middle.append(np.exp(np.log(initial_value) + t * net_return + (np.sqrt(t) * sigma * alpha_50)))

        return middle

    def bad_development(self):
        net_return = self.net_return()
        self.initial_value = initial_value
        self.sigma = sigma
        self.alpha_05 = alpha_05
        bad = []
        for t in range(31):
            bad.append(np.exp(np.log(initial_value) + t * net_return + (np.sqrt(t) * sigma * alpha_05)))

        return bad

#Dashboard
from bokeh.embed import file_html
from bokeh.resources import CDN
from bokeh.layouts import column, row
from bokeh.models import CustomJS, Slider
from bokeh.plotting import ColumnDataSource, figure, output_file, show
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Patch, Plot

x = range(0, t, 1)
y = schlechte
z = gute
q = mittlere

#damit wir den Wert sehen, wenn wir mit der Maus drber gehen
TOOLTIPS = [
    ("Year", "$index"),
    ("Value of Capital", "$y{€0.2f}")]

#Unsere Quellen
source = ColumnDataSource(data=dict(x=x, y=y, z=z, q=q))

#Der gesamte Plot
plot = figure(y_range=(initial_value*0.7, initial_value*2), x_range=(0, 5), plot_width=1000, plot_height=400,
              x_axis_label='Year', y_axis_label='Value of Capital'
              , toolbar_location=None
              , tooltips=TOOLTIPS)

#Hintergrundfarbe des Plots
plot.background_fill_color = '#122235'
plot.background_fill_alpha = 1

#Farbe neben dem Plot
plot.border_fill_color = "white"
plot.min_border_left = 80

#grüne Linie
plot.line('x', 'z', legend_label='Good Development', source=source,
          line_width=3, line_alpha=1, line_color='green')

#weiße Linie
plot.line('x', 'q', legend_label='Medium Development', source=source,
          line_width=3, line_alpha=1, line_color='white')

#rote Linie
plot.line('x', 'y', legend_label='Bad Development', source=source,
          line_width=3, line_alpha=1, line_color='red')

plot.xgrid.grid_line_color = None #damit wir keine vertikalen Linien haben
plot.ygrid.grid_line_alpha = 0.5 #für die horizontalen gestrichelten Linien
plot.ygrid.grid_line_dash = [6, 4]

#Slider
betrag = Slider(start=100000, end=1000000, value=1, step=10000, title="Anlagebetrag")
var = Slider(start=3, end=25, value=1, step=1, title="Anlagestrategie in %VaR")

#Legende
plot.legend.border_line_width = 1
plot.legend.border_line_color = "grey"
plot.legend.border_line_alpha = 0.5
plot.legend.label_text_color = "white"
plot.legend.background_fill_color = "#44898e"
plot.legend.location='top_left'

callback = CustomJS(args=dict(source=source, betrag=betrag, var=var),
                    code="""
    var data = source.data;
   var f = cb_obj.value
   var x = data['x']
   var y = data['y']
   var z = data['z']
   for (var i = 0; i < x.length; i++) {
      y[i] = Math.pow(x[i], f)
   }
   source.change.emit();
""")

betrag.js_on_change('value', callback)
var.js_on_change('value', callback)

layout = row(
    plot,
    column(betrag, var),
)

output_file("slider.html", title="ETF-Sparplan")

#html = file_html(layout, CDN, "ETF-Sparplan")

html = file_html(plot, CDN, "ETF-Sparplan")
print(html)

betrag.js_on_change('value', callback)

#show(layout)
show(plot)