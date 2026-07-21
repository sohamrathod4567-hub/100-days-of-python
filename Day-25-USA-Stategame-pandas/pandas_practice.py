import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].tolist()
print(temp_list)

print(data["temp"].mean())
print(data["temp"].max())

#Get the data in columns
# print(data["condition"])
print(data.condition)