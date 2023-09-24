"""
Author: SantosXPC
Date: 24/09/2023
Description: This code allows the user to input a YouTube video URL and then uses the pytube library to download the video stream with the highest resolution from that URL.

Usage: Run the code, copy and paste the last code of any Youtube video, i.e. https://www.youtube.com/watch?v=J3_UPuNxx74, just copy+paste "J3_UPuNxx74" code.

License: GNU General Public License (GPL)

"""

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