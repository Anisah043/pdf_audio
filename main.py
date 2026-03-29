import PyPDF2
from TTS.api import TTS
import os

PDF_PATH = "/input/book.pdf"
OUTPUT_PATH = "/output/my_voice_output.wav"
VOICE_SAMPLE = "/input/my_voice.wav"

def clone_and_read(filepath, voice_sample):
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts")
    pdfreader = PyPDF2.PdfReader(filepath)
    full_text = ""

    for page in pdfreader.pages:
        full_text += page.extract_text()

    tts.tts_to_file(
        text = full_text,
        speaker_wav = voice_sample,
        language = "en",
        file_path = OUTPUT_PATH
    )
    print({OUTPUT_PATH})

clone_and_read(PDF_PATH, VOICE_SAMPLE)
    