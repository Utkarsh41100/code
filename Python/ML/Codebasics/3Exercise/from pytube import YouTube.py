from pytube import YouTube

def download_youtube_video(url, save_path):
    try:
        # Create a YouTube object with the given URL
        yt = YouTube(url)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Download the video to the specified path
        stream.download(output_path=save_path)
        
        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
video_url = 'https://youtu.be/vsWrXfO3wWw'
download_path = 'D:/Utkarsh'
download_youtube_video(video_url, download_path)
