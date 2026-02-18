#  Programming Assignment 6b - Speech

In this assignment, you will convert sampled sentences into audio files using text-to-speech, and then transcribe the audio files back into text using speech-to-text.

## Cloning the Assignment

Select the folder in which you'd like to clone the assignment, and run the following commands in the command line to clone it.

```
cd folder/to/put/assignment
git clone https://github.com/cs124/pa6b-speech.git
```

## Using a Text Editor
Like PA6a, this assignment is not run on Jupyter Notebooks. This means that you may have to use a text editor (i.e., Visual Studio Code). For those of you that might not be familiar with this, please refer to this [guide](https://code.visualstudio.com/docs/getstarted/getting-started) to get started, or come to office hours!


## Environment Setup

PA6b requires the Cartesia package. There are two ways to setup your environment:

1. Activate the `cs124` environment you previously created, then install the required package:

```
conda activate cs124
pip install cartesia
```

2. Create a new environment called `cs124_pa6b`:

```
conda env create -f environment_pa6b.yml
conda activate cs124_pa6b
```

## Getting Your Cartesia API Key

In this assignment, you'll use the Cartesia API for both text-to-speech and speech-to-text. An **API key** is like a password that allows your code to access Cartesia's services. Here's how to get yours:

### Step 1: Create a Cartesia Account
1. Go to https://play.cartesia.ai/sign-up
2. Sign up for a free account

### Step 2: Generate Your API Key
1. Once logged in, look at the left menu under **PLATFORM**
2. Click on **API Keys**
3. Click the **+ New** button at the top right
4. Add a description for your key (e.g., `cs124_pa6b`)
5. Click **Create**
6. Copy your API key (it will look like `sk_car_...`)

### Step 3: Set Your API Key
Before running any scripts, set your API key as an environment variable in your terminal:
```
export CARTESIA_API_KEY=your_api_key_here
```
Replace `your_api_key_here` with the actual key you copied from the dashboard.

**Important:** Cartesia's free tier API comes with a rate limit. While this rate limit is more than enough to complete this assignment, please beware of overusage.

## Part 1: Convert Sampled Sentences into Audio Files

We have provided a default `sampled_sentences.json` file for you to use. If you'd like, you can optionally replace it with the sentences you sampled from your trained model in PA6a.

You should use the Cartesia API to convert your sampled sentences into audio files. You can do so by running the `tts.py` script. This script will automatically save the audio file as a wav file called `sampled_sentences_speech.wav`.

```
python tts.py
```

### Optional: Customize the Voice

You can browse and try out different voices on the [Cartesia Playground](https://play.cartesia.ai/voices). To use a different voice, you can replace the voice `id` in `tts.py` with the ID of the voice you'd like to use:

1. Go to the [Cartesia Voice Library](https://play.cartesia.ai/voices)
2. Browse and listen to different voices
3. Click on a voice you like
4. On the right side, click the three dots (⋮) next to the voice
5. Click **Copy ID** from the menu
6. Open `tts.py` and find line 15:
   ```python
   "id": "694f9389-aac1-45b6-b726-9d9369183238",
   ```
7. Replace the ID with your chosen voice's ID (paste the ID you copied)

## Part 2: Transcribe the Audio Files into Text

Next, you should use the Cartesia API to transcribe the audio files into text. You can do so by running the `speech_to_text.py` script. This script will automatically save the text file as a txt file called `sampled_sentences_speech.txt`.

```
python speech_to_text.py
```

You will include the transcribed file `sampled_sentences_speech.txt` in the submission as part of the grading. You are also encouraged to try what happens when you record yourself reading the sampled sentences in a noisy environment and transcribe the audio file back into text; and compare the quality of the transcription with the original sampled sentences.

## Part 3: Error Analysis

Now that you've run the TTS→STT pipeline, analyze what happened to your text by answering the questions in `responses.py`. Each question is defined as a function, where you should fill in your answer in the response strings.

### Question 1: Error Classification

Compare your original `sampled_sentences.json` to the final `sampled_sentences_speech.txt`. Identify and describe three distinct types of errors or information loss you observe. For each type, provide a specific example from your results and explain what aspect of the TTS (text-to-speech) or STT (speech-to-text) process likely caused it.

### Question 2: Model Bias and Training Data

Based on the errors you observed, what can you infer about the training data or design priorities of the speech-to-text model? Consider: What types of content does it handle well vs. poorly? What trade-offs might the model designers have made?

### Question 3: Formatting as Information

Your original text likely had formatting elements (capitalization, line breaks, punctuation, etc.) that disappeared in the final transcription. Choose one formatting element that was lost and explain: (a) Why current speech systems can't preserve it, and (b) What would be required to preserve it in a future system.

## Part 4: Zip and Submit 

Run `bash create_assignment_zip.sh` to zip your submission and submit the zip file to Gradescope.

To recap, the submission zip should include the following files:

- `sampled_sentences_speech.wav`: the audio file generated from your sampled sentences
- `sampled_sentences_speech.txt`: the transcribed text of the audio file
- `responses.py`: your answers to the error analysis questions

**Note:** Because your submission includes a large audio file, the upload and grading on Gradescope may take longer than usual. This is normal -- please be patient and wait for it to complete.
