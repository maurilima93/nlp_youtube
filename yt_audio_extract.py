from pytube import YouTube
from moviepy.editor import *

def download_audio_from_youtube(url, output_path='audio.mp3'):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    video.download(output_path=output_path)
    clip = AudioFileClip(output_path)
    clip.write_audiofile(output_path.replace('.mp4', '.mp3'))
    clip.close()

# Exemplo de uso
download_audio_from_youtube('https://www.youtube.com/watch?v=aircAruvnKk')
