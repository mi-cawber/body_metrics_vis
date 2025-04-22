# Import the pandas library - pandas is widely used for data manipulation and analysis
# We'll use it to easily read, process, and analyze our CSV data
import pandas as pd

def read_calorie_tracker_pandas(filename):
    """
    Read a calorie tracking CSV file and convert it to a pandas DataFrame.
    A DataFrame is like a table or spreadsheet in Python that makes data manipulation easy.
    
    Parameters:
    filename (str): The name of the CSV file to read
    
    Returns:
    pandas.DataFrame: A DataFrame containing the calorie tracking data
    """
    
    # Read the CSV file into a pandas DataFrame
    # parse_dates=['Date'] - This tells pandas to convert the 'Date' column to datetime objects
    # This allows us to do date-based operations later (like filtering by month/year)
    # dtype parameter specifies the data type for each column
    df = pd.read_csv(filename, 
                    parse_dates=['Date'],  # Convert the Date column to datetime objects
                    dtype={'Calories': int, 'Protein': int})  # Ensure these columns are integers
    
    # Clean up column names by removing any whitespace
    # This is a good practice to avoid issues with inconsistent spacing
    df.columns = df.columns.str.strip()
    
    # Return the processed DataFrame
    return df

# Example of how to use the function
# Replace 'calorie_tracker.csv' with your actual filename
df = read_calorie_tracker_pandas('calorie_tracker.csv')

# Print the first 5 rows of the DataFrame to check the data was loaded correctly
# .head() is a common way to preview DataFrame contents
print("Preview of the data:")
print(df.head())

# Example: Calculate total calories for all entries
# The .sum() function adds up all values in the specified column
total_calories = df['Calories'].sum()
print(f"Total calories recorded: {total_calories}")

# Example: Calculate average protein intake
# The .mean() function calculates the average of all values in the column
avg_protein = df['Protein'].mean()
print(f"Average protein intake: {avg_protein:.1f}g")

# Example: Filter data for a specific date
# This creates a new DataFrame containing only rows where the Date matches our criteria
specific_date = '2025-02-02'
day_data = df[df['Date'] == specific_date]
print(f"\nEntries for {specific_date}:")
print(day_data)

# Example: Group by date and calculate daily totals
# This is useful if you have multiple entries per day
# groupby() combines rows with the same date
# agg() applies the specified functions to each column in the grouped data
daily_totals = df.groupby('Date').agg({
    'Calories': 'sum',  # Sum calories for each date
    'Protein': 'sum'    # Sum protein for each date
})
print("\nDaily totals:")
print(daily_totals)