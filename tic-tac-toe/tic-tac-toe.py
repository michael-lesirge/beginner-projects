def main():
    print("Welcome to tic-tac-toe with python!")
    color_mode = bool_input("Does you console support ASCII color codes")
    print()

    width = height = 3
    if bool_input("Do you want a custom board"):
        message = "Enter the {m} of the board: "
        width, height = int_input(message.format(m="width")), int_input(message.format(m="height"))
    print()

    board = Board(width, height)

    Player.board = board
    Player.color_mode = color_mode

    players = []
    if bool_input("Do you want a custom players"):
        for i in range(1, int_input("Enter the number of players: ") + 1):
            print()
            print(f"Player {i}")
            new_player = create_player()
            players.append(new_player)
    else:
        players.append(Player("X", "red"))
        players.append(Player("O", "blue"))
    print()

    playing = True
    while playing:
        print(f"Round {board.rounds}")
        board.reset()
        for i in range(board.size):
            player = players[i % len(players)]
            print(board)
            print(f"{player}'s turn.")

            player.place()

            if board.detect_is_winner(player):
                print(board)
                player.wins += 1
                print(f"Player {player} wins!")
                break

        else:
            print(board)
            print("It's a tie!")
        print()

        for player in players:
            print(f"{player}: {player.wins}")
        print()

        playing = bool_input("Do you want to play again")

    print("Good Bye!")


class Board:
    def __init__(self, width=3, height=3):
        self.width = int(width)
        self.height = int(height)
        self.size = (self.width * self.height)

        self.rounds = 0

        self._board = None
        self.reset()

    def reset(self):
        self.rounds += 1
        self._board = {i: str(i) for i in range(1, self.size + 1)}

    def _in_board(self, loc):
        return 1 <= loc <= self.size

    def _empty_location(self, loc):
        return self._board[loc] == str(loc)

    def place(self, loc: int, val):
        if not self._in_board(loc):
            raise ValueError(f"location must be from 1 to {self.size}")
        if not self._empty_location(loc):
            raise ValueError("location is already occupied")
        self._board[loc] = val

    def detect_is_winner(self, player):
        for i in range(1, self.size + 1, self.width):
            if all(((self._board[j] == player) for j in range(i, i + self.width))):
                return True

        for i in range(1, self.width + 1):
            if all(((self._board[j] == player) for j in range(i, self.size + 1, self.width))):
                return True

        if self.width == self.height:
            if all(((self._board[i] == player) for i in range(1, self.size + 1, self.width + 1))) or \
                    all(((self._board[i] == player) for i in range(self.width, self.size, self.width - 1))):
                return True
        return False

    def __setitem__(self, key, value):
        self.place(key, value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._board})"

    def __str__(self):
        max_num_len = len(str(self.size))
        rows = []
        row = []
        for i in range(1, self.size + 1):
            row.append(add_buffer(self._board[i], max_num_len))
            if i % self.width == 0:
                rows.append(" " + (" | ".join(row)) + " \n")
                row = []

        line = "-" + ("-" * max_num_len) + "-"
        return "\n" + (((line + "+") * (self.width - 1)) + line + "\n").join(rows)


class Player:
    board = None
    color_mode = False

    colors = {
        "red": "\u001b[31m",
        "blue": "\u001b[34m",
        "green": "\u001b[32m",
        "yellow": "\u001b[33m",
        "magenta": "\u001b[35m",
        "cyan": "\u001b[36m",
        "white": "\u001b[37m",
    }

    def __init__(self, char: str, color=None):
        if len(char) != 1:
            raise ValueError("Player character must be one character")
        if not char.isalpha():
            raise ValueError("Player character must be a letter")
        self.char = char.upper()

        color = color.lower()
        if color not in Player.colors:
            raise ValueError(f"{color} is not an available color")
        self.color = Player.colors[color]

        self.wins = 0

    def place(self):
        while True:
            try:
                print()
                loc = input("Enter where you want to go: ")
                if not loc.isnumeric():
                    raise ValueError("Location must be a number")
                Player.board.place(int(loc), self)
                return
            except ValueError as exs:
                print_invalid(exs)

    def __repr__(self):
        return f"{self.__class__.__name__}(char={self.char}, wins={self.wins})"

    def __str__(self):
        if Player.color_mode:
            return self.color + "\033[1m" + self.char + "\033[0m"
        return self.char


def add_buffer(val, amount, *, buffer=" "):
    amount -= (1 if isinstance(val, Player) else len(val))

    side_amount, extra = divmod(amount, 2)

    return (buffer * (side_amount + extra)) + str(val) + (buffer * side_amount)


def print_invalid(exs):
    print(f"Invalid input, {exs}.")


def bool_input(prompt):
    while True:
        user_input = input(prompt + " (y/n): ").strip().lower()
        if user_input in ("y", "yes", "true"):
            return True
        elif user_input in ("n", "no", "false"):
            return False
        print_invalid("answer with yes/no")


def int_input(prompt):
    while True:
        try:
            user_input = input(prompt).strip()
            return int(user_input)
        except ValueError:
            print_invalid("answer with a number")


def create_player():
    while True:
        try:
            char = input("Letter: ").strip()
            color = None
            if Player.color_mode:
                color = input("Color: ").strip()
            return Player(char, color)
        except ValueError as exs:
            print_invalid(exs)


if __name__ == "__main__":
    main()
