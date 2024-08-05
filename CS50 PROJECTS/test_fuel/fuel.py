def main():
    x = input("Fraction: ")
    per = convert(x)
    print(gauge(per))

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        per = round((x / y) * 100)
        return per
    except ValueError:
        raise ValueError("Invalid fraction")
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()