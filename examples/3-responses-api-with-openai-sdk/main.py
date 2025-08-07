import os

from openai import OpenAI
from obiguard import OBIGUARD_GATEWAY_URL, Obiguard

obiguard_client = Obiguard(
    obiguard_api_key='sk-obg***',  # Your Obiguard policy group API key
    provider='openai',
)

openai_client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=OBIGUARD_GATEWAY_URL,
    default_headers=obiguard_client.copy_headers()
)

response = openai_client.responses.create(
    model="gpt-4o",
    instructions="You are a coding assistant that talks like a pirate.",
    input="How do I check if a Python object is an instance of a class?",
)

print(response)
