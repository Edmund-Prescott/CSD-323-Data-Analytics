from email.header import Header
import pandas as pd
 
data = pd.read_csv("C:/Users/edmun/weight-height.csv")
 
data_male = data[data["Gender "] == "Male"]
 
from scipy import stats
res = stats.normaltest(data_male["Height"])
print(res) # Test suggest it's normal
 
import statistics
mean_height_male = statistics.mean(data_male["Height"])
sd_height_male = statistics.stdev(data_male["Height"])
 
print("Sd: " + str(sd_height_male))
 
data_female = data[data["Gender "] == "Female"]

res = stats.normaltest(data_female["Height"])
print(res) # Test suggest it's normal
 
 
import statistics
mean_height_female = statistics.mean(data_female["Height"])
sd_height_female = statistics.stdev(data_female["Height"])
 
print("Sd: " + str(sd_height_female))
 
# The conditions are fulfilled -->
# Both sets are normal
# Both have similar standard deviations
 
# Now we can answer the question
# According to this data are females on average taller than males
 
print("Mean Male: " + str(mean_height_male))
print("Mean Female: " + str(mean_height_female))
 
res_tt = stats.ttest_ind(data_male["Height"], data_female["Height"])
print(res_tt)