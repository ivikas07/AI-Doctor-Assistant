# File: voice_of_the_patient.py

from groq import Groq


def transcribe_with_groq(
    GROQ_API_KEY,
    auido_filepath,
    stt_model
):

    if not auido_filepath:
        return ""

    client = Groq(
        api_key=GROQ_API_KEY
    )

    with open(
        auido_filepath,
        "rb"
    ) as audio_file:

        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model=stt_model,
            language="en"
        )

    return transcription.text