import tkinter as tk
import customtkinter
from pytube import YouTube
import threading
import os

def startDownload():
    def download_video():
        try:
            ytLink = link.get()
            ytObject = YouTube(ytLink)
            video = ytObject.streams.get_highest_resolution()

            # Set the download path to ~/Downloads
            download_path = os.path.expanduser('~/Downloads')
            video.download(output_path=download_path)

            print('Download complete')
        except Exception as e:
            print('Error:', e)

    download_thread = threading.Thread(target=download_video)
    download_thread.start()

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

title = customtkinter.CTkLabel(app, text='Insert a valid YouTube Link')
title.pack(padx=10, pady=10)

link = customtkinter.CTkEntry(app, width=400, height=40)
link.pack()

download = customtkinter.CTkButton(app, text='Download', command=startDownload)
download.pack()

app.mainloop()
