import whisper
from piper import PiperVoice
from pathlib import Path
import tempfile
import wave
import io

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
    audio_bytes = io.BytesIO()
    with wave.open(audio_bytes, "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(v.config.sample_rate)
        v.synthesize(text, wav_file)
    with open(output_file, "wb") as f:
        f.write(audio_bytes.getvalue())
    return output_file
