import pandas as pd
from scipy import stats
import statistics

data = pd.read_csv("C:/Users/edmun/weight-height.csv")

m_data = data[data['Gender '] == 'Male']
m_weight = m_data['Weight']

mean_m_weight = m_weight.mean()
stdev_m_weight = statistics.stdev(m_weight)

print(stats.uniform(min(m_weight), max(m_weight)).pdf(190))
print(round(stats.norm(mean_m_weight, stdev_m_weight).pdf(190), 2))
print(round(stats.norm(mean_m_weight, stdev_m_weight).cdf(190), 2))
print(round(stats.norm(mean_m_weight, stdev_m_weight).ppf(.90), 2))