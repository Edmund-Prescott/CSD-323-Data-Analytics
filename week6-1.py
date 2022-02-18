import pandas as pd
import statsmodels.api as sm
import numpy as np

t = [3, 4, 5, 6, 7, 8, 9]
y = np.array([16, 10, 20, 16, 24, 18, 28])
maxShift = 3
size = y.size
yt = y[maxShift:size]
yt1 = y[maxShift-1:size-1]
yt2 = y[maxShift-2:size-2]
yt3 = y[maxShift-3:size-3]
 
data = pd.DataFrame(list(zip(yt, yt1, yt2, yt3)), columns = ['yt', 'yt1', 'yt2', 'yt3'])
X = data[['yt1', 'yt2', 'yt3']]
Y = data['yt']
 
X = sm.add_constant(X)
 
model = sm.OLS(Y, X)
result = model.fit()
print(result.summary())