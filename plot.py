import streamlit as st
import numpy as np   
from numpy import random
import matplotlib.pyplot as plt 
 
st.title('My First Streamlit App')

N = st.number_input(label='Input some number', min_value=10,   max_value=1000, value=100)  

list_of_nos = []  
for i in range(N):  
    list_of_nos.append(random.rand())

fig, ax = plt.subplots()  
plt.hist(list_of_nos, range=[0,1]) 
st.pyplot(fig) 