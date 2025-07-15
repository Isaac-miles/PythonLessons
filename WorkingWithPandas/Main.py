
import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)

# print(data['temp'].mean())
# print(data['temp'].max())

# get data in Columns
# print(data['condition'])
# print(data.condition)

# get data in Row
# print(data[data.day =='Monday'])
# print(data[data.temp == data.temp.max()])

monday = data[data.day =='Monday']
# print(monday.condition)
monday_temp = monday.temp[0]
print(monday_temp * 9/5 + 32)

# create a dataframe from scratch
data_dictionary = {
    "student":['Miles','Zico','Wrld'],
    "scores":[76,56,65]
}
data_1 = pandas.DataFrame(data_dictionary)
print(data_1)
data.to_csv("student_data")
