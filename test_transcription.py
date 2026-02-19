from cartesia import Cartesia
import os

client = Cartesia(api_key=os.getenv("CARTESIA_API_KEY"))

# TODO: Update the filepath below to point to your audio clip of choice
audio_filepath = "your_audio_clip.wav"


print(f"Transcribing audio from: {audio_filepath}")
print("=" * 60)

with open(audio_filepath, "rb") as audio_file:
    response = client.stt.transcribe(
        file=audio_file,
        model="ink-whisper",
        language="en",
    )

print("\nTranscription:")
print("-" * 60)
print(response.text)
print("-" * 60)

# Save the transcription to a file
output_filename = 'test_transcription_output.txt'
with open(output_filename, 'w') as f:
    f.write(response.text)

print(f"\n✓ Transcription saved to: {output_filename}")
print("\nNext steps:")
print("1. Open test_transcription_output.txt to see the AI transcription")
print("2. Manually transcribe your audio clip yourself")
print("3. Compare the two transcriptions and answer the questions in responses.py")
