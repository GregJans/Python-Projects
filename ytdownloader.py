import pytube

p = pytube.Playlist("https://www.youtube.com/playlist?list=PLqGhVyOFc2J3Lt23F5b8RctjHYDwxx_QN")

for video in p.videos:
    print(f"Downloading {video.title}")
    video.streams.filter(only_audio=True, mime_type="audio/mp4").first().download("C:/Users/gtj08/OneDrive/Documents/Music/Star Wars Ep3")
