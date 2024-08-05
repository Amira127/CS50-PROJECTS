def main():
    total=0
    while True  :
        order=get_taqueria("Item:")
        if order == '/n':
            print("")
            break
        total=order+total
        print(f"Total: ${total}0")

def get_taqueria (prompt):
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    while True:
        try:
            item = input(prompt).strip().title()
            return  menu[item]
        except EOFError:
             return '/n'
        except KeyError:
             pass

main()