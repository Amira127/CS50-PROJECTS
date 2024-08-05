import random
def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        if answer(x, y) :
            score += 1
    print("score= ", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except:
            pass

def generate_integer(level):
    if level == 1:
        numb = random.randint(0, 9)
    elif level == 2:
        numb = random.randint(10, 99)
    else:
        numb = random.randint(100, 999)
    return numb


def answer(x, y):
    round = 0
    while round < 3:
        try:
            answer = int(input(f" {x} + {y} = "))
            if answer == x + y:
                return True
            else:
                round += 1
                print("EEE")
        except:
            round += 1
            print("EEE")

    print(f" {x} + {y} = {x+y}")


if __name__ == "__main__":
    main()
