import math
import csv

with open("data.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

# Step 1: Finding the mean
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total = total + int(x)
    mean = total / n
    return mean

# Step 2: Subtract mean from all values and square
squared_list = []
for num in data:
    a = int(num) - mean(data)
    a = a**2
    squared_list.append(a)

# Step 3: Finding the sum
s = 0
for i in squared_list:
    s = s + i

# Step 4: Divide sum by total - 1
res = s / (len(data) - 1)

# Step 5: Find square root
ans = math.sqrt(res)
print(f"Answer: {str(ans)}")