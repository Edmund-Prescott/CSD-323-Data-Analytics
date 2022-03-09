points = {
    'Point' : ['A','B','C','D','E','F','G'],
    'x' : [2, 3, 5, 7, 1, 10, 11],
    'y' : [3, 2, 4, 8, 2, 9, 8]
}
 
import pandas as pd
 
data = pd.DataFrame(points)
print(data)

import matplotlib.pyplot as plt

plt.scatter(data['x'], data['y'])
#plt.show()

x = data.iloc[:, 1:3]
print(x)

from sklearn.cluster import KMeans
kmeans = KMeans(3)
kmeans.fit(x)
 
clusters = kmeans.fit_predict(x)
print(clusters)

plt.scatter(data['x'], data['y'], c=clusters)
#plt.show()

n_cluster = range(1, 7)
inertia = []
for i in n_cluster:
    kmeans = KMeans(i)
    kmeans.fit(x)
    inertia.append(kmeans.inertia_)
 
plt.clf()
plt.plot(n_cluster, inertia)

kmeans = KMeans(4)
kmeans.fit(x)
clusters = kmeans.fit_predict(x)
 
plt.clf()
plt.scatter(data['x'], data['y'], c=clusters)
plt.show()

data = pd.read_csv("C:/Users/edmun/World Indicators.csv")

data_female = data[data["Gender "] == "Female"]

female_life_expectancy = data_female["Life Expectancy Female"]
female_birth_rate = data_female["Birth Rate"]