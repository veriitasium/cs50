camel_case = input("camelCase: ")

print("snake_case: ", end="")

for char in camel_case:
    if char.isupper():
        print(f'_{char.lower()}', end="")
        continue
    print(char, end="")

print()