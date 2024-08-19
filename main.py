import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq client with your API key
client = Groq(api_key=os.environ.get("OPENAI_API_KEY"))

def create_chat_completion(prompt):
    # Create a chat completion request
    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": prompt,
        }],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content

def prepare_prompt(history, query):
    # Extract messages from the history tuples
    context = "\n".join([message for _, message in history])
    return f"""
You are a grocery planner with expertise in meal planning, grocery shopping, and food storage. You should provide detailed responses related to 
these topics. If the question is not related to grocery planning, respond with: 
"I am a grocery planner and cannot answer this question." If you need to ask a question in response, ask only a single question.
Here is the conversation history:
{context}
User query: {query}
"""


