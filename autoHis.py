#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import plotly.express as px
import streamlit as st

# Load CSV data into a Pandas DataFrame
df = pd.read_csv('train.csv')

# Select only the numerical columns from the main DataFrame
numerical_df = df.select_dtypes(include=["float64", "int64"])

# Create a histogram chart for each numerical column
for column in numerical_df.columns:
    fig = px.histogram(numerical_df, x=column, title=f"{column} Distribution")
    st.plotly_chart(fig, use_container_width=True)

