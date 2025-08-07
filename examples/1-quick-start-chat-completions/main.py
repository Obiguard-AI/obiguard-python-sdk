from obiguard import Obiguard

client = Obiguard(
    obiguard_api_key="vk-obg***",  # Your Obiguard virtual key
    provider='openai',
    strict_open_ai_compliance=False
)

response = client.chat.completions.create(
    model='Qwen/Qwen2.5-32B-Instruct',
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message)
