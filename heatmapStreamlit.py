#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

# Load CSV data into a pandas DataFrame
@st.cache
def load_data():
    df = pd.read_csv("train.csv")  # Replace with your actual CSV file path
    return df

data = load_data()

# Separate numerical and categorical columns
numerical_df = data.select_dtypes(include=["float64", "int64"])
categorical_df = data.select_dtypes(include=["object"])

# Create a heatmap using Seaborn
st.write("Heatmap of Correlation Matrix:")
corr_matrix = numerical_df.corr()
plt.figure(figsize=(10, 8))
# sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
# st.pyplot()
fig1 = sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
st.pyplot(fig1)

# Display the DataFrames
st.write("Numerical DataFrame:")
st.dataframe(numerical_df)

st.write("Categorical DataFrame:")
st.dataframe(categorical_df)

