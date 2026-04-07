import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250110.csv")
print(data)

df = pd.DataFrame(data)

infor = df.info()
print(infor)

grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_count)
print(red_count)
print(black_count)

data_dict = {
    "Fur color" : ["Gray", "Cinnamon","Black"],
    "Count": [grey_count,red_count,black_count]
}

df2 = pd.DataFrame(data_dict)
df2.to_csv("squirrel_count.csv")