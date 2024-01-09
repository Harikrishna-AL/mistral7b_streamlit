import streamlit as st
import requests
from streamlit_chat import message


def chat_ui(prompt,response):
    
    message(response)

class Mistral7BChat:
    def __init__(self):
        self.api_endpoint = "https://harikrishna-al--mistral-inference-model-generate-dev.modal.run"
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}
        # self.chat_history = []

    def query_mistral_7b(self, input_text, context="You were developed by mistral jsut to write taglines for products"):
        form_data = {
            "prompt": input_text,
            "context": context
            }
    
        response = requests.post(self.api_endpoint, data=form_data, headers=self.headers)

        if response.status_code == 200:
            output_text = response.json()["output_text"]
            # self.chat_history.append({"user": input_text, "mistral_7b": output_text})
            return output_text
        else:
            return f"Error: {response.status_code} - {response.text}"

def main():
    st.title("Mistral 7B Chat Interface")

    chatbot = Mistral7BChat()

    # Display chat history
    # for chat_entry in chatbot.chat_history:
    #     if chat_entry["user"]:
    #         st.text(f"You: {chat_entry['user']}")
    #     if chat_entry["mistral_7b"]:
    #         st.text(f"Mistral 7B: {chat_entry['mistral_7b']}")

    # Get user input
    # user_input = st.text_input("Enter your message:")
    user_input = st.chat_input("Enter your message:")
    if user_input is not None:
        message(user_input, is_user=True)

    if user_input:
        response_text = chatbot.query_mistral_7b(user_input)
        message(response_text)


if __name__ == "__main__":
    main()
