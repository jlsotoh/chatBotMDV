import backend
import streamlit as st
from streamlit_chat import message

st.markdown(
    """
 <header style='padding:20px 0;background-color: #072146;color: #fff;'> <div style='width: 600px; margin: 0 auto;'><img src='https://ideeo.mx/bbva/chatbot/img/logoBBVA.png' style='width: 120px;'></div></header>
""",
    unsafe_allow_html=True,
)

st.html(
    "<div style='display: flex; justify-content: space-between;'><div><h1>Chat Modelo de Ventas</h1><span>Puedes realizarme preguntas relacionadas a los materiales existentes</span></div><div><img width='130' src='https://ideeo.mx/bbva/chatbot/img/chat.png'></div></div>"
)

if "preguntas" not in st.session_state:
    st.session_state.preguntas = []
if "respuestas" not in st.session_state:
    st.session_state.respuestas = []


def click():
    if st.session_state.user != "":
        pregunta = st.session_state.user
        respuesta = backend.consulta(pregunta)

        st.session_state.preguntas.append(pregunta)
        st.session_state.respuestas.append(respuesta)

        # Limpiar el input de usuario después de enviar la pregunta
        st.session_state.user = ""


with st.form("my-form"):
    query = st.text_input(
        "¿En qué te puedo ayudar?",
        key="user",
        help="Pulsa Enviar para hacer la pregunta",
    )
    submit_button = st.form_submit_button("Enviar", on_click=click)

if st.session_state.preguntas:
    for i in range(len(st.session_state.respuestas) - 1, -1, -1):
        message(st.session_state.respuestas[i], key=str(i))

    # Opción para continuar la conversación
    continuar_conversacion = st.checkbox("Quieres hacer otra pregunta?")
    if not continuar_conversacion:
        st.session_state.preguntas = []
        st.session_state.respuestas = []
