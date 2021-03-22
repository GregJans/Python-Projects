import pytube

url = "insert playlist url here"
dl_location = "insert directory here where to download the files"

p = pytube.Playlist(url)

for video in p.videos:
    print(f"Downloading {video.title}")
    # change filter perameters acordingly
    video.streams.filter(only_audio=True, mime_type="audio/mp4").first().download(dl_location)
