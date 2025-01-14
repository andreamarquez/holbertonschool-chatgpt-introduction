#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()
        if self.check_win():
            print("Congratulations! You've won the game.")

    def count_mines_nearby(self, x, y):
        count = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                    if (y + dy) * self.width + (x + dx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if self.revealed[y][x]:
            return True
        self.revealed[y][x] = True
        if (y * self.width + x) in self.mines:
            return False
        if self.count_mines_nearby(x, y) == 0:
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                        self.reveal(x + dx, y + dy)
        return True

    def check_win(self):
        for y in range(self.height):
            for x in range(self.width):
                if not self.revealed[y][x] and (y * self.width + x) not in self.mines:
                    return False
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                if self.check_win():
                    self.print_board()
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
