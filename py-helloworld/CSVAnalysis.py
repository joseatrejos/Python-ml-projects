import matplotlib.pyplot as plot
import pandas as pd

# This is going to store the whole csv file in a variable
rawData = pd.read_csv('py-helloworld\StudentsPerformance.csv')


# This rawData variable will print the whole CSV withouth any processing
# print(rawData)


# This variable with rawData.info will analyze the amount & types of data that each column contains 
# dataInfo = rawData.info()
# print(dataInfo)


# This is going to store the csv file's Gender and Math Score columns in a variable
dataNeeded = pd.read_csv('py-helloworld\StudentsPerformance.csv', usecols=['gender', 'math score'])
# print(dataNeeded)



# This will create a variable that filters the column "gender" and shows ONLY the female or male results
femaleFilter = dataNeeded['gender'].isin(['female'])
maleFilter = dataNeeded['gender'].isin(['male'])

# We apply the filters' criteria to the csv and store the values into a variable
femaleData = dataNeeded[femaleFilter]
maleData = dataNeeded[maleFilter]

# Finally, we print
print(femaleData)
print(maleData)

