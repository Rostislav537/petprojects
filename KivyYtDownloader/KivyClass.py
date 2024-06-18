import pytube
import ffmpeg

# Получить URL видео
url = "https://www.youtube.com/watch?v=voMCTIBTi8U"

# Создать объект YouTube
yt = pytube.YouTube(url)

# Получить информацию о видео
video = yt.streams.first()  # Получите первый доступный поток

# Загрузить видео в любом качестве
video.download()

# Получить путь к загруженному видео
video_path = video.default_filename

# Конвертировать видео в 144p 3gp
ffmpeg.input(fr"C:\Users\Driver707\PycharmProjects\kivyDev\{video.title}").output("my_video.3gp", format="3gp", preset="veryfast", vcodec="mpeg4", qscale=1, acodec="aac", aq=2).run()