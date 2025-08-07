from obiguard import Obiguard

obiguard_client = Obiguard(
    obiguard_api_key='vk-ob***',  # Your Obiguard virtual key proxy to OpenAI
    provider='openai',
)

response = obiguard_client.responses.create(
    model="gpt-4o",
    instructions="You are helpful assistant",
    input="Talk about a unicorn",
)

print(response)
