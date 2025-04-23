import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("muscle_mass.csv")

def muscle_mass_plot():
    plt.plot(df["date"], df["muscle_mass"])
    plt.title("Muscle Mass % Over Time")
    plt.xlabel("Date")
    plt.ylabel("Muscle Mass")
    plt.show()

muscle_mass_plot()