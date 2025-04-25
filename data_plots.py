# this file contains functions to create plots for all of my different measurements

import matplotlib.pyplot as plt
import pandas as pd

# for calories plot
#def calories_plot():
   # df_calories = pd.read_csv("calories_protein.csv")
    #plt.plot(df_calories["date"], df_calories["calories"])
    #plt.title("Calories Consumed By Date")
    #plt.xlabel("Date")
    #plt.ylabel("Calories")
    #plt.show()

# for body weight plot
def weight_plot():
    df_weight = pd.read_csv("weight.csv")
    plt.plot(df_weight["date"],df_weight["weight"])
    plt.title("Weight Over Time")
    plt.xlabel("Date")
    plt.ylabel("Weight (lbs)")
    plt.show()

# for body fat plot
def body_fat_plot():
    df_body_fat = pd.read_csv("body_fat.csv")
    plt.plot(df_body_fat["date"], df_body_fat["body_fat"])
    plt.title("Body Fat % Over Time")
    plt.xlabel("Date")
    plt.ylabel("Body Fat")
    plt.show()
 
# for muscle mass plot
def muscle_mass_plot():
    df_muscle_mass = pd.read_csv("muscle_mass.csv")
    plt.plot(df_muscle_mass["date"], df_muscle_mass["muscle_mass"])
    plt.title("Muscle Mass % Over Time")
    plt.xlabel("Date")
    plt.ylabel("Muscle Mass")
    plt.show()