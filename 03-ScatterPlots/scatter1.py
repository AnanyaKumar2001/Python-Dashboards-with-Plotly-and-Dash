import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(x = random_x, y = random_y, mode = 'markers')]
pyo.plot(data, filename='scatter1.html')
