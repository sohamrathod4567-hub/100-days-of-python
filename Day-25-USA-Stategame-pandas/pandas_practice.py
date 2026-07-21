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
# data_dict = {
#     "students": ["Amy", " James", "Angela"],
#     "scores" : [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color" ] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color" ] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color" ] == "Black"])

print(gray_count)
print(cinnamon_count)
print(black_count)

data_dict = {
    "Fur color": ["Gray" , "Cinnamon" , "Black"],
    "Count" : [gray_count, cinnamon_count, black_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")