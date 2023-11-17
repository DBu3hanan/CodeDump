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

    def display(self):
        for row in self.board:
            print(' '.join(row))
        print()

def play_crossword():
    words = ['python', 'crossword', 'game', 'code', 'example']
    crossword = Crossword(words)

    print("Welcome to the Crossword Puzzle Game!\n")
    crossword.display()

    while True:
        guess = input("Enter your guess (row column direction word): ").split()
        row, col, direction, word = map(str, guess)

        if direction.lower() == 'across':
            for i, letter in enumerate(word):
                crossword.board[int(row)][int(col) + i] = letter
        elif direction.lower() == 'down':
            for i, letter in enumerate(word):
                crossword.board[int(row) + i][int(col)] = letter

        crossword.display()

        if all(letter != ' ' for row in crossword.board for letter in row):
            print("Congratulations! You completed the crossword puzzle!")
            break

if __name__ == "__main__":
    play_crossword()
