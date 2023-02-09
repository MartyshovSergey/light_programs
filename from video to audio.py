import moviepy.editor
from pathlib import Path

video_file = Path('Linkin Park - In The End.mp4')

# указываем модулю с каким файлом ему нужно работать
video = moviepy.editor.VideoFileClip(f'{video_file}')

# получаем аудио дорожку из файла
audio = video.audio

# сохраняем аудио дорожку в файл
# свойство stem забирает название, но отбрасывает расширение
audio.write_audiofile(f'{video_file.stem}.mp3')
