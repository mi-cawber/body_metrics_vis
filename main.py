import matplotlib.pyplot as plt

#establish chronological dates for measurements
dates = ["2/03/25", "2/09/25", "2/16/25", "2/23/25", "3/02/25", "3/09/25", "3/16/25", 
               "3/23/25", "3/30/25", "4/06/25", "4/13/25", "4/20/25"]

#create some data, 1D arrays
weight = [171.6, 168.3, 166.8, 164.4, 166.1, 163.5, 163.7, 162.0, 161.6, 158.7, 163.8, 159.2]
muscle_mass = [71.7, 72.3, 72.5, 73.1, 72.7, 73.3, 73.2, 73.5, 73.6, 74.2, 73.2, 74.2]
bodyfat = [24.5, 23.8, 23.5, 22.9, 23.3, 22.8, 22.8, 22.4, 22.3, 21.7, 22.8, 21.8]

# a function to plot graphs
#fmtfor pyplot = "[marker][line][color]"
def make_plot(x, y, title, fmt = "-g", xlabel = "Date", ylabel = " "):
    plt.plot(x, y, fmt)
    plt.title(title)
    plt.show()


make_plot(dates, weight, "Weight")