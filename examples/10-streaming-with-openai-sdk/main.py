#!/usr/bin/env -S poetry run python

import asyncio
import os

from obiguard import Obiguard, OBIGUARD_GATEWAY_URL
from openai import OpenAI, AsyncOpenAI

# This script assumes you have the OPENAI_API_KEY environment variable set to a valid OpenAI API key.
#
# You can run this script from the root directory like so:
# `python examples/streaming.py`


obiguard_client = Obiguard(
    obiguard_api_key="sk-obg***",  # Your Obiguard policy group API key
    provider='openai',
    strict_open_ai_compliance=False
)


def sync_main() -> None:
    openai_client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url=OBIGUARD_GATEWAY_URL,
        default_headers=obiguard_client.copy_headers()
    )
    response = openai_client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="1,2,3,",
        max_tokens=5,
        temperature=0,
        stream=True,
    )

    # You can manually control iteration over the response
    first = next(response)
    print(f"got response data: {first.to_json()}")

    # Or you could automatically iterate through all of data.
    # Note that the for loop will not exit until *all* of the data has been processed.
    for data in response:
        print(data.to_json())


async def async_main() -> None:
    openai_client = AsyncOpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url=OBIGUARD_GATEWAY_URL,
        default_headers=obiguard_client.copy_headers()
    )
    response = await openai_client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="1,2,3,",
        max_tokens=5,
        temperature=0,
        stream=True,
    )

    # You can manually control iteration over the response.
    # In Python 3.10+ you can also use the `await anext(response)` builtin instead
    first = await response.__anext__()
    print(f"got response data: {first.to_json()}")

    # Or you could automatically iterate through all of data.
    # Note that the for loop will not exit until *all* of the data has been processed.
    async for data in response:
        print(data.to_json())


sync_main()

asyncio.run(async_main())
