#note you might have to install ffmpeg for media conversion
#you can also use pytubefix or pytube also
import yt_dlp #Youtube downloader 
import tkinter as tk #GUI
from tkinter import filedialog

def download_video(url, save_path): #takes url and save_path from the user
    try:
        ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4', #merges webm and mp4 using ffmpeg
        'keepvideo': True  # Keeps original files
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: #yt_dlp is a downloader instance
            ydl.download([url])
            print("Video downloaded successfully!")
    except Exception as e:
        print(f"Error: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory() #opens the directory in which we want to save the vid in
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk() #.Tk represents mostly the main window of an application
    root.withdraw()#hides the main window instead of displaying it

    video_url = input("Enter the YouTube video URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Starting download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
