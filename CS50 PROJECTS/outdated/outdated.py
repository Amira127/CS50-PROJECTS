def main():
    date=get_date()

def get_date():
    months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        date=input("Date:").title().strip()
        try:
            if "/" in date:
                MM, DD, YYYY=date.split("/")
            if " " in date:
                MM, DD, YYYY=date.split(" ")
                while MM not in months:
                    date=input("Date:").title().strip()
                    MM, DD, YYYY=date.split(" ")
                MM=(months.index(MM))+1
                if "," not in DD:
                    test=False
                DD, etc =DD.split(",")
            if not (0<int(DD)<32 and 0<int(MM)<13) :
                test=False
            elif 0<int(DD)<32 and 0<int(MM)<13:
                print(YYYY,end="-")
                print(f"{int(MM):02}",end="-")
                print(f"{int(DD):02}")
                break
        except ValueError:
            date=input("Date:").title().strip()
        except test ==False:
            date=input("Date:").title().strip()


main()