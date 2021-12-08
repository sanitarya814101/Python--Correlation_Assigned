
# Correlation of Students marks V/S Number of days present

import numpy as np
import csv


def getDataSource(data_path):
    student_marks = []
    days_present = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            student_marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {
        "x": student_marks, "y": days_present
    }


def findingCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between student marks and number of days present is: ",
          correlation[0, 1])


def main():
    data_path = "Student Marks vs Days Present.csv"
    dataSource = getDataSource(data_path)
    findingCorrelation(dataSource)


main()
