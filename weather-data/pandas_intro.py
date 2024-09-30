import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

# Get data in Columns

temp_list = data['temp'].to_list()
print(temp_list)
print(data.temp.mean())
print(data.temp.max())

condition_list = data.condition.to_list()
print(condition_list)

# Get data in Rows

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# Create DataFrame from scratch

data_dict = {
    "students": ["Anna", "James", "Angela"],
    "scores": [74, 96, 54]
}
data = pandas.DataFrame(data=data_dict)
data.to_csv("student_score.csv")