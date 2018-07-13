
import seaborn as sns
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.offline as offline
import plotly.graph_objs as go
init_notebook_mode(connected=True)
from plotly.graph_objs import *


trace1 = go.Bar(
    x=REVENUE_WIND_CORR['PERIOD'],
    y=REVENUE_WIND_CORR['EST_REVENUE_CHANGE'],
    name='Est Rev Change'

)
trace2 = go.Scatter(
    x=REVENUE_WIND_CORR['PERIOD'],
    y=REVENUE_WIND_CORR['BASE_WIND_MW'],
    name='Wind MW',
    yaxis='y2'
)

data = [trace1, trace2]

layout = go.Layout(
    title='Estimated Revenue Change versus Wind MW',
    yaxis=dict(
        title='Est Revenue Change $'
    ),
    yaxis2=dict(
        title='Wind MW',
        overlaying='y',
        side='right'
    )
)
fig = go.Figure(data=data, layout=layout)
offline.iplot(fig, filename='bar-line')