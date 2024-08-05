import validators

def main():
    print(check_validation(input("What's your email address? ")))


def check_validation(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()