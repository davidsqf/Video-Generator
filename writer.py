# writer.py

from openai import OpenAI
from config import OPENAI_API_KEY

class WriterAgent:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = "gpt-4-turbo"

    def propose_ideas(self):
        prompt = "Generate a list of 5 unique and attractive story ideas suitable for a wide audience."
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        ideas = response.choices[0].message.content.strip()
        return ideas

    def revise_ideas(self, feedback):
        prompt = f"Revise the previous story ideas based on the following feedback:\n{feedback}"
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        revised_ideas = response.choices[0].message.content.strip()
        return revised_ideas

    def compose_outline(self, idea):
        prompt = f"Create a detailed outline for the following story idea:\n{idea}"
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        outline = response.choices[0].message.content.strip()
        return outline

    def compose_full_story(self, outline):
        prompt = f"Write a full, engaging story based on the following outline:\n{outline}"
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        story = response.choices[0].message.content.strip()
        return story

    def summarize_story(self, story):
        prompt = f"Provide a concise, one-paragraph summary of the following story, focusing on the main themes and visuals that could inspire an illustrative image:\n\n{story}"
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150  # Limit the response length
        )
        summary = response.choices[0].message.content.strip()
        return summary
