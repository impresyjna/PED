import csv
with open('X_train.csv') as csvfile:
    matrix = csv.DictReader(csvfile)
    first_row = next(matrix)
    num_cols = len(first_row)
    row_count = sum(1 for row in csvfile)
    print("Liczba cech: " + str(num_cols))
    print("Liczba przykladow: " + str(row_count))
