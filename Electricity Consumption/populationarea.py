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
    csv_reader = csv.reader(csv_file, delimiter=',')     # opens file, reads it and writes it to a python variable

    for row in csv_reader:    # appends all information as different lists
        info.append(row)

    info_without_header = info[1:]    # gets rid of the header
    for country in info:
        list_of_countries.append(country[0])

    list_of_countries.pop(0)
    countries_population = []
    countries_area = []

    for country in info_without_header:      # searches for the indexes of Population and Area, then adds that value to country population and area lists
        population_index = float(country[find_value("Population")])
        countries_population.append(population_index)
        area_index = float(country[find_value("Area(sq km)")])
        countries_area.append(area_index)

    #print(list_of_countries)
    #print(countries_population)
    #print(countries_area)

    plt.rcParams["figure.figsize"] = (13,8) 
    s = [countries_population[n] / countries_area[n] for n in range(12)]
    plt.scatter(countries_area, countries_population, s=s)
    plt.yscale('log')
    plt.xscale('log')
    plt.loglog()
    plt.grid()
    for i, txt in enumerate(list_of_countries):
        plt.annotate(txt, ((countries_area[i]*1.05), countries_population[i]*1.05))
    plt.xlabel('Area (sq km)', fontsize = 20)
    plt.ylabel('Population', fontsize = 20)
    plt.title('Population / Area', fontsize = 20)
    #plt.show()
    plt.tick_params(labelsize = 20)
    plt.savefig('PopulationArea.jpg', dpi = 75)
    plt.show()