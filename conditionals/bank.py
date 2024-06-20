def main():
    compromise = value(input("Greeting: "))
    print(f"${compromise}")


def value(greeting):
    greeting = greeting.lower()
    compromise = 0
    if greeting.__contains__('hello'):
        compromise = 0
    elif greeting.startswith('h'):
        compromise = 20
    else:
        compromise = 100
    return compromise        


if __name__ == "__main__":
    main()