import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("calories_protein.csv")

def calories_plot():
    plt.plot(df["date"], df["calories"])
    plt.title("Calories Consumed By Date")
    plt.xlabel("Date")
    plt.ylabel("Calories")
    plt.show()

calories_plot()