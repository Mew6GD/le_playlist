import tkinter as tk
from tkinter import filedialog
import pygame.mixer

class Song:
    def __init__(self):
        pass


song1, song2 = Song(), Song()
playlist = [song1, song2]

def shuffle():
    pass

def next():
    pass

def previous():
    pass

pygame.mixer.init()
root=tk.Tk()
root.title("Pokemon Playlist")

def open_mp3():
    global mp3_file_path
    mp3_file_path = filedialog.askopenfilename(filetypes=[("Pokemon Playlist","songs\*.mp3")])
    if mp3_file_path:
        # file_label.config(text=f"Selected: {mp3_file_path.split('/')(-1)}")
        print("Path found")

