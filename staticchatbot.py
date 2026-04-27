import streamlit as st
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi! How can I help you?"
    elif "your name" in user_input:
        return "I am a simple chatbot."
    elif "course" in user_input:
        return "We offer AI, Web Development, and Data Science courses."
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."
st.title("Simple Chatbot")
user_input = st.text_input("You:")
if st.button("Send"):
    if user_input:
        response = chatbot_response(user_input)
        st.text_area("Bot:", value=response, height=100)