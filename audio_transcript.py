import openai
from transformers import WhisperForConditionalGeneration, WhisperTokenizer

def transcribe_audio(file_path):
    model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large")
    tokenizer = WhisperTokenizer.from_pretrained("openai/whisper-large")
    
    audio_input = tokenizer(file_path, return_tensors="pt").input_features
    generated_ids = model.generate(audio_input)
    transcription = tokenizer.decode(generated_ids[0])
    
    return transcription

def save_transcription_to_txt(transcription, file_name='transcription.txt'):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(transcription)

# Exemplo de uso
transcription = transcribe_audio('audio.mp3')
print(transcription)

# Salvando a transcrição em um arquivo de texto
save_transcription_to_txt(transcription)
