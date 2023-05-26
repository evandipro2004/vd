import pytube

def download_video(video_url):
    video = pytube.YouTube(video_url)

    # Get the highest resolution available.
    video_stream = video.streams.get_highest_resolution()

    # Download the video.
    video_stream.download()

if __name__ == "__main__":
    video_url = input("Enter the video URL: ")

    download_video(video_url)