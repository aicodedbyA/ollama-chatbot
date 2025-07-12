import ollama

MODEL_NAME = "pie_Chatbot"  # Replace with your model name from ollama list

def chat():
    print("🤖 Chatbot is ready. Type 'exit' to quit.\n")

    history = []

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        history.append({"role": "user", "content": user_input})
        try:
            print(f"🔄 Sending request to {MODEL_NAME}...")
            response = ollama.chat(
                model=MODEL_NAME,
                messages=history
            )

            assistant_message = response['message']['content']
            print(f"Bot: {assistant_message}\n")

            history.append({"role": "assistant", "content": assistant_message})
        except Exception as e:
            print(f"❌ Error: {e}")
            break


if __name__ == "__main__":
    chat()
