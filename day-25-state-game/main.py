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
print(data["temp"])
