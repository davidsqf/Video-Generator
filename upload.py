# upload.py

import os
import sys
import time
from pathlib import Path
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from config import CLIENT_SECRETS_FILE, OUTPUTS_DIR, SCOPES
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Uploader:
    def __init__(self):
        self.client_secrets_file = CLIENT_SECRETS_FILE
        self.scopes = SCOPES
        self.credentials = None
        self.youtube = None

    def authenticate(self):
        creds = None
        token_path = Path("token.json")
        if token_path.exists():
            creds = Credentials.from_authorized_user_file(str(token_path), self.scopes)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.client_secrets_file, self.scopes)
                creds = flow.run_local_server(port=0)
            with open(token_path, 'w') as token_file:
                token_file.write(creds.to_json())
        self.credentials = creds
        self.youtube = build('youtube', 'v3', credentials=creds)
        logger.info("Authentication successful.")

    def upload_video(self, video_file, title, description="", tags=None, category_id="22", privacy_status="public", made_for_kids=False, self_declared_made_for_kids=None, age_restricted=True):
        if not self.youtube:
            logger.error("You must authenticate before uploading.")
            return

        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': tags or [],
                'categoryId': category_id,
            },
            'status': {
                'privacyStatus': privacy_status,
                'selfDeclaredMadeForKids': self_declared_made_for_kids if self_declared_made_for_kids is not None else not made_for_kids,
            },
        }

        if age_restricted:
            body['ageGating'] = {
                'ageRestricted': True
            }

        media_body = MediaFileUpload(video_file, chunksize=-1, resumable=True)

        try:
            request = self.youtube.videos().insert(
                part="snippet,status",
                body=body,
                media_body=media_body
            )
            response = None
            while response is None:
                status, response = request.next_chunk()
                if status:
                    logger.info(f"Upload progress: {int(status.progress() * 100)}%")
            if 'id' in response:
                logger.info(f"Video uploaded successfully. Video ID: {response['id']}")
                return response['id']
            else:
                logger.error(f"The upload failed with an unexpected response: {response}")
                return None
        except HttpError as e:
            logger.error(f"An HTTP error {e.resp.status} occurred: {e.content}")
            return None
