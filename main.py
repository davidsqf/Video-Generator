# main.py

import os
from writer import WriterAgent
from reviewer import ReviewerAgent
from artist import ArtistAgent
from speaker import SpeakerAgent
from moviepy.editor import ImageClip, AudioFileClip


def main(generate_story, generate_image, generate_audio):
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
    if generate_story:
        writer = WriterAgent()
        reviewer = ReviewerAgent()

        # Idea generation and review loop
        ideas = writer.propose_ideas()
        for _ in range(3):
            print("Writer Proposes Ideas:\n", ideas)
            feedback = reviewer.review_ideas(ideas)
            print("Reviewer Feedback on Ideas:\n", feedback)
            if "10/10" in feedback:
                break
            ideas = writer.revise_ideas(feedback)

        # Save the final ideas
        with open("outputs/story_idea.txt", "w") as f:
            f.write(ideas)

        # Select the best idea (Assuming the first one for simplicity)
        best_idea = ideas.strip().split('\n')[0]

        # Outline generation and review loop
        outline = writer.compose_outline(best_idea)
        for _ in range(3):
            feedback = reviewer.review_outline(outline)
            print("Reviewer Feedback on Outline:\n", feedback)
            if "No further suggestions" in feedback or "looks good" in feedback.lower():
                break
            outline = writer.compose_outline(feedback)

        # Save the final outline
        with open("outputs/story_outline.txt", "w") as f:
            f.write(outline)

        # Full story generation and review loop
        story = writer.compose_full_story(outline)
        for _ in range(3):
            feedback = reviewer.review_story(story)
            print("Reviewer Feedback on Story:\n", feedback)
            if "No further suggestions" in feedback or "well done" in feedback.lower():
                break
            story = writer.compose_full_story(feedback)

        # Save the final story
        with open("outputs/full_story.txt", "w") as f:
            f.write(story)

        summary = writer.summarize_story(story)
        with open("outputs/story_summary.txt", "w") as f:
            f.write(summary)

    if generate_image:
        with open("outputs/story_summary.txt", 'r') as f:
            summary = f.read()

        # Generate image
        artist = ArtistAgent()
        image_path = artist.generate_image(summary)
    if generate_audio:
        with open("outputs/full_story.txt", 'r') as f:
            story = f.read()
        # Generate audio
        speaker = SpeakerAgent()
        audio_path = speaker.generate_audio(story)

    # Create video
    image_path = "outputs/story_image.png"
    audio_path = "outputs/story_audio.mp3"
    create_video(image_path, audio_path)

    print("All outputs have been generated and saved in the 'outputs' directory.")


def create_video(image_path, audio_path):
    audio_clip = AudioFileClip(audio_path)
    image_clip = ImageClip(image_path).set_duration(audio_clip.duration)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.write_videofile("outputs/story_video.mp4", fps=24)


if __name__ == "__main__":
    main(generate_story=False, generate_image=False, generate_audio=True)
