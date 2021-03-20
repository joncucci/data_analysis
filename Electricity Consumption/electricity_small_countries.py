import csv
import matplotlib.pyplot as plt
import numpy as np 

info = []
list_of_countries = []

def find_value(string_to_find):
    i = 0
    for words in info[0]:
        if words == string_to_find:
            return i
        else:
            i += 1


with open('factbook_updated.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        info.append(row)

    info_without_header = info[1:]
    for country in info:
        list_of_countries.append(country[0])

    list_of_countries.pop(0)
    graphed_countries = list_of_countries[8:]
    print(graphed_countries)
    electricity_con = []
    electricity_prod = []

    for country in info_without_header[8:]:
        consumption_index = float(country[find_value("Electricity - consumption(kWh)")])
        electricity_con.append(consumption_index / 10**12)
        production_index = float(country[find_value("Electricity - production(kWh)")])
        electricity_prod.append(production_index / 10**12)

    plt.rcParams["figure.figsize"] = (13,8)
    bar_width = 0.25
    r1 = np.arange(len(electricity_con))
    r2 = [x + bar_width for x in r1]

    plt.bar(r1, electricity_con, width = bar_width, label = "Consumption", color = "#ff5a4f")
    plt.bar(r2, electricity_prod, width = bar_width, label = "Production", color = "#54ff54")
    plt.xticks([r + bar_width/2 for r in range(len(electricity_con))], graphed_countries)
    plt.xlabel('Countries', fontsize = 20)
    plt.ylabel('Electricity (Trillion kWh)', fontsize = 20)
    plt.title('Electricity Consumption vs. Production\n(Small Countries)', fontsize = 20)
    plt.tick_params(labelsize = 20)
    plt.legend(loc = "upper right")
    plt.grid(alpha = 0.25)
    plt.savefig('electricity_small.jpg', dpi = 75)
    plt.show()
