def main():
    greeting = input("Greeting: ").strip().upper()
    print(f"${value(greeting)}")


def value(greeting):
    if "Hello" == greeting[0:5]:
        promise = 0
    elif "H" == greeting[0]:
        promise = 20
    else:
        promise = 100
    return promise

if __name__ == "__main__":
    main()