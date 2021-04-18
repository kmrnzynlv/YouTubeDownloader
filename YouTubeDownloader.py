from pytube import YouTube

link = input("Enter the YouTube URL: ")
yt = YouTube(link)
videos = yt.streams

video = list(enumerate(videos))
for i in video:
     print(i)

dn_option = int(input(" Enter the Number: "))
dn_video = videos[dn_option]
dn_video.download()

print ("Downloaded Successfully, Check Your Folder")

