from transformers import WhisperForConditionalGeneration, WhisperTokenizer, GPT2LMHeadModel, GPT2Tokenizer


def transcribe_audio_with_whisper(audio_path):
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large")
    tokenizer = WhisperTokenizer.from_pretrained("openai/whisper-large")
    
    audio_input = tokenizer(audio_path, return_tensors="pt").input_features
    generated_ids = model.generate(audio_input)
    transcription = tokenizer.decode(generated_ids[0])
    
    return transcription

transcription = transcribe_audio_with_whisper('downloaded_audio.mp3')
print(transcription)

def process_text_with_gpt2(text, model_name="gpt2", max_length=150):
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    
    inputs = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1)
    
    processed_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return processed_text

processed_text = process_text_with_gpt2(transcription)
print(processed_text)