import whisper
from piper import PiperVoice
from pathlib import Path
import tempfile
import wave
import numpy as np

PROJECT_ROOT = Path(__file__).parent.parent
WHISPER_MODEL = whisper.load_model("base")
VOICE_MODEL = PROJECT_ROOT / "piper" / "es_ES-davefx-medium.onnx"

voice = None

def get_voice():
    global voice
    if voice is None:
        voice = PiperVoice.load(str(VOICE_MODEL))
    return voice

def transcribe_audio(audio_path: str) -> str:
    result = WHISPER_MODEL.transcribe(audio_path, language="es")
    return result["text"].strip()

def synthesize_speech(text: str) -> Path:
    output_file = Path(tempfile.mkstemp(suffix=".wav")[1])
    v = get_voice()
    
    # Recolectar todos los chunks
    audio_chunks = []
    for audio_chunk in v.synthesize(text):
        # Convertir float array a int16
        audio_int16 = (audio_chunk.audio_float_array * 32767).astype(np.int16)
        audio_chunks.append(audio_int16)
    
    # Concatenar y escribir
    full_audio = np.concatenate(audio_chunks)
    
    with wave.open(str(output_file), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(v.config.sample_rate)
        wav_file.writeframes(full_audio.tobytes())
    
    return output_file
