from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from gtts import gTTS
import os

app = FastAPI()

class TextData(BaseModel):
    text: str
    language: str

@app.post("/text_to_speech/")
async def produce_text_to_speech(text_data: TextData, background_tasks: BackgroundTasks):
    language = text_data.language
    text = text_data.text

    if language == 'en':
        tts = gTTS(text, lang='en')
        tts.save('output.mp3')
    elif language == 'hi':
        tts = gTTS(text, lang='hi')
        tts.save('output.mp3')
    elif language == 'bn':
        tts = gTTS(text, lang='bn')
        tts.save('output.mp3')
    else:
        print("Unsupported language")

    filepath = './output.mp3'
    filename = os.path.basename(filepath)
    headers = {'Content-Disposition': f'attachment; filename="{filename}"'}
    return FileResponse(filepath, headers=headers, media_type="audio/mp3")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
