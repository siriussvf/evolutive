import gradio as gr
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from config import *

llm = ChatOpenAI(base_url=LM_STUDIO_URL, api_key="lm-studio", model=LM_STUDIO_MODEL, temperature=TEMPERATURE, max_tokens=MAX_TOKENS)
chat_history = []

def initialize_chat():
    global chat_history
    chat_history = [SystemMessage(content=f"Eres {APP_NAME}. Respondes en español.")]

def chat_function(message, history):
    global chat_history
    if not chat_history: initialize_chat()
    chat_history.append(HumanMessage(content=message))
    try:
        response = llm.invoke(chat_history)
        ai_message = response.content
        chat_history.append(AIMessage(content=ai_message))
        return ai_message
    except Exception as e:
        return f"Error: {e}"

def clear_chat():
    global chat_history
    initialize_chat()
    return []

with gr.Blocks(title=APP_NAME, theme=gr.themes.Soft()) as demo:
    gr.Markdown(f"# {APP_NAME}")
    chatbot = gr.Chatbot(height=500)
    with gr.Row():
        msg = gr.Textbox(label="Mensaje", placeholder="Escribe...", scale=4)
        submit = gr.Button("Enviar", variant="primary", scale=1)
    clear = gr.Button("Limpiar")
    msg.submit(chat_function, [msg, chatbot], [chatbot]).then(lambda: "", None, [msg])
    submit.click(chat_function, [msg, chatbot], [chatbot]).then(lambda: "", None, [msg])
    clear.click(clear_chat, None, [chatbot])

initialize_chat()
if __name__ == "__main__":
    print(f"Iniciando {APP_NAME} en http://localhost:7860")
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)
