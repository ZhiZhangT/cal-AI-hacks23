from fastapi import FastAPI, UploadFile, File
from aiohttp import ClientSession
from fastapi.middleware.cors import CORSMiddleware
import io
import moviepy.editor as mp


import numpy as np
from pydub import AudioSegment

import os

app = FastAPI()
OPENAI_API_KEY = os.getenv("isk-O0pMhXMushdl6VZ4OqpLT3BlbkFJNIhHxeivBY1qakf2DwiF")  # your OpenAI API Key

origins = [
    "http://localhost:3000",  # React app address
    # other origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
<<<<<<< HEAD
@app.post("/uploadvideo")
async def upload_video(video: UploadFile):

    print(video.filename)

    # CONVERT VIDEO TO AUDIO:
    my_clip = mp.VideoFileClip(video)
    my_clip.audio.write_audiofile(r"video_transcript.wav")

    # LOCATE SAVED AUDIO

    # USE WHISPER TO GET TRANSCRIPT OF AUDIO

    # SAVE TRANSCRIPT
    
    return {"filename": video.filename}
'''
@app.post("/transcribe/")
async def transcribe_audio(audio: UploadFile = File(...)):
=======
# @app.post("/uploadaudio")
# async def upload_audio(audio: UploadFile = File(...)):
#     # Get the filename before converting to an AudioSegment
#     filename = audio.filename

#     # read the uploaded file
#     audio_bytes = await audio.read()

#     # convert the bytes to a stream
#     audio_stream = io.BytesIO(audio_bytes)
    
#     # load the audio file
#     audio = AudioSegment.from_file(audio_stream)

#     # convert to mono and 8000 Hz sample rate
#     audio = audio.set_channels(1).set_frame_rate(8000)

#     # get the raw audio data as a bytestring
#     raw_data = audio.raw_data

#     # convert the raw audio data to Int16 format
#     audio_data = np.frombuffer(raw_data, dtype=np.int16)

#     # convert the audio data to little endian byte order
#     audio_data = audio_data.astype('<i2')

#     # convert back to bytes
#     audio_bytes = audio_data.tobytes()

#     # Save the audio file to the local filesystem
#     with open(f"test/{filename}", "wb") as f:
#         f.write(audio_bytes)

#     return {"filename": filename}


# @app.post("/transcribe")
# async def transcribe_audio(audio: UploadFile):
#     # read the uploaded file
#     audio_bytes = await audio.read()
    
#     async with ClientSession() as session:
#         response = await session.post(
#             "https://api.openai.com/v1/whisper/asr",
#             headers={
#                 "Authorization": f"Bearer {OPENAI_API_KEY}",
#                 "Openai-Organization": "org-tjIV1GRkqtPxOQkDXsPsm8J3",  # replace with your OpenAI org ID
#                 "Content-Type": "audio/wav",  # assuming the uploaded file is in wav format
#             },
#             data=audio_bytes,
#         )
#         response.raise_for_status()
#         result = await response.json()
#         print(result)
#     return {"transcription": result}

@app.post("/uploadaudio")
async def upload_audio(audio: UploadFile = File(...)):
    # Get the filename before converting to an AudioSegment
    filename = audio.filename

>>>>>>> ad985c826a742fdc789ea96b6258ff3a6c947100
    # read the uploaded file
    audio_bytes = await audio.read()

    # convert the bytes to a stream
    audio_stream = io.BytesIO(audio_bytes)
    
    # load the audio file
    audio = AudioSegment.from_file(audio_stream)

    # convert to mono and 8000 Hz sample rate
    audio = audio.set_channels(1).set_frame_rate(8000)

    # get the raw audio data as a bytestring
    raw_data = audio.raw_data

    # convert the raw audio data to Int16 format
    audio_data = np.frombuffer(raw_data, dtype=np.int16)

    # convert the audio data to little endian byte order
    audio_data = audio_data.astype('<i2')

    # convert back to bytes
    audio_bytes = audio_data.tobytes()

    # Save the audio file to the local filesystem
    with open(f"test/{filename}", "wb") as f:
        f.write(audio_bytes)
        
    # Start a new ClientSession for making HTTP requests
    async with ClientSession() as session:
        # Send a POST request to the Whisper ASR API
        response = await session.post(
            "https://api.openai.com/v1/whisper/asr",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Openai-Organization": "org-tjIV1GRkqtPxOQkDXsPsm8J3",  # replace with your OpenAI org ID
                "Content-Type": "audio/wav",  # assuming the uploaded file is in wav format
            },
            data=audio_bytes,
        )
        # Raise an error if the request was not successful
        response.raise_for_status()
        # Get the response data as JSON
        result = await response.json()

<<<<<<< HEAD
    return {"transcription": result}
'''

=======
    return {"filename": filename, "transcription": result}
>>>>>>> ad985c826a742fdc789ea96b6258ff3a6c947100
