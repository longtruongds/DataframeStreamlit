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

# Create a heatmap using Seaborn
plt.figure(figsize=(20, 16))  # Set the size of the plot
sns.heatmap(numerical_df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)

# Assign the plot to the variable fig1
fig1 = plt.gcf()

# Display the plot in Streamlit
st.pyplot(fig1)

