def main():
    x = input("Fraction: ")
    per = convert(x)
    print(gauge(per))

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x <= y:
                per = round((x / y) * 100)
                return per

        except (ValueError, ZeroDivisionError):
            fraction = input("Fraction: ")
            pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()