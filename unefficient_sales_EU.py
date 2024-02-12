import numpy as np
import pandas as pd
import time

# Start time
start_time = time.time()

# Video games sales percentage for a specific region in the dataset
def calc_sales_percentage(sales_region, global_sales):
   sales_percentage = sales_region / global_sales
   return np.round(sales_percentage, 2)

sales_perc = calc_sales_percentage(1000, 10000)
# print(sales_perc)

#  Convert the datase to pandas dataframe
video_games_sales_df = pd.read_csv('vgsales.csv')
# print(video_games_sales_df.head())

# Create a new column in the dataset to store the percentage of sales for each video game based on EU_Sales
sales_perc_list = []
for i in range(len(video_games_sales_df)):
#    look each individual row in the dataset
   row = video_games_sales_df.iloc[i]
   eu_sales = row['EU_Sales']
   global_sales = row['Global_Sales']
   sales_perc = calc_sales_percentage(eu_sales, global_sales)
   sales_perc_list.append(sales_perc)
video_games_sales_df['Sales_Perc_EU'] = sales_perc_list

print(video_games_sales_df.head(15))

# End time
end_time = time.time()
# Calculate the execution time
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")