import tkinter as tk
from tkinter import messagebox
import random

class Crossword:
    def __init__(self, words):
        self.words = words
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
        self.place_words()

    def place_words(self):
        for word in self.words:
            direction = random.choice(['across', 'down'])
            if direction == 'across':
                x = random.randint(0, 10 - len(word))
                y = random.randint(0, 9)
                for i, letter in enumerate(word):
                    self.board[y][x + i] = letter
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 10 - len(word))
                for i, letter in enumerate(word):
                    self.board[y + i][x] = letter

    def check_completion(self):
        return all(letter != ' ' for row in self.board for letter in row)

class CrosswordGUI(tk.Tk):
    def __init__(self, crossword):
        super().__init__()
        self.crossword = crossword
        self.title("Crossword Puzzle Game")
        self.geometry("300x300")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Crossword Puzzle Game")
        self.label.pack()

        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.pack()

        self.display_board()

        self.entry_label = tk.Label(self, text="Enter your guess (row column direction word):")
        self.entry_label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_guess)
        self.submit_button.pack()

    def display_board(self):
        for i, row in enumerate(self.crossword.board):
            for j, letter in enumerate(row):
                self.canvas.create_text(j * 30 + 15, i * 30 + 15, text=letter, font=("Arial", 12), tags="board")

    def submit_guess(self):
        guess = self.entry.get().split()
        if len(guess) == 4:
            row, col, direction, word = map(str, guess)

            if direction.lower() == 'across':
                for i, letter in enumerate(word):
                    self.crossword.board[int(row)][int(col) + i] = letter
            elif direction.lower() == 'down':
                for i, letter in enumerate(word):
                    self.crossword.board[int(row) + i][int(col)] = letter

            self.canvas.delete("board")
            self.display_board()

            if self.crossword.check_completion():
                messagebox.showinfo("Congratulations!", "You completed the crossword puzzle!")
                self.destroy()
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid guess.")

def play_crossword_gui():
    words = ['python', 'crossword', 'game', 'code', 'example']
    crossword = Crossword(words)

    app = CrosswordGUI(crossword)
    app.mainloop()

if __name__ == "__main__":
    play_crossword_gui()
