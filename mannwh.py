# (C) Iikka Pietilä, +358407296709, iikka.pietila@tuni.fi
# Simple Mann-Whitney-U calculator for multiple dichotomous variables
# Requires Scipy, Numpy and CSV

import scipy
import numpy
import csv
import sys

from numpy import mean
from numpy import median
from numpy import std
from scipy.stats import mannwhitneyu

# Check that numpy and scipy has loaded okay and print their versions
print ("Python version", sys.version)
print ("numpy version", numpy.__version__, "ok")
print ("scipy version", scipy.__version__, "ok")
print()

# Initialize an empty list for data to be loaded to
# Open csv and read it's data
rows_list = []
with open("dichos_for_mannwu.csv") as data_main:
    linereader = csv.reader(data_main, delimiter = " ", quotechar = "|")
    for line in linereader:
        rows_list.append(line)

# Read lines from linereader to a list called main_list for later working
main_list = []
for line in rows_list:
    for item in line:
        item = item.split(";")
        main_list.append(item)

# Make a list for variables
variables = []
for item in main_list[0]:
    variables.append(item)

# Initialize a variable to count loop rounds
column_index = int(0)

# Start a loop to go through all game genres
for column_index in range (len(main_list[0]) - 5):

    # Initialize lists for variables A, B, and E
    # A = Sum variable Social Participation
    # B = Sum variable Digital Social Participation
    # E = Societal Participation
    sum_a_yes = []
    sum_a_no = []

    sum_b_yes = []
    sum_b_no = []

    sum_e_yes = []
    sum_e_no = []

    # Start a loop to go through each observational unit line by line
    for line in main_list:
        n = 0

        # Divide the values of each sum variable into two classes according to
        # the value of n'th dichotomical variable (Gaming genre)
        # Add the according values to the lists
        try:
            if float(line[column_index]) == 0 and line[13] != "empty":
                sum_a_no.append(float(line[13]))
            if float(line[column_index]) == 1 and line[13] != "empty":
                sum_a_yes.append(float(line[13]))


            if float(line[column_index]) == 0 and line[14] != "empty":
                sum_b_no.append(float(line[14]))
            if float(line[column_index]) == 1 and line[14] != "empty":
                sum_b_yes.append(float(line[14]))


            if float(line[column_index]) == 0 and line[17] != "empty":
                sum_e_no.append(float(line[17]))
            if float(line[column_index]) == 1 and line[17] != "empty":
                sum_e_yes.append(float(line[17]))

        except ValueError:
            n = n + 1
            continue

    # Print the statistics of sum variable on each loop accordingly

    print()
    print("*****", main_list[0][column_index])

    stat, p = mannwhitneyu(sum_a_no, sum_a_yes, alternative="two-sided")
    if p < 0.05:
        print("Sum A Social participation")
        print("sum_a_no: mean = %.2f, median = %.2f, stdv = %.2f, len = %.0f" % (mean(sum_a_no), median(sum_a_no), std(sum_a_no), len(sum_a_no)))
        print("sum_a_yes: mean = %.2f, median = %.2f, stdv = %.2f, len = %.0f" % (mean(sum_a_yes), median(sum_a_yes), std(sum_a_yes), len(sum_a_yes)))
        print("#### Statistics = %.2f, p = %.2f" % (stat, p))
        print()


    stat, p = mannwhitneyu(sum_b_no, sum_b_yes, alternative="two-sided")
    if p < 0.05:
        print("Sum B Digital Social participation")
        print("sum_b_no: mean = %.2f, median = %.2f, stdv = %.2f, len = %.0f" % (mean(sum_b_no), median(sum_b_no), std(sum_b_no), len(sum_b_no)))
        print("sum_b_yes: mean = %.2f, median = %.2f, stdv = %.2f, len = %.0f" % (mean(sum_b_yes), median(sum_b_yes), std(sum_b_yes), len(sum_b_yes)))
        print("#### Statistics = %.2f, p = %.2f" % (stat, p))
        print()

    stat, p = mannwhitneyu(sum_e_no, sum_e_yes, alternative="two-sided")
    if p < 0.05:
        print("Sum E Societal participation")
        print("sum_e_no: mean = %.2f, median = %.2f, stdv = %.2f, len = %.0f" % (mean(sum_e_no), median(sum_e_no), std(sum_e_no), len(sum_e_no)))
        print("sum_e_yes: mean = %.2f, median = %.2f, stdv = %.2f, len = %.0f" % (mean(sum_e_yes), median(sum_e_yes), std(sum_e_yes), len(sum_e_yes)))
        print("#### Statistics = %.2f, p = %.2f" % (stat, p))


    print()
    print("****** END OF", main_list[0][column_index])
    print("-------------------------------------------")
    print()

    # Add one to the loop counter
    column_index += 1

print()
print("end")