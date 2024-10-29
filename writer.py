# writer.py

from openai import OpenAI
from config import *
from colorama import Fore, Back, Style, init

init(autoreset=True)


class WriterAgent:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = WRITER_MODEL

    def propose_ideas(self):
        prompt = (f"You are an experienced story writer. "
                  f"Generate a list of {NUM_STORY_IDEA} unique and attractive story idea/ideas suitable for adult "
                  f"audience. "
                  f"Provide only the ideas and nothing else.")
        print(Fore.YELLOW + prompt)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        ideas = response.choices[0].message.content.strip()
        print(Fore.GREEN + "---- Writer Proposes Ideas:\n", Fore.GREEN + ideas)
        return ideas

    def revise_ideas(self, ideas, feedback):
        prompt = (f"You are an experienced story writer. "
                  f"Revise these story ideas based on the given feedback: \n"
                  f"Story ideas: {{{ideas}}}\n"
                  f"Feedback: {{{feedback}}}\n"
                  f"Provide only the ideas and nothing else.")
        print(Fore.YELLOW + prompt)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        revised_ideas = response.choices[0].message.content.strip()
        print(Fore.GREEN + "---- Writer Proposes Revised Ideas:\n", Fore.GREEN + revised_ideas)
        return revised_ideas

    def compose_outline(self, idea):
        prompt = (f"You are an experienced story writer. "
                  f"Create a very detailed outline for the following story idea: "
                  f"\n{{{idea}}}\n"
                  f"Provide only the outline and nothing else.")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        outline = response.choices[0].message.content.strip()
        print(Fore.GREEN + "---- Writer Proposes Outline:\n", Fore.GREEN + outline)
        return outline

    def revise_outline(self, outline, feedback):
        prompt = (f"You are an experienced story writer. "
                  f"Revise this story outline based on the given feedback: "
                  f"Story outline: {{{outline}}}\n"
                  f"Feedback: {{{feedback}}}\n"
                  f"Provide only the outline and nothing else.")
        print(Fore.YELLOW + prompt)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        revised_outline = response.choices[0].message.content.strip()
        print(Fore.GREEN + "---- Writer Proposes Revised Outline:\n", Fore.GREEN + revised_outline)
        return revised_outline

    def compose_full_story(self, outline):
        prompt = (f"You are an experienced story writer. "
                  f"Write a full, engaging story following the given outline. "
                  f"The length of the story should be at least {STORY_LENGTH} words. "
                  f"Here is the outline: "
                  f"\n{{{outline}}}\n"
                  f"Provide only the story and nothing else.")
        print(Fore.YELLOW + prompt)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        story = response.choices[0].message.content.strip()
        print(Fore.GREEN + "---- Writer Proposes Story:\n", Fore.GREEN + story)
        return story

    def revise_full_story(self, story, feedback):
        prompt = (f"You are an experienced story writer. "
                  f"Revise this story based on the given feedback, ensure the story is attractive: \n"
                  f"Story: {{{story}}}\n"
                  f"Feedback: {{{feedback}}}\n"
                  f"Provide only the story and nothing else.")
        print(Fore.YELLOW + prompt)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        revised_story = response.choices[0].message.content.strip()
        print(Fore.GREEN + "---- Writer Proposes Revised Story:\n", Fore.GREEN + revised_story)
        return revised_story

    def summarize_story(self, story):
        prompt = (f"You are an experienced story writer. "
                  f"Provide a concise, one-paragraph summary of the following story, "
                  f"focusing on the main themes and visuals that could inspire an illustrative image: \n\n{story}\n"
                  f"Provide only the summary and nothing else.")
        print(Fore.YELLOW + prompt)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150  # Limit the response length
        )
        summary = response.choices[0].message.content.strip()
        print(Fore.GREEN + "---- Writer Proposes Summary:\n", Fore.GREEN + summary)
        return summary

    def generate_tags(self, story):
        prompt = (f"You are an experienced story writer. "
                  f"Provide a few concise tags of the following story, "
                  f"these tags will be used to categorize the story. "
                  f"Separate the tags by $ sign: "
                  f"\n{{{story}}}\n"
                  f"Provide only the tags and nothing else.")
        print(Fore.YELLOW + prompt)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100  # Limit the response length
        )
        tags = response.choices[0].message.content.strip().split('$')
        print(Fore.GREEN + "---- Writer Proposes tags:\n", Fore.GREEN + tags)
        return tags

    def write_catchy_description(self, story):
        prompt = (f"You are an experienced story writer. "
                  f"Provide a short and catchy description of the following story: "
                  f"\n{{{story}}}\n"
                  f"Provide only the description and nothing else.")
        print(Fore.YELLOW + prompt)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150  # Limit the response length
        )
        description = response.choices[0].message.content.strip()
        print(Fore.GREEN + "---- Writer Proposes Description:\n", Fore.GREEN + description)
        return description
