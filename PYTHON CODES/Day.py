# Import necessary modules
import random  # Generates random numbers

# Function to write a message to a file
def write_to_file():
    """Writes a simple message to a file."""
    file = open("example.txt", "w")  # Open file in write mode
    file.write("Hello, this is a test message!")  # Write message
    file.close()  # Close the file
    print("Message written to example.txt")

# Function to read from a file
def read_from_file():
    """Reads content from a file and prints it."""
    try:
        file = open("example.txt", "r")  # Open file in read mode
        content = file.read()  # Read file content
        file.close()  # Close the file
        print("Reading from file:")
        print(content)  # Print file content
    except FileNotFoundError:
        print("File not found.")  # Handle missing file

# Class to represent a Person
class Person:
    """Represents a person with a name and age."""
    def __init__(self, name, age):
        self.name = name  # Store name
        self.age = age  # Store age

    def greet(self):
        """Prints a greeting message."""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Simple number guessing game
def play_guessing_game():
    """A simple number guessing game."""
    secret_number = random.randint(1, 10)  # Generate a random number
    print("Guess a number between 1 and 10.")
    
    attempts = 3  # Allow the user 3 attempts
    
    for attempt in range(attempts):
        try:
            guess = int(input("Enter your guess: "))  # Get user input
            if guess == secret_number:
                print("Congratulations! You guessed correctly.")
                return
            elif guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print(f"Sorry, the correct number was {secret_number}.")

# Main execution area
if __name__ == "__main__":
    person = Person("John", 25)  # Create a Person instance
    person.greet()  # Call the greet method
    
    write_to_file()  # Write message to file
    read_from_file()  # Read and print file content
    
    play_guessing_game()  # Start the guessing game
