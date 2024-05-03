#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

st.header('st.button')

if st.button('Stay Hello'):
    # if yes ; meaning button is pressed
    st.write('Why Hello there')
else:
    st.write('Goodbye')


# In[ ]:




