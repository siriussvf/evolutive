import whisper
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

def transcribe(audio_file, language="es"):
    """Transcribe audio a texto usando Whisper"""
    model = whisper.load_model("base")
    result = model.transcribe(str(audio_file), language=language)
    return result["text"].strip()

if __name__ == "__main__":
    print("Modulo de transcripcion de voz cargado correctamente")
