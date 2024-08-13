import streamlit as st

import streamlit as st
from random import randint

questions = spanish_vocabulary_quiz = spanish_vocabulary_quiz = [
    ("house", "casa"),
    ("water", "agua"),
    ("food", "comida"),
    ("school", "escuela"),
    ("car", "coche"),
    ("book", "libro"),
    ("dog", "perro"),
    ("cat", "gato"),
    ("sun", "sol"),
    ("moon", "luna"),
    ("star", "estrella"),
    ("tree", "árbol"),
    ("flower", "flor"),
    ("bird", "pájaro"),
    ("friend", "amigo"),
    ("family", "familia"),
    ("child", "niño"),
    ("baby", "bebé"),
    ("man", "hombre"),
    ("woman", "mujer"),
    ("brother", "hermano"),
    ("sister", "hermana"),
    ("father", "padre"),
    ("mother", "madre"),
    ("day", "día"),
    ("night", "noche"),
    ("morning", "mañana"),
    ("afternoon", "tarde"),
    ("evening", "noche"),
    ("week", "semana"),
    ("month", "mes"),
    ("year", "año"),
    ("time", "tiempo"),
    ("door", "puerta"),
    ("window", "ventana"),
    ("table", "mesa"),
    ("chair", "silla"),
    ("bed", "cama"),
    ("kitchen", "cocina"),
    ("bathroom", "baño"),
    ("shirt", "camisa"),
    ("pants", "pantalones"),
    ("shoes", "zapatos"),
    ("hat", "sombrero"),
    ("red", "rojo"),
    ("blue", "azul"),
    ("green", "verde"),
    ("black", "negro"),
    ("white", "blanco")
]



question_count = len(questions)

def display_question():
    random_question = randint(0, question_count - 1)
    st.session_state["question_text"] = questions[random_question][0]
    st.session_state["answer_text"] = ""  # Clear the answer when showing a new question

def display_answer():
    if "question_text" in st.session_state:
        question_text = st.session_state["question_text"]
        for question, answer in questions:
            if question == question_text:
                st.session_state["answer_text"] = answer
                break

if "question_text" not in st.session_state:
    st.session_state["question_text"] = ""
if "answer_text" not in st.session_state:
    st.session_state["answer_text"] = ""

st.write("### :rainbow[Quiz Cardz] :books:")

blank_space_0 = st.write("")

with st.container(height=250):
    header_blank1, header_title, header_blank2 = st.columns(3, gap="large")
    with header_title:
        st.write("#### Question:")
    question_text = st.write(st.session_state["question_text"])

blank_space_1 = st.write("")
    
blank1, next_question, answer, blank2 = st.columns(4, gap="large")

with blank1:
    st.empty()

with next_question:
    st.button("Next Question", on_click=display_question)

with blank2:
    st.empty()

with answer:
    st.button("Answer", on_click=display_answer)

blank_space_2 = st.write("")

with st.container(height=250):
    header_blank1, header_title, header_blank2 = st.columns(3, gap="large")
    with header_title:
        st.write("#### Answer:")
    answer_text = st.write(st.session_state["answer_text"])
