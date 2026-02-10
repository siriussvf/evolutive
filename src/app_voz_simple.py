import gradio as gr
from voice import synthesize_speech

# Test simple de sintesis de voz
def hablar(texto):
    if not texto:
        return None
    audio = synthesize_speech(texto)
    return str(audio)

with gr.Blocks() as demo:
    gr.Markdown("# iE - Test de Voz")
    texto = gr.Textbox(label="Texto a sintetizar")
    btn = gr.Button("Hablar")
    audio = gr.Audio(label="Audio")
    btn.click(hablar, inputs=[texto], outputs=[audio])

demo.launch(server_name="127.0.0.1", server_port=7860)
