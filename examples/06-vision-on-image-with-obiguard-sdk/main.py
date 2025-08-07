from obiguard import Obiguard

prompt = "What is in this image?"
img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/2023_06_08_Raccoon1.jpg/1599px-2023_06_08_Raccoon1.jpg"

obiguard_client = Obiguard(
    obiguard_api_key='vk-obg***',  # Your Obiguard virtual key proxy to OpenAI
    provider='openai',
)

response = obiguard_client.responses.create(
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
