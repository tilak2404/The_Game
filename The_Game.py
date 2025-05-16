import tkinter as tk
import random

# List of choices
choices = ['Rock', 'Paper', 'Scissors']

# Score variables
user_score = 0
computer_score = 0

# Function to play the game
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        user_score += 1
        result = "You Win!"
    else:
        computer_score += 1
        result = "You Lose!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score: You - {user_score} | Computer - {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text="Score: You - 0 | Computer - 0")

# GUI setup
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("500x500")
root.configure(bg="black")

# Title Label
title_label = tk.Label(root, text="Choose Rock, Paper or Scissors", font=("Arial", 14), bg="black", fg="white")
title_label.pack(pady=20)

# Buttons
rock_btn = tk.Button(root, text="Rock", width=15, command=lambda: play('Rock'))
rock_btn.pack(pady=10)

paper_btn = tk.Button(root, text="Paper", width=15, command=lambda: play('Paper'))
paper_btn.pack(pady=10)

scissors_btn = tk.Button(root, text="Scissors", width=15, command=lambda: play('Scissors'))
scissors_btn.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), fg="cyan", bg="black")
result_label.pack(pady=20)

# Score label
score_label = tk.Label(root, text="Score: You - 0 | Computer - 0", font=("Arial", 12, "bold"), fg="yellow", bg="black")
score_label.pack(pady=10)

# Reset Button
reset_btn = tk.Button(root, text="Reset Game", width=15, bg="red", fg="white", command=reset_game)
reset_btn.pack(pady=20)

# Run the GUI
root.mainloop()
