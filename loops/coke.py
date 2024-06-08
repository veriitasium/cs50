cook_price = 50
insert = 0
while insert < 50:
    print(f"Amount Due: {50 - insert}")
    prompt = int(input("Insert Coin: "))
    if prompt == 5 or prompt == 10 or prompt == 25:
        insert += prompt

change = insert - cook_price
print(f"Change Owed: {change}")