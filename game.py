class Game:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.winner = None

    def make_move(self, index):
        # Αν το κελί είναι ήδη γεμάτο ή το παιχνίδι έχει τελειώσει, δεν κάνει τίποτα
        if self.board[index] != "" or self.winner is not None:
            return False

        # Τοποθέτηση του X ή O
        self.board[index] = self.current_player

        # Έλεγχος νίκης
        if self.check_winner(self.current_player):
            self.winner = self.current_player

        # Έλεγχος για ισοπαλία
        elif "" not in self.board:
            self.winner = "Draw"

        else:
            # Αλλαγή παίκτη
            self.current_player = "O" if self.current_player == "X" else "X"

        return True

    def check_winner(self, player):
        win_patterns = [
            (0,1,2), (3,4,5), (6,7,8),   # οριζόντιες
            (0,3,6), (1,4,7), (2,5,8),   # κάθετες
            (0,4,8), (2,4,6)             # διαγώνιες
        ]

        for a, b, c in win_patterns:
            if self.board[a] == self.board[b] == self.board[c] == player:
                return True

        return False