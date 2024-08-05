def main():
    import random
    numb=get_numb("Level: ")
    rdnumb= random.randint(1, numb)
    while True:
        guess=get_numb("Guess: ")
        if guess<rdnumb:
            print("Too small!")
        elif guess>rdnumb:
            print("Too large!")
        elif guess==rdnumb:
            print("Just right!")
            break

def get_numb(prompt):
    while True:
        try:
            n=int(input(prompt))
            if n<=0:
                pass
            else:
                break
        except ValueError:
            pass


    return n

if __name__=="__main__":
    main()