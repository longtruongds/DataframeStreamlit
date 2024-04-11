#!/usr/bin/env python
# coding: utf-8

# In[1]:


# data analysis and wrangling
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


input_df = pd.read_csv('train_FE.csv')
numeric_df = input_df.select_dtypes(exclude=['object'])
# numeric_df.columns
drop_cols=['Unnamed: 0']
numeric_df = numeric_df.drop(drop_cols, axis=1)
# numeric_df.columns

# Kỹ thuật chuyển cột SalePrice thành cột đầu tiên
cols = list(numeric_df)
# move the column to head of list using index, pop and insert
cols.insert(0, cols.pop(cols.index('SalePrice')))
heatmap_df = numeric_df.loc[:, cols]



# Create a heatmap using Seaborn
plt.figure(figsize=(40, 16))  # Set the size of the plot
sns.heatmap(heatmap_df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)

# Assign the plot to the variable fig1
fig1 = plt.gcf()

# Display the plot in Streamlit
st.pyplot(fig1)
