# importing packages
import numpy as np
import pandas as pd

# reading your data(our data is china gdp)
df = pd.read_csv("china_gdp.csv")
df.head(10)

# ploting data
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
x_data, y_data = (df["Year"].values, df["Value"].values)
plt.plot(x_data, y_data, 'ro')
plt.ylabel('GDP')
plt.xlabel('Year')
plt.show()