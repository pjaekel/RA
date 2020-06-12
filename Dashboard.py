import plotly.plotly as py
from plotly.graph_objs import *
from plotly.graph_objs.scatter.marker import Line
py.sign_in('pjaekel', 'YhmumTX1TzwV3saekZoC')
trace1 = {
  "fill": "tonexty",
  "line": {
    "color": "rgba(255, 153, 51, 1.0)",
    "width": [0,inf]
  },
  "mode": "lines",
  "name": "a",
  "type": "scatter",
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  "y": [0.17048910089864067, 0.05390702725063046, 0.7560889217240573, 0.7393313216390578, 0.7562979443674754, 0.983908108492343, 0.4552096139092071, 0.751939393026647, 0.42441695150031034, 0.6119820237450841],
  "fillcolor": "rgba(255, 153, 51, 0.3)"
}
trace2 = {
  "fill": "tonexty",
  "line": {
    "color": "rgba(55, 128, 191, 1.0)",
    "width": [0,3]
  },
  "mode": "lines",
  "name": "b",
  "type": "scatter",
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  "y": [1.0921498980687505, 0.628379692444796, 1.6804387333467445, 1.1741874271317159, 1.7098535938519392, 1.0165440369832146, 0.8201578488720772, 1.019179653143562, 0.5391840333768539, 0.9023036941696878],
  "fillcolor": "rgba(55, 128, 191, 0.3)"
}
trace3 = {
  "fill": "tonexty",
  "line": {
    "color": "rgba(50, 171, 96, 1.0)",
    "width": [0,3]
  },
  "mode": "lines",
  "name": "c",
  "type": "scatter",
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  "y": [1.5084498776097979, 1.0993096327196032, 2.5468884763826125, 1.3139261978658, 1.7288516603693358, 1.3500413551768342, 1.4111774146124456, 1.1245312639069405, 1.4068617318281056, 0.9236499701488171],
  "fillcolor": "rgba(50, 171, 96, 0.3)"
}
trace4 = {
  "fill": "tonexty",
  "line": {
    "color": "rgba(128, 0, 128, 1.0)",
    "width": [0, 3]
  },
  "mode": "lines",
  "name": "d",
  "type": "scatter",
  "x": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  "y": [1.912915766078795, 1.6450103381519354, 3.523866933241722, 1.656799203492564, 2.666064160881149, 2.2985767814076814, 1.6491300653173326, 1.2880873970749964, 2.192375146193222, 1.6271909616796654],
  "fillcolor": "rgba(128, 0, 128, 0.3)"
}
data = Data([trace1, trace2, trace3, trace4])
layout = {
  "legend": {
    "font": {"color": "#4D5663"},
    "bgcolor": "#F5F6F9"
  },
  "xaxis1": {
    "title": "",
    "tickfont": {"color": "#4D5663"},
    "gridcolor": "#E1E5ED",
    "titlefont": {"color": "#4D5663"},
    "zerolinecolor": "#E1E5ED"
  },
  "yaxis1": {
    "title": "",
    "tickfont": {"color": "#4D5663"},
    "zeroline": False,
    "gridcolor": "#E1E5ED",
    "titlefont": {"color": "#4D5663"},
    "zerolinecolor": "#E1E5ED"
  },
  "plot_bgcolor": "#F5F6F9",
  "paper_bgcolor": "#F5F6F9"
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)