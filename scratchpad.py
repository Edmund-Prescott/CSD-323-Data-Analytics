from operator import mod
from unittest import result
from numpy import sort
import pandas as pd
from scipy import stats

import statsmodels.api as sm

data = pd.read_csv("C:/Users/edmun/World Indicators.csv")

us_data = data[data['Country/Region'] == 'United States']

us_population = us_data['Population Total']
us_year = us_data['Year']

X = sm.add_constant(us_year)
model = sm.OLS(us_population, X)
result = model.fit()

#print(result.summary())

us_year_population = us_data[['Year','Population Total']]

#print(us_year_population)


africa_data = data[data['Region'] == 'Africa']

africa_year_population = africa_data[['Year','Population Total']]

#print(africa_year_population)

byyear = africa_year_population.groupby("Year", as_index=False).sum()

#print(byyear)

Y = byyear["Population Total"]

X = sm.add_constant(byyear["Year"])

model = sm.OLS(Y, X)
fit = model.fit()

#print(fit.params)
#fit.predict(X)
#print(fit.params[0])
#print(fit.params[1])

a = result.params[0]+result.params[1]*2015
print('['+'{:e}'.format(a)+']')
#data = pd.read_csv("C:/Users/edmun/weight-height.csv")

#m_data = data[data['Gender '] == 'Male']
#m_weight = m_data['Weight']

#mean_m_weight = m_weight.mean()
#stdev_m_weight = statistics.stdev(m_weight)

#print(stats.uniform(min(m_weight), max(m_weight)).pdf(190))
#print(round(stats.norm(mean_m_weight, stdev_m_weight).pdf(190), 2))
#print(round(stats.norm(mean_m_weight, stdev_m_weight).cdf(190), 2))
#print(round(stats.norm(mean_m_weight, stdev_m_weight).ppf(.90), 2))
