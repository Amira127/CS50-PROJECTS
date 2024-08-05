def main():
    str = input("Input:")
    print("Output:", omitted(str))


def shorten(word):
    vowels = ["A", "E", "I", "O", "U"]
    output = ""
    for verif in word:
        if verif.upper() not in vowels:
            output = output + verif
    return output


if __name__ == "__main__":
    main()
