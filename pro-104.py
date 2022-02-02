import pandas as pd
import statistics
data = pd.read_csv("SOCR-HeightWeight.csv")

# Mean of Height.
height = data["Height(Inches)"].tolist()
sum = 0
for i in height:
    sum = sum+i
print(sum)
mean = sum/len(height)
print(mean)

# Mean of Weight.
weight = data["Weight(Pounds)"].tolist()
sum = 0
for i in weight:
    sum = sum+i
print(sum)
mean = sum/len(weight)
print(mean)

# Median of Height.
height.sort()
heightMedian = statistics.median(height)
print(heightMedian)

# Median of Weight.
weight.sort()
weightMedian = statistics.median(weight)
print(weightMedian)

# Mode of Height.
mode = statistics.mode(height)
print(mode)

# Mode of Weight.
mode = statistics.mode(weight)
print(mode)




