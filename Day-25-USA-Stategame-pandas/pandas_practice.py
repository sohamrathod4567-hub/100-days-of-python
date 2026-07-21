import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data)

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].tolist()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get the data in columns
# # # print(data["condition"])
# # print(data.condition)
#
# #Get data in Row
# print(data[data.day == "Monday"])
#
# print(data[data.temp == max(data.temp)])
#
# monday = data[data.day == "Monday"]
# print(monday.temp)

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", " James", "Angela"],
    "scores" : [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")