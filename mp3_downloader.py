from pytube import YouTube


while True:
    yt=YouTube((input("Enter link\n")))
    video = yt.streams.filter(only_audio=True).first()
    video.download("mp3")
    print("Done")

