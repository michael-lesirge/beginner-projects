def add_zero(s):
    """
    adds a leading zero if first number is decimal
    """
    if s[0] == '.':
        return '0' + s
    return s


class Bill:
    currency_type = "bill"

    def __init__(self, amount: int):
        self.amount = amount
        self.amount_str = str(amount)
        self.amount_str = self.amount_str[:-2] + '.' + self.amount_str[-2:]
        self.amount_str = add_zero(self.amount_str)
        self.amount_float = float(self.amount_str)

    def __repr__(self):
        return f"Bill({self.amount})"

    def __float__(self):
        return self.amount_float

    def __int__(self):
        return self.amount

    def __str__(self):
        return f"{CURRENCY}{self.amount_str} {self.currency_type}"


class Coin(Bill):
    currency_type = "coin"

    def __init__(self, amount: int):
        super(Coin, self).__init__(amount)
        # ex: Nickle, Dime
        # self.name = name

    # def __str__(self):
    #     return self.name


CURRENCY = '$'
AMOUNTS = iter((
    Bill(10000), Bill(5000), Bill(2000), Bill(1000), Bill(500), Bill(100),
    Coin(25), Coin(10), Coin(5), Coin(1),
))


def make_change(total_amount, *, mode=None, value_type=None, amounts=AMOUNTS):
    """
    mode must be list or dict
    val_type must be int, str or float
    """
    if mode is None:
        mode = list
    if value_type is None:
        value_type = int

    if mode == dict:
        change = {}

        def add_change(val):
            change[value_type(val)] = change.get(value_type(val), 0) + 1
    elif mode == list:
        change = []

        # mode == int or mode is None
        def add_change(val):
            change.append(value_type(val))
    else:
        raise TypeError("mode must be list or dict")

    current = next(amounts)

    while total_amount > 0:
        if total_amount - current.amount >= 0:
            total_amount -= current.amount
            add_change(current)
        else:
            current = next(amounts)

    return change


def escape(s: str):
    """
    check if s is a leave character
    """
    return s in ["e", "ex", "exit"]


def to_int(s: str):
    """
    s -> float -> int
    """
    return int(float(add_zero(s)) * 100)


def run_test():
    print("enter input as number of cents int ex: $10.00 = 1000")

    output_type = list  # list or dict
    val_type = str  # int, float or str

    amount = int(input("Enter a amount (in cents): "))

    final = make_change(amount, mode=output_type, value_type=val_type)
    print(final)


def main():
    print("Enter 'e' or 'exit' to exit")

    output_type = list  # list, dict
    val_type = str  # int (fixed point), float, str

    running = True
    while running:
        owed = input("How much is owed (as float): " + CURRENCY)
        if escape(owed):
            break
        tendered = input("How much was given: " + CURRENCY)
        if escape(tendered):
            break

        difference = to_int(tendered) - to_int(owed)
        if difference == 0:
            print("They have payed the exact amount")
        elif difference < 0:
            print(f"They still owe {CURRENCY}{difference}")
        else:
            final = make_change(difference, mode=output_type, value_type=val_type)
            print(final)
        print()


if __name__ == '__main__':
    test_mode = False
    if test_mode:
        run_test()
    else:
        main()
