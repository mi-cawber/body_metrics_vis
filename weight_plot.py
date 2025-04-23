import pandas as pd
import matplotlib.pyplot as plt
# create dataframe using my weight csv
df = pd.read_csv("weight.csv")

x = df["Date"]
y = df["Weight"]

def weight_plot():
    plt.plot(x,y)
    plt.title("Weight Over Time")
    plt.xlabel("Date")
    plt.ylabel("Weight (lbs)")
    plt.show()