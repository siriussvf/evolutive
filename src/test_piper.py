from voice import synthesize_speech

texto = "Hola, soy iE, tu inteligencia evolutiva."
print(f"Sintetizando: {texto}")
audio_path = synthesize_speech(texto)
print(f"Audio generado en: {audio_path}")
print("Prueba el audio con: open", audio_path)
