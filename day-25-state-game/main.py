# with open("weather_data.csv") as the_weather:
#     data = the_weather.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     csv = csv.reader(data_file)
#     temperatures = []
#     for row in csv:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# average_temperature = data.temp.mean()
# max_temperature = data.temp.max()
# print(f"Average temperature: {average_temperature}")
# print(f"Max temperature: {max_temperature}")
# print(f"Max temperature day:\n{data[data.temp == max_temperature]}")

# monday = data[data.day == "Monday"]
# monday_temp_F = int(monday.temp * 9/5 + 32)
# print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

student_scores = pandas.DataFrame(data_dict)
print(student_scores)
student_scores.to_csv("student_scores.csv")
