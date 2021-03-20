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
    line = 0

    for row in csv_reader:
        info.append(row)

    info_without_header = info[1:]
    for country in info:
        list_of_countries.append(country[0])

    list_of_countries.pop(0)
    countries_population = []

    for country in info_without_header:
        new_value = float(country[find_value("Population")])
        countries_population.append(new_value)

    print(list_of_countries)
    print(countries_population)

    plt.rcParams["figure.figsize"] = (13,8)
    plt.bar(list_of_countries,countries_population)
    plt.yscale('log')
    for index, value in enumerate(countries_population):

        plt.text(index - .4, value*1.05, "{:,}".format(int(value)), fontsize = 8)

    plt.title("Populations", fontsize = 20)
    plt.xticks(fontsize = 9)
    plt.yticks(fontsize = 18)
    plt.xlabel("Countries", fontsize = 20)
    plt.ylabel("Population", fontsize = 20)
    plt.savefig('populations.jpg',bbox_inches='tight', dpi = 100)
    plt.show()

