import re


def main():
    print(convert(input("Hours: ")))

def convert_am(hour):
    if int(hour) == 12 :
        return 0
    return int(hour)

def convert_pm(hour):
    if int(hour) != 12 :
        return int(hour) + 12
    return int(hour)

def convert_format(hour, minute, am_pm):
    if am_pm == "AM":
        new_hour = convert_am(hour)
    else:
        new_hour = convert_pm(hour)
    if minute == None :
        return f"{new_hour:02}:00"
    else:
        return f"{new_hour:02}:{minute}"

def convert(s):
    matches = re.search(r"^(\d+):?([0-5][0-9])? ((?:AM|PM)) to (\d+):?([0-5][0-9])? ((?:AM|PM))$", s)
    if matches:
        if int(matches.group(1)) > 12 or  int(matches.group(4)) > 12:
            raise ValueError("Check the hour provided")
        first_part_time = convert_format(matches.group(1), matches.group(2), matches.group(3))
        second_part_time = convert_format (matches.group(4), matches.group(5), matches.group(6))
        return f"{first_part_time} to {second_part_time}"
    else:
        raise ValueError("Invalid time")





if __name__ == "__main__":
    main()
