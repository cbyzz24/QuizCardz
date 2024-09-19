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
    ("white", "blanco"),
    ("look at or watch tv (watch tv)", "mirar"),
    ("I look at", "yo miro"),
    ("you look at", "tú miras"),
    ("s/he looks at", "ella/él mira"),
    ("you (formal) look at", "usted mira"),
    ("we look at", "nosotros miramos"),
    ("they look at", "ellas/ellos miran"),
    ("yall look at", "ustedes miran"),
    ("to have", "tener"),
    ("I have", "yo tengo"),
    ("you have", "tú tienes"),
    ("s/he has", "ella/él tiene"),
    ("you (formal) have", "Ud. tiene"),
    ("we have", "nosotros tenemos"),
    ("they have", "ellas/ellos tienen"),
    ("yall have", "Uds. tienen"),
    ("to have fear", "tener miedo"),
    ("I have fear", "yo tengo miedo"),
    ("you have fear", "tú tienes miedo"),
    ("s/he has fear", "ella/él tiene miedo"),
    ("you (formal) have fear", "Ud. tiene miedo"),
    ("we have fear", "nosotros tenemos miedo"),
    ("they have fear", "ellas/ellos tienen miedo"),
    ("yall have fear", "Uds. tienen miedo"),
    ("toward", "hacia"),
    ("fear", "miedo"),
    ("of", "de"),
]



question_count = len(questions)

def display_question():
    random_question = randint(0, question_count - 1)
    st.session_state["spanish_question_text"] = questions[random_question][0]
    st.session_state["spanish_answer_text"] = ""  # Clear the answer when showing a new question

def display_answer():
    if "spanish_question_text" in st.session_state:
        spanish_question_text = st.session_state["spanish_question_text"]
        for question, answer in questions:
            if question == spanish_question_text:
                st.session_state["spanish_answer_text"] = answer
                break

if "spanish_question_text" not in st.session_state:
    st.session_state["spanish_question_text"] = ""
if "spanish_answer_text" not in st.session_state:
    st.session_state["spanish_answer_text"] = ""


st.write("### :rainbow[Quiz Cardz] :books:")

with st.container(height=180):
    # header_title = st.columns(3, gap="large")
    # with header_title:
    st.write("###### Question:")
    spanish_question_text = st.write(st.session_state["spanish_question_text"])
    

st.button("Next Question", use_container_width=True, on_click=display_question)

st.button("Answer", use_container_width=True, on_click=display_answer)

with st.container(height=180):
    # header_blank1, header_title, header_blank2 = st.columns(3, gap="large")
    # with header_title:
    st.write("###### Answer:")
    spanish_answer_text = st.write(st.session_state["spanish_answer_text"])
    
    
    
    
# st.write("### :rainbow[Quiz Cardz] :books:")

# blank_space_0 = st.write("")

# with st.container(height=250):
#     header_blank1, header_title, header_blank2 = st.columns(3, gap="large")
#     with header_title:
#         st.write("#### Question:")
#     question_text = st.write(st.session_state["question_text"])

# blank_space_1 = st.write("")
    
# blank1, next_question, answer, blank2 = st.columns(4, gap="large")

# with blank1:
#     st.empty()

# with next_question:
#     st.button("Next Question", on_click=display_question)

# with blank2:
#     st.empty()

# with answer:
#     st.button("Answer", on_click=display_answer)

# blank_space_2 = st.write("")

# with st.container(height=250):
#     header_blank1, header_title, header_blank2 = st.columns(3, gap="large")
#     with header_title:
#         st.write("#### Answer:")
#     answer_text = st.write(st.session_state["answer_text"])
