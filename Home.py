import streamlit as st
from random import randint

with st.container(height=150, border=False):
    st.write("")
    
st.write("### Welcome To:")

# with st.container(height=100, border=False):
#     st.write("")

blank1, brand_logo, blank2 = st.columns(3, gap="large")

with blank1:
    st.empty()
with brand_logo:
    st.write("# :rainbow[Quiz Cardz] :books:")
with blank2:
    st.empty()