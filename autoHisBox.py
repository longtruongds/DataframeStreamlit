#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load your CSV data into a DataFrame
df = pd.read_csv('train.csv')

# Select only numerical columns
numerical_df = df.select_dtypes(include='number')

# # Create a subplot with boxplot and histogram
# fig = go.Figure()

# for col in numerical_df.columns:
#     # Create boxplot
#     boxplot = px.box(numerical_df, y=col, title=f"Boxplot for {col}")
#     fig.add_trace(boxplot.data[0])

#     # Create histogram
#     histogram = px.histogram(numerical_df, x=col, title=f"Histogram for {col}")
#     fig.add_trace(histogram.data[0])

# # Update subplot layout
# fig.update_layout(title="Boxplot and Histogram for Numerical Columns", showlegend=False)

# # Display the combined plot in Streamlit
# st.plotly_chart(fig, use_container_width=True)







# In[ ]:


for col1 in numerical_df.columns:
    # Create a figure with two subplots (boxplot and histogram)
    fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={'height_ratios': (.15, .85)}, figsize=(10, 6))
    # Boxplot
    sns.boxplot(numerical_df[col1], orient='h', ax=ax_box, color='blue')
    # Histogram
    sns.histplot(data=numerical_df, x=col1, ax=ax_hist, color='blue')
    # Remove x-axis label for the boxplot
    ax_box.set(xlabel='')
    # plt.show()    
    #------------------------
    stats_categorical = numerical_df[col1].describe().round(2)

    st.pyplot(fig)


# In[ ]:


# # Create a dictionary to store plots
# plots = {}
# for column in numerical_df.columns:
#     fig, ax = plt.subplots()
#     ax.boxplot(numerical_df[column])
#     ax.set_title(f"Boxplot for {column}")
#     plots[column] = fig

# # Streamlit App
# st.title("Boxplots for Numerical Columns")
# for column, plot in plots.items():
#     st.write(f"## {column}")
#     st.pyplot(plot)

