# speaker.py

from config import *
from openai import OpenAI, APIError
from pathlib import Path
from pydub import AudioSegment
import re


class SpeakerAgent:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = SPEAKER_MODEL
        self.voice = SPEAKER_VOICE  # You can change this to an available voice
        self.max_chars = 4000  # Slightly less than 4096 to account for any overhead
        self.output_dir = Path("outputs")
        self.output_dir.mkdir(exist_ok=True)

    def split_text(self, text):
        # Split text into chunks not exceeding max_chars
        sentences = re.split('(?<=[.!?]) +', text)
        chunks = []
        current_chunk = ''

        for sentence in sentences:
            if len(current_chunk) + len(sentence) + 1 <= self.max_chars:
                current_chunk += ' ' + sentence if current_chunk else sentence
            else:
                chunks.append(current_chunk)
                current_chunk = sentence
        if current_chunk:
            chunks.append(current_chunk)
        return chunks

    def generate_audio(self, story_text):
        # Split the text into manageable chunks
        text_chunks = self.split_text(story_text)
        audio_segments = []
        try:
            for idx, chunk in enumerate(text_chunks):
                print(f"Generating audio for chunk {idx + 1}/{len(text_chunks)}...")
                response = self.client.audio.speech.create(
                    model=self.model,
                    voice=self.voice,
                    input=chunk
                )
                chunk_audio_path = self.output_dir / f"story_audio_chunk_{idx}.mp3"
                response.stream_to_file(chunk_audio_path)
                # Load the audio segment
                audio_segment = AudioSegment.from_file(chunk_audio_path)
                audio_segments.append(audio_segment)
                # Optionally, delete the chunk audio file after loading
                # chunk_audio_path.unlink()
            # Concatenate all audio segments
            final_audio = sum(audio_segments)
            final_audio_path = AUDIO_PATH
            final_audio.export(final_audio_path, format="mp3")
            print(f"Audio generation complete. Saved to {final_audio_path}")
            return str(final_audio_path)
        except APIError as e:
            print(f"An error occurred while generating the audio: {e}")
            return None
