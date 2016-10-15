from __future__ import division
import numpy as np


cols_count = 0
row_count = 0
non_zero = 0
x_data = np.loadtxt(open("X_train.csv", "r"), delimiter=",")
for row in x_data:
    row_count += 1
    if (cols_count < len(row)):
        cols_count = len(row)
    for column in row:
        if (column != 0):
            non_zero += 1

array = np.genfromtxt('Y_train.csv', delimiter="\n")
unique_set = set(array)
classes = {}

for value in unique_set:
    classes[value] = 0

for value in array:
    classes[value] += 1

dom_class = max(classes, key=classes.get)

print("Dominujaca klasa oraz jej prawdopodobienstwo: " + str(dom_class) + " " + str(classes[dom_class]/len(array)))


print("Liczba cech: " + str(cols_count))
print("Liczba przykladow: " + str(row_count))
print("Liczba niezerowych wartosci cech: " + str(non_zero))
