import sys
import openai


# Set up your OpenAI API key
openai.api_key = "<API_KEY>"
bot_bahviour = "You are a little princess that answer any question"
#bot_bahviour = "You are a angry bot that comlplain about everything"

# Define a function to generate chat responses
def generate_chat_response(prompt, history):
    messages = history + [
        {"role": "system", "content": bot_bahviour},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
            )
    return response['choices'][0]['message']['content']

# Define a function to prompt the user for input and generate a response
def chat_with_gpt(user_input=None):
    history = []
    while True:
        if user_input:
            prompt = user_input
            user_input = None
        else:
            prompt = input("\nYou: ")
        if prompt.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        chatbot_response = generate_chat_response(prompt, history)
        history.append({"role": "user", "content": prompt})
        history.append({"role": "assistant", "content": chatbot_response})
        print(f"\nChatbot: {chatbot_response}")
        if user_input is None:
            continue
        else:
            return chatbot_response

if len(sys.argv) == 2:
    user_input = sys.argv[1]
    history = []
    result = generate_chat_response(user_input, history)
    print(result)
    sys.exit()
else:
    chat_with_gpt()
