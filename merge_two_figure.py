import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

fig1 = px.line(df, x='P', y='F', color='V', template='seaborn').update_layout(showlegend=True)
fig2 = px.line(df_requirement, x='pressure', y='flow', color='temperature')

fig = go.Figure()
fig.add_traces(fig1.data)
fig.add_traces(fig2.data)
fig.update_xaxes(title_text='Pressure (KPA)')
fig.update_yaxes(title_text='Flow (l/h)')
fig.show()

#one more example with custom legend
fig1 = px.line(y=g_loss_list, template='seaborn').update_traces(showlegend=True, name='g_loss')
fig2 = px.line(y=d_loss_list).update_traces(showlegend=True, name='d_loss')

fig = go.Figure()
fig.add_traces(fig1.data)
fig.add_traces(fig2.data)
fig.update_layout(showlegend=True)
fig.show()
