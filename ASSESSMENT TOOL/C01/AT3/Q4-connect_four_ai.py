import tkinter as tk
from tkinter import messagebox
import math
import random

ROWS = 6
COLUMNS = 7
CELL_SIZE = 75

EMPTY = 0
HUMAN = 1
AI = 2


class ConnectFourAI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four AI Challenge")

        self.board = [
            [EMPTY for _ in range(COLUMNS)]
            for _ in range(ROWS)
        ]

        self.game_over = False

        tk.Label(
            root,
            text="CONNECT FOUR – HUMAN VS AI",
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        self.status_label = tk.Label(
            root,
            text="Your Turn – Click Any Column",
            font=("Arial", 14, "bold")
        )
        self.status_label.pack(pady=5)

        self.canvas = tk.Canvas(
            root,
            width=COLUMNS * CELL_SIZE,
            height=ROWS * CELL_SIZE,
            bg="blue"
        )
        self.canvas.pack(padx=20, pady=10)

        self.canvas.bind("<Button-1>", self.human_move)

        tk.Button(
            root,
            text="Reset Game",
            font=("Arial", 13, "bold"),
            command=self.reset_game
        ).pack(pady=10)

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")

        for row in range(ROWS):
            for column in range(COLUMNS):
                x1 = column * CELL_SIZE + 7
                y1 = row * CELL_SIZE + 7
                x2 = x1 + CELL_SIZE - 14
                y2 = y1 + CELL_SIZE - 14

                value = self.board[row][column]

                if value == HUMAN:
                    colour = "red"
                elif value == AI:
                    colour = "yellow"
                else:
                    colour = "white"

                self.canvas.create_oval(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=colour,
                    outline="black",
                    width=2
                )

    def human_move(self, event):
        if self.game_over:
            return

        column = event.x // CELL_SIZE

        if column < 0 or column >= COLUMNS:
            return

        if not self.is_valid_column(self.board, column):
            self.status_label.config(
                text="Column is full. Select another column."
            )
            return

        row = self.get_open_row(self.board, column)
        self.board[row][column] = HUMAN
        self.draw_board()

        if self.winning_move(self.board, HUMAN):
            self.game_over = True
            self.status_label.config(text="You Won!")
            messagebox.showinfo(
                "Game Over",
                "Congratulations! You connected four pieces."
            )
            return

        if self.board_full(self.board):
            self.game_over = True
            self.status_label.config(text="Game Draw!")
            messagebox.showinfo("Game Over", "The game is a draw.")
            return

        self.status_label.config(text="AI is thinking...")
        self.root.update()

        self.root.after(500, self.ai_move)

    def ai_move(self):
        if self.game_over:
            return

        column, score = self.minimax(
            self.board,
            depth=5,
            alpha=-math.inf,
            beta=math.inf,
            maximizing=True
        )

        if column is None:
            valid_columns = self.get_valid_columns(self.board)

            if valid_columns:
                column = random.choice(valid_columns)

        if column is not None:
            row = self.get_open_row(self.board, column)
            self.board[row][column] = AI

        self.draw_board()

        if self.winning_move(self.board, AI):
            self.game_over = True
            self.status_label.config(text="AI Won!")
            messagebox.showinfo(
                "Game Over",
                "The AI connected four pieces."
            )
            return

        if self.board_full(self.board):
            self.game_over = True
            self.status_label.config(text="Game Draw!")
            messagebox.showinfo("Game Over", "The game is a draw.")
            return

        self.status_label.config(
            text="Your Turn – Click Any Column"
        )

    def is_valid_column(self, board, column):
        return board[0][column] == EMPTY

    def get_open_row(self, board, column):
        for row in range(ROWS - 1, -1, -1):
            if board[row][column] == EMPTY:
                return row

        return None

    def get_valid_columns(self, board):
        return [
            column
            for column in range(COLUMNS)
            if self.is_valid_column(board, column)
        ]

    def board_full(self, board):
        return len(self.get_valid_columns(board)) == 0

    def copy_board(self, board):
        return [row[:] for row in board]

    def winning_move(self, board, piece):
        # Horizontal check
        for row in range(ROWS):
            for column in range(COLUMNS - 3):
                if (
                    board[row][column] == piece
                    and board[row][column + 1] == piece
                    and board[row][column + 2] == piece
                    and board[row][column + 3] == piece
                ):
                    return True

        # Vertical check
        for column in range(COLUMNS):
            for row in range(ROWS - 3):
                if (
                    board[row][column] == piece
                    and board[row + 1][column] == piece
                    and board[row + 2][column] == piece
                    and board[row + 3][column] == piece
                ):
                    return True

        # Downward diagonal check
        for row in range(ROWS - 3):
            for column in range(COLUMNS - 3):
                if (
                    board[row][column] == piece
                    and board[row + 1][column + 1] == piece
                    and board[row + 2][column + 2] == piece
                    and board[row + 3][column + 3] == piece
                ):
                    return True

        # Upward diagonal check
        for row in range(3, ROWS):
            for column in range(COLUMNS - 3):
                if (
                    board[row][column] == piece
                    and board[row - 1][column + 1] == piece
                    and board[row - 2][column + 2] == piece
                    and board[row - 3][column + 3] == piece
                ):
                    return True

        return False

    def evaluate_window(self, window, piece):
        score = 0

        if piece == AI:
            opponent = HUMAN
        else:
            opponent = AI

        if window.count(piece) == 4:
            score += 100

        elif (
            window.count(piece) == 3
            and window.count(EMPTY) == 1
        ):
            score += 5

        elif (
            window.count(piece) == 2
            and window.count(EMPTY) == 2
        ):
            score += 2

        if (
            window.count(opponent) == 3
            and window.count(EMPTY) == 1
        ):
            score -= 6

        return score

    def score_position(self, board, piece):
        score = 0

        # Give preference to centre column
        centre_column = [
            board[row][COLUMNS // 2]
            for row in range(ROWS)
        ]

        score += centre_column.count(piece) * 3

        # Horizontal scoring
        for row in range(ROWS):
            row_values = board[row]

            for column in range(COLUMNS - 3):
                window = row_values[column:column + 4]
                score += self.evaluate_window(window, piece)

        # Vertical scoring
        for column in range(COLUMNS):
            column_values = [
                board[row][column]
                for row in range(ROWS)
            ]

            for row in range(ROWS - 3):
                window = column_values[row:row + 4]
                score += self.evaluate_window(window, piece)

        # Downward diagonal scoring
        for row in range(ROWS - 3):
            for column in range(COLUMNS - 3):
                window = [
                    board[row + index][column + index]
                    for index in range(4)
                ]

                score += self.evaluate_window(window, piece)

        # Upward diagonal scoring
        for row in range(3, ROWS):
            for column in range(COLUMNS - 3):
                window = [
                    board[row - index][column + index]
                    for index in range(4)
                ]

                score += self.evaluate_window(window, piece)

        return score

    def terminal_state(self, board):
        return (
            self.winning_move(board, HUMAN)
            or self.winning_move(board, AI)
            or self.board_full(board)
        )

    def minimax(
        self,
        board,
        depth,
        alpha,
        beta,
        maximizing
    ):
        valid_columns = self.get_valid_columns(board)
        terminal = self.terminal_state(board)

        if depth == 0 or terminal:
            if terminal:
                if self.winning_move(board, AI):
                    return None, 1000000

                if self.winning_move(board, HUMAN):
                    return None, -1000000

                return None, 0

            return None, self.score_position(board, AI)

        if maximizing:
            best_score = -math.inf
            best_column = random.choice(valid_columns)

            for column in valid_columns:
                row = self.get_open_row(board, column)
                temporary_board = self.copy_board(board)
                temporary_board[row][column] = AI

                new_score = self.minimax(
                    temporary_board,
                    depth - 1,
                    alpha,
                    beta,
                    False
                )[1]

                if new_score > best_score:
                    best_score = new_score
                    best_column = column

                alpha = max(alpha, best_score)

                if alpha >= beta:
                    break

            return best_column, best_score

        best_score = math.inf
        best_column = random.choice(valid_columns)

        for column in valid_columns:
            row = self.get_open_row(board, column)
            temporary_board = self.copy_board(board)
            temporary_board[row][column] = HUMAN

            new_score = self.minimax(
                temporary_board,
                depth - 1,
                alpha,
                beta,
                True
            )[1]

            if new_score < best_score:
                best_score = new_score
                best_column = column

            beta = min(beta, best_score)

            if alpha >= beta:
                break

        return best_column, best_score

    def reset_game(self):
        self.board = [
            [EMPTY for _ in range(COLUMNS)]
            for _ in range(ROWS)
        ]

        self.game_over = False

        self.status_label.config(
            text="Your Turn – Click Any Column"
        )

        self.draw_board()


def main():
    root = tk.Tk()
    ConnectFourAI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
