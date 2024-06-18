from pytube import YouTube
class YouTubeDispatcher:
    def __init__(self):
        pass
    def downloadVideo(self, url, resolution, outpath) -> str:
        """Опции для скачивания видео:
                *resolution
                *file_extension
                *outpath
                *name
        """
        yt_object = YouTube(url)
        print(yt_object.streams)
        stream=yt_object.streams.filter(res=resolution).first()
        print(stream)
        stream.download(output_path=outpath)

        return f"{outpath}"

    def searchVideo(self, url) -> dict:
        """Получает информацию о видео"""
        yt_object = YouTube(url)
        streams=yt_object.streams
        resolutions_video = sorted(set(stream.resolution for stream in streams.filter(type='video')), reverse=True, key=lambda s: int(s.split('p')[0]))
        out_dict={"title":yt_object.title,
                  "img_path":yt_object.thumbnail_url,
                  "author":yt_object.author,
                  "video_streams":resolutions_video}
        print(out_dict)
        return out_dict

