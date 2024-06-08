greeting = input("Greeting: ").strip().lower()
compromise = 0


if greeting.__contains__("hello"):
    print(f"${compromise}")
elif greeting.startswith("h"):
    compromise = 20
    print(f"${compromise}")
else:
    compromise = 100
    print(f"${compromise}")