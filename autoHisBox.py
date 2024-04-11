#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# Load your CSV data into a DataFrame
df = pd.read_csv('train.csv')

# Select only numerical columns
numerical_df = df.select_dtypes(include='number')

# Create a subplot with boxplot and histogram
fig = go.Figure()

for col in numerical_df.columns:
    # Create boxplot
    boxplot = px.box(numerical_df, y=col, title=f"Boxplot for {col}")
    fig.add_trace(boxplot.data[0])

    # Create histogram
    histogram = px.histogram(numerical_df, x=col, title=f"Histogram for {col}")
    fig.add_trace(histogram.data[0])

# Update subplot layout
fig.update_layout(title="Boxplot and Histogram for Numerical Columns", showlegend=False)

# Display the combined plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

