#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

# Load your CSV data into a DataFrame
df = pd.read_csv('train.csv')

# Select only numerical columns
numerical_df = df.select_dtypes(include='number')

st.title('auto Exploratory Data Analysis')
st.set_page_config(page_title="Superstore!!!", page_icon=":bar_chart:",layout="wide")

for col1 in numerical_df.columns:
    # Create a figure with two subplots (boxplot and histogram)
    fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={'height_ratios': (.15, .85)}, figsize=(10, 6))
    # Boxplot
    sns.boxplot(numerical_df[col1], orient='h', ax=ax_box, color='blue')
    # Histogram
    sns.histplot(data=numerical_df, x=col1, ax=ax_hist, color='blue')
    # Remove x-axis label for the boxplot
    ax_box.set(xlabel='')
    
    # st.write('Statistic describle for ' + str(col1) + " :")
    st.subheader('Statistic describle for ' + str(col1) + " :")

    stats_categorical = numerical_df[col1].describe().round(2)
    stats_categorical

    # st.write('Data visualization for ' + str(col1) + " :")
    st.subheader('Data visualization for ' + str(col1) + " :")
    st.pyplot(fig, use_container_width=True)
    st.divider()

