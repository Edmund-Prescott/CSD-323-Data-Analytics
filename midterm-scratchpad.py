import pandas as pd
from scipy import stats
import statistics
import numpy as np

data = pd.read_csv("C:/Users/edmun/xyab.csv") 

x_data = data["x"]
y_data = data["y"]
a_data = data["a"]
b_data = data["b"]

#res = stats.kstest(x_data, stats.uniform(loc=min(x_data), scale=max(x_data)).cdf) 

print( round( stats.uniform(min(x_data), max(x_data) - min(x_data)).cdf(1.5) , 1) )

print( round( stats.uniform(min(y_data), max(y_data) - min(y_data)).cdf(2.8) , 1) )

a_mean = a_data.mean()
a_stdev = statistics.stdev(a_data)

print( round( stats.norm(a_mean, a_stdev).cdf(1.5) - stats.norm(a_mean, a_stdev).cdf(1.1) , 2) )

b_mean = b_data.mean()
b_stdev = statistics.stdev(b_data)

print( round( stats.norm(b_mean, b_stdev).ppf(.60) , 2) )

ab_data = a_data + b_data

ab_mean = ab_data.mean()
ab_stdev = statistics.stdev(ab_data)

print( round(  stats.norm(ab_mean, ab_stdev).ppf(.90), 2) )