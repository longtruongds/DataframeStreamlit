#!/usr/bin/env python
# coding: utf-8

# In[1]:


# data analysis and wrangling
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# In[2]:


#input_df = pd.read_csv('train_final.csv')
input_df = pd.read_csv('train_FE.csv')


# In[3]:


numeric_df = input_df.select_dtypes(exclude=['object'])


# In[4]:


numeric_df.columns


# In[5]:


drop_cols=['Unnamed: 0']
numeric_df = numeric_df.drop(drop_cols, axis=1)


# In[6]:


numeric_df.columns


# In[7]:


# Kỹ thuật chuyển cột SalePrice thành cột đầu tiên
cols = list(numeric_df)
# move the column to head of list using index, pop and insert
cols.insert(0, cols.pop(cols.index('SalePrice')))
heatmap_df = numeric_df.loc[:, cols]
# plt.figure(figsize=(20, 10))
# sns.heatmap(heatmap_df.corr(), annot=True)


# In[8]:


# Create a heatmap using Seaborn
plt.figure(figsize=(30, 16))  # Set the size of the plot
sns.heatmap(heatmap_df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)

# Assign the plot to the variable fig1
fig1 = plt.gcf()

# Display the plot in Streamlit
st.pyplot(fig1)


# In[9]:


# drop hight correlation column
# Create correlation matrix
corr_matrix = numeric_df.corr().abs()


# In[10]:


# Select upper triangle of correlation matrix
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))


# In[11]:


numeric_df.columns


# In[12]:


to_drop = [column for column in upper.columns if any(upper[column] <0.1)]


# In[13]:


# Drop features 
numeric_df.drop(to_drop, axis=1, inplace=True)


# In[14]:


numeric_df.columns


# In[15]:


numeric_df.head()


# In[16]:


# plt.figure(figsize=(20, 10))
# sns.heatmap(numeric_df.corr(), annot=True)


# In[ ]:





# In[ ]:





# In[ ]:




