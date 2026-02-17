#  Programming Assignment 6b - Speech

In this assignment, you will convert sampled sentences into audio files using text-to-speech, and then transcribe the audio files back into text using speech-to-text.

## Environment Setup

```
conda create -n cs124 python=3.10 -y
conda activate cs124
pip install cartesia
```

You will also need FFmpeg installed for audio file handling. Install it using your platform's package manager:
```
# macOS
brew install ffmpeg

# Debian/Ubuntu
sudo apt install ffmpeg
```

## Part 1: Convert Sampled Sentences into Audio Files

We have provided a default `sampled_sentences.json` file for you to use. If you'd like, you can optionally replace it with the sentences you sampled from your trained model in PA6a.

You should use the Cartesia API to convert your sampled sentences into audio files. You can do so by running the `tts.py` script. This script will automatically save the audio file as a wav file called `sampled_sentences_speech.wav`. Remember that you need to set your Cartesia API key in the `CARTESIA_API_KEY` environment variable, by example, by running:
```
export CARTESIA_API_KEY=your_api_key
```
before running the `tts.py` script.

You can browse and try out different voices on the [Cartesia Playground](https://play.cartesia.ai/voices). To use a different voice, replace the voice `id` in `tts.py` with the ID of the voice you'd like to use.

## Part 2: Transcribe the Audio Files into Text

Next, you should use the Cartesia API to transcribe the audio files into text. You can do so by running the `speech_to_text.py` script. This script will automatically save the text file as a txt file called `sampled_sentences_speech.txt`. Remember that you need to set your Cartesia API key in the `CARTESIA_API_KEY` environment variable, by example, by running:
```
export CARTESIA_API_KEY=your_api_key
```
before running the `speech_to_text.py` script.

We will include the transcribed file `sampled_sentences_speech.txt` in the submission as part of the grading. You are also encouraged to try what happens when you record yourself reading the sampled sentences in a noisy environment and transcribe the audio file back into text; and compare the quality of the transcription with the original sampled sentences.

## Part 3: Zip and Submit 

Run `bash create_assignment_zip.sh` to zip your submission and submit the zip file to Gradescope.

To recap, the submission zip should include the following files:

- `sampled_sentences_speech.txt`: the transcribed text of the audio file of your sampled sentences
