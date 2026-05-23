# File: voice_of_the_doctor.py

from gtts import gTTS
from pydub import AudioSegment


def text_to_speech_with_gtts(input_text, output_filepath):

    try:

        # Generate speech
        tts = gTTS(
            text=input_text,
            lang="en",
            slow=False
        )

        # Save MP3
        tts.save(output_filepath)

        # Convert MP3 to WAV
        audio = AudioSegment.from_mp3(
            output_filepath
        )

        wav_file = "final.wav"

        audio.export(
            wav_file,
            format="wav"
        )

        print("Voice generated successfully")

        # Return wav file path to Gradio
        return wav_file

    except Exception as e:

        print("Error:", e)

        return None