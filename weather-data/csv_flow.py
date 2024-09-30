import csv

with open("weather_data.csv") as data_source:
    data = csv.reader(data_source)
    temperatures = []
    for row in data:
        # print(row)
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
