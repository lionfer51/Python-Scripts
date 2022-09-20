from pytube import Playlist
import msvcrt
enlace="https://www.youtube.com/watch?v=YifEjhKf2pM&list=PLNu0KtNPXTjJVk17JzJR1xaJ5OXzPyRVR&ab_channel=TempleSour"

p=Playlist(enlace)

print(f'Downloading: {p.title}')
#Downloading: Python Tutorial for Beginers (For Absolute Beginners)
for video in p.videos:
    print(video.title)
    #video.streams.filter(res='720p')[-1].download("D:/")
    video.streams.get_highest_resolution().download("D:/")
    print("Descargado c:")