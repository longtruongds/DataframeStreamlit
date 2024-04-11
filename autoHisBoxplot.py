#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import plotly.express as px
import streamlit as st

# Load your CSV data into a DataFrame
df = pd.read_csv('train.csv')

# Select only numerical columns
numerical_df = df.select_dtypes(include='number')

# Loop through numerical columns and create plots
for col in numerical_df.columns:
    # Create boxplot
    boxplot = px.box(numerical_df, y=col, title=f"Boxplot for {col}")
    
    # Create histogram
    histogram = px.histogram(numerical_df, x=col, title=f"Histogram for {col}")

    # Combine plots (optional)
    combined_plot = boxplot | histogram

    # Display the combined plot in Streamlit
    st.plotly_chart(combined_plot, use_container_width=True)

