class Currency:
    def __init__(self, amount: int):
        self.amount: int = amount

    def __repr__(self):
        return f"Currency({self.amount})"

    def __hash__(self):
        return hash(self.amount)
    
    def __float__(self):
        return self.amount/100

    def __int__(self):
        return self.amount

    def __str__(self):
        return "${:.2f}".format(float(self))

AMOUNTS = iter((
    Currency(10000), Currency(5000), Currency(2000), Currency(1000), Currency(500), Currency(100),
    Currency(25), Currency(10), Currency(5), Currency(1),
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

    change = mode()

    if mode == dict:
        def add_change(val):
            change[value_type(val)] = change.get(value_type(val), 0) + 1
    elif mode == list:
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

def main():
    output_type = dict  # list, dict
    val_type = str  # int, str, float
    
    # owed = input("How much is owed: $")
    # tendered = input("How much was given: $")
    # difference = (float(tendered)*100) - (float(owed)*100)

    difference = float(input("what is the difference: $"))*100

    if difference == 0:
        print("They have payed the exact amount")
    elif difference < 0:
        print(f"They still need to pay ${difference}")
    else:
        final = make_change(difference, mode=output_type, value_type=val_type)
        print(final)


if __name__ == '__main__':
    main()
