# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:17:35 2024

@author: USER
"""

from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from gtts import gTTS
import os

app = FastAPI()

class TextData(BaseModel):
    text: str
    language: str

def text_to_speech(text: str, language: str):
    if language == 'en':
        tts = gTTS(text, lang='en')
        tts.save('output.mp3')
        os.system('start output.mp3')
    elif language == 'hi':
        tts = gTTS(text, lang='hi')
        tts.save('output.mp3')
        os.system('start output.mp3')
    elif language == 'bn':
        tts = gTTS(text, lang='bn')
        tts.save('output.mp3')
        os.system('start output.mp3')
    else:
        print("Unsupported language")

@app.get("/")
async def main():
    return { "message": "working fine" }

@app.post("/text_to_speech/")
async def produce_text_to_speech(text_data: TextData, background_tasks: BackgroundTasks):
    background_tasks.add_task(text_to_speech, text_data.text, text_data.language)
    return {"message": "Text to speech conversion has been started."}
