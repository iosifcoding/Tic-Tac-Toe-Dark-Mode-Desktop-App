# Tic Tac Toe – Dark Mode Edition 🎮  
A clean, minimal, and modern implementation of Tic-Tac-Toe built with Python and Tkinter.  
This version features a **fully custom dark UI**, **Player vs Player gameplay**, **clear and bold X/O symbols**, and a **macOS-safe Reset control**.

---

## 📸 Screenshot  
![03073BB0-C9A5-4F09-A860-230341ECDC38_1_201_a](https://github.com/user-attachments/assets/21bdadbb-277f-45bd-af1d-1a2e42580467)
![79D42BEB-E192-43B2-ADB5-0FC4743F5C4B_1_201_a](https://github.com/user-attachments/assets/31d3d9f8-b19b-4358-a4a4-b4b688c9de44)


---

## ✨ Features

- 🌓 Full custom **Dark Mode UI**
- 👥 **Player vs Player** mode only (simple & focused)
- 🏆 Built-in **Scoreboard** (X Wins / O Wins / Draws)
- ♻️ **Reset control** fully compatible with macOS (uses a Label-Button)
- 🔲 Clean and modern 3×3 board
- ⚡ Instant response with no lag
- 🧼 Organized architecture (UI + Logic separated)

---

## 📁 Project Structure
TicTacToe_Game/
│
├── game.py        # Core game logic (moves, win conditions, board state)
├── ui.py          # Full UI: dark theme, scoreboard, grid, reset label
├── main.py        # Application entry point
└── README.md      # Project documentation

---

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/iosifcoding/TicTacToe_Game.git
cd TicTacToe_Game

2.	Make sure you have Python 3.10+ installed:
python3 --version
3.	No external dependencies are required.
Tkinter is included with standard Python installations.

▶️ Run the Game
python3 main.py

🧠 How It Works
	•	game.py contains the full game logic:
	•	board state
	•	turn handling
	•	win detection
	•	draw conditions
	•	ui.py handles:
	•	window layout
	•	dark theme styling
	•	rendering of the grid
	•	scoreboard
	•	reset control built using a Label instead of Button (necessary for macOS visibility)
	•	main.py initializes and launches the UI.

⸻

🛠 Technologies Used
	•	Python 3
	•	Tkinter (GUI library)
	•	Object-Oriented Design

⸻

💡 Future Enhancements
	•	Highlight winning row/column/diagonal
	•	Hover animations
	•	Player name input
	•	Light/Dark mode toggle
	•	Sound effects (click / win / draw)
	•	Online multiplayer
	•	Packaging as a standalone macOS .app or Windows .exe

⸻

👤 Author

Developed by Iosif Kiriakidis (iosifcoding@gmail.com)
Feel free to explore my GitHub profile for more projects.
