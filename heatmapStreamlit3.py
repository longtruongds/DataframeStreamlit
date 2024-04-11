#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load CSV data into a DataFrame
csv_file_path = "train.csv"
df = pd.read_csv(csv_file_path)

# Select numerical columns
numerical_df = df.select_dtypes(include=["float64", "int64"])





# Separate features and target columns
target_column = numerical_df["SalePrice"]
feature_columns = df.columns[df.columns != target_column]

# Calculate correlation between features and target
correlation_matrix = numerical_df.corr()
target_correlations = correlation_matrix[target_column].abs().sort_values(ascending=False)

# Select top 10 features with highest absolute correlation
n = 10
top_features = target_correlations.index[1:n+1]  # Exclude the target column itself

# Create a new DataFrame with only the selected features
selected_df = numerical_df[top_features]

# Create a heatmap using Seaborn
plt.figure(figsize=(30, 16))  # Set the size of the plot
sns.heatmap(selected_df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)

# Assign the plot to the variable fig1
fig1 = plt.gcf()

# Display the plot in Streamlit
st.pyplot(fig1)

