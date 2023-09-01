# -*- coding: utf-8 -*-
"""SOM

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jX-BYj_1ku_scCHIc5QVv9JkiFhuhl5p
"""

import numpy as np
import matplotlib.pyplot as plt

n_cities = 100
cities = np.random.rand(n_cities, 2)
# Define the SOM
n_rows = 10
n_cols = 10
n_iterations = 100
lr_initial = 0.1
# Initialize the SOM
X = np.random.rand(n_rows*n_cols, 2)

# Define the neighborhood function
def neighborhood(d, sigma):
    return np.exp(-d**2/(2*sigma**2))
# Train the SOM
for t in range(n_iterations):
# Randomly select a city
    city_idx = np.random.randint(n_cities)
    city = cities[city_idx]
# Compute distances from city to each node in the SOM
    D = np.linalg.norm(X - city, axis=1)
# Find the winning node (i.e., the node with the closest coordinates to the city)
    winner_idx = np.argmin(D)
# Compute the neighborhood function
    sigma = n_rows/2 * np.exp(-t/n_iterations)
    lr = lr_initial * np.exp(-t/n_iterations)
    N = neighborhood(np.arange(n_rows*n_cols), sigma)
# Update the coordinates of the winning node and its neighbors
    X -= lr * N[:, np.newaxis] * (X - city)
# Find the order in which the cities are visited
order = np.argsort(np.linalg.norm(X - cities[:, np.newaxis], axis=2), axis=1)[:, 0]

# Plot the results
plt.scatter(X[:, 0], X[:, 1])
plt.plot(cities[order, 0], cities[order, 1], '-o', color='red')
plt.show()