from cartesia import Cartesia
import json
import os

client = Cartesia(api_key=os.getenv("CARTESIA_API_KEY"))

sampled_sentences = json.load(open('sampled_sentences.json'))
all_sentences = "\n".join(sampled_sentences)

response = client.tts.generate(
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

response.write_to_file("sampled_sentences_speech.wav")
print("Audio saved to sampled_sentences_speech.wav")
