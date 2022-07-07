def main():
    running = True
    while running:
        user_input = input("enter a, b, c: ")

        if user_input in ["e", "ex", "exit"]:
            running = False
        else:
            try:
                print("x =", quad(*parse_input(user_input)))
            except Exception as err:
                print("Error:", err)
                print("Could be no solution.")
        print()


def sqrt(x):
    if x < 0:
        raise Exception("can not square negative number")
    return x ** 0.5


def gcd(x, *nums):
    if len(nums) == 0:
        return x
    y, *new_nums = nums
    while y:
        x, y = y, x % y
    return abs(gcd(x, *new_nums))


def parse_input(val: str):
    mapper = {"-": " -", "+": " "}
    new = ""
    for char in val:
        new += mapper.get(char, char)

    final = []
    for x in new.split(" "):
        if x not in ["", " "]:
            final.append(float(x))
    return final


def quad(a, b, c):
    left = (-1 * b)
    right = (sqrt((b ** 2) - (4 * a * c)))
    div = (2 * a)

    lr_p = (left + right)
    lr_m = (left - right)

    left_div = (lr_p / div)
    right_div = (lr_m / div)

    print(lr_p, "/", div, " | ", lr_m, "/", div, sep="")
    l_gcd, r_gcd = gcd(lr_p, div), gcd(lr_m, div)

    print(lr_p/l_gcd, "/", div/l_gcd, " | ", lr_m, "/", div, sep="")

    return {round(left_div, 2), round(right_div, 2)}


main()
