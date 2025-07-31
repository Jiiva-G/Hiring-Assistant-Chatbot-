    
import streamlit as st
import openai
import os


# Set your OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY", "your-openai-api-key")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "step" not in st.session_state:
    st.session_state.step = 0

if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {}

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Title
st.title("🤖 Hiring Assistant Chatbot")
st.markdown("Welcome! I'm here to assist with your initial interview screening.\n\nType 'exit' or 'bye' anytime to end the chat.")

# GPT Call Function (Updated for openai>=1.0.0)
def ask_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a technical recruiter assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# Input Handler Function
def handle_user_input():
    user_input = st.session_state.user_input

    # Display user message
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Exit command
    if user_input.lower() in ["exit", "quit", "bye", "thank you"]:
        bot_reply = "Thank you for your time! We'll be in touch soon. 👋"
        st.session_state.chat_history.append(("assistant", bot_reply))
        with st.chat_message("assistant"):
            st.markdown(bot_reply)
        st.session_state.user_input = ""
        st.stop()

    # Form questions
    questions = ["First Name","Name", "Email", "Phone", "Years of Experience", "Desired Position(s)", "Tech Stack", "Current Location"]

    if st.session_state.step < len(questions):
        key = questions[st.session_state.step]
        st.session_state.candidate_data[key] = user_input
        st.session_state.step += 1

        if st.session_state.step < len(questions):
            next_key = questions[st.session_state.step]
            bot_reply = f"Please provide your {next_key}:"
        else:
            tech_stack = st.session_state.candidate_data.get("Tech Stack", "")
            bot_reply = ask_gpt(f"Generate 3 technical interview questions for each of the following tech stack items: {tech_stack}")
    else:
        bot_reply = ask_gpt(user_input)

    # Display assistant reply
    st.session_state.chat_history.append(("assistant", bot_reply))
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    # Clear input
    st.session_state.user_input = ""

# Input box with handler
st.text_input("Type your message and press Enter:", key="user_input", on_change=handle_user_input)

# Display chat history
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(message)
