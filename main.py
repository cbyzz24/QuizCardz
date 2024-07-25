import streamlit as st

st.write("### :rainbow[Quiz Cardz] :books:")

blank_space_0 = st.write("")

with st.container(height=250):
    header_blank1, header_title, header_blank2 = st.columns(3, gap="large")
    with header_blank1:
        st.empty()
    with header_title:
        st.write("#### Question:")
    with header_blank2:
        st.empty()
    st.write("*Sample Question*")

blank_space_1 = st.write("")
    
blank1, next_question, answer, blank2 = st.columns(4, gap="large")

with blank1:
    st.empty()

with next_question:
    st.button("Next Question")

with blank2:
    st.empty()

with answer:
    st.button("Answer")

blank_space_2 = st.write("")

with st.container(height=250):
    header_blank1, header_title, header_blank2 = st.columns(3, gap="large")
    with header_blank1:
        st.empty()
    with header_title:
        st.write("#### Answer:")
    with header_blank2:
        st.empty()
    st.write("*Sample Answer*")




