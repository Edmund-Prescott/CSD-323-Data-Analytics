from operator import mod
from unittest import result
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import pyodbc

server = 'ludsampledb.database.windows.net'
database = 'SampleDB'
username = 'sampleadmin'
password = 'bC5B+=fd'   
driver= '{SQL Server}'

# get a look at available tables => "SELECT * FROM information_schema.tables"
# get a look at the table I want => "SELECT * FROM dbo.Orders"
query = "SELECT ROUND(SUM(Sales),2) FROM dbo.Orders GROUP BY YEAR(Order_Date), MONTH(Order_Date) ORDER BY YEAR(Order_Date), MONTH(Order_Date)"

sales = []

with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    data = pd.read_sql(query,conn)

sales = np.array(data)
sales = sales.flatten()
sales = list(sales)

print(sales[0:10])
y = np.array(sales)

maxshift = 3
size = y.size
 
t = range(0,size)[maxshift:size]
yt = y[maxshift:size]
yt1 = y[maxshift-1:size-1]
yt2 = y[maxshift-2:size-2]
yt3 = y[maxshift-3:size-3]
 
data = pd.DataFrame(list(zip(t,yt, yt1, yt2, yt3)), columns = ['t','y', 'yt1', 'yt2', 'yt3'])
 
Y = data["y"]
X = data[['yt3','yt2','yt1','t']]
 
X = sm.add_constant(X)
 
model = sm.OLS(Y, X)
result = model.fit()


print(result.predict([1,   list(y)[-1], list(y)[-2], list(y)[-3], t[-1]+1   ]))



# data = pd.read_csv("C:/Users/edmun/World Indicators.csv")

# us_data = data[data['Country/Region'] == 'United States']

# us_population = us_data['Population Total']
# us_year = us_data['Year']

# X = sm.add_constant(us_year)
# model = sm.OLS(us_population, X)
# result = model.fit()

# print(result.summary())

# us_year_population = us_data[['Year','Population Total']]

# print(us_year_population)


# africa_data = data[data['Region'] == 'Africa']

# africa_year_population = africa_data[['Year','Population Total']]

# #print(africa_year_population)

# byyear = africa_year_population.groupby("Year", as_index=False).sum()

# print(byyear)

# Y = byyear["Population Total"]

# X = sm.add_constant(byyear["Year"])

# model = sm.OLS(Y, X)
# fit = model.fit()

# print(fit.params)
# fit.predict(X)
# print(fit.params[0])
# print(fit.params[1])

# a = result.params[0]+result.params[1]*2015
# print('['+'{:e}'.format(a)+']')
# data = pd.read_csv("C:/Users/edmun/weight-height.csv")

# m_data = data[data['Gender '] == 'Male']
# m_weight = m_data['Weight']

# mean_m_weight = m_weight.mean()
# stdev_m_weight = statistics.stdev(m_weight)

# print(stats.uniform(min(m_weight), max(m_weight)).pdf(190))
# print(round(stats.norm(mean_m_weight, stdev_m_weight).pdf(190), 2))
# print(round(stats.norm(mean_m_weight, stdev_m_weight).cdf(190), 2))
# print(round(stats.norm(mean_m_weight, stdev_m_weight).ppf(.90), 2))
