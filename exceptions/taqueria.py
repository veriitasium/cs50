menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def search_for_key(item):
    for key in menu:
        if key.lower() == item.lower():
            return menu[key]
    return 0




def main():
    total = 0.
    while True:
        try:
            item = input("Item: ").strip()

            total += search_for_key(item)
            print(total)
        except KeyError:
            pass
        except EOFError:
            print()
            break

main()