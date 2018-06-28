# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 11:22:14 2018

@author: mcboe72
"""

#Note: THIS CODE WILL NOT WORK - IT IS JUST SUPPOSED TO SERVE AS A TEMPLATE
#YOU WILL NEED TO IMPORT OR CONNECT TO A DATA SOURCE AND SET THE WORKING DIRECTORY
#USET THIS TEMPLATE FOR A COLOR CODED MAP BASED OFF YOUR CHOSEN DATA


#Import packages, including, pandas and use pd.read_csv to import data

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.offline as offline
import plotly.graph_objs as go
init_notebook_mode(connected=True)
from plotly.graph_objs import *
import cufflinks as cf
import math as math

#Activate mapbox access token
#NOTE - YOU WILL NEED TO GET A TOKEN FROM MAPBOX AND PUT IT BETWEEN THE QUOTES

mapbox_access_token = ''

#Create individual datasets for each color or category

MAY22_0 = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['EST_REVENUE_CHANGE']<(-8957)]
MAY22_1 = ENERGY_REVENUE_CHANGES_MAY22[(ENERGY_REVENUE_CHANGES_MAY22['EST_REVENUE_CHANGE']<(-2420)) & (ENERGY_REVENUE_CHANGES_MAY22['EST_REVENUE_CHANGE']>(-8957))]
MAY22_2 = ENERGY_REVENUE_CHANGES_MAY22[(ENERGY_REVENUE_CHANGES_MAY22['EST_REVENUE_CHANGE']<(0)) & (ENERGY_REVENUE_CHANGES_MAY22['EST_REVENUE_CHANGE']>(-2420))]
MAY22_3 = ENERGY_REVENUE_CHANGES_MAY22[(ENERGY_REVENUE_CHANGES_MAY22['EST_REVENUE_CHANGE']==0)]
MAY22_4 = ENERGY_REVENUE_CHANGES_MAY22[(ENERGY_REVENUE_CHANGES_MAY22['EST_REVENUE_CHANGE']<(1888)) & (ENERGY_REVENUE_CHANGES_MAY22['EST_REVENUE_CHANGE']>(0))]
MAY22_5 = ENERGY_REVENUE_CHANGES_MAY22[(ENERGY_REVENUE_CHANGES_MAY22['EST_REVENUE_CHANGE']<(8696)) & (ENERGY_REVENUE_CHANGES_MAY22['EST_REVENUE_CHANGE']>(1888))]
MAY22_6 = ENERGY_REVENUE_CHANGES_MAY22[(ENERGY_REVENUE_CHANGES_MAY22['EST_REVENUE_CHANGE']<(17461)) & (ENERGY_REVENUE_CHANGES_MAY22['EST_REVENUE_CHANGE']>(8696))]
MAY22_7 = ENERGY_REVENUE_CHANGES_MAY22[(ENERGY_REVENUE_CHANGES_MAY22['EST_REVENUE_CHANGE']>(17461))]

#The index has to be set to whatever column you search on to create the traces below

MAY22_0.set_index('RESOURCE_NAME', inplace=True)
MAY22_1.set_index('RESOURCE_NAME', inplace=True)
MAY22_2.set_index('RESOURCE_NAME', inplace=True)
MAY22_3.set_index('RESOURCE_NAME', inplace=True)
MAY22_4.set_index('RESOURCE_NAME', inplace=True)
MAY22_5.set_index('RESOURCE_NAME', inplace=True)
MAY22_6.set_index('RESOURCE_NAME', inplace=True)
MAY22_7.set_index('RESOURCE_NAME', inplace=True)



REVENUE_DATA_MAY22 = []

for UNIT in list(MAY22_0.index):
    trace=(dict(
        lat = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LATITUDE'],
        lon = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LONGITUDE'],
        name = UNIT,
        marker = dict(size = 10, 
        color = 'rgba(144, 19, 19, 1)',
        ),
        type = 'scattermapbox'
         ))
    REVENUE_DATA_MAY22.append(trace)

for UNIT in list(ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME']):
    if UNIT in list(MAY22_1.index):
        trace = dict(
        lat = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LATITUDE'],
        lon = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LONGITUDE'],
        name = UNIT,
        marker = dict(size = 10, 
        color = 'rgba(208, 22, 22, 1)'
        ),
        type = 'scattermapbox'
         )
        REVENUE_DATA_MAY22.append(trace)   

    elif UNIT in list(MAY22_2.index):
        trace = dict(
        lat = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LATITUDE'],
        lon = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LONGITUDE'],
        name = UNIT,
        marker = dict(size = 10, 
        color = 'rgba(242, 166, 166, 1)'
        ),
        type = 'scattermapbox'
         )
        REVENUE_DATA_MAY22.append(trace)   
    
    elif UNIT in list(MAY22_3.index):
        trace = dict(
        lat = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LATITUDE'],
        lon = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LONGITUDE'],
        name = UNIT,
        marker = dict(size = 10, 
        color = 'rgba(247, 247, 247, 1)'
        ),
        type = 'scattermapbox'
         )
        REVENUE_DATA_MAY22.append(trace)   
        
    elif UNIT in list(MAY22_4.index):
        trace = dict(
        lat = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LATITUDE'],
        lon = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LONGITUDE'],
        name = UNIT,
        marker = dict(size = 10, 
        color = 'rgba(136, 205, 236, 1)'
        ),
        type = 'scattermapbox'
         )
        REVENUE_DATA_MAY22.append(trace)   

    elif UNIT in list(MAY22_5.index):
        trace = dict(
        lat = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LATITUDE'],
        lon = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LONGITUDE'],
        name = UNIT,
        marker = dict(size = 10, 
        color = 'rgba(60, 125, 215, 1)'
        ),
        type = 'scattermapbox'
         )
        REVENUE_DATA_MAY22.append(trace)   
    
    elif UNIT in list(MAY22_6.index):
        trace = dict(
        lat = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LATITUDE'],
        lon = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LONGITUDE'],
        name = UNIT,
        marker = dict(size = 10, 
        color = 'rgba(42, 69, 203, 1)'
        ),
        type = 'scattermapbox'
         )
        REVENUE_DATA_MAY22.append(trace)   
        
            
    elif UNIT in list(MAY22_7.index):
        trace = dict(
        lat = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LATITUDE'],
        lon = ENERGY_REVENUE_CHANGES_MAY22[ENERGY_REVENUE_CHANGES_MAY22['RESOURCE_NAME'] == UNIT]['LONGITUDE'],
        name = UNIT,
        marker = dict(size = 10, 
        color = 'rgba(49, 35, 128, 1)'
        ),
        type = 'scattermapbox'
         )
        REVENUE_DATA_MAY22.append(trace)   
    

len(REVENUE_DATA_MAY22)

#Define the layout

layout_revenue = dict(
    height = 800,
    hovermode='closest',
    hoverlabel = dict(bgcolor='#000000'),
    showlegend=False,
    margin = dict( t=0, b=0, l=0, r=0 ),
    font = dict( color='#FFFFFF', size=11 ),
    paper_bgcolor = '#000000',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=38,
            lon=-98
        ),
        pitch=0,
        zoom=4,
        style='dark'
    ),
)


annotations_revenue_MAY22 = list([
    dict(text='OGE NDVER Wind RT Price Chasing Impact on Resource Node Revenue May 22 2016', font=dict(color='White',size=18), borderpad=10, 
         x=0.50, y=0.99, yref='paper', align='left', showarrow=False, bgcolor='gray'),
    dict(text='LEGEND: <br> <br> REDS: Behavior Depressed Revenue <br> <br> BLUES: Behavior Inflated Revenue', 
         font=dict(color='White',size=12), borderpad=10, 
         x=0.01, y=0.01, xref='page', yref='page', align='left', showarrow=False, bgcolor='gray'),
    dict(text='WARNING: Contains CUI // INV / PRIV', font=dict(color='Red',size=12), borderpad=10, 
         x=0.99, y=0.01, yref='paper', align='right', showarrow=False, bgcolor='White'),
    
])


layout_revenue['annotations'] = annotations_revenue_MAY22

REVENUE_CHANGES_MAY22 = dict(data=REVENUE_DATA_MAY22, layout=layout_revenue)
offline.iplot(REVENUE_CHANGES_MAY22)