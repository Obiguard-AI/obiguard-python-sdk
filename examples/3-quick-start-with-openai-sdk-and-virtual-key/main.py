import os

from openai import OpenAI
from obiguard import OBIGUARD_GATEWAY_URL, Obiguard

# This example showcases the use of OpenAI SDK with AI providers other than OpenAI.

obiguard_client = Obiguard(
    obiguard_api_key=os.environ.get("OBIGUARD_API_KEY"),  # Your Obiguard virtual key
    provider='openai',
)

openai_client = OpenAI(
    api_key="N/A",  # Not needed when using Obiguard virtual key
    base_url=OBIGUARD_GATEWAY_URL,
    default_headers=obiguard_client.copy_headers()
)

completion = openai_client.chat.completions.create(
    model='Qwen/Qwen2.5-32B-Instruct',
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)
print(completion.choices[0].message)
