import tkinter as tk
import random

# Quiz questions with options and answers
quiz_questions = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".py", ".pt", ".pyt", ".python"],
        "answer": ".py"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "define", "function"],
        "answer": "def"
    },
    {
        "question": "Which of these is NOT a Python data type?",
        "options": ["String", "Tuple", "Dictionary", "Array"],
        "answer": "Array"
    },
    {
        "question": "What will `print(type(10))` output?",
        "options": ["int", "float", "double", "number"],
        "answer": "int"
    },
    {
        "question": "Who developed Python?",
        "options": ["Guido van Rossum", "Elon Musk", "Bill Gates", "Mark Zuckerberg"],
        "answer": "Guido van Rossum"
    }
]

# Shuffle the questions for randomness
random.shuffle(quiz_questions)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Game 🏆")
        self.root.geometry("500x400")
        self.root.configure(bg="lightblue")

        self.score = 0
        self.q_index = 0

        # Title
        self.title_label = tk.Label(root, text="🎮 Python Quiz Game 🎮", font=("Arial", 16, "bold"), bg="lightblue")
        self.title_label.pack(pady=10)

        # Question Label
        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, bg="white", fg="black", relief="solid", padx=10, pady=10)
        self.question_label.pack(pady=20)

        # Buttons for multiple-choice options
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 12), width=25, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        # Score Label
        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 12, "bold"), bg="lightblue")
        self.score_label.pack(pady=10)

        # Next Question Button
        self.next_button = tk.Button(root, text="Next Question", font=("Arial", 12, "bold"), command=self.load_question, state="disabled")
        self.next_button.pack(pady=10)

        # Play Again Button (Hidden initially)
        self.play_again_button = tk.Button(root, text="Play Again", font=("Arial", 12, "bold"), command=self.reset_game)
        
        self.load_question()  # Load the first question

    def load_question(self):
        """Loads the next question in the quiz."""
        if self.q_index < len(quiz_questions):
            question_data = quiz_questions[self.q_index]
            self.question_label.config(text=question_data["question"])
            
            # Shuffle options to randomize answer order
            random.shuffle(question_data["options"])

            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option, state="normal")

            self.next_button.config(state="disabled")
        else:
            self.end_quiz()

    def check_answer(self, selected_index):
        """Checks the answer and updates score."""
        selected_option = self.option_buttons[selected_index].cget("text")
        correct_answer = quiz_questions[self.q_index]["answer"]

        if selected_option == correct_answer:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.question_label.config(text="✅ Correct!", fg="green")
        else:
            self.question_label.config(text=f"❌ Wrong! Correct answer: {correct_answer}", fg="red")

        # Disable buttons after answering
        for btn in self.option_buttons:
            btn.config(state="disabled")

        self.q_index += 1
        self.next_button.config(state="normal")

    def end_quiz(self):
        """Displays final score and shows Play Again button."""
        self.question_label.config(text=f"🎉 Quiz Over! Your final score: {self.score}/{len(quiz_questions)}")
        self.next_button.pack_forget()  # Hide Next button
        self.play_again_button.pack(pady=10)  # Show Play Again button

    def reset_game(self):
        """Resets the quiz for a new game."""
        self.q_index = 0
        self.score = 0
        self.score_label.config(text="Score: 0")
        random.shuffle(quiz_questions)
        self.play_again_button.pack_forget()  # Hide Play Again button
        self.next_button.pack(pady=10)  # Show Next button
        self.load_question()

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
