import gradio as gr
from langchain_openai import ChatOpenAI
from config import *

llm = ChatOpenAI(base_url=LM_STUDIO_URL, api_key="lm-studio", model=LM_STUDIO_MODEL, temperature=0.7)

def predict(message):
    try:
        response = llm.invoke([{"role": "user", "content": message}])
        return response.content
    except:
        return "Error conectando con el modelo"

iface = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(label="Tu mensaje", placeholder="Escribe aquí..."),
    outputs=gr.Textbox(label="Respuesta de iE"),
    title=f"🤖 {APP_NAME}",
    description="Tu Inteligencia Evolutiva local con Qwen2.5-7B"
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)
