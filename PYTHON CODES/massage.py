import tkinter as tk
import random
import json
import os

# File to save favorite colors
FILENAME = "favorite_colors.json"

# Fun messages list
fun_messages = [
    "Wow, that's a cool color choice! 🎨",
    "Great pick! That color suits you perfectly. 😊",
    "Awesome! That color reminds me of something beautiful! 🌈",
    "Nice choice! It's one of my favorites too! 🌟",
    "Your color choice is amazing! Keep shining! ✨"
]

def load_favorite_colors():
    """Load favorite colors from file."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return {}

def save_favorite_color(name, color):
    """Save the user's favorite color to a file."""
    favorites = load_favorite_colors()
    favorites[name] = color
    with open(FILENAME, "w") as file:
        json.dump(favorites, file, indent=4)

def show_greeting():
    """Display a personalized greeting message with a fun twist."""
    name = name_entry.get().strip()
    color = color_entry.get().strip()

    if name and color:
        save_favorite_color(name, color)
        message = random.choice(fun_messages)
        greeting_label.config(text=f"Hello, {name}! Your favorite color, {color}, is awesome! 🎨\n{message}", fg=color)
        display_favorites()
    else:
        greeting_label.config(text="Please enter both name and color!", fg="red")

def display_favorites():
    """Display saved favorite colors."""
    favorites = load_favorite_colors()
    fav_text = "💖 Favorite Colors 💖\n"
    for user, color in favorites.items():
        fav_text += f"{user}: {color}\n"
    favorites_label.config(text=fav_text)

def launch_gui():
    """Launch the GUI version of the app."""
    global root, name_entry, color_entry, greeting_label, favorites_label

    root = tk.Tk()
    root.title("Personalized Greeting App 👋")
    root.geometry("400x400")
    root.configure(bg="lightblue")

    # Labels & Input Fields
    tk.Label(root, text="Enter your name:", font=("Arial", 12), bg="lightblue").pack(pady=5)
    name_entry = tk.Entry(root, font=("Arial", 12))
    name_entry.pack(pady=5)

    tk.Label(root, text="Enter your favorite color:", font=("Arial", 12), bg="lightblue").pack(pady=5)
    color_entry = tk.Entry(root, font=("Arial", 12))
    color_entry.pack(pady=5)

    # Button to display greeting
    greet_button = tk.Button(root, text="Show Greeting", font=("Arial", 12, "bold"), command=show_greeting, bg="yellow")
    greet_button.pack(pady=10)

    # Label to display the personalized greeting
    greeting_label = tk.Label(root, text="", font=("Arial", 12, "bold"), wraplength=300, bg="white", fg="black", relief="solid", padx=10, pady=10)
    greeting_label.pack(pady=10)

    # Label to display favorite colors
    favorites_label = tk.Label(root, text="💖 Favorite Colors 💖\n", font=("Arial", 12), bg="lightblue", fg="darkblue", justify="left")
    favorites_label.pack(pady=10)

    display_favorites()  # Show saved favorites

    # Run the Tkinter main loop
    root.mainloop()

# Console Version
name = input("What is your name? ").strip()
color = input("What is your favorite color? ").strip()

if name and color:
    save_favorite_color(name, color)
    print(f"Hello, {name}! Your favorite color, {color}, is awesome! 🎨")
    print(random.choice(fun_messages))  # Display a random fun message

    # Show saved favorite colors
    favorites = load_favorite_colors()
    print("\n💖 Favorite Colors 💖")
    for user, fav_color in favorites.items():
        print(f"{user}: {fav_color}")
else:
    print("Please enter both your name and favorite color.")

# Ask if the user wants to launch the GUI version
choice = input("\nDo you want to try the GUI version? (yes/no): ").strip().lower()
if choice == "yes":
    launch_gui()
else:
    print("Goodbye! Have a great day! 😊")
