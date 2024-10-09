# main.py
import time

from artist import ArtistAgent
from config import *
from reviewer import ReviewerAgent
from speaker import SpeakerAgent
from upload import Uploader
from video_maker import VideoMaker
from writer import WriterAgent


def main(generate_story, generate_image, generate_audio, make_video, upload_video):
    if not os.path.exists('outputs'):
        os.makedirs('outputs')

    if generate_story:
        writer = WriterAgent()
        reviewer = ReviewerAgent()

        # Idea generation and review loop
        ideas = writer.propose_ideas()
        for _ in range(EPOCH_STORY_IDEA):
            print("Writer Proposes Ideas:\n", ideas)
            feedback = reviewer.review_ideas(ideas)
            print("Reviewer Feedback on Ideas:\n", feedback)
            if "10/10" in feedback:
                break
            ideas = writer.revise_ideas(feedback)

        # Save the final ideas
        with open(STORY_IDEA_PATH, "w") as f:
            f.write(ideas)

        # Select the best idea (Assuming the first one for simplicity)
        best_idea = ideas.strip().split('\n')[0]

        # Outline generation and review loop
        outline = writer.compose_outline(best_idea)
        for _ in range(EPOCH_STORY_OUTLINE):
            feedback = reviewer.review_outline(outline)
            print("Reviewer Feedback on Outline:\n", feedback)
            if "No further suggestions" in feedback or "looks good" in feedback.lower():
                break
            outline = writer.compose_outline(feedback)

        # Save the final outline
        with open(STORY_OUTLINE_PATH, "w") as f:
            f.write(outline)

        # Full story generation and review loop
        story = writer.compose_full_story(outline)
        for _ in range(EPOCH_FULL_STORY):
            feedback = reviewer.review_story(story)
            print("Reviewer Feedback on Story:\n", feedback)
            if "No further suggestions" in feedback or "well done" in feedback.lower():
                break
            story = writer.compose_full_story(feedback)

        # Save the final story
        with open(FULL_STORY_PATH, "w") as f:
            f.write(story)

        summary = writer.summarize_story(story)
        with open(STORY_SUMMARY_PATH, "w") as f:
            f.write(summary)

    if generate_image:
        with open(STORY_SUMMARY_PATH, 'r') as f:
            summary = f.read()

        # Generate image
        artist = ArtistAgent()
        artist.generate_image(summary)

    if generate_audio:
        with open(FULL_STORY_PATH, 'r') as f:
            story = f.read()
        # Generate audio
        speaker = SpeakerAgent()
        speaker.generate_audio(story)

    if make_video:
        # Create video
        video_maker = VideoMaker()
        video_maker.create_video(IMAGE_PATH, AUDIO_PATH)
        print("All outputs have been generated and saved in the 'outputs' directory.")

    # Upload video to YouTube
    if upload_video:
        with open(FULL_STORY_PATH, 'r') as f:
            story = f.read()
        writer = WriterAgent()
        tags = writer.generate_tags(story)
        description = writer.write_catchy_description(story)
        uploader = Uploader()
        uploader.authenticate()
        title = get_title_of_full_story()
        category_id = "22"  # Category ID for "People & Blogs"
        age_restricted = True
        uploader.upload_video(
            VIDEO_OUTPUT_PATH,
            title,
            description,
            tags,
            category_id,
            age_restricted
        )


def get_title_of_full_story():
    with open(FULL_STORY_PATH) as f:
        first_line = f.readline()
    return first_line


if __name__ == "__main__":
    start = time.time()
    main(
        generate_story=True,
        generate_image=True,
        generate_audio=True,
        make_video=True,
        upload_video=True
    )
    end = time.time()
    duration = end - start
    print(f'The whole process took {duration} seconds')
