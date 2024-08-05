import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if matches := re.search(r"^(\d{1,4})\.(\d{1,4})\.(\d{1,4})\.(\d{1,4})$", ip):
            for i in range(1, 5):
                if not (0 <= int(matches.group(i)) <= 255):
                    return False
            return True
    else:
        return False


if __name__ == "__main__":
    main()
