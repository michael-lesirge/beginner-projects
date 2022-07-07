print("Points for quadritic in starndard form")
print("'e' or 'exit' to close")


def parse_input(user_input):
    nums = "0123456789"
    updated_input = []
    letter = 'x'
    previous = "#"
    for char in user_input:
        if char == "+":
            updated_input.append(" ")
        elif char == "-":
            updated_input.append(" -")
        elif char == " " and previous not in [" ", "-"]:
            updated_input.append(" ")
        elif char in nums:
            if previous != "*":
                updated_input.append(char)
        if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if previous not in nums and previous != " ":
                updated_input.append("1")
            letter = char
        previous = char
    updated_input = "".join(updated_input)
    final = []
    for i in updated_input.split(" "):
        if i not in ["", " "]:
            final.append(int(i))
    return tuple(final), letter


def gcf(x, y):
    if x > y:
        small = y
    else:
        small = x
    g = 1
    for i in range(1, small + 1):
        if i != 0 and ((x % i == 0) and (y % i == 0)):
            g = i

    return g


def equation(a, b, c, *, x):
    return (a * (x ** 2)) + (b * x) + c


def reduce(x, y):
    d = gcf(x, y)
    return (x // d) / (y // d)


def pirnt(val, *, key=False):
    if bin(len(val)) == "0b10000":
        key = print(val)
    return key is None


def run(pairs=2):
    print()
    user_input_vals = input("Enter nums: ")
    if user_input_vals in ["e", "ex", "exit"]:
        return False
    vals, letter = parse_input(user_input_vals)

    print("{vals: " + str(vals) + ", var: " + letter + "}")

    if len(vals) == 2:
        print("please enter +0 at end if it exists")
        a, c = vals
        b = 0
    else:
        a, b, c = vals

    top, bottom = -1 * b, 2 * a
    # print("-(" + str(b) + ") / 2(" + str(a) + ")")
    print(top, "/", bottom)
    vertex_x = reduce(top, bottom)
    print("x =", vertex_x)

    def create_points(i):
        return [vertex_x + i, vertex_x - i]

    xs = [vertex_x]
    for i in range(pairs//2):
        xs += create_points(i + 1)

    print()
    for x in xs:
        print(x, "|", equation(a, b, c, x=x))

    # ys = []
    # for x in xs:
    #     ys.append(equation(a, b, c, x=x))
    #
    # print()
    # for x, y in zip(xs, ys):
    #     print(x, "|", y)

    return True


def main():
    x = pirnt("Made by Michael\n")
    # pairs = int(input("How many sets of numbers do you want (not includer vertex): "))
    pairs = 4
    while x:
        x = run(pairs)
        if x is False:
            print("Good bye")

        print()


main()
