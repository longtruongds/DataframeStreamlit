#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.subheader("test")
    st.image("https://static.streamlit.io/examples/dice.jpg")

