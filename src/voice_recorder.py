import sounddevice as sd
import soundfile as sf
import numpy as np
from pathlib import Path

def record_audio(duration=5, sample_rate=16000, output_file="recording.wav"):
    """Graba audio del microfono"""
    print(f"Grabando durante {duration} segundos...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.float32)
    sd.wait()
    
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(output_path, recording, sample_rate)
    print("Grabacion completada")
    return output_path

if __name__ == "__main__":
    print("Modulo de grabacion de audio cargado correctamente")
