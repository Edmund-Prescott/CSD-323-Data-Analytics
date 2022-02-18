# t = [1, 2, 3, 4, 5]
#y = [3, 5, 7, 9, 11, 13, 15]
 
import numpy as np
 
y = np.array([2, 11, 4, 13, 6, 15, 8, 17, 10, 19])
 
maxshift = 2
size = y.size
 
yt = y[maxshift:size]
# yt = np.roll(y, -2)[0:size-maxshift]
yt1 = y[maxshift-1:size-1]
# yt1 = np.roll(y, -1)[0:size-maxshift]
yt2 = y[maxshift-2:size-2]
# yt1 = np.roll(y, 0)[0:size-maxshift]
 
import pandas as pd
 
data = pd.DataFrame(list(zip(yt, yt1, yt2)), columns = ['y', 'yt1', 'yt2'])
 
Y = data["y"]
X = data[['yt1', 'yt2']]
 
import statsmodels.api as sm
 
X = sm.add_constant(X)
 
model = sm.OLS(Y, X)
result = model.fit()
 
print(result.summary())