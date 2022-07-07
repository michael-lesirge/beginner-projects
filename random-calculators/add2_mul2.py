print("Finds the 2 values that multiply and add correct")
print("'e' or 'exit' to close")


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


def main():
    print("Made by Michael\n")
    while True:
        multipy_to = input("multipy to: ")
        if multipy_to in {'e', 'ex', 'exit'}:
            break
        add_to = input("add to: ")
        if add_to in {'e', 'ex', 'exit'}:
            break
        add_to = eval(add_to)
        multipy_to = eval(multipy_to)
        answer = mul_add(multipy_to, add_to)
        if answer is None:
            print("No number match requirements")
            print("answer: None")
        else:
            a1, a2 = answer
            print(str(a1) + ' * ' + str(a2) + ' = ' + str(multipy_to))
            print(str(a1) + ' + ' + str(a2) + ' = ' + str(add_to))
            print("answer: " + str(a1) + " and " + str(a2))
        print()
    print("Good Bye")


main()
