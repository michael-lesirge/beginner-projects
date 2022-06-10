
color_mode = (input("Does you console support color codes (y/n): ").strip().lower() in ["y", "yes"])

class Board:
    default = " "

    def __init__(self):
        self.board = {}
        self.reset()

    def reset(self):
        self.placed = 0
        self.board = {i: None for i in range(1, 10)}

    def in_board(self, loc):
        return 1 <= loc <= 9

    def empty_location(self, loc):
        return self.board[loc] == Board.default

    def place(self, loc, val):
        self.board[loc] = val


    def is_winner(self, player_char):
        for i in range(1, 10, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] == player_char:
                return True
        for i in range(1, 4, 1):
            if self.board[i] == self.board[i+3] == self.board[i+6] == player_char:
                return True

        if self.board[5] == player_char:
            if self.board[1] == self.board[9] == player_char or self.board[3] == self.board[7] == player_char:
                return True
        return False

    def __repr__(self):
        return f"Board({self.board})"

    def __str__(self):
        return "\n" + ("\n---+---+---\n".join([ " " + (" | ".join([str(j) if self.board[j] == None else self.board[j] for j in range(i, i+3)])) for i in range(1, 10, 3)])) + "\n"
        
class Player:
    colors = {"X": "\033[31m", "O": "\033[34m"}

    def __init__(self, char: str, board: Board):
        self.char = char.capitalize()
        self.board = board
        self.wins = 0
    
    def place(self, loc: str):
        if not loc.isnumeric():
            raise Exception("Input must be a number")
        loc = int(loc)
        if not self.board.in_board(loc):
            raise Exception("location must be from 1 to 9")
        if self.board.empty_location(loc):
            raise Exception("location is already occupied")
        
        self.board.place(loc, str(self))
        return True
    
    def __repr__(self):
        return f"Player(char={self.char}, wins={self.wins})"

    def __str__(self):
        if color_mode:
            return Player.colors[self.char] + self.char + "\033[0m"
        return self.char

def main():
    board = Board()
    players = (Player("X", board), Player("O", board))

    playing = True
    while playing:
        board.reset()
        for i in range(9):
            player = players[i%2]
            print(board)
            print(f"{player}'s turn.")

            valid = False
            while not valid:
                try:
                    print()
                    loc = input("Enter where you want to go: ")
                    valid = player.place(loc)
                except Exception as exs:
                    print(f"Invalid input, {exs}")
            
            if board.is_winner(str(player)):
                print(board)
                print(f"Player {player} wins!")
                break

        else:
            print(board)
            print("It's a tie!")

        print()
        playing = (input("Do you want to play agien (y/n): ").strip().lower() in ["y", "yes"])
    print("Good Bye!")

if __name__ == "__main__":
    main()
