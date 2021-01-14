import pytube

print("Enter video URLs")
videos = []
while True:
    url = input("")
    if url == "OKAY":
        break
    videos.append(url)

for indexnum, video in enumerate(videos):
    down = pytube.YouTube(video)
    stream = down.streams.get_by_itag(22)
    print(f"Downloading video {indexnum}")
    stream.download()
    print("The download is complete")
