"""
PA6b Error Analysis Responses

Complete each function below by returning a string with your answer.
Each response should be 3-5 sentences.
"""

def question_1():
    """
    Question 1: Error Classification
    
    Compare your original sampled_sentences.json to the final 
    sampled_sentences_speech.txt. Identify and describe three distinct 
    types of errors or information loss you observe. For each type, 
    provide a specific example from your results and explain what aspect 
    of the TTS (text-to-speech) or STT (speech-to-text) process likely 
    caused it.
    """

    # TODO: Your answer below
    response = """
    
    """
    return response


def question_2():
    """
    Question 2: Model Bias and Training Data
    
    Based on the errors you observed, what can you infer about the 
    training data or design priorities of the speech-to-text model? 
    Consider: What types of content does it handle well vs. poorly? 
    What trade-offs might the model designers have made?
    """

    # TODO: Your answer below
    response = """
    
    """
    return response


def question_3():
    """
    Question 3: Formatting as Information
    
    Your original text likely had formatting elements (capitalization, 
    line breaks, punctuation, etc.) that disappeared in the final 
    transcription. Choose one formatting element that was lost and 
    explain: (a) Why current speech systems can't preserve it, and 
    (b) What would be required to preserve it in a future system.
    """

    # TODO: Your answer below
    response = """
    
    """
    return response


def question_4():
    """
    Question 4: The "Good Enough" Threshold
    
    Disability law often reduces accommodation quality to a single metric 
    like word error rate, yet this ignores dimensions like subtitle timing, 
    speaker identification, or tonal cues — things human captioners naturally 
    attend to. What does it mean for access to collapse something as 
    multidimensional as communication into a single number? How do you view 
    the relationship or difference between meeting legal requirements and 
    providing equal access?
    """

    # TODO: Your answer below
    response = """
    
    """
    return response


def question_5():
    """
    Question 5: The Curb-Cut Effect
    
    High-quality transcription is a classic example of universal design—a 
    feature built for disability that benefits a much broader population. 
    Beyond the D/deaf and hard-of-hearing communities, identify other groups 
    who rely on these transcriptions. Do you rely on captions? How does a 
    noticeably worse AI transcription impact their ability to engage with 
    content?
    """

    # TODO: Your answer below
    response = """
    
    """
    return response


def question_6():
    """
    Question 6: Compare and Contrast
    
    Given your manual transcription above, note every instance where the AI 
    model hallucinated a word, skipped a phrase, or sanitized the speech by 
    removing pauses and stutters. What do you notice about the model's failures?
    
    In your response, include:
    - Your manual transcription
    - The AI transcription (from test_transcription_output.txt)
    - Your analysis
    """

    # TODO: Your answer below
    response = """
    
    """
    return response


def question_7():
    """
    Question 7: Whose Voice Gets Transcribed?
    
    These systems have real stakes — an automated transcription used in a 
    job interview, a 911 call, or a courtroom can fail certain speakers 
    entirely. Research shows that ASR model performance varies significantly 
    across different speakers. Do you find these patterns of performance 
    variation in your data, or does your clip tell a different story? Does 
    what you observed correspond with your own experience using voice systems 
    like Siri, Google Assistant, customer service phone trees, or your car's 
    navigation? What does either result reveal about the assumptions baked 
    into these systems about what counts as the default way of speaking?
    """

    # TODO: Your answer below
    response = """
    
    """
    return response
