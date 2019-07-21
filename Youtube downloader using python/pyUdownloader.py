import pafy

url = "https://www.youtube.com/watch?v=N_iW0VC3IdI"
video = pafy.new(url)

streams = video.videostreams
for i in streams:
    print(i)

# get best resolution regardless of format
best = video.getbest()

print(best.resolution, best.extension)
print(best.get_filesize())

# Download the video
best.download()