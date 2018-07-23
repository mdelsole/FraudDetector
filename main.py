import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Not a binary "did they commit fraud" but more depth, identifying patterns and then people who potentially cheated

dataset = pd.read_csv("Credit_Card_Applications.csv")
# Divide data into two parts, the customer info and whether or not their application was accepted (the last column)
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values

# Feature scaling (normalize all features to between 0 and 1)
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range=(0, 1))
# Apply the scaling
X = sc.fit_transform(X)

"""
Strategy: Detect the mean euclidean distance from the origing point of the neighborhood that we define. Outliers will be
the ones likely to be frauds; they are different than normal transactions
"""

# Training the SOM. Implementation for som written in minisom file
from minisom import MiniSom
# X,y are dimensions of the map, pretty arbitrary selection. I chose 10x10 because we won't need too many features
# Input length is amount of columns, sigma is radius of the different neighborhoods (1 is default)
som = MiniSom(x=10, y=10, input_len=15, sigma=1.0, learning_rate=0.5)

# Initialize the weights randomly and train it on the data using those weights for 100 iterations
som.random_weights_init(X)
som.train_random(data=X, num_iteration=100)

# Visualizing the results
from pylab import bone, pcolor, colorbar, plot, show
# Initialize the window
bone()
# Correspond colors to mean interneuron differences
pcolor(som.distance_map().T)
# Add a legend bar and labels
colorbar()
markers = ['o','s']
colors = ['r','g']
# For all the indexes and vectors of customers at the different iterations
for i,x in enumerate(X):
    w = som.winner(x)
    plot(w[0]+0.5, w[1]+0.5, markers[y[i]], markeredgecolor = colors[y[i]], markerfacecolor = 'None', markersize = 10, markeredgewidth = 2)
show()
