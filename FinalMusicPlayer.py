# Importing all files 
import os
import tkinter as tk
import pygame
from PIL import Image, ImageTk

# Setting up the GUI window 
class MusicPlayer(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("860x620")
        self.master.configure(background="brown")
        self.master.resizable(False, False)

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Set up music list 
        self.music_list = []
        for filename in os.listdir("Music"):
            if filename.endswith(".mp3"):
                self.music_list.append(filename)

        # Set up current song index
        self.current_song = 0

        # Set up album art
        self.album_art = Image.open("awesome.jpg")
        self.album_art = self.album_art.resize((450, 430))
        self.album_art_tk = ImageTk.PhotoImage(self.album_art)

        # Set up GUI elements with their button labels 
        self.album_art_label = tk.Label(self.master, image=self.album_art_tk)
        self.album_art_label.pack(side=tk.TOP, pady=10)

        self.song_title_label = tk.Label(self.master, text=self.music_list[self.current_song], font=("serif", 18))
        self.song_title_label.pack(side=tk.TOP)

        self.controls_frame = tk.Frame(self.master)
        self.controls_frame.pack(side=tk.TOP, pady=10)

        self.last_button = tk.Button(self.controls_frame, text="<<", command=self.play_last, font=("serif", 12), bg="white", fg="black", relief=tk.FLAT, width=8)
        self.last_button.pack(side=tk.LEFT, padx=5)

        self.play_button = tk.Button(self.controls_frame, text="Play", command=self.play_music, font=("serif", 12), bg="white", fg="black", relief=tk.FLAT, width=8)
        self.play_button.pack(side=tk.LEFT, padx=5)

        self.pause_button = tk.Button(self.controls_frame, text="Pause", command=self.pause_music, font=("serif", 12), bg="white", fg="black", relief=tk.FLAT, width=8)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        self.next_button = tk.Button(self.controls_frame, text=">>", command=self.play_next, font=("serif", 12), bg="white", fg="black", relief=tk.FLAT, width=8)
        self.next_button.pack(side=tk.LEFT, padx=5)

    # defining the play_music element so that the songs will play from the folder 
    def play_music(self):
        pygame.mixer.music.load("Music/"+ self.music_list[self.current_song])
        pygame.mixer.music.play()

    # defining all the buttons to work when the user clicks on them 

    def pause_music(self):
        pygame.mixer.music.pause()

    # the self.current_song element variable, retrieves the current song's information in the GUI 
    def play_next(self):
        self.current_song = (self.current_song + 1) % len(self.music_list)
        self.song_title_label.config(text=self.music_list[self.current_song])
        self.album_art = Image.open("awesome.jpg")  
        self.album_art = self.album_art.resize((450, 430))
        self.album_art_tk = ImageTk.PhotoImage(self.album_art)
        self.album_art_label.config(image=self.album_art_tk)
        self.play_music()

    # allows the user to play the last song again 
    def play_last(self):
        self.current_song = (self.current_song - 1) % len(self.music_list)
        self.song_title_label.config(text=self.music_list[self.current_song])
        self.album_art = Image.open("awesome.jpg")  
        self.album_art = self.album_art.resize((450, 430))
       
# Execute the music player using Tkinter 
root = tk.Tk()
player = MusicPlayer(root)
player.pack()
root.mainloop()