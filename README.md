# 🩺 AI Doctor Assistant

AI Doctor Assistant is a multimodal healthcare assistant that combines image understanding, speech recognition, AI-powered medical responses, and voice output into one interactive application.

The project allows users to upload medical images and ask questions through voice recording. The AI analyzes the image and spoken query, generates a medical-style response, speaks the response back to the user, and creates downloadable medical reports.

---

## 🚀 Features

✅ Upload medical images for analysis  
✅ Record patient questions using microphone input  
✅ Speech-to-text conversion using Groq Whisper  
✅ AI-powered medical response generation  
✅ Text-to-speech doctor voice response  
✅ Downloadable PDF medical reports  
✅ Interactive Gradio web interface  
✅ Consultation history support  

---

## 🛠 Technologies Used

- Python
- Gradio
- Groq API
- Whisper Large V3
- Llama Vision Model
- gTTS
- ReportLab

---

## 📂 Project Structure

```bash
AI-Doctor-Assistant/
│
├── ai_doctor.py
├── brain_of_the_doctor.py
├── voice_of_the_patient.py
├── voice_of_the_doctor.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── images/
```

## ⚙ Installation

Clone repository:

```bash
git clone https://github.com/ivikas07/AI-Doctor-Assistant.git
```

Move into project folder:

```bash
cd AI-Doctor-Assistant
```

Create virtual environment:

```bash
python -m venv myenv
```

Activate virtual environment:

Windows:

```bash
myenv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶ Run Project

```bash
python ai_doctor.py
```

Open browser:

```bash
http://127.0.0.1:7860
```

---

## 📸 How it works

1. Upload a medical image
2. Record your symptoms or question
3. AI converts speech to text
4. AI analyzes image + question
5. Doctor response is generated
6. Voice response is created
7. PDF report can be downloaded

---

## Future Improvements

- User login system
- Cloud deployment
- Real-time consultation
- Better voice models
- Medical history storage

---

## 👨‍💻 Author

Vikas Sharma

GitHub:
https://github.com/ivikas07