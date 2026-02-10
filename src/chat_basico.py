from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from config import *

llm = ChatOpenAI(
    base_url=LM_STUDIO_URL,
    api_key="lm-studio",
    model=LM_STUDIO_MODEL,
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS
)

messages = []

def chat():
    print("=" * 60)
    print(f"🤖 {APP_NAME.upper()}")
    print("=" * 60)
    print("\nEscribe '/salir' para terminar\n")
    
    system_message = SystemMessage(content=f"Eres un asistente de {APP_NAME}. Respondes en español de forma clara y amigable.")
    messages.append(system_message)
    
    while True:
        user_input = input("👤 Tú: ").strip()
        
        if user_input.lower() in ['/salir', 'salir', 'exit']:
            print("\n👋 ¡Hasta luego!\n")
            break
        
        if not user_input:
            continue
        
        messages.append(HumanMessage(content=user_input))
        
        try:
            print("\n🤖 IA: ", end="", flush=True)
            response = llm.invoke(messages)
            print(response.content + "\n")
            messages.append(AIMessage(content=response.content))
        except Exception as e:
            print(f"\n❌ Error: {e}\n")
            break

if __name__ == "__main__":
    chat()
