import csv

with open("./weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
    for d in data:
        print(d.strip())

with open("weather_data.csv") as file_content:
    data = csv.reader(file_content)
    temperature = []
    for row in data:
        if row[1] != 'temp':
            temperature.append(int(row[1]))
    print(temperature)
