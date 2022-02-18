import pandas as pd
import statsmodels.api as sm
import pyodbc
import matplotlib.pyplot as plt
 
import numpy as np
 
data = pd.read_csv("C:/Users/edmun/AirPassengers.csv") 
t_data = data['Month']
y_data = data['#Passengers']

#y = np.array([2,11,4,13,6,15,8,17,10,19])
#t = np.array([3,4,5,6,7,8,9])

#y = np.array([2,13,6,16,10,20,16,24,18,28])
y = y_data

maxshift = 3
size = y.size
 
t = range(0,size)[maxshift:size]
#print(t)
yt = y[maxshift:size]
# yt = np.roll(y, -2)[0:size-maxshift]
yt1 = y[maxshift-1:size-1]
# yt1 = np.roll(y, -1)[0:size-maxshift]
yt2 = y[maxshift-2:size-2]
# yt1 = np.roll(y, 0)[0:size-maxshift]
yt3 = y[maxshift-3:size-3]
# yt1 = np.roll(y, 0)[0:size-maxshift]
 
import pandas as pd
 
data = pd.DataFrame(list(zip(t,yt, yt1, yt2, yt3)), columns = ['t','y', 'yt1', 'yt2', 'yt3'])
 
Y = data["y"]
X = data[['yt2','yt1','t']]
 
import statsmodels.api as sm
 
X = sm.add_constant(X)
 
model = sm.OLS(Y, X)
result = model.fit()

#print(result.summary())

print(result.predict( [1, list(y)[-2], list(y)[-1], t[-1]+1]) )