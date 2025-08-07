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

completion = openai_client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)
print(completion.choices[0].message)
