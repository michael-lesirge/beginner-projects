import numpy as np
"""
super inefficient but its more to learn numpy 
"""

def reduce(numerator: int, denominator: int) -> int:
    def gcd(n, d):
        while d:
            n, d = d, n % d
        return n

    greatest = gcd(numerator, denominator)
    return (numerator//greatest, denominator//greatest)


def dice_chances(dice_sides: int, num_of_dice: int, /, flat: bool = False, as_list: bool = False) -> np.array:
    if num_of_dice <= 0 or dice_sides <= 0:
        dice_nums_total = np.array([], dtype=np.int32)
    else:
        def create(*args):
            # return sum((num+1 for num in args))
            total = 0
            for num in args:
                total += num + 1
            return total

        dice_nums_total = np.array(
            [np.fromfunction(create, (dice_sides for _ in range(num_of_dice)), dtype=np.int32)]
        )

        if flat:
            dice_nums_total = dice_nums_total.flatten()
    return dice_nums_total


def main():
    ROUND_TO = 5

    dice_sides = int(input("How many sides does the dice have: ").removeprefix("d").strip())
    num_of_dice = int(input("How many dice do you want: "))

    dice_nums_total = dice_chances(dice_sides, num_of_dice)

    print(dice_nums_total)

    dice_nums_flat = dice_nums_total.flatten()
    count_nums = np.bincount(dice_nums_flat)
    len_nums = dice_nums_flat.size

    if len_nums == 0:
        print("No roles will be possible")
        return

    avg_num = count_nums.argmax()
    min_num, max_num = dice_nums_flat.min(initial=num_of_dice), dice_nums_flat.max(initial=0)
    

    print(f"\n{min_num=}, {max_num=}, {avg_num=}, {len_nums=}")

    print(
        f"\nThe minimum role you could get is {min_num} "
        f"and the maximum is a {max_num}.\n"
        f"The most common role will be a {avg_num}.\n"
        )

    while True:
        user_request = input("Enter your number: ")
        if user_request.lower() in ["exit", "ex", "leave"]:
            print("Good bye!")
            return
        else:
            user_request = int(user_request)

            try:
                amount = count_nums[user_request]
            except IndexError:
                amount = 0

            reduced_n, reduced_d = reduce(amount, len_nums)
            if (reduced_n, reduced_d) == (amount, len_nums):
                reduced = ''
            else:
                reduced = f"({reduced_n} in {reduced_d})" + " "

            print(f"{amount} in {len_nums} {reduced}chance of getting a {user_request}.")
            print(f"{round(((amount / len_nums) * 100), ROUND_TO)}% chance.\n")


if __name__ == "__main__":
    main()
