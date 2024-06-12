import tkinter as tk
from tkinter import messagebox
import random

GREEN = '#27e512'
YELLOW = '#e8ef0e'
GRAY = '#4c4c4c'
FONT = 'Verdana 24'

root = tk.Tk()
root.title('Wordle')
root.geometry("800x600")
root.configure(bg="#0a325e")

words = []
with open('words.txt', 'r') as file:
    words = [word.strip().upper() for word in file.readlines()]

attempts_left = 6
target_word = random.choice(words)
guessed_letters = [''] * len(target_word)

def is_word_guessed():
    return ''.join(guessed_letters) == target_word

def handle_letter(letter):
    global attempts_left
    if attempts_left > 0 and letter not in guessed_letters:
        if letter in target_word:
            for i in range(len(target_word)):
                if target_word[i] == letter:
                    guessed_letters[i] = letter
            if is_word_guessed():
                messagebox.showinfo("Congratulations", f"You guessed '{target_word}'!")
                reset_game()
        else:
            attempts_left -= 1
            if attempts_left == 0:
                messagebox.showinfo("Game Over", f"Out of attempts! The word was '{target_word}'.")
                reset_game()
        update_display()

def reset_game():
    global attempts_left, target_word, guessed_letters
    attempts_left = 6
    target_word = random.choice(words)
    guessed_letters = [''] * len(target_word)
    update_display()

def update_display():
    for widget in root.winfo_children():
        widget.destroy()

    for i in range(len(target_word)):
        letter = guessed_letters[i] if guessed_letters[i] else '_'
        label = tk.Label(root, text=letter, font=FONT, width=3, bg="#0a325e", fg='white')
        label.grid(row=1, column=i, padx=5, pady=20)
        if guessed_letters[i]:
            label.config(fg=GREEN if guessed_letters[i] == target_word[i] else YELLOW)

    row = 2
    col = 0
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        tk.Button(root, text=char, font=FONT, width=3, bg="#1a4b87", fg='white', command=lambda c=char: handle_letter(c)).grid(row=row, column=col, padx=10, pady=10)
        col += 1
        if col == 13:
            row += 1
            col = 0

    tk.Label(root, text=f"Attempts left: {attempts_left}", font='Helvetica 14 bold', bg="#0a325e", fg='white').grid(row=row+1, column=0, columnspan=len(target_word), pady=20)

update_display()

root.mainloop()
