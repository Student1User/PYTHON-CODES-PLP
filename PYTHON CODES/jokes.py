import random
import tkinter as tk
from tkinter import messagebox

# List of programming jokes
jokes = [
    "Why do Python programmers prefer dark mode? Because light attracts bugs! 🐛",
    "Why do programmers hate nature? It has too many bugs. 🐞",
    "Why did the Python developer break up with Java? Because he couldn't handle the class differences! 🤣",
    "How do you comfort a JavaScript bug? You console it. 😆",
    "Why do programmers prefer iOS development? Because Android has too many exceptions. 📱",
    "Why was the function feeling sad? It didn’t get any arguments. 😢",
    "Why do Python programmers hate recursion? Because they keep getting StackOverflow errors! 🔄"
]

# Function to display a random joke
def tell_joke():
    joke = random.choice(jokes)
    joke_label.config(text=joke)

# GUI setup
root = tk.Tk()
root.title("Random Joke Generator 🤣")
root.geometry("500x300")
root.configure(bg="lightblue")

# Title Label
title_label = tk.Label(root, text="😂 Random Programming Joke 😂", font=("Arial", 14, "bold"), bg="lightblue")
title_label.pack(pady=10)

# Joke Label
joke_label = tk.Label(root, text="Click the button to get a joke!", font=("Arial", 12), wraplength=400, bg="white", fg="black", relief="solid", padx=10, pady=10)
joke_label.pack(pady=20)

# Joke Button
joke_button = tk.Button(root, text="Get Joke", font=("Arial", 12, "bold"), command=tell_joke, bg="yellow", fg="black")
joke_button.pack()

# Run the GUI loop
root.mainloop()
