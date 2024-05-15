# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'path_to_file' with the actual path where you saved the CSV file)
path_to_file = '/content/SampleSuperstore.csv'
data = pd.read_csv(path_to_file)

# Display the first few rows of the dataset
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Get summary statistics of numerical columns
print(data.describe())

# Visualize the distribution of numerical columns
sns.pairplot(data)
plt.show()

# Explore categorical variables
plt.figure(figsize=(10, 6))
sns.countplot(x='Category', data=data)
plt.title('Count of Products by Category')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Sub-Category', data=data)
plt.title('Count of Products by Sub-Category')
plt.xticks(rotation=90)
plt.show()

# Analyze profit by different categories
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Profit', data=data)
plt.title('Profit by Category')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='Sub-Category', y='Profit', data=data)
plt.title('Profit by Sub-Category')
plt.xticks(rotation=90)
plt.show()

# Identify weak areas for improvement
weak_areas = data.groupby(['Category', 'Sub-Category'])['Profit'].sum().sort_values().head(10)
print("Weak areas for improvement based on low profits:")
print(weak_areas)
