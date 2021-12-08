
# Correlation of cups of coffee V/S hours of sleep

import numpy as np
import csv


def getDataSource(data_path):
    coffee = []
    hours = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            hours.append(float(row["sleep in hours"]))

    return {
        "x": coffee, "y": hours
    }


def findingCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between hours and coffees is: ", correlation[0, 1])


def main():
    data_path = "cups of coffee vs hours of sleep.csv"
    dataSource = getDataSource(data_path)
    findingCorrelation(dataSource)


main()
