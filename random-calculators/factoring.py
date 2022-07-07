print("Factoring in standard form")
print("'e' or 'exit' to close")


def add_exo(val, exo):
    val = str(val)
    if val == '1':
        return exo
    return val + exo


def plus(val_input):
    val = str(val_input)
    if val[0] == '-':
        return val
    return '+' + val


def plus_tuple(val_input):
    return '(' + ''.join([str(val_input[0])] + [plus(i) for i in val_input[1:]]) + ')'


def gcf(input_nums, first_num=True):
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

    if first_num:
        if input_nums[0] >= 0:
            all_neg = 1
        else:
            all_neg = -1

    r = range(min(nums), 1, -1)

    for i in r:
        a = []
        for num in nums:
            a.append(num % i == 0)
        if all(a):
            i *= all_neg
            return i, tuple((num // i for num in input_nums))
    return 1 * all_neg, tuple(input_nums)


def mul_add(multipy_to, add_to):
    m = float(add_to)
    n = int(multipy_to)

    if n == 0:
        return int(m), 0

    if m < 0 < n:
        o = -1
        m *= -1
    else:
        o = 1

    if n > 0:
        z = range(1, n)
    else:
        z = range(n * -1, n, -1)

    for i in z:
        if i == 0:
            continue
        x = n / i

        if x + i == m:
            val1 = int(x) * o
            val2 = i * o
            return val1, val2

    return False


def add_exo_tuple(vals, letter):
    if int(vals[1]) == 0:
        return add_exo(vals[0], letter + "**2") + plus(vals[2])
    return add_exo(vals[0], letter + "**2") + plus(add_exo(vals[1], letter)) + plus(vals[2])


def format_output(gf: int, x: tuple, y: tuple, letter, first_exo=''):
    def format_tuple(x, first_exo):
        n = []
        if int(x[0]) == 1:
            n.append(letter + first_exo)
        else:
            n.append(str(x[0]) + letter + first_exo)

        n.append(str(x[1]))

        return n

    x = format_tuple(x, '')
    y = format_tuple(y, first_exo)
    x = plus_tuple(x)
    y = plus_tuple(y)

    if gf == 1:
        return ''.join(x) + ''.join(y)
    return str(gf) + ''.join(x) + ''.join(y)


def parse_input(user_input):
    if user_input in {'e', 'ex', 'exit'}:
        return False, False
    updated_input = []
    previous = '#'
    letter = 'x'
    for char in user_input:
        if char == '+':
            updated_input.append(' ')
        elif char == '-':
            updated_input.append(' -')
        elif char == ' ' and previous not in [' ', '-']:
            updated_input.append(' ')
        elif char in '0123456789':
            if previous != '*':
                updated_input.append(char)
        if char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if previous not in '0123456789 ':
                updated_input.append("1")
            letter = char
        previous = char

    updated_input = ''.join(updated_input)
    final = []
    for i in updated_input.split(' '):
        if i not in ['', ' ']:
            final.append(int(i))
    return final, letter


def run():
    user_input_vals = input("Enter nums: ")
    vals, letter = parse_input(user_input_vals)
    if not vals:
        return False
    print('{vals: ' + str(vals) + ', var: ' + letter + ', terms: ' + str(len(vals)) + '}')
    first_exo = ''
    prime = 'prime\n'
    gf = 1
    if len(vals) == 4:
        first_exo = '**2'
        gf, vals = gcf(vals, False)
        if gf != 1:
            print(gf, plus_tuple(vals))

    if len(vals) == 2:
        vals = (vals[0], 0, vals[1])

    if len(vals) == 3:
        print(add_exo_tuple(vals, letter))
        gf, vals = gcf(vals, False)
        if gf != 1:
            prime = ''
            print(gf, plus_tuple(vals))

        x1, x2 = mul_add(vals[0] * vals[-1], vals[len(vals) // 2])
        if x1 is False and x2 is False:
            print(prime + "Final: " + add_exo_tuple(vals, letter))
            return True
        print(vals[len(vals) // 2], "-->", x1, x2)
        vals = vals[0], x1, x2, vals[-1]

    nx1 = vals[0:2]
    nx2 = vals[2:4]

    print(plus_tuple(nx1) + plus_tuple(nx2))

    y1, x1 = gcf(nx1)
    y2, x2 = gcf(nx2)
    print(plus_tuple(nx1) + ' / ' + str(y1))
    print(plus_tuple(nx2) + ' / ' + str(y2))
    print(str(y1) + '(' + str(x1[0]) + letter + plus(x1[1]) + ')' + plus(y2) + '(' + str(x2[0]) + letter + plus(
        x2[1]) + ')')

    print("Final:", format_output(gf, x1, (y1, y2), letter, first_exo))
    return True


def main():
    while True:
        x = run()
        if x is False:
            print("Good bye!")
            break
        print()


main()
