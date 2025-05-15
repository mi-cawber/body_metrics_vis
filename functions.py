# this file contains functions to create plots for all of my different measurements
import matplotlib.pyplot as plt
import pandas as pd

# universal plot function
def data_plot(file, column, title):
    df = pd.read_csv(file)
    plt.plot(df["date"], df[column])
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(column)
    plt.show()

# function to calculate average from any file
def average_calculator(file, column):
    data = pd.read_csv(file)
    total = 0
    for value in data[column]:
        total += value
    avg = total / len(data[column])
    print(avg)