import csv
import matplotlib.pyplot as plt
import numpy as np
import decimal

with open('MinimumWageData.csv', 'r') as min_wage_file:

    information = []
    years = {}
    locations = []
    averages = []

    min_wage_read = csv.reader(min_wage_file, delimiter=',')

    for row in min_wage_read:    # reads file and makes it into a more easily read list
        if row[1] == "State":
            continue
        else:
            information.append(row)

    for num in range(1968, 2018): # assigns years to a dictionary
        years[str(num)] = []

    for row in information: # finds all minimum wages of each year
        try:
            try:
                if (float(row[4]) != 0):
                    years[row[0]].append(float(row[4]))
            except ValueError:
                continue
        except KeyError:
            continue
    for k in years: # finds the average of each year
        average = sum(years[k]) / len(years[k])
        averages.append(round(average, 2))
    print(averages)

    #formatting the graph

    plt.rcParams["figure.figsize"] = (12,7)
    plt.plot(list(years.keys()), averages, marker = 'o', color = "green")
    plt.xticks(['1968', '1978', '1988', '1998', '2008', '2017'])
    plt.yticks(list(range(9)))
    plt.ylabel('U.S. Currency ($)', fontsize = 15)
    plt.xlabel('Year', fontsize = 15)
    plt.title('Average Minimum Wage', fontsize = 20)
    plt.grid(alpha = .25)
    plt.tick_params(labelsize = 20)
    plt.savefig('Average_min_wage.jpg')
    plt.show()