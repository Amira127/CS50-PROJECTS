def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # All vanity plates must start with at least two letters.
    # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if len(s) < 2 or len(s) > 6 or s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # No periods, spaces, or punctuation marks are allowed.
    for c in s:
        if c in [".", " ", ",", "!", "?"]:
            return False

    # The first number used cannot be a ‘0’.
    numbers = ""
    is_number = False
    for i in range(0, len(s)):
        if s[i].isnumeric() == True:
            is_number = True
            numbers += s[i]
            if numbers[0] == "0":
                return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    while is_number:
        num = s.index(numbers[0])
        for i in range(num, len(s)):
            if s[i].isalpha():
                return False
        break

    return True


if __name__ == "__main__":
    main()
