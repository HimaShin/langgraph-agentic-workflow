import os
from dotenv import load_dotenv
import together

load_dotenv()
together.api_key = os.getenv("TOGETHER_API_KEY")

def call_gpt(prompt):
    response = together.Complete.create(
        prompt=f"You are a helpful assistant.\nUser: {prompt}\nAssistant:",
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        max_tokens=300,
        temperature=0.7,
        top_k=50,
        top_p=0.7,
        repetition_penalty=1.1,
    )
    return response['choices'][0]['text'].strip()
