import os
from openai import OpenAI
from obiguard import OBIGUARD_GATEWAY_URL, Obiguard

prompt = "What is in this image?"
img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/2023_06_08_Raccoon1.jpg/1599px-2023_06_08_Raccoon1.jpg"

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
    model="gpt-4o-mini",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url": f"{img_url}"},
            ],
        }
    ],
)

print(response)
