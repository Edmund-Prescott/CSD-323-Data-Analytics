import numpy as np
from sklearn.linear_model import LinearRegression

# Here we tried to find a correlation between movie trailer views on youtube and the movie's box office sales

# Movie trailer views on youtube
x = np.array([27232907,
148038861,
91360819,
1200000,
893000,
2000000,
251000000,
48000000,
64000000,
67000000]).reshape((-1,1))

# Box office sales
y = np.array([1344000000,
2798000000,
1403000000,
44000000,
27000000,
4700000,
2048600000,
306800000,
327481748,
1370000000])

model = LinearRegression().fit(x,y)

print('a:', model.coef_)
print('b:', model.intercept_)

print('score: ', model.score(x,y)) # % chance of a linear relationship

x_new = np.array([5]).reshape((-1,1))
print('predicted for 5: ',model.predict(x_new))