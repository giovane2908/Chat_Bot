import streamlit as st
import chat_bot

st.title("🤖 Chatbot")

# Inicializa o histórico do chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
prompt = st.chat_input("Digite sua mensagem aqui...")
if prompt:
    # Adiciona a mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Exibe a mensagem do usuário
    with st.chat_message("user"):
        st.markdown(prompt)

    # Obtém e exibe a resposta do chatbot
    resposta = chat_bot.enviar_mensagem(prompt)
    with st.chat_message("assistant"):
        st.markdown(resposta)

    # Adiciona a resposta ao histórico
    st.session_state.messages.append({"role": "assistant", "content": resposta})

# Botão para encerrar o chatbot
if st.button("Encerrar Chat"):
    st.session_state.messages = []
    st.success("Chat encerrado. Recarregue a página para iniciar uma nova conversa.")
