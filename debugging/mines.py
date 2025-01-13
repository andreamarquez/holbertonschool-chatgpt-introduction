#!/usr/bin/env python3

import random

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = mines
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.place_mines()
        self.calculate_numbers()
        self.non_mine_cells = width * height - mines

    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] != -1:
                self.board[y][x] = -1
                mines_placed += 1

    def calculate_numbers(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == -1:
                    continue
                self.board[y][x] = self.count_mines_nearby(x, y)

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.board[ny][nx] == -1:
                    count += 1
        return count

    def print_board(self, reveal=False):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if self.board[y][x] == -1:
                        row += "* "
                    else:
                        row += f"{self.board[y][x]} "
                else:
                    row += ". "
            print(row)
        print()

    def reveal(self, x, y):
        if self.revealed[y][x]:
            return True
        if self.board[y][x] == -1:
            return False
        self.revealed[y][x] = True
        self.non_mine_cells -= 1
        if self.board[y][x] == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
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
                if self.non_mine_cells == 0:
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
    