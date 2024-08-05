#You can include a.m. and p.m. in your input
def main():
    time=input("What time is it?")
    if 7<=convert(time)<=8:
        print("breakfast time")
    elif 12<=convert(time)<=13:
        print("lunch time")
    elif 18<=convert(time)<=19:
        print("dinner time")

#challenge accepted :)
def convert(time):
    hours, minutes = time.split(":")
    if 'p.m.' in time:
        minute= minutes.rstrip('p.m.')
        dec=((int(minute)*50)/30)*0.01
        float=int(hours)+12+dec
    elif 'a.m.' in time:
        minute= minutes.rstrip('a.m.')
        dec=((int(minute)*50)/30)*0.01
        float=int(hours)+dec
    else:
        dec=((int(minutes)*50)/30)*0.01
        float=int(hours)+dec
    return float


if __name__ == "__main__":
    main()