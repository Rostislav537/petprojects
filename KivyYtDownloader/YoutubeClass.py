from pytube import YouTube
class YouTubeDispatcher:
    def __init__(self):
        pass
    def downloadVideo(self, url, resolution, outpath) -> str:
        """Download video with options:
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
        """Get information about video"""
        yt_object = YouTube(url)
        streams=yt_object.streams
        resolutions_video = sorted(set(stream.resolution for stream in streams.filter(type='video')), reverse=True, key=lambda s: int(s.split('p')[0]))
        out_dict={"title":yt_object.title,
                  "img_path":yt_object.thumbnail_url,
                  "author":yt_object.author,
                  "video_streams":resolutions_video}
        print(out_dict)
        return out_dict
f=YouTubeDispatcher()
f.searchVideo("https://www.youtube.com/watch?v=ZuW_sMSrEXg&t=0s&ab_channel=GalileoRU")
f.downloadVideo("https://www.youtube.com/watch?v=GnlFmiLuVXc&ab_channel=ViteC%E2%96%BAPlay", "360p", "D:\DownloadS")