import tkinter as tk
from tkinter import messagebox

def sum_of_list():
    user_input = entry_list.get()
    try:
        num_list = list(map(int, user_input.split()))
        result = sum(num_list)
        messagebox.showinfo("Sum of List", f"The sum of the list is: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers separated by spaces.")

def show_books():
    books = ("Book 1", "Book 2", "Book 3", "Book 4", "Book 5")
    messagebox.showinfo("Favorite Books", "\n".join(books))

def store_person_info():
    name = entry_name.get()
    age = entry_age.get()
    color = entry_color.get()
    if name and age.isdigit() and color:
        person_info = {"Name": name, "Age": int(age), "Favorite Color": color}
        messagebox.showinfo("Person Info", str(person_info))
    else:
        messagebox.showerror("Error", "Please enter valid information.")

def common_elements():
    set1_input = entry_set1.get()
    set2_input = entry_set2.get()
    try:
        set1 = set(map(int, set1_input.split()))
        set2 = set(map(int, set2_input.split()))
        common = set1.intersection(set2)
        messagebox.showinfo("Common Elements", f"Common elements: {common}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers separated by spaces.")

def odd_length_words():
    words = entry_words.get().split()
    odd_words = [word for word in words if len(word) % 2 != 0]
    messagebox.showinfo("Odd Length Words", f"Words with odd lengths: {', '.join(odd_words)}")

# UI Setup
root = tk.Tk()
root.title("Python Tasks UI")
root.geometry("400x500")

# Sum of List
tk.Label(root, text="Enter numbers separated by space:").pack()
entry_list = tk.Entry(root)
entry_list.pack()
tk.Button(root, text="Compute Sum", command=sum_of_list).pack()

# Favorite Books
tk.Button(root, text="Show Favorite Books", command=show_books).pack()

# Person Info
tk.Label(root, text="Enter Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()
tk.Label(root, text="Enter Age:").pack()
entry_age = tk.Entry(root)
entry_age.pack()
tk.Label(root, text="Enter Favorite Color:").pack()
entry_color = tk.Entry(root)
entry_color.pack()
tk.Button(root, text="Store Person Info", command=store_person_info).pack()

# Common Elements in Sets
tk.Label(root, text="Enter Set 1 (space-separated integers):").pack()
entry_set1 = tk.Entry(root)
entry_set1.pack()
tk.Label(root, text="Enter Set 2 (space-separated integers):").pack()
entry_set2 = tk.Entry(root)
entry_set2.pack()
tk.Button(root, text="Find Common Elements", command=common_elements).pack()

# Odd Length Words
tk.Label(root, text="Enter words separated by space:").pack()
entry_words = tk.Entry(root)
entry_words.pack()
tk.Button(root, text="Find Odd Length Words", command=odd_length_words).pack()

root.mainloop()
