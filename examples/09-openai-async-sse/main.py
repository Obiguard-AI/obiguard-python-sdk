import asyncio
import os
from openai import AsyncOpenAI
from obiguard import OBIGUARD_GATEWAY_URL, Obiguard

obiguard_client = Obiguard(
    obiguard_api_key='sk-obg***',  # Your Obiguard policy group API key
    provider='openai',
)

openai_client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=OBIGUARD_GATEWAY_URL,
    default_headers=obiguard_client.copy_headers()
)


async def main():
    stream = await openai_client.responses.create(
        model="gpt-4o",
        input="Write a one-sentence bedtime story about a unicorn.",
        stream=True,
    )

    async for event in stream:
        print(event)


asyncio.run(main())
