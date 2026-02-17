from cartesia import Cartesia
import json
import os

client = Cartesia(api_key=os.getenv("CARTESIA_API_KEY"))

sampled_sentences = json.load(open('sampled_sentences.json'))
all_sentences = "\n".join(sampled_sentences)

chunk_iter = client.tts.bytes(
    model_id="sonic-3",
    transcript=all_sentences,
    voice={
        "mode": "id",
        "id": "694f9389-aac1-45b6-b726-9d9369183238",
    },
    output_format={
        "container": "wav",
        "sample_rate": 44100,
        "encoding": "pcm_s16le",
    },
)

with open("sampled_sentences_speech.wav", "wb") as f:
    for chunk in chunk_iter:
        f.write(chunk)
print("Audio saved to sampled_sentences_speech.wav")
