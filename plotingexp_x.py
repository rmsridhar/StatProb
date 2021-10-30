import plotly.graph_objects as go
import math
s=0
x=[0,0,0,0,0,0,0,0,0,0,0]
y=[0,0,0,0,0,0,0,0,0,0,0]
for i in range(-5,5):
    x[s]=i
    y.append(s)
    y[s]=math.exp(-1*i)
    print(x[s])
    print(y[s])
    s=s+1   

fig=go.Figure(data=go.Scatter(x=x,y=y,mode='markers'))

fig.show()
