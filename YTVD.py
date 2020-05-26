import os
import numpy
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import pytube
import time
from moviepy.video.io.VideoFileClip import VideoFileClip
import PySimpleGUI as sg

def downloadVideo(videoUrl, convertMP3, saveLocation):
    sg.Popup("Downloading: " + videoUrl, "Save Location: " + saveLocation, "Note: The window may say Not responding. That is normal, just wait", "", "Press Ok to being download", line_width=1000)
    
    try:
        videoDownloaded = pytube.YouTube(videoUrl).streams.first().download(saveLocation)
    except pytube.exceptions.RegexMatchError:
        sg.Popup("Invalid URL", videoUrl + " is not a vlid video URL", line_width=1000)
        return
    except Exception as erro:
        sg.Popup("Download Failed", "Could not download video: " + str(erro), line_width=1000)
        return
    
    if convertMP3:
        videoTMP = VideoFileClip(videoDownloaded)
        videoTMP.audio.write_audiofile(videoDownloaded + ".mp3")
        sg.Popup("Download was Successfull", "Downloaded: " + videoDownloaded, "Saved To: " + saveLocation + "/" + videoDownloaded + ".mp3")
        return

    sg.Popup("Download was Successfull", "Downloaded: " + videoDownloaded, "Saved To: " + saveLocation + "/" + videoDownloaded)

sg.theme('Dark Blue 3')
layout = [
    [sg.Text("", size=(11,0)), sg.Text("YouTube Video Downloader", size=(25, 0), font=("Helvetica", 25))],
    [sg.Text("YouTube Video URL: "), sg.InputText("", size=(40,0)), sg.Checkbox("Convert MP3")],
    [sg.Text("Save Location: "), sg.InputText("", size=(52,0)), sg.FolderBrowse("Browse")],
    [sg.Text("", size=(15,0)), sg.Button("Download", size=(40,0))],
    [sg.Text("")],
    [sg.Text("Created by @IWickGames, GitHub.com/iwickgames"), sg.Text("", size=(25,0)), sg.Button("Cancel")]
]
window = sg.Window('YouTube Video Downloader     V1.0', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    downloadVideo(values[0], values[1], values[2])
    pass

window.close()