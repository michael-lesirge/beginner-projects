def add_zero(s):
    """
    adds a leading zero if first number is decimal
    """
    if s[0] == '.':
        return '0' + s
    return s

class Bill:
    __slots__ = "amount", "amount_str"

    def __init__(self, amount):
        self.amount = amount
        self.amount_str = str(amount)
        self.amount_str = self.amount_str[:-2] + '.' + self.amount_str[-2:]
        self.amount_str = add_zero(self.amount)

    def __repr__(self):
        return f"Bill({self.amount})"

    def __float__(self):
        return float(self.amount_str)

    def __int__(self):
        return self.amount

    def __str__(self):
        return f"${self.amount_str}"


def make_change(total_amount, *, mode=None, val_type=None):
    """
    mode must be list or dict
    val_type must be int, str or float
    """
    if mode is None:
        mode = list
    if val_type is None:
        val_type = int

    amounts = iter((
        Bill(10000), Bill(5000), Bill(2000), Bill(1000), Bill(500), Bill(100),
        Bill(25), Bill(10), Bill(5), Bill(1),
    ))

    if mode == dict:
        change = {}

        def add_change(val):
            change[val_type(val)] = change.get(val_type(val), 0) + 1
    elif mode == list:
        change = []

        # mode == int or mode is None
        def add_change(val):
            change.append(val_type(val))
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



def main():
    print("Enter 'e' or 'exit' to exit")
    output_type, value_type = (list, str)
    running = True
    while running:
        owed = input("How much is owed (as float): ")
        if escape(owed):
            break
        tendered = input("How much was given")
        if escape(tendered):
            break

        difference = to_int(tendered) - to_int(owed)
        final = 

if __name__ == '__main__':
    main()
