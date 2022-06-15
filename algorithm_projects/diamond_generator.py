def create_diamond(edge_height, full_char="#", blank_char=" ") -> str:
    final = []

    for i in range(edge_height):
        final.append((blank_char * ((edge_height - i) - 1)) + (full_char * ((i * 2) + 1)))
    final.extend(reversed(final[:-1]))

    return "\n".join(final)


def main():
    diamond_edge_height = int(input("Enter edge height of diamond: "))
    diamond = create_diamond(diamond_edge_height, "#", " ")
    print()
    print(diamond)


if __name__ == "__main__":
    main()
