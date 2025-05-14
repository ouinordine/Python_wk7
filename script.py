import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO

# Use the my_novels dataset
csv_data = """adventure,romance,comedy
1000 leagues under the sea,blossoms of the savannah,hekaya za abunwasi
mitchell and the machines,river and the source,mr bean
"""
csv_file = StringIO(csv_data)
df = pd.read_csv(csv_file)

# Add some numerical data, as the original dataset is entirely categorical
df['adventure_sales'] = [150, 200, 175]
df['romance_sales'] = [100, 120, 110]
df['comedy_sales'] = [80, 90, 85]
df['year'] = [2020, 2021, 2022]

# Task 1: Load and Explore the Dataset
# 1.  Load the dataset using pandas.
#     Save the dataset to a CSV file named "my_novels.csv"
df.to_csv("my_novels.csv", index=False)  # index=False prevents writing the DataFrame index to the CSV
print("Dataset saved to my_novels.csv")


# 2.  Display the first few rows of the dataset using .head() to inspect the data.
print("First 5 rows of the dataset:")
print(df.head())

# 3.  Explore the structure of the dataset by checking the data types and any missing values.
print("\nDataset information:")
df.info()

print("\nMissing values per column:")
print(df.isnull().sum())

# 4.  Clean the dataset by either filling or dropping any missing values.
#     There are no missing values in this dataset, so no cleaning is needed.


# Task 2: Basic Data Analysis
# 1.  Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using .describe().
print("\nBasic statistics of numerical columns:")
print(df.describe())

# 2.  Perform groupings on a categorical column and compute the mean of a numerical column for each group.
print("\nAverage sales amount per adventure category:")
print(df.groupby('adventure')['adventure_sales'].mean())

print("\nAverage sales amount per romance category:")
print(df.groupby('romance')['romance_sales'].mean())

print("\nAverage sales amount per comedy category:")
print(df.groupby('comedy')['comedy_sales'].mean())


# 3.  Identify any patterns or interesting findings from your analysis.
print("\nPatterns and Interesting Findings:")
print("The describe() output shows the distribution of sales amounts across the added numerical columns.")
print("The groupby output shows the average sales amount for each item within the adventure, romance, and comedy categories.")
print("This allows us to compare which items in each category performed better in terms of sales.")


# Task 3: Data Visualization
# 1. Create at least four different types of visualizations:

# a) Line chart showing trends over time (e.g., time-series of sales data).
plt.figure(figsize=(10, 6))
plt.plot(df['year'], df['adventure_sales'], marker='o', label='Adventure Sales')
plt.plot(df['year'], df['romance_sales'], marker='o', label='Romance Sales')
plt.plot(df['year'], df['comedy_sales'], marker='o', label='Comedy Sales')
plt.title('Sales Trends Over Time')
plt.xlabel('Year')
plt.ylabel('Sales (in thousands)')
plt.legend()
plt.grid(True)
plt.show()

# b) Bar chart showing the comparison of a numerical value across categories (e.g., average sales per category).
plt.figure(figsize=(10, 6))
plt.bar(['Adventure', 'Romance', 'Comedy'], [df['adventure_sales'].mean(), df['romance_sales'].mean(), df['comedy_sales'].mean()])
plt.title('Average Sales Amount per Category')
plt.xlabel('Category')
plt.ylabel('Average Sales Amount (in thousands)')
plt.grid(True)
plt.show()


# c) Histogram of a numerical column to understand its distribution.
plt.figure(figsize=(10, 6))
plt.hist(df['adventure_sales'], bins=3, alpha=0.7, color='skyblue')  # Adjust bins as needed.  Using 3 since we have only 3 data points.
plt.title('Distribution of Adventure Sales')
plt.xlabel('Sales (in thousands)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# d) Scatter plot to visualize the relationship between two numerical columns
plt.figure(figsize=(10, 6))
plt.scatter(df['adventure_sales'], df['romance_sales'], color='salmon')
plt.title('Relationship between Adventure and Romance Sales')
plt.xlabel('Adventure Sales (in thousands)')
plt.ylabel('Romance Sales (in thousands)')
plt.grid(True)
plt.show()