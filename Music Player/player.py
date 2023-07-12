import pygame
from tkinter import *
from tkinter import filedialog

# Initialize Pygame
pygame.init()

# Create the main window
window = Tk()
window.title("Music Player")
window.geometry("350x350")
window.resizable(0,0)
window.configure(bg="#000000")

image_icon=PhotoImage(file="m1.png")
window.iconphoto (False, image_icon)

current_track = None
volume = 0.5  # Initial volume

# Function to select a track
def select_track():
    global current_track
    current_track = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("Music Files", "*.mp3")])
    label["text"] = f"Track: {current_track}"

# Function to play the music
def play_music():
    if current_track:
        pygame.mixer.music.load(current_track)
        pygame.mixer.music.play()

# Function to pause the music
def pause_music():
    pygame.mixer.music.pause()

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# Function to increase the volume
def increase_volume():
    global volume
    if volume < 1.0:
        volume += 0.1
        pygame.mixer.music.set_volume(volume)

# Function to decrease the volume
def decrease_volume():
    global volume
    if volume > 0.0:
        volume -= 0.1
        pygame.mixer.music.set_volume(volume)

# Create the UI elements
Label(text="Please Select the Track", font=("verdana bold", 9), height="2",width=25). place (x=70, y=40)


Button(text="Select Track", font=("verdana bold", 8),height="2", width=10, bg="#1089ff", fg="white", bd=2, command=select_track).place(x=135,y=106)
Button(text="Play", font=("verdana bold", 8),height="2", width=20, bg="#27AE60", fg="white", bd=2, command=play_music).place(x=91,y=170)
Button(text="Pause", font=("verdana bold", 8),height="2", width=10, bg="#FF5733", fg="white", bd=2, command=pause_music).place(x=135,y=230)
Button(text="Volume +", font=("verdana bold", 8),height="2", width=10, bg="#FFC300", fg="white", bd=2, command=increase_volume).place(x=262,y=170)
Button(text="Volume -", font=("verdana bold", 8), height="2", width=10, bg="#FFC300", fg="white", bd=2, command=decrease_volume).place(x=0,y=170)

Label(text="Project By Pujan Gampa", font=("verdana bold", 9), height="2",width=43). place (x=0, y=315)

# Start the main loop
window.mainloop()
