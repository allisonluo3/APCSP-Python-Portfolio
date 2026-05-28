#Allison
#Video Game Dev
#Analyze the data, and unravel the story that the data is showing us
#Initialize
import pandas as pd
data = pd.read_csv('influencer.csv')
month = data['Month'].tolist()
views = data['Views'].tolist()
dislikes = data['Dislikes'].tolist()
subscriber = data['Subscriber(+-)'].tolist()
revenue = data['Revenue'].tolist()
filter = []

#Functions
def humble(count):
    for i in range(len(month)):
        if views[i] <= count:
            filter.append(month[i])
    print(filter)
    filter.clear()

def golden_age(count):
    for i in range(len(month)):
        if subscriber[i] >= count:
            filter.append(month[i])
    print(filter)
    filter.clear()

def scandal(money):
    for i in range(len(month)):
        if revenue[i] <= money:
            filter.append(month[i])
    print(filter)
    filter.clear()

#Main
humble(2000)
print(data.loc[0:10])
golden_age(50000)
print(data.loc[64:72])
scandal(0)
print(data.loc[[98, 107]])
