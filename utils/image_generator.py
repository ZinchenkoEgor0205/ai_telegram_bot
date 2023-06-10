from base64 import b64decode
import openai
import asyncio


async def get_images(prompt: str):
    response = await asyncio.to_thread(
        openai.Image.create,
        prompt=prompt,
        n=1,
        size='256x256',
        response_format='b64_json'
    )
    image_data = b64decode(response['data'][0]['b64_json'])

    return image_data


async def generate_image(prompt: str, key: str) -> bytes:
    openai.api_key = key  # enter your openai API key
    task = asyncio.create_task(get_images(prompt))
    image_data = await task
    return image_data
