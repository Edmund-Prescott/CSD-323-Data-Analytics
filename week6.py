import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
 

server = 'ludsampledb.database.windows.net'
database = 'SampleDB'
username = 'sampleadmin'
password = 'bC5B+=fd'   
driver= '{SQL Server}'


with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    data = pd.read_sql("SELECT SUM([Population Total]) as Population, Year, Region FROM dbo.WorldIndicators WHERE Region='Asia' GROUP BY [Year], Region",conn)

print(data)

plot = plt.figure()
axis = plot.add_axes([0, 0, 1, 1])
axis.bar(data['Year'], data['Population'])
plt.show()

asia_population = data['Population']
asia_year = data['Year']

X = sm.add_constant(asia_year)
model = sm.OLS(asia_population, X)
result = model.fit()

prediction = result.predict([1,2015])
print(prediction)

