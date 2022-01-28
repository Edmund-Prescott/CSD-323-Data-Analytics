import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# (inclusize, exclusive, count)
n = 1000
data = np.random.randint(1, 7, size=n)
# plt.hist(data) 
# plt.show() 


res = stats.kstest(data, stats.uniform(loc=min(data), scale=max(data)).cdf) 
print(res) 

rolleddice = 0

for i in range(1, 50):
    roll = np.random.randint(1, 7, size=n)
    rolleddice += roll

w = round()


plt.hist(rolleddice) 
plt.show() 

normal_res = stats.normaltest(rolleddice)
print(normal_res)