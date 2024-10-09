# artist.py

from openai import OpenAI, APIError
import requests
from config import OPENAI_API_KEY

class ArtistAgent:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate_image(self, summary):
        prompt = f"Create an eye-catching and attractive image that represents the following story:\n\n{summary}\n\nThe image should be visually engaging and suitable as a thumbnail."
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            image_url = response.data[0].url
            # Download the image
            image_data = requests.get(image_url).content
            image_path = "outputs/story_image.png"
            with open(image_path, "wb") as handler:
                handler.write(image_data)
            return image_path
        except APIError as e:
            print(f"An error occurred while generating the image: {e}")
            return None