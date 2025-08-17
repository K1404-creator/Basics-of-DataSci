import matplotlib.pyplot as plt
import plotly.graph_objects as go

#INTERACTIVE LINE CHART
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

# Sales = [1000, 1500, 2000, 2500, 3000]


# fig = go.Figure(data=go.Scatter(x=months, y=Sales, mode='lines+markers', marker=dict(color='blue')))



# fig.update_layout(title='Sales data', xaxis_title='Month', yaxis_title='Sales')



# fig.show()

# interactive scatter


study_hour = [1, 2, 3, 4, 5]

scores = [10, 20, 30, 40, 50]


fig = go.Figure(data = go.Scatter(x=study_hour, y=scores, mode='lines+markers', marker=dict(color='red', size=10)))

fig.update_layout(title='Study Hours vs Scores', xaxis_title='Study Hours', yaxis_title='Scores')

fig.show()