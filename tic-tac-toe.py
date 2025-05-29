import tkinter as tk
from tkinter import messagebox

# -----------------------------------
# Tic Tac Toe Game - Tkinter GUI
# -----------------------------------

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - GUI Game")
        self.root.resizable(False, False)

        # Players
        self.player1 = "X"
        self.player2 = "O"
        self.current_player = self.player1

        # Game state
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.player1_score = 0
        self.player2_score = 0

        # GUI Setup
        self.create_widgets()

    def create_widgets(self):
        # Title label
        self.title_label = tk.Label(self.root, text="Tic Tac Toe", font=("Arial", 20, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Scoreboard
        self.score_label = tk.Label(
            self.root,
            text=f"Player X: {self.player1_score}    Player O: {self.player2_score}",
            font=("Arial", 14)
        )
        self.score_label.grid(row=1, column=0, columnspan=3)

        # Game buttons
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.root,
                    text="",
                    font=("Arial", 24),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.on_click(row, col)
                )
                button.grid(row=i+2, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

        # Reset button
        self.reset_button = tk.Button(
            self.root,
            text="Reset Game",
            font=("Arial", 12),
            command=self.reset_game
        )
        self.reset_button.grid(row=5, column=0, columnspan=3, pady=10)

        # Turn label
        self.turn_label = tk.Label(
            self.root,
            text=f"Turn: Player {self.current_player}",
            font=("Arial", 12)
        )
        self.turn_label.grid(row=6, column=0, columnspan=3)

    def on_click(self, row, col):
        # If cell is empty
        if self.board[row][col] == "":
            # Update cell and button
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state="disabled")

            # Check for winner
            if self.check_winner(self.current_player):
                self.end_game(winner=self.current_player)
            elif self.is_draw():
                self.end_game(winner=None)
            else:
                self.switch_player()
        else:
            # Optional: warn user that cell is taken
            pass

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        self.turn_label.config(text=f"Turn: Player {self.current_player}")

    def check_winner(self, player):
        # Check rows and columns
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True
            if all(self.board[j][i] == player for j in range(3)):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_draw(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def end_game(self, winner):
        # Show result
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            if winner == self.player1:
                self.player1_score += 1
            else:
                self.player2_score += 1
        else:
            messagebox.showinfo("Game Over", "It's a draw!")

        # Disable all buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="disabled")

        # Update scoreboard
        self.score_label.config(
            text=f"Player X: {self.player1_score}    Player O: {self.player2_score}"
        )

    def reset_game(self):
        # Reset state
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = self.player1
        self.turn_label.config(text=f"Turn: Player {self.current_player}")

        # Reset buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal")


# Start the game
if __name__== "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
