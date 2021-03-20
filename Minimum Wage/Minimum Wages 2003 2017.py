import csv
import matplotlib.pyplot as plt
import numpy as np

with open('MinimumWageData.csv', 'r') as min_wage_file:

    information = []
    years = {}
    locations = []

    low_wages_1988_2002 = []

    min_wage_read = csv.reader(min_wage_file, delimiter=',')

    for row in min_wage_read:    # reads file and makes it into a more easily read list
        if row[1] == ("Puerto Rico" or "U.S. Virgin Islands" or "Federal (FLSA)" or "Guam" or "District of Columbia"):
            continue
        else:
            information.append(row)

    for num in range(2003, 2018):
        years[str(num)] = 10

    for num in range(2003, 2018):
        maximums = []
        for row in information:
            try:
                if int(row[0]) == num:
                    maximums.append(float(row[4]))
                maximums.remove(0)
                years[str(num)] = max(maximums)
            except ValueError:
                continue
        for row in information:
            try:
                if float(row[4]) == years[str(num)]:
                    locations.append(row[1])
                    break
                else:
                    continue
            except ValueError:
                continue
    locations = [sub.replace('District of Columbia', 'Wash. D.C.') for sub in locations]
    locations = [sub.replace('Massachusetts', 'Mass.') for sub in locations]
    print(locations)
    plt.rcParams["figure.figsize"] = (12,7)
    plt.bar(list(years.keys()), list(years.values()), facecolor = "green", width = 0.75)
    plt.yticks(range(0, 14))
    plt.ylabel("U.S. Currency ($)", fontsize = 15)
    plt.xlabel("Years", fontsize = 15)
    plt.title("Highest Min. Wage State in The U.S. Per Year (2003-2017)", fontsize = 20)
    for x, locations in enumerate(locations):
        plt.annotate(locations + "\n" + str(list(years.values())[x]), ((list(years.keys())[x]), list(years.values())[x] + 0.25), size = 7, ha = 'center')
    plt.grid(alpha = 0.25)
    plt.tick_params(labelsize = 10)
    plt.savefig('MinWages2003_2017.jpg')
    plt.show()