import streamlit as st

st.title("Echo Bot")
# Initialize chat history
if "messages" not in st.session_state:#crea la sesión de la app, no hay mensaje crea la sesión nueva
    st.session_state.messages = []
# Display chat messages from history on app rerun - de la fila 7 a la 9 lo que hace es con un for itera la lista que cree en la lista 5, le está diciendo en la 9 "para esos [lista 5] traeme los mensajes"
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
       st.markdown(message["content"])
# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt}) #me trae el history de mensajes del user
    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response}) #me trae el history de mensajes del assistant