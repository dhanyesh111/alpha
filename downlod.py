import requests
import pytube
url = input()
data = requests.get(url.get())
f = open(f"{downloadName.get()}.jpg", "wb")
f.write(data.content)
f.close()
downlodBtn = Button(self.windos, text="start",command=start)
downlodBtn.pack()

 video_url = 'https://youtu.be/mS60nG6bJwo'
 youtube = pytube.YouTube(video_url)
 video = youtube.streams.first()
video.download("hai.mp4")