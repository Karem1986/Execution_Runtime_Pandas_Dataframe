# Testing if using .iterrows() is fasten than using iloc
import numpy as np
import pandas as pd
import time

# Start time
start_time = time.time()

#  Convert the datase to pandas dataframe
video_games_sales_df = pd.read_csv('vgsales.csv')
# print(video_games_sales_df.head())

# Calculat total global sales for all games:
total_global_sales = video_games_sales_df['Global_Sales'].sum()

# Function to calculate the percentage of Global Sales for each record in the dataset
def calc_sales_percentage(global_sales):
   sales_percentage = global_sales / total_global_sales * 100
   return np.round(sales_percentage, 2)

sales_perc = calc_sales_percentage(82.74)
print(sales_perc)

# Add Total_Global_Sales to the df
video_games_sales_df['Total_Global_Sales'] = video_games_sales_df['Global_Sales'].sum()
print(video_games_sales_df.head())

# # Create a new column in the dataset to store the percentage of sales for each video game based on EU_Sales
sales_perc_list = []
for i, row in video_games_sales_df.iterrows():
# using the index of each row as the first element and the data in each row as the second element of the returned object which is a tuple
   global_sales = row['Global_Sales']
   sales_perc = calc_sales_percentage(global_sales)
   sales_perc_list.append(sales_perc)
video_games_sales_df['Sales_Percentage'] = sales_perc_list

# print(video_games_sales_df.head(10))

# End time
end_time = time.time()
# Calculate the execution time
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")

# RESULTS: execution time is significantly much lower than using iloc: 32 seconds vs 42 seconds. 
