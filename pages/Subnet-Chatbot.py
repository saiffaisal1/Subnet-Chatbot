import streamlit as st
import random
import time
import shelve

st.title("Subnetting Chatbot")


def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])


# Save chat history to shelve file
def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages


# Sidebar with a button to delete chat history
with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state.messages = []
        save_chat_history([])
    if st.button("Save Chat History"):
        save_chat_history(st.session_state.messages)


# Loads the chat history after app rerun
if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Streamed response emulator
def response_generator():
    if prompt=="hi" or prompt=="hello":
        response = random.choice(
            [
                "Hello there! How can I assist you today?",
                "Hi, human! Is there anything I can help you with?",
                "Do you need help?",
            ]
        )    
        for word in response.split():
            yield word + " "
            time.sleep(0.05)

    if prompt=="What is Subnetting?":
        response1 = "IDK, KYS and git gud"    
        for word in response1.split():
            yield word + " "
            time.sleep(0.05)

    if prompt=="Explain FLSM and VLSM?":    
        response2 = "Sure, sike KYS and git gud" 
        for word in response2.split():
            yield word + " "
            time.sleep(0.05)
            
    if prompt=="Bye":
        response3= "Fuck outta here!"
        for word in response3.split():
            yield word + " "
            time.sleep(0.05)

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
 # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

