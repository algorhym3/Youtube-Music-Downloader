from pytube import YouTube
from pytube import Playlist

playlist = Playlist('https://www.youtube.com/watch?v=JGwWNGJdvx8&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj')
playlist.populate_video_urls()
for videoUrl in playlist.video_urls:
    try:    CurrentVideo = YouTube(videoUrl)
    except: print "issue with videoURL :- {0}",videoUrl
    try :
        print CurrentVideo.title
        print CurrentVideo.length
        print videoUrl
        print CurrentVideo.views
        print CurrentVideo.thumbnail_url
    except:
        print ("something went wrong with video url :- {0}",videoUrl)
'''Chess = YouTube('https://www.youtube.com/watch?v=AoYWmQddmpY&t=5217s')
print Chess.streams.all()[0].download()'''