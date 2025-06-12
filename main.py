from groq import Groq
import gradio as gr
from gtts import gTTS
import tempfile

# Replace this with your actual Groq API key
groq_api_key = "your_groq_api_key_here"
client = Groq(api_key=groq_api_key)

def decode_dream(dream_text):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a magical dream interpreter."},
            {"role": "user", "content": dream_text}
        ]
    )
    meaning = response.choices[0].message.content
    tts = gTTS(meaning)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        audio_path = fp.name
    return meaning, audio_path

interface = gr.Interface(
    fn=decode_dream,
    inputs=gr.Textbox(label="🌙 Describe Your Dream"),
    outputs=[gr.Textbox(label="💭 Dream Meaning"), gr.Audio(label="🔊 Listen")],
    title="Dream Decoder AI",
    description="Get voice + text interpretation of your dreams"
)

interface.launch()
