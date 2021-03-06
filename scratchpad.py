from operator import mod
from unittest import result
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import pyodbc


zero =  [ 1,1,1,
          1,0,1,
          1,0,1,
          1,0,1,
          1,1,1]

one =   [ 0,0,1,
          0,0,1,
          0,0,1,
          0,0,1,
          0,0,1]

two =   [ 1,1,1,
          0,0,1,
          1,1,1,
          1,0,0,
          1,1,1]

three = [ 1,1,1,
          0,0,1,
          0,1,1,
          0,0,1,
          1,1,1]

four =  [ 1,0,1,
          1,0,1,
          1,1,1,
          0,0,1,
          0,0,1]

five =  [ 1,1,1,
          1,0,0,
          1,1,1,
          0,0,1,
          1,1,1]

six =   [ 1,1,1,
          1,0,0,
          1,1,1,
          1,0,1,
          1,1,1]

seven = [ 1,1,1,
          0,0,1,
          0,0,1,
          0,0,1,
          0,0,1]

eight = [ 1,1,1,
          1,0,1,
          1,1,1,
          1,0,1,
          1,1,1]

nine =  [ 1,1,1,
          1,0,1,
          1,1,1,
          0,0,1,
          1,1,1]

cols = list(['m00','m01', 'm02', 'm10', 'm11', 'm12', 'm20', 'm21', 'm22', 'm30','m31','m32','m40','m41','m42'])
data = pd.DataFrame([zero,one, two, three, four, five, six, seven, eight, nine], columns = cols)

x = data[['m00','m01','m10','m12','m21','m40','m41']]

y = [0,1,2,3,4,5,6,7,8,9]

model = sm.OLS(y, x)
result = model.fit()

print(result.summary())

#server = 'ludsampledb.database.windows.net'
#database = 'SampleDB'
#username = 'sampleadmin'
#password = 'bC5B+=fd'   
#driver= '{SQL Server}'

# get a look at available tables => "SELECT * FROM information_schema.tables"
# get a look at the table I want => "SELECT * FROM dbo.Orders"
#query = "SELECT ROUND(SUM(Sales),2) FROM dbo.Orders GROUP BY YEAR(Order_Date), MONTH(Order_Date) ORDER BY YEAR(Order_Date), MONTH(Order_Date)"

#sales = []

#with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
#    data = pd.read_sql(query,conn)

#sales = np.array(data)
#sales = sales.flatten()
#sales = list(sales)

#print(sales[0:10])
#y = np.array(sales)

#maxshift = 3
#size = y.size

#t = range(0,size)[maxshift:size]
#yt = y[maxshift:size]
#yt1 = y[maxshift-1:size-1]
#yt2 = y[maxshift-2:size-2]
#yt3 = y[maxshift-3:size-3]

#data = pd.DataFrame(list(zip(t, yt, yt1, yt2, yt3)), columns = ['t', 'y', 'yt1', 'yt2', 'yt3'])

#Y = data["y"]

#X = data[['yt1','t' ]]

#model = sm.OLS(Y, X)
#result = model.fit()

#print(round(result.predict([list(y)[-1], t[-1]+1])[0], 2))

#Y = data["y"]

#X = data[['yt2','yt1','t' ]]

#model = sm.OLS(Y, X)
#result = model.fit()


#print(round(result.predict([list(y)[-1],list(y)[-1], t[-1]+1])[0], 2))
#print(round(result.predict([list(y)[-1], t[-3]+3])[0], 2))



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
