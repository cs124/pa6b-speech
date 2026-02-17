from cartesia import Cartesia
import os

client = Cartesia(api_key=os.getenv("CARTESIA_API_KEY"))

with open("sampled_sentences_speech.wav", "rb") as audio_file:
    response = client.stt.transcribe(
        file=audio_file,
        model="ink-whisper",
        language="en",
    )

print(response.text)

with open('sampled_sentences_speech.txt', 'w') as f:
    f.write(response.text)
