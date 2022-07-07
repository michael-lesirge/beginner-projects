print("'ex' to end.\nformat exa: '7(81', '320'\nno spaces.\n'(' = root sign")

all_ps = {i * i for i in range(1, 100)}

def box(n):
    from math import sqrt
    if n in all_ps:
        print("(" + str(n) + "=" + str(int(sqrt(n))) + "\n" + str(n) + " is perfect square")
        return n, 0

    h_n = n / 2

    good_pss = []
    for ps in all_ps:
        if ps <= h_n:
            good_pss.append(ps)

    good_pss_0 = []
    for good_ps in good_pss:
        if n % good_ps == 0:
            good_pss_0.append(good_ps)

    x = max(good_pss_0)
    print("(" + str(x) + " * (" + str(int(n / x)) + " = " + str(n))
    print(str(int(sqrt(x))) + " * (" + str(int(n / x)) + " = " + str(n))
    return x, n / x


def format_n(n, times=1):
    from math import sqrt
    if n[1] == 0:
        if times != 1:
            print(str(times) + "*" + str(int(sqrt(n[0]))))
        print("Final answer: " + str(int(sqrt(n[0]) * times)))
    else:
        if times != 1:
            print(str(times) + "*" + str(int(sqrt(n[0]))) + "(" + str(int(n[1])))
        print("Final answer: " + str(int(sqrt(n[0]) * times)) + "(" + str(int(n[1])))


def main():
    while True:
        user_input = input("\nEnter radical: ")
        if user_input.lower() in ["ex", "exit"]:
            break
        try:
            if user_input.count('(') == 1:
                user_input = user_input.split("(")
                answer = box(int(user_input[1]))
                try:
                    try:
                        format_n(answer, int(user_input[0]))
                    except ValueError:
                        format_n(answer, 1)
                except IndexError:
                    format_n(answer)
            else:
                answer = box(int(user_input))
                format_n(answer)
        except ValueError:
            print("Please enter something reasonable.")


main()
