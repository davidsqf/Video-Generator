# reviewer.py

from openai import OpenAI
from config import *

class ReviewerAgent:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = REVIEWER_MODEL

    def review_ideas(self, ideas):
        prompt = f"Review the following story ideas, provide comments, and give a score out of 10 for their attractiveness:\n{ideas}"
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        feedback = response.choices[0].message.content.strip()
        return feedback

    def review_outline(self, outline):
        prompt = f"Review the following story outline and provide constructive feedback:\n{outline}"
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        feedback = response.choices[0].message.content.strip()
        return feedback

    def review_story(self, story):
        prompt = f"Review the following story and provide constructive feedback for improvement:\n{story}"
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        feedback = response.choices[0].message.content.strip()
        return feedback
