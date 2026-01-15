import yt_dlp
from pathlib import Path

homeDirectory = Path.home()


def downloadVideo(videoURL, save_path=f"{homeDirectory}/Downloads/Yt-dlp/Video"):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': f"{save_path}/%(title)s.%(ext)s",
        'noplaylist': True
    }
    
    try: 
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: # type: ignore (vs code is being a bitch ignore this please)
            ydl.download([videoURL])
        print(f"Successfully downloaded {videoURL}")
    except Exception as e:
        print(f"an error occured: {e}")
        
def downloadAudio(videoURL, save_path=f"{homeDirectory}/Downloads/Yt-dlp/Audio"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            
        }],
        'outtmpl': f"{save_path}/%(title)s.%(ext)s",
        'noplaylist': True
    }
    
    try: 
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: # type: ignore (vs code is being a bitch ignore this please)
            ydl.download([videoURL])
        print(f"Successfully downloaded {videoURL}")
    except Exception as e:
        print(f"an error occured: {e}")
