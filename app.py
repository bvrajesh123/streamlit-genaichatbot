import streamlit as st
from chatbot import (
    openai_chatbot_response,
    gemini_chatbot_response
)

# Page Config
st.set_page_config(
    page_title="Memory Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Memory Based AI Chatbot")

# Sidebar
with st.sidebar:
    st.header("Settings")

    model_choice = st.selectbox(
        "Choose Model",
        ["OpenAI", "Gemini"]
    )

    if st.button("Clear Memory"):
        st.session_state.messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            }
        ]
        st.rerun()

# Initialize Memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        }
    ]

# Display Chat History
for message in st.session_state.messages:

    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
user_input = st.chat_input("Ask me anything...")

if user_input:

    # Add User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            if model_choice == "OpenAI":
                response = openai_chatbot_response(
                    st.session_state.messages
                )

            else:
                response = gemini_chatbot_response(
                    st.session_state.messages
                )

            st.markdown(response)

    # Save Assistant Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )