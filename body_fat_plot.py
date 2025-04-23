import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("body_fat.csv")

def body_fat_plot():
    plt.plot(df["date"], df["body_fat"])
    plt.title("Body Fat % Over Time")
    plt.xlabel("Date")
    plt.ylabel("Body Fat")
    plt.tight_layout()
    plt.show()

body_fat_plot()