def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting =greeting.strip().upper()
    if "HELLO" == greeting[0:5]:
        return 0
    elif "H" == greeting[0]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
