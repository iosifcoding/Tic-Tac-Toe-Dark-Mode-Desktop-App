import tkinter as tk
from tkinter import messagebox
from game import Game

# -----------------------------------------------------------
#  DARK MODE COLORS
# -----------------------------------------------------------
DARK_BG = "#1E1E1E"
DARK_BUTTON = "#3C3C3C"
SYMBOL_COLOR = "#000000"
TEXT_COLOR = "#FFFFFF"
ACCENT = "#0078D7"

# -----------------------------------------------------------
class TicTacToeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Dark Mode")
        self.root.configure(bg=DARK_BG)

        self.game = Game()

        self.x_wins = 0
        self.o_wins = 0
        self.draws = 0

        self.setup_ui()

    # -------------------------------------------------------
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # -------------------------------------------------------
    def setup_ui(self):
        self.clear_window()
        self.game.reset()

        main_frame = tk.Frame(self.root, bg=DARK_BG)
        main_frame.pack(expand=True, fill="both")

        # ----- Game Grid -----
        grid_frame = tk.Frame(main_frame, bg=DARK_BG)
        grid_frame.pack(side="left", padx=30, pady=30)

        self.buttons = []
        for i in range(9):
            btn = tk.Button(
                grid_frame,
                text="",
                font=("Helvetica", 32, "bold"),
                bg=DARK_BUTTON,
                fg=SYMBOL_COLOR,
                width=5,
                height=2,
                relief="flat",
                borderwidth=0,
                highlightthickness=0,
                command=lambda i=i: self.handle_move(i),
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        # ----- Sidebar -----
        sidebar = tk.Frame(main_frame, bg=DARK_BG, width=200)
        sidebar.pack(side="right", fill="y")

        title = tk.Label(
            sidebar,
            text="Player vs Player",
            font=("Helvetica", 18, "bold"),
            bg=DARK_BG,
            fg=TEXT_COLOR,
        )
        title.pack(pady=20)

        self.score_label = tk.Label(
            sidebar,
            text=self.get_score_text(),
            font=("Helvetica", 14),
            bg=DARK_BG,
            fg=TEXT_COLOR,
        )
        self.score_label.pack(pady=10)

        # ---------------------------------------------------
        # RESET AS LABEL BUTTON  ★★ FIX FOR MACOS ★★
        # ---------------------------------------------------
        self.reset_label = tk.Label(
            sidebar,
            text="Reset Board",
            font=("Helvetica", 16, "bold"),
            bg=ACCENT,
            fg="white",
            width=12,
            height=1,
            padx=10,
            pady=5,
        )

        # Bind left-click
        self.reset_label.bind("<Button-1>", lambda e: self.reset_board())

        self.reset_label.pack(pady=20)

    # -------------------------------------------------------
    def get_score_text(self):
        return f"X Wins: {self.x_wins}\nO Wins: {self.o_wins}\nDraws: {self.draws}"

    # -------------------------------------------------------
    def handle_move(self, index):
        if not self.game.make_move(index):
            return

        self.update_ui()
        self.check_end()

    # -------------------------------------------------------
    def update_ui(self):
        for i in range(9):
            self.buttons[i]["text"] = self.game.board[i]

    # -------------------------------------------------------
    def check_end(self):
        if self.game.winner == "X":
            self.x_wins += 1
            self.score_label.config(text=self.get_score_text())
            messagebox.showinfo("Game Over", "Player X Wins!")
            self.reset_board()
            return True

        if self.game.winner == "O":
            self.o_wins += 1
            self.score_label.config(text=self.get_score_text())
            messagebox.showinfo("Game Over", "Player O Wins!")
            self.reset_board()
            return True

        if self.game.winner == "Draw":
            self.draws += 1
            self.score_label.config(text=self.get_score_text())
            messagebox.showinfo("Game Over", "Draw!")
            self.reset_board()
            return True

        return False

    # -------------------------------------------------------
    def reset_board(self):
        self.game.reset()
        for btn in self.buttons:
            btn["text"] = ""
            btn.configure(bg=DARK_BUTTON, fg=SYMBOL_COLOR)

        # Reset the label button style (macOS-safe)
        self.reset_label.configure(bg=ACCENT, fg="white")