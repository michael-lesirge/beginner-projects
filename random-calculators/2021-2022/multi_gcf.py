print("Finds greatest command factor")
print("'e' or 'exit' to close")


def gcf(input_nums):
    if len(input_nums) == 0:
        return 1, tuple()
    nums = []
    all_neg = -1

    for num in input_nums:
        if num >= 0:
            all_neg = 1
            nums.append(num)
        else:
            nums.append(num * -1)

    r = range(min(nums), 1, -1)

    for i in r:
        a = []
        for num in nums:
            a.append(num % i == 0)
        if all(a):
            i *= all_neg
            return i, tuple((num // i for num in input_nums))
    return 1 * all_neg, tuple(input_nums)


def parse_input(user_input):
    nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    updated_input = []
    previous = ''
    for char in user_input:
        if char == '+':
            updated_input.append(' ')
        elif char == '-':
            updated_input.append(' -')
        elif char == ' ' and previous not in [' ', '-']:
            updated_input.append(' ')
        elif char in nums:
            if previous != '*':
                updated_input.append(char)
        previous = char

    updated_input = ''.join(updated_input)
    final = []
    for i in updated_input.split(' '):
        if i not in ['', ' ']:
            final.append(int(i))
    return final


def main():
    print("Made by Michael\n")
    while True:
        user_nums = input("enter nums: ")
        if user_nums in {'e', 'ex', 'exit'}:
            break
        nums = tuple(parse_input(user_nums))
        gcf_of_nums, new_nums = gcf(nums)
        print(gcf_of_nums, new_nums)
        # print(nums, "/", gcf_of_nums,  "=", new_nums)
        if gcf_of_nums == 1:
            print("Prime")
        else:
            print("gcf =", gcf_of_nums)
            print("new numbers =", new_nums)
        print()
    print("Good Bye")


main()
