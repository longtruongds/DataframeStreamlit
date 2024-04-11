#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import streamlit as st

# Load CSV data into a DataFrame
csv_file_path = "train.csv"
df = pd.read_csv(csv_file_path)

# Create a Streamlit app
st.title("CSV Data Display")
st.write("Here's the loaded data from the CSV file:")

# Display the DataFrame
st.dataframe(df)

# You can also use st.table(df) for a tabular view

