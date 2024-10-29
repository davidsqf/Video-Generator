# config.py

import os
from dotenv import load_dotenv

load_dotenv()

# Existing configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# New configuration for YouTube upload
CLIENT_SECRETS_FILE = "google_cloud_credentials.json"
OUTPUTS_DIR = "outputs"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

VIDEO_OUTPUT_PATH = "outputs/story_video.mp4"
FPS = 24

IMAGE_PATH = "outputs/story_image.png"
AUDIO_PATH = "outputs/story_audio.mp3"

FULL_STORY_PATH = "outputs/full_story.txt"
STORY_SUMMARY_PATH = "outputs/story_summary.txt"
STORY_OUTLINE_PATH = "outputs/story_outline.txt"
STORY_IDEA_PATH = "outputs/story_idea.txt"

NUM_STORY_IDEA = 1
STORY_LENGTH = 3000

EPOCH_STORY_IDEA = 10
EPOCH_STORY_OUTLINE = 20
EPOCH_FULL_STORY = 2

WRITER_MODEL = "gpt-4-turbo"
REVIEWER_MODEL = "gpt-4-turbo"
ARTIST_MODEL = "dall-e-3"
ARTIST_SIZE = "1024x1024"
ARTIST_QUALITY = "standard"
SPEAKER_MODEL = "tts-1-hd"
SPEAKER_VOICE = "nova"

REVIEW_EARLY_TERMINATION_KEYWORD = "<<GOOD ENOUGH>>"
