from pytube import YouTube
import streamlit as st

st.title("Youtube Video Downloader")

def Download(link, path):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(path)
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = st.text_input("Enter the link of the video")
# choose the path on your computer
path = st.text_input("Enter the path of the video")

st.download_button ("Download", Download(link, path))
