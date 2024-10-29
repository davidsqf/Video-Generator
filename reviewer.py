# reviewer.py

from openai import OpenAI
from config import *
from colorama import Fore, Back, Style, init

init(autoreset=True)


class ReviewerAgent:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = REVIEWER_MODEL

    def review_ideas(self, ideas):
        prompt = (f"You are an experienced story writer. "
                  f"Review the following story ideas, "
                  f"provide very detailed comments about how to improve the attractiveness: "
                  f"\n{{{ideas}}} "
                  f"If you think the ideas are already good enough, say {REVIEW_EARLY_TERMINATION_KEYWORD} "
                  f"Provide only the feedback and nothing else.")
        print(Fore.YELLOW + prompt)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        feedback = response.choices[0].message.content.strip()
        print(Fore.BLUE + "---- Reviewer Feedback on Ideas:\n", Fore.BLUE + feedback)
        return feedback

    def review_outline(self, outline):
        prompt = (f"You are an experienced story writer. "
                  f"Review the following story outline "
                  f"and provide constructive feedback about how to improve the attractiveness: "
                  f"\n{{{outline}}} "
                  f"If you think the outline is already good enough, say {REVIEW_EARLY_TERMINATION_KEYWORD} "
                  f"Provide only the feedback and nothing else.")
        print(Fore.YELLOW + prompt)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        feedback = response.choices[0].message.content.strip()
        print(Fore.BLUE + "---- Reviewer Feedback on Outline:\n", Fore.BLUE + feedback)
        return feedback

    def review_story(self, story):
        prompt = (f"You are an experienced story writer. "
                  f"Review the following story and provide constructive feedback "
                  f"about how to improve the attractiveness: "
                  f"\n{{{story}}} "
                  f"If you think the story is already good enough, say {REVIEW_EARLY_TERMINATION_KEYWORD} "
                  f"Provide only the feedback and nothing else.")
        print(Fore.YELLOW + prompt)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        feedback = response.choices[0].message.content.strip()
        print(Fore.BLUE + "---- Reviewer Feedback on Full Story:\n", Fore.BLUE + feedback)
        return feedback
