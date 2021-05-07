from pytube import YouTube

class Downloader:

    def __init__(self, downloadlink):
        self.downloadlink = downloadlink
        self.youtubelink = YouTube(self.downloadlink)

    def download(self):
        print("Title: ",self.youtubelink.title)
        print("Number of views: ",self.youtubelink.views)
        print("Length of video: ",self.youtubelink.length,"seconds")
        print("Ratings: ",self.youtubelink.rating)
        print("----------------------------------------------")
        ys = self.youtubelink.streams.get_highest_resolution()
        ys.download()


