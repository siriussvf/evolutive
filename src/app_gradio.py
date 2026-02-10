import gradio as gr
import requests
from voice import transcribe_audio, synthesize_speech

LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"

def process_audio(audio):
    if audio is None:
        return "No hay audio", None
    
    try:
        text = transcribe_audio(audio)
        print(f"Transcrito: {text}")
    except Exception as e:
        return f"Error transcribiendo: {e}", None
    
    try:
        resp = requests.post(LM_STUDIO_URL, json={
            "model": "local",
            "messages": [{"role": "user", "content": text}],
            "temperature": 0.7,
            "max_tokens": 300
        }, timeout=20)
        
        if resp.status_code == 200:
            reply = resp.json()["choices"][0]["message"]["content"]
        else:
            reply = "Error en LM Studio"
    except:
        reply = "No conecta con LM Studio"
    
    try:
        audio_out = synthesize_speech(reply)
        return f"Tú: {text}\n\niE: {reply}", str(audio_out)
    except:
        return f"Tú: {text}\n\niE: {reply}", None

demo = gr.Interface(
    fn=process_audio,
    inputs=gr.Audio(sources=["microphone"], type="filepath"),
    outputs=[
        gr.Textbox(label="Conversación"),
        gr.Audio(label="Respuesta de iE", autoplay=True)
    ],
    title="iE - Inteligencia Evolutiva",
    description="Habla con iE usando tu micrófono"
)

if __name__ == "__main__":
    demo.launch(share=True)
