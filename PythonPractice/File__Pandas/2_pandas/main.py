import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data)
print()
print(data["temp"])
print()

data_dict = data.to_dict()
print(data_dict)
print()

temp_list = data["temp"].to_list()
print(temp_list)
print()

print(data["temp"].mean())
print()

print(data["temp"].max())
print()

#get data in column
print(data["condition"])
print(data.condition)
print()

#get data in row
print(data[data.day == "Monday"])
print()
print(data[data.temp == data.temp.max()])
print()

monday = data[data.day == "Monday"]
print(monday.condition)
print()
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)
print()

data_dict = {
    "students" : ["Pushkar", "Parashar","Automata"],
    "scores": [99,89,100]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("newdata.csv")