import os
from openai import OpenAI

# Initialize the client (API key must be set in environment variable OPENAI_API_KEY)
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://api.deepseek.com"
)

# Start with the system message (defines assistant behavior)
messages = [
    {"role": "system", "content": "You are a helpful assistant"}
]

print("Interactive session with DeepSeek started. Type 'quit' or 'exit' to stop.\n")

while True:
    # Get user input
    user_input = input("You: ")
    if user_input.lower() in ("quit", "exit"):
        print("Goodbye!")
        break

    # Append user message to conversation history
    messages.append({"role": "user", "content": user_input})

    # Call the API (streaming = False for simplicity)
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            stream=False
        )
        assistant_reply = response.choices[0].message.content
        print(f"Assistant: {assistant_reply}\n")

        # Append assistant reply to history so the model remembers context
        messages.append({"role": "assistant", "content": assistant_reply})

    except Exception as e:
        print(f"Error: {e}")
        break