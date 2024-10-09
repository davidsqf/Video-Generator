from moviepy.editor import ImageClip, AudioFileClip

# speaker.py

from config import OPENAI_API_KEY, VIDEO_OUTPUT_PATH, FPS
from openai import OpenAI, APIError
from pathlib import Path
from pydub import AudioSegment
import re


class VideoMaker:
    def __init__(self):
        pass

    def create_video(self, image_path, audio_path):
        audio_clip = AudioFileClip(audio_path)
        image_clip = ImageClip(image_path).set_duration(audio_clip.duration)
        video_clip = image_clip.set_audio(audio_clip)
        video_clip.write_videofile(VIDEO_OUTPUT_PATH, fps=FPS)
