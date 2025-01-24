import os
import re
from pytubefix import YouTube
from pytubefix.exceptions import PytubeFixError

def main():
    url = input("Please enter a YouTube URL: ")
    format = 'mp3'   # support mp3/m4a, default is mp3
    yt_mp3_download(url, format)
    
def yt_mp3_download(url, format='mp3'):
    output_folder = format.upper()
    os.makedirs(output_folder, exist_ok=True)
    
    try:
        yt = YouTube(url)
        print('Video Title: ', yt.title)
        
        better_title = re.sub(r'[<>:"/\\|?*]', '', yt.title)
        
        print("Downloading audio...")
        ys = yt.streams.get_audio_only()
        ys.download(output_path=output_folder, filename=f"{better_title}.{format}", skip_existing=True)
        
        output_path = os.path.join(output_folder, f"{better_title}.{format}")
        print(f"Audio has been correctly downloaded {output_path}")
    except PytubeFixError as e:
        print(f"PyTube Error: {e}")
    except ValueError as e:
        print(f"Process Error: {e}")
    except Exception as e:
        print(f"Unknow Error: {e}")

if __name__ == "__main__":
    main()