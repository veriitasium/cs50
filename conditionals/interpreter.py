x, y, z = input("Expression: ").split(" ")

result = float()

match y:
    case "+": result = float(x) + float(z)
    case "-": result = float(x) - float(z)
    case "/": result = float(x) / float(z)
    case "*": result = float(x) * float(z)
    case _: print("Unknown sign; signs should encompass '+', '-', '*', and '/'")

print('{0:.1f}'.format(result))