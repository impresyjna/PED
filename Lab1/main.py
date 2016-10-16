from __future__ import division
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

cols_count = 0
row_count = 0
non_zero = 0
x_data = np.loadtxt(open("X_train.csv", "r"), delimiter=",")
for row in x_data:
    print("Waiting")
    row_count += 1
    if (cols_count < len(row)):
        cols_count = len(row)
    for column in row:
        if (column != 0):
            non_zero += 1

file = open("results.txt", "w")
index = 0
with PdfPages('histograms.pdf') as pdf:
    for column in x_data.T:
        file.write("Cecha nr " + str(index) + "\n")
        file.write("Srednia: " + str(sum(column) / float(len(column))) + "\n")
        file.write("Wariancja: " + str(np.var(column)) + "\n")
        file.write("Unikalne wartosci: " + str(len(set(column))) + "\n")
        plt.hist(column)
        plt.title("Cecha nr " + str(index))
        pdf.savefig()
        plt.close()
        index += 1


array = np.genfromtxt('Y_train.csv', delimiter="\n")
unique_set = set(array)
classes = {}

for value in unique_set:
    classes[value] = 0

for value in array:
    classes[value] += 1

dom_class = max(classes, key=classes.get)

file.write("Dominujaca klasa oraz jej prawdopodobienstwo: " + str(dom_class) + " " + str(classes[dom_class]/len(array)) + "\n")


file.write("Liczba cech: " + str(cols_count) + "\n")
file.write("Liczba przykladow: " + str(row_count) + "\n")
file.write("Liczba niezerowych wartosci cech: " + str(non_zero) + "\n")

file.close()

print("Done")
