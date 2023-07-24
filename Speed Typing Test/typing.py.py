import time
import tkinter as tk
from tkinter import messagebox

class SpeedTypingTest(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Speed Typing Test")
        self.geometry("400x300")
        self.configure(bg="Black")
        self.resizable(False, False)
        self.sentence = "Twinkle, Twinkle, little star."
        self.typing_started = False
        self.label = tk.Label(self, text="TYPE THE FOLLOWING SENTENCE :", font=("Verdana bold", 12))
        self.label.pack(pady=20)
        self.sentence_label = tk.Label(self, text=self.sentence, font=("Arial", 12, "bold"), wraplength=500)
        self.sentence_label.pack(pady=10)
        self.start_button = tk.Button(self, text="Start Typing", command=self.start_typing, bd=2, bg="#4CAF50", fg="white", font=("Arial", 14))
        self.start_button.pack(pady=30)

    def calculate_typing_speed(self, time_taken):
        return (len(self.sentence.split()) / time_taken) * 60

    def start_typing(self):
        if not self.typing_started:
            self.typing_started = True
            self.start_time = time.time()
            self.user_input = tk.StringVar()
            self.input_entry = tk.Entry(self, textvariable=self.user_input, font=("Arial", 14), width=40)
            self.input_entry.pack(pady=10)
            self.input_entry.focus_set()
            self.input_entry.bind("<Return>", self.end_typing)
            self.start_button.config(text="Submit", bd= 2,font=("Verdana bold", 12),bg="#FF5722")
        else:
            self.end_typing()

    def end_typing(self, event=None):
        if not self.typing_started:
            return
        self.typing_started = False
        self.end_time = time.time()
        user_input_text = self.user_input.get()
        result = "correctly" if user_input_text == self.sentence else "incorrectly"
        time_taken = self.end_time - self.start_time
        typing_speed = self.calculate_typing_speed(time_taken)
        messagebox.showinfo("Speed Typing Test", f"Time taken: {round(time_taken, 2)} seconds\nYour typing speed: {round(typing_speed, 2)} WPM\nYou typed the sentence {result}.")
        self.start_button.config(text="Start Typing", bg="#4CAF50")
        self.input_entry.destroy()

if __name__ == "__main__":
    app = SpeedTypingTest()
    app.mainloop()
