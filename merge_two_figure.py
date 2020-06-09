import pandas as pd
import plotly.express as px
import pickle

fig1 = px.line(df, x='P', y='F', color='V', template='seaborn').update_layout(showlegend=True)
fig2 = px.line(df_requirement, x='pressure', y='flow', color='temperature')

import plotly.graph_objects as go
fig = go.Figure()
fig.add_traces(fig1.data)
fig.add_traces(fig2.data)
fig.update_xaxes(title_text='Pressure (KPA)')
fig.update_yaxes(title_text='Flow (l/h)')
fig.show()
