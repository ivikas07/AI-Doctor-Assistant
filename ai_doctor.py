from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import styles

import os
import gradio as gr
import datetime

# ==========================
# SYSTEM PROMPT
# ==========================

system_prompt = (
    "You have to act as a doctor for learning purposes only. "
    "Analyze symptoms and image carefully. "
    "Give a short professional response without markdown. "
    "Maximum 2 sentences."
)

# ==========================
# PDF GENERATOR
# ==========================

def generate_pdf(patient_query, doctor_response):

    filename = f"Medical_Report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    doc = SimpleDocTemplate(filename)

    style = styles.getSampleStyleSheet()

    story=[]

    title=Paragraph(
        "AI Doctor Medical Consultation Report",
        style['Title']
    )

    date=Paragraph(
        f"<b>Date:</b> {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
        style['BodyText']
    )

    patient=Paragraph(
        f"<b>Patient Query:</b><br/><br/>{patient_query}",
        style['BodyText']
    )

    doctor=Paragraph(
        f"<b>Doctor Analysis:</b><br/><br/>{doctor_response}",
        style['BodyText']
    )

    story.append(title)
    story.append(Spacer(1,20))

    story.append(date)
    story.append(Spacer(1,20))

    story.append(patient)
    story.append(Spacer(1,20))

    story.append(doctor)

    doc.build(story)

    return filename


# ==========================
# MAIN FUNCTION
# ==========================

def process_inputs(audio_filepath,image_filepath,history):

    speech_to_text_output=""

    if audio_filepath:

        speech_to_text_output=transcribe_with_groq(
            GROQ_API_KEY=os.getenv("GROQ_API_KEY"),
            auido_filepath=audio_filepath,
            stt_model="whisper-large-v3"
        )

    else:

        speech_to_text_output="No voice input given."


    if image_filepath:

        doctor_response=analyze_image_with_query(
            query=system_prompt+" "+speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="meta-llama/llama-4-scout-17b-16e-instruct"
        )

    else:

        doctor_response="Please upload image."


    voice_of_doctor=text_to_speech_with_gtts(
        doctor_response,
        "final.mp3"
    )


    print("Voice generated successfully")


    # FIXED CHAT HISTORY FORMAT
    history.append(
        {
            "role":"user",
            "content":speech_to_text_output
        }
    )

    history.append(
        {
            "role":"assistant",
            "content":doctor_response
        }
    )


    report_file=generate_pdf(
        speech_to_text_output,
        doctor_response
    )


    return (
        speech_to_text_output,
        doctor_response,
        voice_of_doctor,
        history,
        report_file
    )


# ==========================
# UI
# ==========================

with gr.Blocks() as demo:

    gr.Markdown(
        "# 🩺 AI Doctor Assistant"
    )

    with gr.Row():

        audio=gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="Record Patient Voice"
        )

        image=gr.Image(
            type="filepath",
            label="Upload Medical Image"
        )

    btn=gr.Button("Analyze")

    speech_box=gr.Textbox(
        label="Speech To Text"
    )

    doctor_box=gr.Textbox(
        label="Doctor Analysis"
    )

    doctor_voice=gr.Audio(
        label="Doctor Voice"
    )

    chatbot=gr.Chatbot(
        label="Consultation History"
    )

    report=gr.File(
        label="Download Medical Report"
    )

    state=gr.State([])

    btn.click(
        fn=process_inputs,

        inputs=[
            audio,
            image,
            state
        ],

        outputs=[
            speech_box,
            doctor_box,
            doctor_voice,
            chatbot,
            report
        ]
    )


demo.launch(
    debug=True
)