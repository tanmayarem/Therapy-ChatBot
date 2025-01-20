pip install groq gradio

import gradio as gr
from groq import Groq

# Initialize the Groq client with your API key
client = Groq(api_key="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")

# Define a function to handle the conversation
def groq_chatbot(user_input):
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                {
  "role": "system",
  "content": "You are a compassionate and supportive chatbot designed to act as a friendly and understanding companion for people going through tough times. Your responses should exude warmth, empathy, and positivity while providing helpful guidance or simply being a good listener. Always acknowledge the user's feelings, offer comforting words, and suggest gentle, actionable steps when appropriate. Maintain an uplifting tone, ensuring the user feels heard, valued, and supported throughout the conversation."
}
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""

    return response

# Create the Gradio interface
iface = gr.Interface(
    fn=groq_chatbot,
    inputs=gr.Textbox(label="Ask your question"),
    outputs="text",
    title="Helpful Chatbot",
    description="What is troubling you today?",
)

# Launch the interface
iface.launch()
