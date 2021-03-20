import csv
import matplotlib.pyplot as plt
import numpy as np
import decimal

with open('MinimumWageData.csv', 'r') as min_wage_file: # opening the csv file

    information = []
    years = {}
    

    min_wage_read = csv.reader(min_wage_file, delimiter=',')

    for row in min_wage_read:    # reads file and makes it into a more easily read list
        if row[1] == "State":
            continue
        else:
            information.append(row)

    for num in range(1968, 2018): # adds each year to a dictionary
        years[str(num)] = []

    for row in information: # finds all states named 'New Jersey' and adds it's min wage to a dictionary per year
        if row[1] == 'New Jersey':
            years[row[0]] = float(row[4])
        else:
            continue

    # configuring the graph

    plt.rcParams["figure.figsize"] = (12,7)
    plt.plot(list(years.keys()), list(years.values()), marker = 'o', color = 'green')
    plt.xticks(['1968', '1978', '1988', '1998', '2008', '2017'])
    plt.yticks(list(range(9)))
    plt.tick_params(labelsize = 20)
    plt.xlabel('Years', size = 15)
    plt.ylabel('U.S. Currency ($)', size = 15)
    plt.title("New Jersey's Min. Wage by Year", fontsize = 20)
    plt.grid(alpha = 0.25)
    plt.savefig('NJ_min_wage.jpg')
    plt.show()