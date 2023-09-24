# This code allows the user to input a YouTube video URL and then uses the pytube library
# to download the video stream with the highest resolution from that URL.

# Import the pytube library for downloading YouTube videos
import pytube

# Prompt the user to enter a YouTube URL
video_url = input("Enter Youtube URL(last code): ")
video_url = "https://www.youtube.com/watch?v=" + video_url
print(video_url)

# Create a pytube video instance for the provided URL
video_instance = pytube.YouTube(video_url)

# Get the stream with the highest resolution for the video
stream = video_instance.streams.get_highest_resolution()

# Download the video stream
stream.download()