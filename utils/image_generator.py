import time
from base64 import b64decode

import openai
import json
import asyncio

from utils.key import key


async def get_images(prompt: str):
    response = await asyncio.to_thread(openai.Image.create, prompt=prompt, n=1, size='256x256',
                                       response_format='b64_json')

    with open('data.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    image_data = b64decode(response['data'][0]['b64_json'])

    return image_data


async def main(prompt):
    openai.api_key = key  # enter your openai API key
    task = asyncio.create_task(get_images(prompt))
    image_data = await task
    return image_data


async def generate_image(prompt) -> bytes:
    image_data = await main(prompt)  # todo uncomment

    return image_data
