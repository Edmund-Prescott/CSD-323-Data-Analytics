from os import stat
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statistics

data = pd.read_csv("C:/Users/edmun/weight-height.csv")

x = data['Height']

female_data = data[data['Gender '] == 'Female']
female_height = female_data['Height']

mean_female_height = female_height.mean()
stdev_female_height = statistics.stdev(female_height)

male_data = data[data['Gender '] == 'Male']
male_height = male_data['Height']

mean_male_height = male_height.mean()
stdev_male_height = statistics.stdev(male_height)

print("Male")
print("Mean height: ")
print(str(male_height.mean()))
print(str(statistics.stdev(male_height)))


print("\nFemale")
print("Mean height: ")
print(str(female_height.mean()))
print(str(statistics.stdev(female_height)))

print("----------------------------------------")

print(stats.norm(mean_male_height, stdev_male_height).pdf(67))

print(stats.norm(mean_male_height, stdev_male_height).cdf(70))

print(1 - stats.norm(mean_male_height, stdev_male_height).cdf(68))

print(stats.norm(mean_male_height, stdev_male_height).cdf(70) - stats.norm(mean_male_height, stdev_male_height).cdf(65))

print(stats.norm(mean_male_height, stdev_male_height).ppf(.90))

