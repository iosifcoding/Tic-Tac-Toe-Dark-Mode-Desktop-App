import tkinter as tk
from ui import TicTacToeUI

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    root.resizable(False, False)

    app = TicTacToeUI(root)

    root.mainloop()