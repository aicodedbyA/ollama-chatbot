import streamlit as st
import ollama
import os
import datetime

log_dir = "Logs"
os.makedirs(log_dir, exist_ok=True)


MODEL_NAME = "pie_Chatbot"

st.set_page_config(page_title="🧠 Company Chatbot", layout="centered")

st.title("🤖 Company Knowledge Chatbot")
st.markdown("Ask anything related to internal projects, HR, or teams.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box
user_input = st.chat_input("Ask me something...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Send to Ollama
    with st.spinner("Generating response..."):
        try:
            response = ollama.chat(
                model=MODEL_NAME,
                messages=st.session_state.messages
            )
            assistant_reply = response['message']['content']

        except Exception as e:
            assistant_reply = f"❌ Error: {e}"

    # Display bot reply
    st.chat_message("assistant").markdown(assistant_reply)
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

#Logging the users history------>
def save_chat_log():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"chat_log_{timestamp}.txt"
    filepath = os.path.join("Logs", filename)

    with open(filepath, "w") as f:
        for msg in st.session_state.messages:
            role = msg["role"].capitalize()
            f.write(f"{role}: {msg['content']}\n\n")

    print(f"✅ Chat log saved to {filepath}")

if st.button("💾 End Chat & Save Log"):
    save_chat_log()
    st.success("Chat log saved!")


