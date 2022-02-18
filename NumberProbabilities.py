from os import stat
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

# Load data from an excel spreedsheet
data = pd.read_csv("C:/Users/edmun/file3.csv") 

# Use that data to make a histogram
dat = data["x"] 
plt.hist(dat) 
plt.show() 

# Look for uniform distribution
res = stats.kstest(dat, stats.uniform(loc=min(dat), scale=max(dat)).cdf) 
print(res) 

# % Chance that a given number will be less that 75 
print(stats.uniform(min(dat), max(dat)).cdf(75))

# % Chance that a given number will be 43
print(stats.uniform(loc=min(dat), scale=max(dat)).pdf(43))