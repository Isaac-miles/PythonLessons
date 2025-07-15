
import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(data['temp'].mean())