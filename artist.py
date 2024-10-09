# artist.py

from openai import OpenAI, APIError
import requests
from config import *


class ArtistAgent:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate_image(self, summary):
        prompt = f"Create an eye-catching and attractive image that represents the following story:\n\n{summary}\n\nThe image should be visually engaging and suitable as a thumbnail."
        try:
            response = self.client.images.generate(
                model=ARTIST_MODEL,
                prompt=prompt,
                size=ARTIST_SIZE,
                quality=ARTIST_QUALITY,
                n=1,
            )
            image_url = response.data[0].url
            # Download the image
            image_data = requests.get(image_url).content
            with open(IMAGE_PATH, "wb") as handler:
                handler.write(image_data)
        except APIError as e:
            print(f"An error occurred while generating the image: {e}")
            return None
